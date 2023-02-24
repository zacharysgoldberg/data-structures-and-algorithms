#include <iostream>
#include <vector>

using namespace std;

/*
1.  Initialize two pointers.
    Move the slow pointer one time forward/backward and the fast pointer two times forward/backward

2.  If loop direction changes at any point, return False

3.  If the direction does not change, check whether both pointers meet at the same node then loop is detected

4.  Repeat until there are exactly n elements in an array
*/

int next(vector<int>& array, int i) {
    return (array[i] + i + array.size()) % array.size();
}


bool circularArrayLoop(vector<int>& array) {
    for (int i = 0; i < array.size(); i++) {
        int slow = i, fast = i;

        if (array[i] == 0) continue;

        while (array[next(array, slow)] * array[i] > 0 &&
            array[next(array, fast)] * array[i] > 0 &&
            array[next(array, next(array, fast))] * array[i] > 0) {

            slow = next(array, slow);
            fast = next(array, next(array, fast));

            if (slow == fast) {
                if (slow == next(array, slow)) break;
                else return true;
            }
        }
        slow = i;
        while (array[slow] * array[i] > 0) {
            int temp = next(array, slow);
            array[slow] = 0;
            slow = temp;
        }
    }
    return false;
}


int main() {
    std::vector<std::vector<int>> input = {
           {-2, -3, -9},
           {-5, -4, -3, -2, -1},
           {-1, -2, -3, -4, -5},
           {2, 1, -1, -2},
           {-1, -2, -3, -4, -5, 6},
           {1, 2, -3, 3, 4, 7, 1}
    };
    for (int i = 0; i < input.size(); i++) {
        // std::cout << i + 1 << ".\tGiven arr: " << PrintArray(input[i]) << "\n";
        cout << "\n\t\tProcessing... \n";
        bool res = circularArrayLoop(input[i]);
        cout << "\n\tFound loop: " << boolalpha << res << "\n";
        cout << string(100, '-') << "\n";
    }

    return 0;
}