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

root = (100)
root.left = (20)
root.right = (30)
root.left.left = (40)
root.left.right = (70)
root.right.left = (90)
root.right.right = (200)

print("These are the numbers that are ")