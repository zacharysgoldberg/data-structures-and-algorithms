#include <vector>
#include <algorithm>

/*
Passes over the array,
catches the maximum/minimum element,
and brings it over to the right side.
*/

void bubbleSort(std::vector<int>& arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        for (int j = arr.size() - i; j > 0; j--)
        {
            if (arr[j] > arr[j + 1])
                arr[j], arr[j + 1] = arr[j + 1], arr[j];
        }
    }
}

std::vector<int> sortBinaryArray(std::vector<int>& arr)
{
    // filter each item and compare them with the prev
    // if item is less than prev, swap them
    int j = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] < 1)
            arr[i], arr[j] = arr[j], arr[i];
        j++;
    }
    return arr;
}

std::pair<int, int> findMaxProd(std::vector<int>& arr)
{
    /*
    Finds the pair having maximum product in a given array
    :param arr: A array of integers
    :return: A pair of integers
    */

    std::sort(arr.begin(), arr.end());
    std::pair<int, int> sortedPair = { arr[-2], arr[-1] };

    return sortedPair;
}