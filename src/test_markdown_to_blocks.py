import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # Notice the lack of indentation here so we don't accidentally include tabs/spaces!
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        # Tests that multiple newlines in a row don't create empty blocks
        md = """
Block 1



Block 2
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block 1",
                "Block 2",
            ],
        )

    def test_markdown_to_blocks_trailing_whitespace(self):
        # Tests that random spaces/tabs before or after a block are stripped
        md = """
   Block with spaces before and after   

	Block with tabs before and after	
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block with spaces before and after",
                "Block with tabs before and after",
            ],
        )

if __name__ == "__main__":
    unittest.main()