#include <vector>
#include <iostream>

/*
Iterates over the given array,
figures out what the correct position of every element is,
and inserts it there.
*/


void insertionSort(std::vector<int>& arr)
{
    for (int i = 1; i < arr.size(); i++)
    {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && key < arr[j])
        {
            std::cout << j << std::endl;
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

