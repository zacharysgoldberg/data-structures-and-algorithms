#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

// Base
class Rectangle {
protected:
    int width, height;

public:
    Rectangle(): width(0), height(0) {}

    void display() {
        std::cout << width << " " << height << std::endl;
    }
};

// Derived
class RectangleArea: public Rectangle {
public:
    void read_input() {
        std::cin >> width >> height;
    }

    void display() {
        std::cout << width * height << std::endl;
    }
};

int main() {
    RectangleArea rectangleArea;

    rectangleArea.read_input();

    rectangleArea.Rectangle::display();

    rectangleArea.display();
}
