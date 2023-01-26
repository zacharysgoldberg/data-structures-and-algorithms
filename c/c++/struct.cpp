#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

struct Student {
    int age;
    std::string firstName;
    std::string lastName;
    int standard;  
};

int main() {
    Student student;
    
    std::cin >> student.age;
    std::cin >> student.firstName;
    std::cin >> student.lastName;
    std::cin >> student.standard;
    
    std::cout << student.age << " " << student.firstName << " " << student.lastName << " " << student.standard << std::endl;
    
    return 0;
}
