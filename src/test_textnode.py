import unittest

from splitdelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
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


        def test_split_images(self):
            node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,)
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
            [   
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
            )
        def test_split_links_multiple(self):
            node = TextNode(
            "Click [here](https://example.com) and also [there](https://another.com)",
            TextType.TEXT,)
            new_nodes = split_nodes_link([node])
            self.assertListEqual([
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" and also ", TextType.TEXT),
            TextNode("there", TextType.LINK, "https://another.com"),
            ],
            new_nodes,
    )




if __name__ == "__main__":
    unittest.main()