from helper import DoubleNode


def sorted_insert_node(head, data):
    node = DoubleNode(data)
    cur = head
    if head is None:
        head = node
        return head
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
                return head
            else:
                cur = cur.next
        cur.next = node
        node.prev = cur
        return head


def reverse_doubly_linked_list(head):
    reverse = head
    curr = head
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        reverse = curr
        curr = curr.prev

    return reverse
