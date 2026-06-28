import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_comprehensive(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_text_to_textnodes_plain_text(self):
        text = "Just standard text with absolutely no markdown."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Just standard text with absolutely no markdown.", TextType.TEXT)
            ],
            nodes
        )

    def test_text_to_textnodes_only_one_type(self):
        text = "![just an image](https://img.com/image.jpg)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("just an image", TextType.IMAGE, "https://img.com/image.jpg")
            ],
            nodes
        )

    def test_text_to_textnodes_multiple_same_type(self):
        text = "**bold one** and then **bold two** with a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("bold one", TextType.BOLD),
                TextNode(" and then ", TextType.TEXT),
                TextNode("bold two", TextType.BOLD),
                TextNode(" with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

if __name__ == "__main__":
    unittest.main()