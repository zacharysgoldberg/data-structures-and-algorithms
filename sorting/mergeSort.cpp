#include <vector>
#include <cmath>

/*
Divides a given array into two halves,
sorts those halves, and merges them in order.
*/

// Works better on linked lists


void mergeSort(std::vector<int>& arr)
{
    if (arr.size() > 1)
    {
        int mid = std::floor(arr.size() / 2);
        std::vector<int> left;
        std::vector<int> right;

        for (int i = 0; i < mid; i++)
        {
            left.push_back(arr[i]);
        }
        for (int i = mid; i < arr.size(); i++)
        {
            right.push_back(arr[i]);
        }

        mergeSort(left);
        mergeSort(right);

        merge(arr, left, right);
    }
}


void merge(std::vector<int>& arr, std::vector<int>& left, std::vector<int>& right)
{
    int i, j, k = 0;

    while (i < left.size() && j < right.size())
    {
        if (left[i] < right[j])
        {
            arr[k] = left[i];
            i++;
        }
        else
        {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < left.size())
    {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < right.size())
    {
        arr[k] = right[j];
        j++;
        k++;
    }
}
