from python.code_challenges.data_structures.binary_tree.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def add(self, value):
        # method body here
        if self.root is None:
            self.root = Node(value)
        elif self.root.value > value:
            if self.root.left is None:
                self.root.left = Node(value)
            else:
                self.root = self.root.left
                return self.add(value)
        elif self.root.value < value:
            if self.root.right is None:
                self.root.right = Node(value)
            else:
                self.root = self.root.right
                return self.add(value)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(3)
    tree.add(2)
    print(tree.root.value)

