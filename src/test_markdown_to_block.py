import unittest

from markdown_blocks import *
class TestMarkdownToBlock(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks,[
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ],)
            
        def test_block_to_block_type(self):
            self.assertEqual(block_to_block_type("# Heading text"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("```print('hello')```"), BlockType.CODE)
            self.assertEqual(block_to_block_type("> Quoted line"), BlockType.QUOTE)
            self.assertEqual(block_to_block_type("- unordered item"), BlockType.UNORDERED_LIST)
            self.assertEqual(block_to_block_type("1. ordered item"), BlockType.ORDERED_LIST)
            self.assertEqual(block_to_block_type("Just a plain paragraph."), BlockType.TEXT)