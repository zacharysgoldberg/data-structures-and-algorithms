#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Student {
private:
    int age;
    std::string firstName;
    std::string lastName;
    int standard;

public:
    int getAge() {
        return age;
    }
    
    void setAge(int a) {
        age = a;
    }
    
    std::string getFirstName() {
        return firstName;
    }
    
    void setFistName(std::string fname) {
        firstName = fname;
    }
    
    std::string getLastName() {
        return lastName;
    }
    
    void setLastName(std::string lname) {
        lastName = lname;
    }  
    
    int getStandard() {
        return standard;
    }
    
    void setStandard(int s) {
        standard = s;
    }
    
    void toString() {
        std::cout << age << "," << firstName << "," << lastName << "," << standard << std::endl;
    }
};

int main() {
    Student student;
    int age, standard;
    std::string firstName, lastName;
    
    std::cin >> age >> firstName >> lastName >> standard;
    
    student.setAge(age);
    student.setFistName(firstName);
    student.setLastName(lastName);
    student.setStandard(standard);
    
    std::cout << student.getAge() << std::endl;
    std::cout << student.getLastName() << ", " << student.getFirstName() << std::endl;
    std::cout << student.getStandard() << "\n\n";
    
    student.toString();
    
    return 0;
}
