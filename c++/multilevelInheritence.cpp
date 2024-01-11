#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Triangle {
public:
    void printTriangle() {
        std::cout << "I am a triangle" << std::endl;
    }
};

class Isosceles: public Triangle {
public:
    void printIsosceles() {
        std::cout << "I am an isosceles triangle" << std::endl;
    }
};

class Equilateral: public Isosceles {
public:
    void printEquilateral() {
        std::cout << "I am an equilateral triangle" << std::endl;
        printIsosceles();
        printTriangle();
    }
};


int main() {

    Equilateral e;

    e.printEquilateral();
}
