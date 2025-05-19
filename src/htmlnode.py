from textnode import TextType


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        HTML_attributes = ""
        if self.props != None:
            for key in self.props:
                HTML_attributes += f'{key}="{self.props[key]}" '
        return HTML_attributes.strip()
    
    def __eq__(self, value):
        if not isinstance(value, HTMLNode):
            return False
        return (
            self.tag == value.tag and
            self.value == value.value and
            self.children == value.children and
            self.props == value.props
        )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return f"{self.value}"
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_html = self.props_to_html()
        if props_html:
            opening_tag = f"<{self.tag} {props_html}>"
        else:
            opening_tag = f"<{self.tag}>"
            
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
    
        closing_tag = f"</{self.tag}>"
    
        return opening_tag + children_html + closing_tag