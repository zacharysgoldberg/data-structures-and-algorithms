#include <vector>
#include <iostream>

class Solution
{
public:
    std::vector<std::vector<int>> result;

    void permutation(std::vector<int>& nums, int i)
    {
        if (i == nums.size())
        {
            result.push_back(nums);
            return;
        }

        for (int j = i; j < nums.size(); j++)
        {
            std::swap(nums[j], nums[i]);
            permutation(nums, i + 1);
            std::swap(nums[i], nums[j]);
        }
    }

    std::vector<std::vector<int>> permute(std::vector<int>& nums)
    {
        permutation(nums, 0);

        return result;
    }
};

int main()
{
    std::vector<int> nums = { 1, 2, 3 };

    Solution* sol = new Solution();

    sol->permute(nums);
}