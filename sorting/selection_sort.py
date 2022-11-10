"""
Iterates over the list and swapping each 
element with the minimum (or maximum) element 
found in the unsorted list with that in the sorted list.
"""


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
