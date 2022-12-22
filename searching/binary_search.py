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


# ==============================================================================

def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    # Base case
    if low > high:
        return - 1
    if x >= lst[high]:
        return lst[high]

    mid = (low + high) // 2

    if lst[mid] < x and lst[mid] > lst[mid - 1] or lst[mid] == x:
        return lst[mid]
    elif lst[mid] < x and lst[mid] < lst[mid + 1]:
        find_floor(lst, mid + 1, high, x)
    elif lst[mid] > x:
        find_floor(lst, low, mid - 1, x)


def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """
    # Base case
    if x <= lst[low]:
        return lst[low]
    if x > lst[high]:
        return -1

    mid = (low + high) // 2
    print(lst[mid])

    if lst[mid] > x and lst[mid] < lst[mid + 1] or lst[mid] == x:
        return lst[mid]
    elif lst[mid] > x and lst[mid] > lst[mid - 1]:
        find_ceiling(lst, low, mid - 1, x)
    elif lst[mid] < x:
        if mid + 1 <= high and x <= lst[mid + 1]:
            return lst[mid + 1]
        find_ceiling(lst, mid + 1, high, x)


def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #
    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)

# ==================================================================================================

    """
    divide the given list into half (say lst1 and lst2) 
    and swap the second (right) half element of lst1 with the first (left) half element of lst2. 
    Keep doing this recursively for lst1 and lst2.
    """


def shuffle_list_rec(lst, low, high):
    if high - low > 1:
        mid = (low + high) // 2
        left = (low + mid) // 2
        right = mid + 1
        for i in range(left + 1, mid + 1):
            lst[i], lst[right] = lst[right], lst[i]
            right += 1

        shuffle_list_rec(lst, low, mid)
        shuffle_list_rec(lst, mid + 1, high)
    return lst


def shuffle_list(lst):
    """
    Shuffles the list
    :param lst: List of integers
    """
    log = math.log2(len(lst)) % 2
    if len(lst) != 2 and log == 0 or log == 1:
        return shuffle_list_rec(lst, 0, len(lst) - 1)

    return lst

# ==========================================================================================


def inversion_count(lst):
    """
    Function to find Inversion Count
    :param lst: List of integers
    :return: The inversion count of the list
    """
    return inversion_count_rec(lst, 0, len(lst) - 1)


def inversion_count_rec(lst, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        # left sub list
        count += inversion_count_rec(lst, low, mid)
        # right sub list
        count += inversion_count_rec(lst, mid + 1, high)
        # calculating both sub lists
        count += get_inversion_count(lst, low, high, mid)

    return count


def get_inversion_count(lst, low, high, mid):
    left = low
    right = mid + 1
    count = 0
    while left <= mid and right <= high:
        if lst[left] < lst[right]:
            left += 1
        else:
            count += (mid - left + 1)
            right += 1
    return count


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
