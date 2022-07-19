from python.code_challenges.data_structures.kary_tree import KaryTree, Node
import copy

def fizz_buzz_tree(kary_tree):
    if kary_tree is None:
        return 'empty tree'
    new_tree = copy.deepcopy(kary_tree)

    def tree_traverse(root):
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "FizzBuzz"
        elif root.value % 3 == 0:
            root.value = "Fizz"
        elif root.value % 5 == 0:
            root.value = "Buzz"
        elif root.value % 3 != 0 or root.value % 5 != 0:
            root.value = str(root.value)
        for child in root.children:
            tree_traverse(child)

    tree_traverse(new_tree.root)
    return new_tree
