from helper import Node, LinkedList


def print_linked_list(head):
    # curr = head
    # while curr:
    #     print(curr.data)
    #     curr = curr.next

    # [recursive]
    if head:
        print(head.data)
        print_linked_list(head.next)


def insert_node_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_node_at_tail(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    # curr = head
    # while curr.next:
    #     curr = curr.next
    # curr.next = new_node

    # [recursive]
    elif head.next is None:
        head.next = new_node
    else:
        insert_node_at_tail(head.next, data)
    return head


def insert_node_at_position(head, data, position):
    new_node = Node(data)
    # index = 0
    # curr = head
    # while curr:
    #     if index == position - 1:
    #         new_node.next = curr.next
    #         curr.next = new_node
    #         break
    #     else:
    #         curr = curr.next
    #         index += 1

    # [recursive]
    if head and position == 1:
        new_node.next = head.next
        head.next = new_node
    else:
        insert_node_at_position(head.next, data, position - 1)
    return head


def delete_node(head, position):
    curr = head
    index = 0
    if position == 0:
        head = head.next
        return head

    while index < position - 1:
        curr = curr.next
        index += 1
    print(curr.next.data)
    curr.next = curr.next.next
    return head


def reverse_print_linked_list(head):
    if head:
        reverse_print_linked_list(head.next)
        print(head.data)


def reverse_linked_list(head):
    nxt = head.next
    curr = head
    reverse = None
    while curr:
        curr.next = reverse
        reverse = curr
        curr = nxt
        if curr:
            nxt = nxt.next

    return reverse


def remove_duplicates(head):
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            # Reassign the next node value to the next value that's different
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


def has_cycle(head):
    curr = head
    node_set = set()

    while curr:
        if curr in node_set:
            return 1
        else:
            node_set.add(curr)
            curr = curr.next

    return 0
