#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#include <numeric>

class Person {
protected:
    std::string name;
    int age;

public:
    Person() {}

    // Person(std::string n, int a): name{ n }, age{ a } {}

    virtual void getdata() {
        std::cin >> name >> age;
    }

    virtual void putdata() {
        std::cout << name << ' ' << age << '\n';
    }

};

class Professor: public Person {
protected:
    int publications;
    int cur_id;

public:
    static int count;
    Professor() { cur_id = ++count; }

    void getdata() {
        std::cin >> name >> age >> publications;
    }

    void putdata() {
        std::cout << name << ' ' << age << ' ' << publications << " " << cur_id << '\n';
    }
};

int Professor::count = 0;

class Student: public Person {
protected:
    int marks[6], sum = 0;
    int cur_id;

public:
    static int count;
    Student() { cur_id = ++count; }

    void getdata() {
        std::cin >> name >> age;
        for (int i = 0; i < 6; i++) {
            std::cin >> marks[i];
        }
        sum = std::accumulate(marks, marks + 6, sum);
    }

    void putdata() {
        std::cout << name << ' ' << age << ' ' << sum << ' ' << cur_id << '\n';
    }
};

int Student::count = 0;

int main() {

    int n, val;
    cin >> n; //The number of objects that is going to be created.
    Person* per[n];

    for (int i = 0;i < n;i++) {

        cin >> val;
        if (val == 1) {
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for (int i = 0;i < n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
