import unittest
from extract_title import extract_title
class TestExtractTitle(unittest.TestCase):

    def test_with_heading(self):
        md = """
# Heading here
        
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        title = extract_title(md)
        expected_title = "Heading here"
        self.assertEqual(expected_title, title)

    def test_without_heading(self):
        md = """
Heading not here
        
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        try:
            title = extract_title(md)
        except Exception as e:
            self.assertEqual(str(e), "No <h1> title to be extracted")