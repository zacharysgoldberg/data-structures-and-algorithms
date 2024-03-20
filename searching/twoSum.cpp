#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution
{

    std::vector<int> twoSum(std::vector<int>& nums, int& target)
    {
        std::vector<int> result;
        std::unordered_map<int, int> possiblePairs; // { num, index }

        for (int i = 0; i < nums.size(); i++)
        {
            int num = nums.at(i);
            int difference = target - num;

            auto pairFound = possiblePairs.find(difference);

            if (pairFound != possiblePairs.end())
            {

                result.push_back(i);
                result.push_back(pairFound->second);
            }
            else
            {
                possiblePairs.insert({ num, i });
            }
        }

        return result;
    }
};