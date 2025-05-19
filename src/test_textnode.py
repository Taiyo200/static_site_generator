import unittest

from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_split_delimiter(self):
        node = TextNode("This is a text node **but with** bold marks", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a text node ", TextType.TEXT),
            TextNode("but with", TextType.BOLD),
            TextNode(" bold marks", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
        
        node2 = TextNode("This is a text node but with `code`.", TextType.TEXT)
        result2 = split_nodes_delimiter([node2], "`", TextType.CODE)
        expected2 = [
            TextNode("This is a text node but with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result2, expected2)


if __name__ == "__main__":
    unittest.main()