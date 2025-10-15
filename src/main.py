from textnode import *
def main():
    text_node = TextNode("hello there", TextType.ITALIC)
    print(text_node.__repr__())

main()