#include <vector>
#include <algorithm>

int* findSum(std::vector<int>& vec, int& n)
{
    std::sort(vec.begin(), vec.end());
    int low = 0;
    int high = vec.size() - 1;

    while (low != high)
    {
        if (vec[low] + vec[high] < n)
            low++;
        else if (vec[low] + vec[high] > n)
            high--;
        else
        {
            int arr[2] = { vec[low], vec[high] };
            return arr;
        }
    }
}