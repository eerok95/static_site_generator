
from copy_contents_from_source import copy_contents
from generate_pages_recursive import generate_pages_recursive
def main():
    copy_contents("./static", "./public")
    generate_pages_recursive("./content","template.html", "./public")
main()