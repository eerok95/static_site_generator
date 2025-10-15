class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:

            props_string = ""
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
            return props_string
        return ""

    def __repr__(self):
        print(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")
    

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        self.__repr__()
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return str(self.value)
        if self.props:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent nodes tag is missing")
        if not self.children:
            raise ValueError("Parent nodes children are missing")
        children_html_string = ""
        props_html = self.props_to_html()
        for child in self.children:
            children_html_string += child.to_html()
        return f"<{self.tag}{props_html}>{children_html_string}</{self.tag}>"
        