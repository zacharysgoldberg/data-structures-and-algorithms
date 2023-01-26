#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    int n, x, a, b;
    std::vector<int> vec;

    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int v;
        std::cin >> v;
        vec.push_back(v);
    }
    std::cin >> x >> a >> b;

    vec.erase(vec.begin() + x - 1);
    vec.erase(vec.begin() + a - 1, vec.begin() + b - 1);

    std::cout << vec.size() << std::endl;
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
}
