from enum import Enum

class TextType(Enum):
    """
    Enum for text types.
    """
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINKS = 5
    IMAGES = 6
    
class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
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