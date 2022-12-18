"""
Passes over the list, 
catches the maximum/minimum element, 
and brings it over to the right side.
"""


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i, -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def sort_binary_list(lst):
    # filter each item and compare them with the prev
    # if item is less than prev, swap them
    j = 0
    for i in range(len(lst)):
        if lst[i] < 1:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1

    return lst


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """
    sorted_lst = sorted(lst)
    return sorted_lst[-2], sorted_lst[-1]
