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
