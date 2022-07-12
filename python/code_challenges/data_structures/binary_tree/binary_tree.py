class BinaryTree:
    """
    [Methods] : pre_order, post_order, in_order
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def insert(self, value):
        """insert node from left to write based on if left or right is empty, empty left gets priority"""

    def pre_order(self):
        """ [Traverse] : Root → Left → Right """
        values_list = []

        def traverse_tree(root):
            if not root:
                return
            values_list.append(root.value)
            traverse_tree(root.left)
            traverse_tree(root.right)

        traverse_tree(self.root)
        return values_list

    def post_order(self):
        """ [Traverse] : Left → Right → Root """
        values_list = []

        def traverse_tree(root):
            if not root:
                return
            traverse_tree(root.left)
            traverse_tree(root.right)
            values_list.append(root.value)

        traverse_tree(self.root)
        return values_list

    def in_order(self):
        """ [Traverse] : Left → Root → Right """
        values_list = []

        def traverse_tree(root):
            if not root:
                return
            traverse_tree(root.left)
            values_list.append(root.value)
            traverse_tree(root.right)

        traverse_tree(self.root)
        return values_list

    def max_value(self):

        def traverse_tree(root):
            largest = 0
            if not root:
                return
            if root.value > largest:
                largest = root.value
            traverse_tree(root.left)
            traverse_tree(root.right)
            return largest

        traverse_tree(self.root)

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
    tree.root = Node('a')
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")
    print(tree.pre_order())
