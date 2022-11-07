from helpers import HashEntry


class HashTable:
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table. Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6    # for resizing to avoid collisions

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        for item in self.bucket:
            head = item
            while head:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.data)
                else:
                    node = new_bucket[new_index]
                    while node:
                        if node.key is head.key:
                            node.data = head.data
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.data)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, data):
        index = self.get_index(key)
        if self.bucket[index] == HashEntry(key, data):
            self.size += 1
        else:
            head = self.bucket[index]
            while head:
                if head.key == key:
                    head.data = data
                    break
                elif head.next is None:
                    head.next = HashEntry(key, data)
                    self.size += 1
                    break
                head = head.next
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        while head:
            if head.key == key:
                return head.data
            head = head.next
        return None

    def delete(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        # If key exists at first slot
        if head.key == key:
            self.bucket[index] = head.next
            self.size -= 1
            return
        # Find the key in slots
        prev = None
        while head:
            if head.key == key:
                prev.next = head.next
                self.size -= 1
                return
            # Else keep moving in chain
            prev = head
            head = head.next

        return


def is_subset(list1, list2):
    s = set(list1)
    for el in list2:
        if el not in s:
            return False
    return True


def is_disjoint(list1, list2):
    s = set(list1)
    for el in list2:
        if el in s:
            return False
    return True


def find_symmetric(my_list):
    pairs = set()
    result = []
    for el in my_list:
        pair = tuple(el)
        el.reverse()
        reverse_pair = tuple(el)
        if reverse_pair in pairs:
            result.append(list(reverse_pair))
            result.append(list(pair))
        else:
            pairs.add(pair)

    return result


"""
Create a reverse dict of the given dict i.e if the given dict has (N,C)
then reverse dict will have (C,N) as key-value pair
Traverse original dict and see if it's key exists in reverse dict
If it doesn't exist then we found our starting point.
After the starting point is found, simply trace the complete path
from the original dict.
"""


def trace_path(my_dict):
    reverse_dict = dict()
    for key in my_dict.keys():
        reverse_dict[my_dict.get(key)] = key
    curr_loc = None
    for key in my_dict.keys():
        if key not in reverse_dict.keys():
            curr_loc = key  # Found starting point
            break
    result = []
    next_loc = my_dict.get(curr_loc)
    while next_loc:
        result.append(list([curr_loc, next_loc]))
        curr_loc = next_loc
        next_loc = my_dict.get(next_loc)

    return result
