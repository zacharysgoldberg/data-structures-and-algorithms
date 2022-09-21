from helper import Node, LinkedList


def insert_node_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_node_at_tail(head, data):
    new_node = Node(data)
    curr = head
    if head is None:
        head = new_node
        return head

    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head


def insert_node_at_position(head, data, position):
    new_node = Node(data)
    curr = head
    index = 0
    while curr:
        if index == position - 1:
            new_node.next = curr.next
            curr.next = new_node
            break
        else:
            curr = curr.next
            index += 1

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
