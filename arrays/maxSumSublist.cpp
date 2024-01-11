#include <vector>

int maxSumSublist(std::vector<int>& arr)
{
    int maxValue = arr[0];
    int currMax = arr[0];

    for (int i = 1; i < arr.size(); i++)
    {
        if (currMax < 0)
        {
            currMax = arr[i];
        }
        else
        {
            currMax += arr[i];
        }
        if (currMax > maxValue)
            maxValue = currMax;
    }
    return maxValue;
}