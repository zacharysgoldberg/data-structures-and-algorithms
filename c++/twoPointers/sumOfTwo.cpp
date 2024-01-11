#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;

    for (int i = 0; i < nums.size(); i++) {
        if (map.find(target - nums[i]) == map.end())
            map[nums[i]] = i;
        else
            return { map[target - nums[i]], i };
    }

    return { -1, -1 };
}


int main() {

    vector<int> nums = { -10,7,19,15 };

    vector<int> result = twoSum(nums, 9);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }

    return 0;
}