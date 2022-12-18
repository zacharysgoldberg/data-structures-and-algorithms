import math


def binary_search(lst, target):
    low = 0
    high = len(lst)

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid

    return None


def pivoted_binary_search(lst, key):
    low = 0
    high = len(lst)

    while low < high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        elif lst[low] <= lst[mid]:
            if lst[low] <= key and lst[mid] > key:
                high = mid
            else:
                low = mid + 1
        else:
            if lst[high - 1] >= key and lst[mid] < key:
                low = mid + 1
            else:
                high = mid

    return None


"""
A function to find a number in a 2D list
:param lst: A 2D list of integers
:param number: A number to be searched in the 2D list
:return: True if the number is found, otherwise False
"""


def find_in(lst, number):
    # Since both the rows and the columns are sorted, \
    # we can first apply binary search on rows and then, \
    # binary search on the columns.
    rows = len(lst)
    cols = len(lst[0])

    low = 0
    high = rows - 1

    if rows > 1:
        while low <= high:
            mid = (high + low) // 2
            if lst[mid][cols - 1] == number:
                return True
            elif lst[mid][cols - 1] < number:
                low = mid + 1
            else:
                high = mid - 1
        if lst[mid][cols - 1] < number:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0

    if rows >= len(lst):
        return False

    low = 0
    high = cols - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[rows][mid] == number:
            return True
        elif lst[rows][mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return False


"""
A function to solve Dutch National Flag Problem
:param lst: A list of integers
:return: A list of solved Dutch National Flag Problem
"""


def dutch_national_flag(lst):
    low = 0
    high = len(lst) - 1
    mid = 0
    # keeps track of the index of last zero in the list (low), \
    # the position of the last two present (high), \
    # and an index mid that moves ahead only when it has found a 1 or when a 0 is swapped with any 1.
    while mid <= high:
        if lst[mid] == 0:
            lst[mid], lst[low] = lst[low], lst[mid]
            low += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1
        else:
            mid += 1

    return lst

# ==========================================

# [Search in a Sorted Infinite Array]


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def bnry_search(reader, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if reader.get(mid) < key:
            low += 1
        elif reader.get(mid) > key:
            high -= 1
        else:
            return mid

    return -1


def search_in_infinite_array(reader, key):
    low, high = 0, 1
    while reader.get(high) < key:
        new_low = high + 1
        high += (high - low + 1) * 2
        # increase to double the bounds size
        low = new_low

    indx = bnry_search(reader, key, low, high)
    return indx


# Next Letter

def search_next_letter(letters, key):
    low = 0
    high = len(letters) - 1
    while low <= high:
        mid = (low + high) // 2
        if letters[mid] > key:
            high -= 1
        else:
            low += 1

    return letters[low % len(letters)]


def main():
    # reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    # print(search_in_infinite_array(reader, 16))
    # print(search_in_infinite_array(reader, 11))
    # reader = ArrayReader([1, 3, 8, 10, 15])
    # print(search_in_infinite_array(reader, 15))
    # print(search_in_infinite_array(reader, 200))

    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
