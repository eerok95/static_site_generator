import os
from markdown_to_html import markdown_to_html_node
from htmlnode import *
from extract_title import extract_title
from copy_contents_from_source import *
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        md = file.read()
        print(f"markdown catched (100 first chars): {md[0:100]}")
    with open(template_path, "r") as file:
        template = file.read()
    html_string = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    full_page =  template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    with open(dest_path, 'x') as file:
        file.write(full_page)
    