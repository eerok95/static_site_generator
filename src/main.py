import sys
from copy_contents_from_source import copy_contents
from generate_pages_recursive import generate_pages_recursive
def main():
    basepath = sys.argv[1]
    print(f"sys.argv[1] -------> {basepath}")
    if len(basepath) == 0:
        basepath = "/"
    copy_contents("./static", "./docs")
    generate_pages_recursive("./content","template.html", "./docs", basepath)
main()