#include <vector>

/*
Iterates over the array and swapping each
element with the minimum (or maximum) element
found in the unsorted array with that in the sorted array.
*/

void selectionSort(std::vector<int> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        int minIndex = i;
        for (int j = i + 1; j < arr.size(); j++)
        {
            if (arr[minIndex] > arr[j])
                minIndex = j;
        }
        arr[i], arr[minIndex] = arr[minIndex], arr[i];
    }
}


