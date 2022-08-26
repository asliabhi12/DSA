


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+= 1
            p = p.parent
        
        return level



    def print_tree(self):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data) 
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("asus"))
    laptop.add_child(TreeNode("apple"))
    laptop.add_child(TreeNode("lenovo"))
    laptop.add_child(TreeNode("rog"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("apple"))
    cellphone.add_child(TreeNode("samsung"))
    cellphone.add_child(TreeNode("xiaomi"))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root



if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass