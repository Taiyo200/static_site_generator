import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container"})
        node3 = HTMLNode("span", "This is a span", [], {"class": "container"})
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        expected_repr = 'HTMLNode(div, This is a div, [], {\'class\': \'container\'})'
        self.assertEqual(repr(node), expected_repr)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")
        
    if __name__ == "__main__":
        unittest.main()