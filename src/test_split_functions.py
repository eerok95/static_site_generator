import unittest
from textnode import *
from split_nodes import *
from text_to_textnodes import text_to_textnodes

class TestSplitImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_images_none(self):
        node = TextNode("No images here.", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [TextNode("No images here.", TextType.TEXT)]
        self.assertListEqual(result, expected)

    def test_split_links_none(self):
        node = TextNode("No links here.", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [TextNode("No links here.", TextType.TEXT)]
        self.assertListEqual(result, expected)
    
class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and then some `yes indeed`"
        nodes = text_to_textnodes(text)
        expected_result = [TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT),
                           TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE),
                           TextNode(" and an ", TextType.TEXT), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                           TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK,"https://boot.dev"), TextNode(" and then some ", TextType.TEXT), TextNode("yes indeed", TextType.CODE)]
       # self.assertEqual(expected_result,nodes)
        print("______________________________________________!!!!")
        print("Expected:", expected_result)
        print("______________________________________________!!!!")
        print("Actual:", nodes)