import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        splitted = node.text.split(delimiter)

        if len(splitted) % 2 == 0:
            raise Exception("Unmatched delimiter")

        for i, chunk in enumerate(splitted):
            if i % 2 == 0:
                new_nodes.append(TextNode(chunk, TextType.TEXT))
            else:
                new_nodes.append(TextNode(chunk, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]+)\)"

    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        pos = 0
        for match in re.finditer(image_pattern, node.text):
            start, end = match.span()
            alt_text, image_url = match.groups()

            if start > pos:
                new_nodes.append(TextNode(node.text[pos:start], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))

            pos = end

        if pos < len(node.text):
            new_nodes.append(TextNode(node.text[pos:], TextType.TEXT))

    return new_nodes
        
    
def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = r"(?<!!)\[([^\[\]]+)\]\(([^\(\)]+)\)"
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        pos = 0
        for match in re.finditer(link_pattern, node.text):
            start, end = match.span()
            link_text, link_url = match.groups()

            if start > pos:
                new_nodes.append(TextNode(node.text[pos:start], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            pos = end

        if pos < len(node.text):
            new_nodes.append(TextNode(node.text[pos:], TextType.TEXT))

    return new_nodes
    
def __eq__(self, value):
    if not isinstance(value, TextNode):
        return False
    return (
        self.text == value.text and
        self.text_type == value.text_type and
        self.url == value.url
    )
def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
    