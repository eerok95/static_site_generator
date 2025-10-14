import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("Something", TextType.ITALIC)
        node2 = TextNode("Something", TextType.PLAIN)
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

if __name__ == "__main__":
    unittest.main()