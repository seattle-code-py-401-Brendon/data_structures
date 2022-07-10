from python.code_challenges.data_structures.binary_tree.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)

        def traverse_tree(root):
            """Traverses through the tree"""
            if root.value < value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    traverse_tree(root.right)
            elif root.value > value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    traverse_tree(root.left)

        traverse_tree(self.root)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(6)
    tree.add(3)
    print(tree.root.left.value)
