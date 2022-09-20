class Node:
    def __init__(self, data=1):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return self.head

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoubleNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
