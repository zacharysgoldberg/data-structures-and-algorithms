#include <iostream>
#include <vector>

using namespace std;

/*
1.  Move the slow pointer x steps forward/backward, where x is the value at the itℎ index of the array

2.  Move the fast pointer x steps forward/backward and do this again for the value at the (i + 1)tℎ index of the array.

3.  Return TRUE when both pointers meet at the same point.

4.  If the direction changes at any point, then break the loop and follow the steps above for the next element of the array.

5.  Return FALSE if we have traversed every element of the array without finding a loop.
*/

int next_step(vector<int> arr, int index, bool current_direction) {
    int arr_size = arr.size();
    bool new_direction = false;
    if (arr[index] >= 0)
        new_direction = true;
    // Loop can't be found if the loop direction is changed
    // or the value of the array element is equal to the length of the array
    if (new_direction != current_direction || abs(arr[index] % arr_size) == 0)
        return -1;
    return (index + arr[index] + arr_size) % arr_size;
}

bool circular_array_loop(vector<int> arr) {
    bool current_direction = false;

    for (int i = 0; i < arr.size(); i++) {
        if (abs(arr[i]) == arr.size())
            continue;
        if (arr[i] >= 0)
            current_direction = true;
        else
            current_direction = false;
        int slow = i, fast = i;

        while (slow != fast || slow != -1 || fast != -1) {
            // Move slow pointer one step and fast pointer two
            // steps forward/backward
            slow = next_step(arr, slow, current_direction);
            if (slow == -1)
                break;
            fast = next_step(arr, fast, current_direction);
            if (fast != -1)
                fast = next_step(arr, fast, current_direction);
            if (slow == fast || fast == -1)
                break;
        }
        if (slow == fast && slow != -1)
            return true;
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
        bool res = circular_array_loop(input[i]);
        cout << "\n\tFound loop: " << boolalpha << res << "\n";
        cout << string(100, '-') << "\n";
    }

    return 0;
}