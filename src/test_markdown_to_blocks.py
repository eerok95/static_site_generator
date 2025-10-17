import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is **bolded** paragraph",
                                  "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                                  "- This is a list\n- with items",])
    def test_single_block(self):
        md = "Just a single block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single block"])

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [""])

    def test_blocks_with_extra_whitespace(self):
        md = "First block   \n\n   Second block\n\n\nThird block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["First block", "Second block", "Third block"]
        )

 #   def test_blocks_with_only_newlines(self):
 #       md = "\n\n\n"
 #       blocks = markdown_to_blocks(md)
 #       self.assertEqual(blocks, [""])
class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_blocktype_quote(self):
        block = ">hello there\n>this is a quote"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, type)

    def test_block_to_blocktype_paragraph(self):
        block = "some text\nmoretext"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, type)

    def test_block_to_blocktype_code(self):
        block = "```code```\n```more code```"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, type)

    def test_block_to_blocktype_heading(self):
        block = "## heading\n### heading"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, type)

    def test_block_to_blocktype_ul(self):
        block = "- this\n- that"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, type)

    def test_block_to_blocktype_ol(self):
        block = "1. I\n2. like\n3. you"
        type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, type)