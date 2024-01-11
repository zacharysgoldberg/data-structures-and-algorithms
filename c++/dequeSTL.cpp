#include <iostream>
#include <deque> 
#include <algorithm>

void printKMax(int arr[], int n, int k) {
    std::deque<int> deq;

    for (int i = 0; i < n; i++) {
        if (deq.empty()) deq.push_back(i);
        // remove elements outside the current window
        if (deq.front() <= i - k) deq.pop_front();
        // move max element to the front
        while (!deq.empty() && arr[i] >= arr[deq.back()]) {
            deq.pop_back();
        }

        deq.push_back(i);
        // print out only when the first window is completed
        if (i >= k - 1) {
            std::cout << arr[deq.front()] << ' ';
        }
    }

    std::cout << '\n';
}

int main() {

    int t;
    std::cin >> t;

    while (t > 0) {
        int n, k;
        std::cin >> n >> k;

        int i;
        int arr[n];

        for (i = 0;i < n;i++)
            std::cin >> arr[i];

        printKMax(arr, n, k);
        t--;
    }
}
