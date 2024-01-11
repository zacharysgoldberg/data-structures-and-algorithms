#include <vector>

/*
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
*/

// The fastest - known, comparison - based sorting algorithm

void quickSort(std::vector<int>& arr, int low, int high)
{
    if (low < high)
    {
        // find pivot element such that
        // element smaller than pivot are on the left
        // element greater than pivot are on the right
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi--);
        quickSort(arr, pi++, high);
    }
}

int partition(std::vector<int>& arr, int& low, int& high)
{
    int pivot = arr[high];
    // pointer for greater element
    int i = low - 1;
    // traverse through all elements
    // compare each element with pivot

    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            // if element smaller than pivot is found
            // swap it with the greater element pointed by i
            i++;
            arr[i], arr[j] = arr[j], arr[i];
        }
    }
    // swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1];
    return i + 1;
}
