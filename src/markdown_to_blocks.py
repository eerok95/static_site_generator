from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):

    if re.match(r"#{1,6} ", block):
        return BlockType.HEADING
    if re.match(r"```",block) and re.match(r"```", block[::-1]):
        return BlockType.CODE
    splitted_block = block.split("\n")
    is_a_quote = True
    is_a_ul = True
    is_a_ol = True
    digit = 1
    for line in splitted_block:
        if re.match(r">.*", line):
            pass
        else:
            is_a_quote = False
        if re.match(r"- ", line):
            pass
        else:
            is_a_ul = False
        if line[0] == str(digit) and re.match(r"\d\. ",line):
            digit += 1
            pass
        else:
            is_a_ol = False

    if is_a_quote:
        return BlockType.QUOTE
    if is_a_ul:
        return BlockType.UNORDERED_LIST
    if is_a_ol:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    
    
    



def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    remove_indexes = []
    for i in range(len(block_strings)):
        block_strings[i] = block_strings[i].strip()
        if block_strings[i] == "\n":
            remove_indexes.append(i)
    for index in remove_indexes:
        del block_strings[index]


    return block_strings
    
    
