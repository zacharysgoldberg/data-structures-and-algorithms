#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

int main() {
    int queries;
    std::set<int> s;

    std::cin >> queries;

    for (int i = 0; i < queries; i++) {
        int y, x;
        std::cin >> y >> x;

        std::set<int>::iterator itr = s.find(x);

        if (y == 1) s.insert(x);
        else if (y == 2 && itr != s.end()) s.erase(x);
        else if (y == 3) {
            itr != s.end() ? std::cout << "Yes\n" : std::cout << "No\n";
        }
    }
}
