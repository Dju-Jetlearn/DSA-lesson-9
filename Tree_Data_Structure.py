class Node:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v

def Inorder(root):
    if root: #checks if it exists
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def Preorder(root):
    if root:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)

#Creating Tree
root = Node(100) #this is the top of the tree
root.left = Node(20) #second left
root.right = Node(30) #second right
root.left.left = Node(40) #every time you turn again, you add a .left/.right
root.left.right = Node(70)
root.right.left = Node(90)
root.right.right = Node(200)

print("Inorder Traversal")
Inorder(root)

print("Preorder Traversal")
Preorder(root)

print("Postorder Traversal")
Postorder(root)