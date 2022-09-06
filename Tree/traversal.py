

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def inOrderTraversal(root):
    if root == None:
        return

    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if root == None:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root == None:
        return
    
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("inorder")
inOrderTraversal(root)

print("preorder")
preOrderTraversal(root)


print("postorder")
postOrderTraversal(root)