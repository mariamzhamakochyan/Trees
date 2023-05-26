class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
                return
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
                return

    def search(self, val):
        if val==self.value:
            return str(val)+" is found"
        elif val < self.value:
            if self.left:
                return self.left.search(val)
            else:
                return str(val)+" is not found"
        else:
            if self.right:
                return self.right.search(val)
            else:
                return str(val)+" is not found" 
       
            
    def display(self):
        if self.left:
            self.left.display()
        print( self.value),
        if self.right:
            self.right.display()

root = Node(2)
root.insert(13)
root.insert(21)
root.insert(41)
root.insert(10)

print(root.search(1))
print(root.search(2))
root.display()
