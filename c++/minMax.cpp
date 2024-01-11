#include <iostream>
#include <string>
#include <vector>


int getMin(std::vector<int> nums, int size) {
    int min = nums[0];

    for (int i = 0; i < size; i++) {
        if (nums[i] < min) {
            min = nums[i];
        }
    }

    return min;
}


int getMax(std::vector<int> nums, int size) {
    int max = nums[0];

    for (int i = 0; i < size; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }

    return max;
}


void getMinAndMax(std::vector<int> nums, int size, int* min, int* max) {
    for (int i = 0; i < size; i++) {
        if (nums[i] < *min) {
            *min = nums[i];
        }
    }

    for (int i = 0; i < size; i++) {
        if (nums[i] > *max) {
            *max = nums[i];
        }
    }
}


int main() {
    std::vector<int> nums = { 5, 4, -2, 29, 6 };

    // int min = getMin(nums, nums.size());
    // int max = getMax(nums, nums.size());

    // std::cout << "Min: " << min << std::endl;
    // std::cout << "Max: " << max << std::endl;

    int min = nums[0];
    int max = nums[0];

    // std::cout << *min << " " << *max << '\n';

    getMinAndMax(nums, nums.size(), &min, &max);

    std::cout << "Min: " << min << '\n';
    std::cout << "Max: " << max << '\n';

    return 0;
}