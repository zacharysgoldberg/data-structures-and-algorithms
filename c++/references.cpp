#include <iostream>
#include <string>

using std::cout;


int a = 5;

int b = 10;

int& c = a;


void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {

    cout << "a: " << a << '\n';

    cout << "b: " << b << '\n';

    swap(a, b);

    cout << "\nswap(a, b)" << '\n';

    cout << "\na: " << a << '\n' << "b: " << b << '\n';

    cout << "\nc: " << c << '\n';

    c = 5;

    cout << "c = 5;" << '\n';

    cout << "a: " << a << '\n';

    //* Cannot reassign a reference to a different variable

    int d = 15;

    cout << "\nd: " << d << '\n';

    c = d;

    cout << "c = d;" << '\n';

    cout << "a: " << a << '\n';

    cout << "c: " << c << '\n';
}