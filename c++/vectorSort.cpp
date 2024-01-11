#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    int n;
    std::cin >> n;

    std::vector<int> vec;
    for (int i = 0; i < n; i++) {
        int v;
        std::cin >> v;
        vec.push_back((v));
    }
    // Sorting Vector
    sort(vec.begin(), vec.end());

    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
}
