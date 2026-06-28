import unittest
from markdown_to_blocks import block_to_type, BlockType

class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_type("###### Heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_type("```\ncode\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_type(">Quote line 1\n>Quote line 2"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        # Normal text
        self.assertEqual(block_to_type("This is just a normal paragraph."), BlockType.PARAGRAPH)
        # Ordered list with wrong increment
        self.assertEqual(block_to_type("1. Item 1\n3. Item 3"), BlockType.PARAGRAPH)
        # Quote missing '>' on one line
        self.assertEqual(block_to_type(">Quote\nNot a quote"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()