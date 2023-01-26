#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    int n;
    std::vector<int> vec;

    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> vec[i];
    }

    int q;
    std::cin >> q;

    for (int i = 0; i < q; i++) {
        int val;
        std::vector<int>::iterator low;
        std::cin >> val;

        low = std::lower_bound(vec.begin(), vec.end(), val);

        if (vec[low - vec.begin()] == val) {
            std::cout << "Yes " << low - vec.begin() + 1 << std::endl;
        }
        else {
            std::cout << "No " << low - vec.begin() + 1 << std::endl;
        }
    }

}
