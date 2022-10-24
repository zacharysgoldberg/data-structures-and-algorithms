class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_pos(self, head, data, position):
        node = Node(data)


def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)


def insert_at_tail(head, data):
    node = Node(data)
    if head is None:
        return node
    elif head.next is None:
        head.next = node
    else:
        insert_at_tail(head.next, data)
    return head


lst = LinkedList()
print(insert_at_tail(lst.head, 1))
insert_at_tail(lst.head, 4)
insert_at_tail(lst.head, 2)
insert_at_tail(lst.head, 7)
insert_at_tail(lst.head, 8)
print_list(lst.head)
