# Define a class for a binary tree node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Function to insert a new node at the end of the tree
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Function to print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Function to search the tree for a value
    def FindVal(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.FindVal(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.FindVal(lkpval)
        else:
            return str(self.data) + " is found"


# Use the functions
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(14)
root.insert(4)
root.insert(7)
root.insert(13)

print("Print tree")
root.PrintTree()

print("Search for 10")
print(root.FindVal(10))

print("Search for -1")
print(root.FindVal(-1))
