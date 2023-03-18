"""
Iterates over the given list,
figures out what the correct position of every element is,
and inserts it there.
"""


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            print(j)
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    print("Unsorted list is:", lst)
    insertion_sort(lst)
    print("Sorted list is: ", lst)

    # print()
    # arr = [31415926535897932384626433832795, 1, 3, 10, 3, 5]
    # insertion_sort(arr)
    # print("Sorted list is: ", arr)
