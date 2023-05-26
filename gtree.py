class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child):
        if child in self.children:
            child.parent = None
            self.children.remove(child)
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def is_root(self):
        return self.parent is None
    
    def get_value(self):
        return self.value
    
    def set_value(self, data):
        self.value = value

