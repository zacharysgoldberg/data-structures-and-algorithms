#include <stdio.h>
#include <iostream>
#include <vector>

void update(int* a, int* b) {
    int sum = *a + *b;
    int absDiff = *a - *b > 0 ? (*a - *b) : -(*a - *b);
    *a = sum;
    *b = absDiff;
}

int main() {
    //* Pointers and References

    int a = 4;
    int b = 5;
    int* pa = &a, * pb = &b;

    std::cout << a << " " << b << std::endl;
    update(pa, pb);
    std::cout << a << " " << b << std::endl;

    //* Arrays & Pointers

    int size;
    std::cin >> size;
    int* arr = new int[size];
    for (int i = 0; i < size; i++) {
        std::cin >> arr[i];
    }
    for (int i = 0; i < size; i++) {
        std::cout << arr[size - i - 1] << " ";
    }

    delete[] arr;

    //* Vector Matrix

    int n, q, k, val, index1, index2;
    std::cout << "\nNumber of variable-length arrays:\n";
    std::cin >> n;
    std::cout << "Number of queries:\n";
    std::cin >> q;

    std::vector<std::vector<int>> vec;

    for (int i = 0; i < n; i++) {
        std::cout << "Number of elements in vector\n";
        std::cin >> k;
        std::vector<int> tmp;
        for (int j = 0; j < k; j++) {
            std::cout << "Value to push into vector\n";
            std::cin >> val;
            tmp.push_back(val);
        }
        vec.push_back(tmp);
    }

    for (int i = 0; i < q; i++) {
        while (true) {
            std::cout << "First and Second index values for " << i + 1 << " iteration\n";
            try {
                std::cin >> index1 >> index2;
                if (index1 >= vec.size()) { throw(index1); }

                else if (index2 >= vec[i].size()) { throw(index2); }

                else { std::cout << vec[index1][index2] << std::endl; break; }
            }
            catch (...) {
                std::cout << "Invalid index selection. Try again.\n";
            }
        }
    }
}