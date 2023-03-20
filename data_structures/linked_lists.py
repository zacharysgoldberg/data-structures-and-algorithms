'''

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self) -> bool:
        if not self.head:
            return True
        else:
            return False

    def length(self) -> int:
        counter = 0
        curr = self.get_head()
        while curr:
            counter += 1
            curr = curr.next

        return counter

    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        return

    def insert_at_tail(self, data):
        node = Node(data)
        if not self.get_head():
            self.head = node
            return self

        curr = self.get_head()
        while curr.next:
            curr = curr.next
        curr.next = node
        return

    def insert(self, data):
        node = Node(data)
        curr = self.head
        while curr:
            if curr.data > data and curr.next.data <= data:
                next_node = curr.next
                curr.next = node
                node.next = next_node
                return
            curr = curr.next

        return

    def search(self, data) -> bool:
        curr = self.get_head()
        while curr:
            if curr.data == data:
                return True
            curr = curr.next

        return False

    def find_mid(self) -> int:
        slow = self.get_head()
        fast = self.get_head()
        if self.length() == 4:
            fast = fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def delete_at_head(self):
        first_node = self.get_head()
        if first_node:
            self.head = first_node.next
            # Free the data in the temp list from memory
            first_node.next = None
        return

    def delete(self, data) -> bool:
        curr = self.get_head()
        prev = self.get_head()
        if curr.data == data:
            self.delete_at_head()
            return True
        while curr:
            if curr.data == data:
                prev.next = curr.next
                # Free the data in the temp list from memory
                curr.next = None
                return True
            prev = curr
            curr = curr.next

        return False

    def remove_duplicates(self):
        visited = set()
        curr = self.get_head()
        prev = self.get_head()
        while curr:
            if curr.data in visited:
                prev.next_element = curr.next_element
                curr = curr.next_element
                continue
            visited.add(curr.data)
            prev = curr
            curr = curr.next_element

    def __str__(self):
        if self.is_empty():
            print("List is empty")
            return False
        curr = self.head
        while curr.next:
            print(curr.data, " -> ", end=" ")
            curr = curr.next
        print(curr.data, " -> None")
        return True


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_at_head(self, data):
        node = DoubleNode(data)
        if not self.is_empty():
            self.head.prev = node
            node.next = self.head
        self.head = node
        if not self.get_tail():
            self.tail = node
        return self.head

    def insert_at_tail(self, data):
        node = DoubleNode(data)
        if not self.get_tail():
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        if not self.get_head():
            self.head = node
        return node

    def insert(self, data):
        node = DoubleNode(data)
        curr = self.head
        if self.is_empty():
            return node
        # Insert at head
        elif curr.data > data:
            return self.insert_at_head(data)
        while curr.next:
            if curr.data < data and curr.next.data >= data:
                node.next = curr.next
                curr.next.prev = node
                curr.next = node
                node.prev = curr
                return self.head
            curr = curr.next

        curr.next = node
        node.prev = curr
        return

    def delete(self, data):
        curr = self.get_head()
        if self.is_empty():
            return False
        if curr.data == data:
            # Point head to the next element of the first element
            self.head = curr.next
            if curr.next and curr.next.prev:
                # Point the next element of the first element to None
                curr.next.prev = None

            return True

        # Traversing/Searching for node to Delete
        while curr:
            if curr.data == data:
                if curr == self.tail:
                    self.remove_tail()
                elif curr.next:
                    # Link the next node and the previous node to each other
                    prev = curr.prev
                    next_node = curr.next
                    prev.next = next_node
                    next_node.prev = prev
                    # previous node pointer was maintained in Singly Linked List
                else:
                    curr.prev.next = None
                return True
            # previousNode = tempNode was used in Singly Linked List
            curr = curr.next

        return False

    def remove_tail(self):
        if self.tail == None:
            return None
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return

    def __str__(self):
        if self.is_empty():
            print("List is empty")
            return False
        curr = self.head
        while curr.next:
            print(curr.data, " <- -> ", end=" ")
            curr = curr.next
        print(curr.data, " <- -> None")
        return True


lst = LinkedList()
lst.__str__()

print()

print("Inserting values in list")
for i in range(1, 10):
    lst.insert_at_head(i)
lst.__str__()

lst.delete_at_head()
lst.__str__()

lst.delete(4)
lst.__str__()

print(lst.search(4))

lst.insert(4)
lst.__str__()

print(lst.search(3))

'''
dblist = DoublyLinkedList()
for i in range(11):
    dblist.insert_at_head(i)

dblist.__str__()
print(dblist.tail.data)

dblist.delete(5)
dblist.__str__()

dblist.delete(0)
dblist.__str__()
print(dblist.tail.data)

dblist.insert_at_tail(0)
dblist.__str__()

print(dblist.tail.data)
'''
