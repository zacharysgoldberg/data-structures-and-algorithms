#include <iostream>
#include <vector>
#include <algorithm>

using std::cout;
using std::endl;


bool findSumOfThree(std::vector<int>& nums, int target) {
    std::sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++) {
        int low = i + 1, high = nums.size() - 1;

        while (low < high) {
            int sum = nums[i] + nums[low] + nums[high];
            if (sum == target)
                return true;
            else if (sum > target)
                high--;
            else
                low++;
        }
    }
    return false;
}

void print(std::vector<int> nums) {
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}

int main() {

    std::vector<std::vector<int>> numsLists = {
        {3, 7, 1, 2, 8, 4, 5},
        {-1, 2, 1, -4, 5, -3},
        {2, 3, 4, 1, 7, 9},
        {1, -1, 0},
        {2, 4, 2, 7, 6, 3, 1} };

    std::vector<std::vector<int>> testLists = {
        {10, 20, 21},
        {-8, 0, 7},
        {8, 10, 20},
        {1, -1, 0},
        {8, 11, 15} };

    for (int i = 0; i < numsLists.size(); i++)
    {
        for (int j = 0; j < testLists[i].size(); j++)
        {
            if (findSumOfThree(numsLists[i], testLists[i][j]))
                std::cout << " \tSum for " << testLists[i][j] << " exists" << std::endl;
            else
                std::cout << " \tSum for " << testLists[i][j] << " does not exist" << std::endl;
        }
        std::cout << std::string(100, '-') << std::endl;
    }
}