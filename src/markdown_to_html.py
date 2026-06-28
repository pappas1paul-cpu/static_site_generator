from markdown_to_blocks import markdown_to_blocks, block_to_type, BlockType
from htmlnode import ParentNode, LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    normalized_text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(normalized_text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_type(block)
        if block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block)))
        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            heading_text = block.lstrip("# ")
            children.append(ParentNode(f"h{level}", text_to_children(heading_text)))
        elif block_type == BlockType.CODE:
            content = block.strip("`").strip("\n") + "\n"
            children.append(ParentNode("pre", [LeafNode("code", content)]))
        elif block_type == BlockType.QUOTE:
            clean_lines = [line.lstrip(">").strip() for line in block.split("\n")]
            children.append(ParentNode("blockquote", text_to_children(" ".join(clean_lines))))
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = [ParentNode("li", text_to_children(line.lstrip("- "))) for line in block.split("\n")]
            children.append(ParentNode("ul", list_items))
        elif block_type == BlockType.ORDERED_LIST:
            list_items = [ParentNode("li", text_to_children(line.split(". ", 1)[1])) for line in block.split("\n")]
            children.append(ParentNode("ol", list_items))
            
    return ParentNode("div", children)