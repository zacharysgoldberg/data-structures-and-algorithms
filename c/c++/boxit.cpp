#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Box {
private:
    int length, breadth, height;

public:
    // Constructors
    Box(): length(0), breadth(0), height(0) {}

    Box(int l, int b, int h) {
        length = l;
        breadth = b;
        height = h;
    }

    Box(const Box& B): length(B.length), breadth(B.breadth), height(B.height) {}

    // Functions
    int getLength() { return length; }

    int getBreadth() { return breadth; }

    int getHeight() { return height; }

    long long CalculateVolume() { return (long long)breadth * length * height; }
    // Operator Overload
    bool operator < (Box& B) {
        if (length < B.length) return true;
        else if (breadth < B.breadth && length == B.length) return true;
        else if (height < B.height && breadth == B.breadth && length == B.length) return true;
        else return false;
    }

    friend std::ostream& operator << (std::ostream& out, Box& B) {
        out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight();
        return out;
    };
};


int main() {

    int n;
    std::cin >> n;
    Box tmp;
    for (int i = 0; i < n; i++) {
        int type;
        std::cin >> type;
        if (type == 1) {
            std::cout << tmp << std::endl;
        }
        if (type == 2) {
            int l, b, h;
            std::cin >> l >> b >> h;
            Box NewBox(l, b, h);
            tmp = NewBox;
            std::cout << tmp << std::endl;
        }
        if (type == 3) {
            int l, b, h;
            std::cin >> l >> b >> h;
            Box NewBox(l, b, h);
            if (NewBox < tmp) {
                std::cout << "Lesser\n";
            }
            else {
                std::cout << "Greater\n";
            }
        }
        if (type == 4) {
            std::cout << tmp.CalculateVolume() << std::endl;
        }
        if (type == 5) {

            Box NewBox(tmp);
            std::cout << NewBox << std::endl;
        }
    }
