import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT,  "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT, None)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT, None)
        node2 = TextNode("This is a different text node", TextType.CODE_TEXT, None )
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()