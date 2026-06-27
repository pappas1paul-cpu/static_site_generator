import unittest
from extract_links_markdown_images import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Here is ![image1](https://url1.com) and ![image2](https://url2.com)"
        )
        self.assertListEqual(
            [("image1", "https://url1.com"), ("image2", "https://url2.com")], 
            matches
        )

    def test_extract_markdown_with_no_images(self):
        matches = extract_markdown_images("This text has no images.")
        self.assertListEqual([], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "Check out [boot dev](https://boot.dev) and [youtube](https://youtube.com)"
        )
        self.assertListEqual(
            [("boot dev", "https://boot.dev"), ("youtube", "https://youtube.com")], 
            matches
        )

    def test_extract_markdown_with_no_links_(self):
        matches = extract_markdown_links("This text has no links.")
        self.assertListEqual([], matches)


    def test_extraction_img_and_link(self):
        text = "Here is a [link](https://boot.dev) and an ![image](https://img.com/img.jpg)"
        
        image_matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://img.com/img.jpg")], image_matches)
        
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://boot.dev")], link_matches)

if __name__ == "__main__":
    unittest.main()