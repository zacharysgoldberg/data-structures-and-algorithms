"""
Divides a given list into two halves, 
sorts those halves, and merges them in order.
"""

# Works better on linked lists


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(lst, left, right)


def merge(lst, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    print("Unsorted list is:", lst)

    merge_sort(lst)
    print()
    print("Sorted list is: ", lst)
