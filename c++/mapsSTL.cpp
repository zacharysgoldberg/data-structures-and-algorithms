#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>


int main() {
    //* Declarations
    int queries, type, marks;
    std::string name;
    std::map<std::string, int> student;

    //* Inputs
    std::cin >> queries;
    for (int i = 0; i < queries; i++) {
        std::cin >> type >> name;

        if (type == 1) {
            std::cin >> marks;
            // student.insert(std::make_pair(name, marks));
            student[name] += marks;
        }
        //* Outputs
        else if (type == 2) student.erase(name);
        else if (type == 3) {
            std::cout << student[name] << std::endl;
        }
    }
}
