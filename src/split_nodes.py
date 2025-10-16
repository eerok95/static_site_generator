from textnode import *
from extract_markdown_images_links import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            sections = node.text.split(delimiter)
            split_nodes = []
            if len(sections) % 2 == 0:
                raise ValueError("Invalid markdown syntax")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(node)

    return new_nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images_info = extract_markdown_images(node.text)
            if len(images_info) == 0 and node.text != "":
                new_nodes.append(node)
                continue
            splittable_text = node.text
            for item in images_info:
                sections = splittable_text.split(f"![{item[0]}]({item[1]})", 1)
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
                splittable_text = sections[1]
                
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links_info = extract_markdown_links(node.text)
            if len(links_info) == 0 and node.text != "":
                new_nodes.append(node)
                continue
            splittable_text = node.text
            for item in links_info:
                sections = splittable_text.split(f"[{item[0]}]({item[1]})", 1)
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(item[0], TextType.LINK, item[1]))
                splittable_text = sections[1]
        else:
            new_nodes.append(node)
    return new_nodes

