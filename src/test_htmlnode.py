import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_is_none(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_not_equal(self):
        node = HTMLNode(props={"class": "greeting"})
        self.assertNotEqual(node.props_to_html(), ' class="wrong-class"')

    def test_props_values_not_equal(self):
        node1 = HTMLNode(props={"id": "header"})
        node2 = HTMLNode(props={"id": "footer"})
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()