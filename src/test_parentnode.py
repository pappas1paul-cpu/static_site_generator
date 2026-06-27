import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span>child</span></div>", parent_node.to_html())
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
             "<div><span><b>grandchild</b></span></div>",parent_node.to_html())

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertRaises(ValueError,node.to_html)

    def test_to_html_no_tag_raises_error(self):
        node = ParentNode(None, [LeafNode("b", "bold")])
        self.assertRaises(ValueError, node.to_html)
            

    def test_to_html_no_children_raises_error(self):
        node = ParentNode("div", None)
        self.assertRaises(ValueError,node.to_html)
        

    def test_to_html_with_props(self):
        node = ParentNode(
            "div", 
            [LeafNode("span", "text")], 
            {"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(),'<div class="container" id="main"><span>text</span></div>'
        )

    def test_to_html_mixed_nested_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode("span", [LeafNode("b", "bold")]),
                LeafNode("i", "italic")
            ]
        )
        self.assertEqual(
            node.to_html(),"<div><span><b>bold</b></span><i>italic</i></div>"            
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "html",
            [
                ParentNode(
                    "body",
                    [
                        ParentNode("div", [LeafNode("p", "deep text")])
                    ]
                )
            ]
        )
        self.assertEqual(
             node.to_html(),"<html><body><div><p>deep text</p></div></body></html>"
        )

    def test_to_html_empty_text_leaf(self):
        node = ParentNode("div", [LeafNode("span", "")])
        self.assertEqual(
         node.to_html(),"<div><span></span></div>"
        )

if __name__ == "__main__":
    unittest.main()