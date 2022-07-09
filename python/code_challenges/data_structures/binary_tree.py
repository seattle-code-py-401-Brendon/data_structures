class BinaryTree:
    """
    [Methods] : pre_order, post_order, in_order
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def insert(self, value):
        """insert node from left to write based on if left or right is empty, empty left gets priority"""
        node = Node(value)
        if self.is_empty() is True:
            self.root = node
        elif self.root.left is None:
            self.root.left = node
        elif self.root.left is not None and self.root.right is None:
            self.root.right = node
        else:
            return self.insert(value)

    def pre_order(self):
        """ [Traverse] : Root → Left → Right """
        pass

    def post_order(self):
        """ [Traverse] : Left → Root → Right """
        pass

    def in_order(self):
        """ [Traverse] : Left → Right → Root """
        pass

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False


class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    print(tree.root.left.value)
