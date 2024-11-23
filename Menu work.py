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

root = Node(100)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(70)
root.right.left = Node(90)
root.right.right = Node(200)

user = input("Do you want to use Inorder, Preorder, or Postorder? ")

if user == "Inorder":
    Inorder(root)
elif user == "Preorder":
    Preorder(root)
elif user == "Postorder":
    Postorder(root)
else:
    print("That is not a valid choice, either choose the options available, or remember there are no spaces and the first letter is capital.")
