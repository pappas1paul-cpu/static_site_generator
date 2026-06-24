class HTMLNode:
    def __init__(self, tag=None, value:str = None, children:list = None, props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __to_html__(self):
        raise NotImplementedError
        pass

    def props_to_html(self):
        if self.props is None:
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f' {key}="{value}"')
        return "".join(props_list)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"