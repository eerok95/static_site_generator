import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild",{"key":"value"})
        grandchild_node2 = LeafNode("b", "grandchild")
        grandchild_node3 = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("h",[parent_node],{"proppening":"Yes!"})
        text = parent_node2.to_html()
        print("---------------------")
        print(text)
        print("----------------------")
        self.assertEqual(
            parent_node2.to_html(),
            text,
        )
class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("Click here", TextType.LINK,"https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"href":"https://www.google.com"})
        self.assertEqual(html_node.value, "Click here")


if __name__ == "__main__":
    unittest.main()