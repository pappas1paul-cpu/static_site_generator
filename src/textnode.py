from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT="text"
    BOLD = "bold"
    ITALIC ="italic"
    CODE = "code"
    LINK = "link"
    IMAGE ="image"

class TextNode:
    def __init__(self,text, text_type:TextType, url = None):
        self.text = text
        self.text_type=text_type
        self.url = url
    
    def __eq__(self, other: "TextNode"):
        return  self.text == other.text and \
                self.text_type==other.text_type and \
                self.url == other.url
    
    def __repr__(self):
        return "TextNode"f"({self.text}, {self.text_type}, {self.url})"
            
def text_node_to_html_node(textnode: TextNode) -> LeafNode:
    if textnode.text_type == TextType.TEXT:
        return LeafNode(None, textnode.text)
    if textnode.text_type == TextType.BOLD:
        return LeafNode("b", textnode.text)
    if textnode.text_type == TextType.ITALIC:
        return LeafNode("i", textnode.text)
    if textnode.text_type == TextType.CODE:
        return LeafNode("code", textnode.text)
    if textnode.text_type == TextType.LINK:
        return LeafNode("a", textnode.text, {"href": textnode.url})
    if textnode.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
    raise Exception(f"Unknown TextType: {textnode.text_type}")
    
            