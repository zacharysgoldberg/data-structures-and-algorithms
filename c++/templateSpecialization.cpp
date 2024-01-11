#include <iostream>

enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };

template <typename T> struct Traits;

template <>
class Traits <Fruit> {
public:
    static std::string name(int index) {
        switch (index) {
        case 0: return "apple";
        case 1: return "orange";
        case 2: return "pear";
        }
        return "unknown";
    }
};

template <>
class Traits <Color> {
public:
    static std::string name(int index) {
        switch (index) {
        case 0: return "red";
        case 1: return "green";
        case 2: return "orange";
        }
        return "unknown";
    }
};


int main()
{
    int t = 0; std::cin >> t;

    for (int i = 0; i != t; ++i) {
        int index1; std::cin >> index1;
        int index2; std::cin >> index2;
        std::cout << Traits<Color>::name(index1) << " ";
        std::cout << Traits<Fruit>::name(index2) << "\n";
    }
}
