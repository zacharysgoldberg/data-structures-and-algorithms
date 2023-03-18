"""
Repeatedly partitions the input into low and high parts, 
and then recursively sorts each of those parts. 
To partition the input, quicksort chooses a 
pivot to divide the data into low and high parts
"""

"""
STEPS:
1. Start with a list of n elements
2. Choose a pivot element from the list to be sorted
3. Partition the list into 2 unsorted sublists, 
    such that all elements in one sublist are less than the pivot 
    and all the elements in the other sublist are greater than the pivot
4. Elements that are equal to the pivot can go in either sublist
5. Sort each sublist recursively to yield two sorted sublists
6. Concatenate the two sorted sublists and the pivot to yield one sorted list
"""

# The fastest-known, comparison-based sorting algorithm


def quick_sort(lst, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)


def partition(lst, low, high):
    pivot = lst[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if lst[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    # swap the pivot element with the greater element specified by i
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


if __name__ == '__main__':

    lst = [5, 4, 2, 1, 3]
    print("Unsorted list: ", lst)

    quick_sort(lst, 0, len(lst) - 1)
    print()
    print("Sorted list: ", lst)
