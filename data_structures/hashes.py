from helpers import HashNode, Node
from singly_linked_lists import LinkedList


class HashTable:
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table. Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashNode objects (by default all None)
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
                    new_bucket[new_index] = HashNode(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node:
                        if node.key is head.key:
                            node.value = head.value
                        elif node.next is None:
                            node.next = HashNode(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        index = self.get_index(key)
        if self.bucket[index] == HashNode(key, value):
            self.size += 1
        else:
            head = self.bucket[index]
            while head:
                if head.key == key:
                    head.value = value
                    break
                elif head.next is None:
                    head.next = HashNode(key, value)
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
                return head.value
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


def trace_path(my_dict):
    """
    Create a reverse dict of the given dict i.e if the given dict has (N,C)
    then reverse dict will have (C,N) as key-value pair
    Traverse original dict and see if it's key exists in reverse dict
    If it doesn't exist then we found our starting point.
    After the starting point is found, simply trace the complete path
    from the original dict.
    """
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


# O(n^2)

def find_pair(my_list):
    """
    Create a dictionary with the key being the sum
    and the value being a pair, i.e key = 3 , value = {1,2}
    Traverse all possible pairs in my_list and store sums in my_dict
    If sum already exists then print out the two pairs.
    """
    result = []
    pairs = dict()
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            sum = my_list[i] + my_list[j]
            if sum not in pairs:
                pairs[sum] = [my_list[i], my_list[j]]
            else:
                result.append(pairs[sum])
                result.append([my_list[i], my_list[j]])
                print(pairs)
                return result


# O(n)

def find_pairs(my_list):
    result = []
    pairs = dict()
    low = 0
    high = len(my_list) - 1
    while low != len(my_list) - 1:
        sum = my_list[low] + my_list[high]
        if low == high:
            high = len(my_list) - 1
            low += 1
        elif sum not in pairs:
            pairs[sum] = [my_list[low], my_list[high]]
            high -= 1
        else:
            result.append(pairs[sum])
            result.append([my_list[low], my_list[high]])
            high -= 1

    return result


def find_sub_zero(my_list):
    """
    3 Conditions:
    If 0 exists in the list
    If the sum becomes zero in the iteration
    If the sum reverts back to a value which was already a key in the hash table. 
    This means that there was a sublist that has a sum of zero making the overall sum to go back to a previous value
    """
    my_dict = dict()
    sum = 0
    for el in my_list:
        sum += el
        if el == 0 or sum == 0 or my_dict.get(sum):
            return True
        my_dict[sum] = el
    return False


def is_formation_possible(lst, word):
    hash_table = HashTable()
    for el in lst:
        hash_table.insert(el, True)
    # Slice the word into two strings in each iteration
    for i in range(len(lst) - 1):
        first_word = word[0: i]
        second_word = word[i:]
        if hash_table.search(first_word) and hash_table.search(second_word):
            return True

    return False


def find_sum(lst, k):
    nums = set()
    for el in lst:
        if k - el in nums:
            return [k - el, el]
        nums.add(el)

    return False


def findFirstUnique(lst):
    counts = dict()
    # Initializing dictionary with pairs like (lst[i], count)
    counts = counts.fromkeys(lst, 0)
    for el in lst:
        counts[el] += 1
    for el in lst:
        if counts[el] == 1:
            return el
    return None


def detect_loop(lst):
    visited = set()
    head = lst.get_head()
    while head:
        if head.data in visited:
            return True
        visited.add(head.data)
        head = head.next_element
    return False
