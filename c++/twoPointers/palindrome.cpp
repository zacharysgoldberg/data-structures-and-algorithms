#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;
using std::string;

//* e.g.
/*
void twoPointers(vector<int> array) {
    int left = 0;
    int right = array.size() - 1;

    while (left <= right) {
        left++;
        right--;
    }
}
*/


std::string isPalindrome(std::string inputString) {
    int left = 0;
    int right = inputString.size() - 1;

    while (left <= right) {
        if (inputString[left] != inputString[right]) {
            return false;
        }
        left++;
        right--;
    }

    return inputString;
}

int main() {
    std::vector<std::string> array = { "kayak", "hello", "RACECAR", "A", "ABCDABCD", "DCBAABCD" };

    for (int i = 0; i < array.size(); i++) {
        std::string result = isPalindrome(array[i]);

        std::cout << result << std::endl;
    }

    return 0;
}