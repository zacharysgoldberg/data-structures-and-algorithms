#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <type_traits>
#include <utility>

template <typename T>
class AddElements {
private:
    T firstElement;

public:
    constexpr AddElements(const T first): firstElement{ first } {}

    constexpr T add(const T secondElement) const noexcept {
        return firstElement + secondElement;
    }
};

template<>
class AddElements<std::string> {
private:
    std::string str1;

public:
    AddElements(const std::string& str)
        noexcept: str1{ str } {}

    std::string concatenate(const std::string& str2) const noexcept {
        return str1 + str2;
    }
};

int start_up() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    return 0;
}

int static r = start_up();

// #define endl '\n';
// 'n' is faster than std::endl;

int main() {

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::string type;
        std::cin >> type;

        if (type == "string") {
            std::string str1, str2;
            std::cin >> str1 >> str2;
            AddElements<std::string> addString(str1);
            std::cout << addString.concatenate(str2) << "\n";
        }
        else if (type == "int") {
            int firstInt, secondInt;
            std::cin >> firstInt >> secondInt;
            AddElements<int> addInt(firstInt);
            std::cout << addInt.add(secondInt) << "\n";
        }
        else if (type == "float") {
            float firstFloat, secondFloat;
            std::cin >> firstFloat >> secondFloat;
            AddElements<float> addFloat(firstFloat);
            std::cout << addFloat.add(secondFloat) << "\n";
        }
    }
}
