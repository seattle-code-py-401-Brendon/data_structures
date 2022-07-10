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

    def contains(self, value):
        if self.root is None:
            return False

        def traverse_tree(root):
            if root.value == value:
                return True
            elif root.value > value:
                if root.left is None:
                    return False
                elif root.left.value == value:
                    return True
                else:
                    return traverse_tree(root.left)
            elif root.value < value:
                if root.right is None:
                    return False
                elif root.right.value == value:
                    return True
                else:
                    return traverse_tree(root.right)

        return traverse_tree(self.root)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    tree.add(8)
    tree.add(1)
    print(tree.root.left.left.value)
    print(tree.root.value)
    print(tree.contains(0))
