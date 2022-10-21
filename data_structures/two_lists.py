from helpers import Node, DoubleNode, LinkedList, DoublyLinkedList


def compare_lists(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next

    if head1 or head2:
        return False
    return True


def merge_linked_lists(head1, head2):
    merged_head = LinkedList()  # Empty linked list
    merged = merged_head

    while head1 or head2:
        if head1 is None:
            merged.next = head2
            return merged_head.next

        elif head2 is None:
            merged.next = head1
            return merged_head.next

        else:
            if head1.data < head2.data:
                merged.next = head1
                head1 = head1.next
            else:
                merged.next = head2
                head2 = head2.next

        merged = merged.next

    return merged_head.next


# print(merge_linked_lists())

def get_node(head, n):
    curr = head
    index = 0
    lst = []
    while curr:
        lst.append(curr.data)
        curr = curr.next
        index += 1

    return lst[index - n - 1]


def find_merge_node(head1, head2):
    a = head1
    b = head2

    while a or b:
        if a == b:
            return a.data
        else:
            a = a.next if a else head2
            b = b.next if b else head1
