#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

int main() {
    int t;
    double a, b, c;

    std::cin >> t;
    for (int i = 0; i < t; i++) {
        std::cin >> a >> b >> c;

        // A
        std::cout << std::hex << std::left << std::showbase << std::nouppercase << (long long)a << std::endl;

        // B
        std::cout << std::dec << std::right << std::setw(15) << std::setfill('_') << std::showpos << std::fixed
            << std::setprecision(2) << b << std::endl;

        // C
        std::cout << std::scientific << std::uppercase << std::noshowpos << std::setprecision(9) << c << std::endl;
    }

}
