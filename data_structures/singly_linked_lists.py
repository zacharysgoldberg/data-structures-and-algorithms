from helpers import Node


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

    def is_empty(self):
        if self.head is None:  # Check whether the head is None
            return True
        else:
            return False

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.head
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if first_element:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def insert_node_at_head(self, head, data):
        new_node = Node(data)
        new_node.next = head
        return new_node

    # [recursive]

    def insert_node_at_tail(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        elif head.next is None:
            head.next = new_node
        else:
            self.insert_node_at_tail(head.next, data)
        return head

    def insert_at_tail(self, lst, data):
        node = Node(data)
        if not lst.head:
            lst.head_node = node
            return

        head = lst.head
        while head.next_element:
            head = head.next_element
        head.next_element = node
        return lst

    def search(self, lst, data):
        head = lst.head
        if not head:
            return False  # value not found
        if head.data == data:
            return True  # value found
        return self.search(head.next_element, data)

    def delete(self, lst, data):
        if lst.is_empty():  # Check if list is empty -> Return False
            return False
        curr = lst.head
        prev = None
        if curr.data == data:
            lst.delete_at_head()
            return True
        while curr:
            if curr.data == data:
                prev.next_element = curr.next_element
                curr.next_element = None
                return True
            prev = curr
            curr = curr.next_element

        return False

    def length(self, lst):
        lst_length = 0

        curr = lst.head
        while curr:
            lst_length += 1
            curr = curr.next_element
        return lst_length

    def insert_node_at_position(self, head, data, position):
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
            self.insert_node_at_position(head.next, data, position - 1)
        return head

    def reverse_print_linked_list(self, head):
        if head:
            self.reverse_print_linked_list(head.next)
            print(head.data)

    def reverse(self, lst):
        prev = None
        curr = lst
        while curr:
            next = curr.next_element
            curr.next_element = prev
            prev = curr
            curr = next
            lst = prev

        return lst

    def remove_duplicates1(self, head):
        curr = head
        while curr.next:
            if curr.data == curr.next.data:
                # Reassign the next node value to the next value that is different
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

    def remove_duplicates2(self, lst):
        outer = lst.head
        while outer:
            inner = outer
            while inner:
                if inner.next_element:
                    if outer.data == inner.next_element.data:
                        inner.next_element = inner.next_element.next_element
                    else:
                        inner = inner.next_element
                else:
                    inner = inner.next_element
            outer = outer.next_element
        return lst

    # [Most Efficient]

    def remove_duplicates3(self, lst):
        visited = set()
        curr = lst.head
        prev = None
        while curr:
            if curr.data not in visited:
                visited.add(curr.data)
                prev = curr
                curr = curr.next_element
            else:
                curr.next_element = None
                prev.next_element = curr.next_element
                curr = curr.next_element
        return lst

    def get_node(self, head, n):
        nodes = []
        length = 0
        curr = head.head_node
        while curr:
            nodes.append(curr.data)
            curr = curr.next_element
            length += 1
        position = length - n + 1
        if not nodes or position < 0 or position > length:
            return -1
        return nodes[position - 1]

    def has_cycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return 1
            else:
                visited.add(curr)
                curr = curr.nexts
        return 0

    def detect_loop(self, lst):
        one = lst.head
        two = lst.head
        while one and two and two.next_element:
            one = one.next_element
            two = one.next_element.next_element
            if one == two:
                return True
        return False

    def find_mid(self, lst):
        left = lst.head
        right = lst.head.next_element
        while right and right.next_element:
            left = left.next_element
            right = right.next_element.next_element
        return left.data

    def intersection(self, list1, list2):
        res = LinkedList()
        visited = set()
        curr1 = list1.head
        curr2 = list2.head
        while curr1:
            if curr1.data not in visited:
                visited.add(curr1.data)
            curr1 = curr1.next_element

        while curr2:
            if curr2.data in visited:
                res.append(curr2.data)
            curr2 = curr2.next_element
        return res


def print_linked_list(head):
    # curr = head
    # while curr:
    #     print(curr.data)
    #     curr = curr.next

    # [recursive]
    if head:
        print(head.data)
        print_linked_list(head.next)


def delete_node(head, data):
    curr = head
    prev = None
    if head is None:
        return None
    elif curr.data == data:
        head = head.next_element
        return head
    while curr:
        if curr.data == data:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next


def delete_node_at_pos(head, position):
    curr = head
    index = 0
    if position == 0:
        head = head.next
        return head
    while index < position - 1:
        curr = curr.next
        index += 1
    curr.next = curr.next.next


if __name__ == '__main__':
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(5)
    lst.append(8)
    print_linked_list(lst.head)
    delete_node_at_pos(lst.head, 2)
    print("========================")
    print_linked_list(lst.head)
    delete_node(lst.head, 5)
    print("========================")
    print_linked_list(lst.head)
