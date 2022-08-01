# create node class
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Linked list class with methods to insert, append, includes, insert before, insert after and convert to string
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """Insert New Node with Value into Linked List
        Args:
            value (any): the value of the node, can be any data type
        """
        # initialization here
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """traverse through Linked List and search for node in linked list
        Args:
            value (any): the nodes value that the method is searching for
        Returns:
            boolean: returns True or False if node is in Linked List
        """
        # method body here
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        """add Node to the end of the Linked List
        Args:
            value (any): the data type can be any
        """
        node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, query, value):
        """insert a node before a specific node in the linked list
        Args:
            query (any): the point where we want to insert before
            value (any): the new node with a value that we will insert before the query
        """
        node = Node(value)
        current = self.head
        # print(current.value)
        if current is None or current.value is query:
            self.insert(value)
            return
        else:
            while current:
                next_node = current.next
                if current.next.value == query:
                    # 1,2,3,none
                    current.next = node
                    node.next = next_node
                    return
                current = current.next

    def insert_after(self, query, value):
        """insert new node after the specified query node
        Args:
            query (any): the node we are looking for to insert after
            value (any): the node with a value that we will insert after the query node
        """

        current = self.head

        if current.next is None:
            self.insert(value)
            return
        while current:
            if current.value == query:
                node = Node(value)
                current.next = node
                return
            current = current.next

    def kthFromEnd(k):
        """get the vale of the node at the (k)location
        Args:
            k (int): the location of where the node is at
        """
        pass

    def print(self):
        if self.head == None:
            print('empty linked list')
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next

    def __str__(self):
        """
        convverts the Linked List to a string and returns the contents as a string
        """
        current = self.head
        values = ""
        if self.head is None:
            return f"NULL"
        while current != None:
            values += "{}".format('{ ' + f"{current.value}" + ' } -> ')
            current = current.next
        values += "NULL"
        return values


class TargetError(Exception):
    """error handling class.
    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="Error"):
        self.message = message


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.print()
