from python.code_challenges.data_structures.binary_tree.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.binary_tree = BinaryTree()

    def add(self, value):
        # method body here
        if self.binary_tree.root is None:
            self.binary_tree.root = Node(value)
        if self.binary_tree.root.value > value:
            if self.binary_tree.root.left is None:
                self.binary_tree.root.left = Node(value)
            else:
                self.binary_tree.root = self.binary_tree.root.left
                return self.insert(value)
        elif self.binary_tree.root.value < value:
            if self.binary_tree.root.right is None:
                self.binary_tree.root.right = Node(value)
            else:
                self.binary_tree.root = self.binary_tree.root.right
                return self.insert(value)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(2)
    tree.add(6)
    print(tree.binary_tree.root.left.value)
    print(tree.binary_tree.root.right.value)
