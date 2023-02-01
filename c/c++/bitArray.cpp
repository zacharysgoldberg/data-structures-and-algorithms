#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>


int main() {
    unsigned int N, S, P, Q;
    std::cin >> N >> S >> P >> Q;

    int x = std::pow(2, 31);

    unsigned int count = 0, a = S, ap = S;

    while (++count < N) {
        a = (a * P + Q) % std::abs(x + 1);  // adjust for negative int
        if (a == S || a == ap) break;
        ap = a;
    }

    std::cout << count;
}
