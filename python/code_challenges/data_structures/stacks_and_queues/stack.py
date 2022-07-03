from python.code_challenges.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        # initialization here
        self.top = top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.value

    def is_empty(self):
        try:
            if self.top is None:
                return True
            else:
                return False
        finally:
            raise InvalidOperationError

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def print(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()
    print('test')
