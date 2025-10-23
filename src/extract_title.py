from markdown_to_blocks import *
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            lines = block.split("\n")
            for line in lines:
                if line.startswith("# "):
                    return line.lstrip("#").strip()
    raise Exception("No <h1> title to be extracted")