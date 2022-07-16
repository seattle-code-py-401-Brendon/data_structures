from python.code_challenges.data_structures.stacks_and_queues.queue import Queue
from python.code_challenges.data_structures.binary_tree.binary_tree import BinaryTree, Node


def breadth_first(binary_tree):

    tree_queue = Queue()
    tree_list = []
    if binary_tree.root is None:
        return tree_list
    tree_queue.enqueue(binary_tree.root)
    while tree_queue.front:
        front_node = tree_queue.dequeue()
        tree_list.append(front_node.value)
        if front_node.left:
            tree_queue.enqueue(front_node.left)
        if front_node.right:
            tree_queue.enqueue(front_node.right)
    return tree_list


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node('a')
    tree.root.left = Node('b')
    tree.root.right = Node('c')
    print(breadth_first(tree))
