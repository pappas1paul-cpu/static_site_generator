import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_paragraph(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_multiple_props(self):
        node = LeafNode("div", "Content", {"class": "container", "id": "main"})
        expected = '<div class="container" id="main">Content</div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_raises_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()