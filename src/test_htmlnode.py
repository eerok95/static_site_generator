import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_is_None(self):
        node = HTMLNode()
        node2 = HTMLNode("p", "Good morning fella", None, None)
        self.assertIsNone(node.props)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNotNone(node2.tag)
        self.assertIsNotNone(node2.value)
    def test_props_string(self):
        node = HTMLNode("a", "Good morning fella", None, {"href":"www.google.fi"})
        node2 = HTMLNode("a", "asdf", None, {"href":"www.google.fi", "tag":"Nonexistent"})
        correct_string = ' href="www.google.fi"'
        correct_string2 = ' href="www.google.fi" tag="Nonexistent"'
        self.assertEqual(correct_string, node.props_to_html())
        self.assertEqual(correct_string2, node2.props_to_html())
    def test_props_string_none(self):
        node = HTMLNode("div", None, None, None)
        self.assertEqual("", node.props_to_html())
    def test_props_string_empty(self):
        node = HTMLNode("div", None, None, {})
        self.assertEqual("", node.props_to_html())

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href":"www.bootdev.com"})
        self.assertEqual(node.to_html(), '<a href="www.bootdev.com">Hello, world!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()