#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Triangle {
public:
    void triangle() {
        std::cout << "I am a triangle" << std::endl;
    }
};

class Isosceles: public Triangle {
public:
    Isosceles() {
        std::cout << "I am an isosceles triangle" << std::endl;
    }

    void isosceles() {
        std::cout << "In an isosceles triangle two sides are equal" << std::endl;
    }
};

int main() {
    Isosceles isc;
    isc.isosceles();
    isc.triangle();
    return 0;
}
