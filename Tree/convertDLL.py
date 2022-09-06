
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

prev = None


def convertDLL(root):
    if root is None:
        return root
    
    head = convertDLL(root.left)
    global prev
    if prev is None:
        head = root

    else:
        root.left = prev
        prev.right = root
    
    prev = root
    convertDLL(root.right)

    return head


def printDLL(head):

    while head is not None:
        print(head.data, end = " ")
        head = head.right


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    head = convertDLL(root)

    printDLL(head)