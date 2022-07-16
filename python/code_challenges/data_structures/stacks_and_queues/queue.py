from python.code_challenges.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, rear=None):
        # initialization here
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = Node(value)

        if self.front is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front:
            temp = self.front
            self.front = temp.next
            return temp.value

        else:
            raise InvalidOperationError()

    def peek(self):
        if self.front is None:
            raise InvalidOperationError()
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def print(self):
        current = self.front
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    pass
    # queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.print()
    # print('**********************')
    # print('**********************')
    # queue.dequeue()
    # queue.print()
