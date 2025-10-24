import os
from generate_page import generate_page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        content_dest_path = os.path.join(dest_dir_path, content)
        print("-----------------------")
        print(f"content_dest_path: {content_dest_path}")
        print("-----------------------")
        if os.path.isfile(content_path) and os.path.splitext(content_path)[1] == ".md":
            content_dest_path = content_dest_path[:-3] + ".html"
            generate_page(content_path, template_path, content_dest_path, basepath)
            continue
        if os.path.isdir(content_path):
            if not os.path.exists(content_dest_path):
                os.mkdir(content_dest_path)
                print(f"copied directory: {content_path} to {content_dest_path}")
            generate_pages_recursive(content_path, template_path, content_dest_path, basepath)