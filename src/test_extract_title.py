import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        
    def test_title_with_extra_spaces(self):
        self.assertEqual(extract_title("  #   Whitespace Title   "), "Whitespace Title")
        
    def test_title_no_space_after_hash(self):
        self.assertEqual(extract_title("#Hello"), "Hello")
        
    def test_multiline_document(self):
        markdown = (
            "This is an intro paragraph.\n"
            "\n"
            "# The Real Title\n"
            "\n"
            "## A Subtitle\n"
            "More text here."
        )
        self.assertEqual(extract_title(markdown), "The Real Title")
        
    def test_missing_h1_raises_exception(self):
        markdown = "Just some standard text\nwithout any headers."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found.")
        
    def test_h2_does_not_count_as_h1(self):
        markdown = "## Secondary Header\n### Tertiary Header"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found.")

if __name__ == "__main__":
    unittest.main()