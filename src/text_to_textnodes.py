from textnode import *
from split_nodes import *

def text_to_textnodes(text):
    nodes_bold = split_nodes_delimiter([TextNode(text,TextType.TEXT)],"**", TextType.BOLD)
    nodes_italic = split_nodes_delimiter(nodes_bold,"_", TextType.ITALIC)
    nodes_code = split_nodes_delimiter(nodes_italic,"`", TextType.CODE)
    nodes_link = split_nodes_link(nodes_code)
    nodes_image = split_nodes_image(nodes_link)
    return nodes_image

