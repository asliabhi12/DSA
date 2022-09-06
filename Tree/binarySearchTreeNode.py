class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add to the left of the subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else: 
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):

        elements = []
        #visit left
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)

            else:
                return False
def mini(node):
    if node is None:
        return float("inf")
    return min(node.data, min(mini(node.left), mini(node.right)))

def maxim(node):
    if node is None:
        return float("-inf")
    return max(node.data, max(maxim(node.left), maxim(node.right)))

def size(node):
    if node is None:
        return 0
    return size(node.right) + size(node.left) + 1

def height(node):
    if not node:
        return 0
    return max(height(node.right) ,height(node.left)) + 1

def curLevel(node, level):
    if node == None:
        return
    if level == 1:
        print(node.data, end=" ")
    
    elif level > 1:
        print(curLevel(node.left, level = level -1))
        print(curLevel(node.right, level = level -1))

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,24]
    numbers_tree = build_tree(numbers)
    # print("size of tree is ",size(numbers_tree))

    # print("maximum elemnt of the binary tree is", maxim(numbers_tree))

    # print("minimum element is ", mini(numbers_tree))

    # print("height of binary tree is ",height(numbers_tree))

    print(curLevel(numbers_tree, 2))

    print(numbers_tree.search(24))