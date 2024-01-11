#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Complex {
public:
    int a, b;

    void input(std::string str) {
        int v1 = 0;
        int i = 0;

        while (str[i] != '+') {
            v1 = v1 * 10 + str[i] - '0';
            i++;
        }

        while (str[i] == ' ' || str[i] == '+' || str[i] == 'i') {
            i++;
        }

        int v2 = 0;

        while (i < str.length()) {
            v2 = v2 * 10 + str[i] - '0';
            i++;
        }

        a = v1;
        b = v2;
    }
};

Complex operator + (const Complex& A, const Complex& B) {
    return { A.a + B.a, A.b + B.b };
}

std::ostream& operator << (std::ostream& out, const Complex& C) {
    out << C.a << (C.b > 0 ? '+' : '-') << 'i' << C.b;
    return out;
}


int main() {

    Complex a, b;

    std::string s1, s2;

    std::cin >> s1;
    std::cin >> s2;

    a.input(s1);
    b.input(s2);

    Complex c = a + b;

    std::cout << c << std::endl;
}