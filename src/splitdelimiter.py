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
    