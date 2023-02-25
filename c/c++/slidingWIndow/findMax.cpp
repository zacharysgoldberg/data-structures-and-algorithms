#include <iostream>
#include <vector>
#include <deque>
#include <string>

using namespace std;


/*
1.  Process the first w elements to initiate the window deque

2.  Start iterating the array/vector

3.  In the window, only keep the indexes of elements from the current sliding window

4.  Remove indexes of all elements smaller than the current element from the window

5.  Add the current element to the window

6.  Add the first element of the window to the output list

7.  Repeat the above steps until the entire array/vector is traversed
*/


vector<int> findMaxSlidingWindow(vector<int>& nums, int windowSize) {
    vector<int> result;
    deque<int> window;

    // Initial window
    for (int i = 0; i < windowSize; i++) {
        while (!window.empty() && nums[i] >= nums[window.back()])
            window.pop_back();

        window.push_back(i);
    }

    result.push_back(nums[window.front()]);
    // Rest of array/vector
    for (int i = windowSize; i < nums.size(); i++) {
        while (!window.empty() && nums[i] >= nums[window.back()])
            window.pop_back();

        if (!window.empty() && window.front() <= i - windowSize)
            window.pop_front();

        window.push_back(i);
        result.push_back(nums[window.front()]);
    }

    // Without using indexes
    /*
    for (int i = 0; i < nums.size(); i++) {
        while (!window.empty() && window.back() < nums[i])
            window.pop_back();

        window.push_back(nums[i]);
        if (i >= windowSize - 1) {
            result.push_back(window.front());
            if (nums[i - windowSize + 1] == window.front())
                window.pop_front();
        }

    }
    */

    return result;
}


ostream& operator <<(ostream& out, vector<int>& nums) {
    cout << "[ ";
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << ' ';
    }
    cout << ']';
    return out;
}

int main() {
    std::vector<int> targetList = { 3, 3, 3, 3, 2, 4, 3, 2, 3, 18 };
    std::vector<std::vector<int>> numsList = { {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
                 {10, 9, 8, 7, 6, 5, 4, 3, 2, 1},
                 {10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
                 {1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30},
                 {10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67},
                 {4, 5, 6, 1, 2, 3},
                 {9, 5, 3, 1, 6, 3},
                 {2, 4, 6, 8, 10, 12, 14, 16},
                 {-1, -1, -2, -4, -6, -7},
                 {4, 4, 4, 4, 4, 4, } };

    for (int i = 0; i < targetList.size(); i++) {
        std::cout << i + 1 << ".\tOriginal array:\t" << numsList[i] << std::endl;
        std::cout << "\tWindow size:\t" << to_string(targetList[i]) << std::endl;
        vector<int> result = findMaxSlidingWindow(numsList[i], targetList[i]);
        std::cout << "\n\tMax:\t" << result << std::endl;
        std::cout << std::string(100, '-') << std::endl;
    }

    return 0;
}