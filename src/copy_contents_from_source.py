import os
import shutil
def copy_contents(from_path, to_path, is_top_level=True):
    if is_top_level:
        print("abs path:" + os.path.abspath(to_path))
        delete_destination_contents(to_path)
    
    from_path_contents = os.listdir(from_path)
    for content in from_path_contents:
        content_from_path = os.path.join(from_path, content)
        content_to_path = os.path.join(to_path, content)

        if os.path.isfile(content_from_path):
            shutil.copy2(content_from_path, content_to_path)
            print(f"copied file: {content_from_path}")
            continue
        if os.path.isdir(content_from_path):
            if not os.path.exists(content_to_path):
                os.mkdir(content_to_path)
                print(f"copied directory: {content_from_path}")
                copy_contents(content_from_path, content_to_path, False)

def delete_destination_contents(to_path):
    to_path_contents = os.listdir(to_path)
    for content in to_path_contents:
        content_path = os.path.join(to_path, content)
        if os.path.isfile(content_path):
            os.remove(content_path)
            continue
        if os.path.isdir(content_path):
            delete_destination_contents(content_path)
            shutil.rmtree(content_path)


