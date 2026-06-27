from textnode import TextNode, TextType
import re
from extract_links_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: missing closing delimiter '{delimiter}' in text: '{node.text}'")
        for i, part in enumerate(parts):
            if part == "":
                continue    
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
        new_nodes = []
        
        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
                
            original_text = old_node.text
            images = extract_markdown_images(original_text)

            if not images:
                new_nodes.append(old_node)
                continue
            
            for image_alt, image_link in images:
                image_markdown = f"![{image_alt}]({image_link})"
                sections = original_text.split(image_markdown, 1)
                
                if len(sections) != 2:
                    raise ValueError(f"Invalid markdown, image section not closed properly: {original_text}")
                    
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                
                original_text = sections[1]
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
                
        return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        
        if not links:
            new_nodes.append(old_node)
            continue
            
        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            
            sections = original_text.split(link_markdown, 1)
            
            if len(sections) != 2:
                raise ValueError(f"Invalid markdown, link section not closed properly: {original_text}")
                
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            original_text = sections[1]
            
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes