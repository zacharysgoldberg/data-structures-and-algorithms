from helpers import DoubleNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:  # Check whether the head is None
            return True
        else:
            return False

    def length(self):
        lst_length = 0

        curr = self.head
        while curr:
            lst_length += 1
            curr = curr.next
        return lst_length

    def insert_head(self, data):
        node = DoubleNode(data)
        node.next = self.head
        if self.is_empty():
            self.head = node
        self.head.prev = node

    def insert_tail(self, data):
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node.prev
        return node

    def remove_head(self):
        if (self.is_empty()):
            return False
        self.head
        temp = self.head
        self.head = self.head.next
        temp = None
        if self.head:
            self.head.prev = None
            return self.head.data

    def sorted_insert_node(self, data):
        node = DoubleNode(data)
        cur = self.head
        if self.head is None:
            self.heads = node
            return self.head
        elif data <= cur.data:
            node.next = cur
            cur.prev = node
            return node
        else:
            while cur.next:
                if data > cur.data and data <= cur.next.data:
                    node.next = cur.next
                    cur.prev = node
                    cur.next = node
                    node.prev = cur
                    return self.head
                else:
                    cur = cur.next
            cur.next = node
            node.prev = cur
            return

    def reverse(self, head):
        reverse = head
        curr = head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            reverse = curr
            curr = curr.prev

        return reverse
