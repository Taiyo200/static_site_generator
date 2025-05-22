from text_to_textnode import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]
