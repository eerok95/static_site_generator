import unittest

from textnode import *
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("Something", TextType.ITALIC)
        node2 = TextNode("Something", TextType.TEXT)
        node3 = TextNode("Something", TextType.LINK)
        node4 = TextNode("Something", TextType.IMAGE)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node4, node3)
    def test_url_None(self):
        node = TextNode("bleh", TextType.LINK)
        self.assertIsNone(node.url)
    def test_url(self):
        node = TextNode("bleh", TextType.LINK, "https://www.google.com")
        self.assertIsNotNone(node.url)
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_with_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node3 = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE)
        expected_result = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)] *3
        self.assertEqual(expected_result,
                         new_nodes)
    def test_with_italic(self):
        node = TextNode("This is _italic_ by the way", TextType.TEXT)
        node2 = TextNode("This is _italic_ by the way", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "_", TextType.ITALIC)
        expected_result = [TextNode("This is ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" by the way", TextType.TEXT)] *2
        self.assertEqual(expected_result,new_nodes)
    def test_with_incorrect_syntax(self):
        node = TextNode("This is italic_ by the way", TextType.TEXT)
        try:
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        except ValueError as v:  
            self.assertEqual(str(v), "Invalid markdown syntax")
        

if __name__ == "__main__":
    unittest.main()