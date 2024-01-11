#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


vector<int> grading_students(vector<int>& grades) {
    int next_multiple;
    for (int i = 0; i < grades.size(); i++) {
        if (grades[i] % 5 != 0 && grades[i] >= 38)
            if (grades[i] % 5 >= 3) {
                next_multiple = (grades[i] / 5 + 1) * 5;
                grades[i] = next_multiple;
            }
    }
    return grades;
}

void print_grades(vector<int> t_grades) {
    for (int i = 0; i < t_grades.size(); i++) {
        cout << t_grades[i] << endl;
    }
}

// Test case
int main()
{
    vector<int> grades = { 73, 67, 38, 33 };

    cout << "Grades before\n----------------\n";
    print_grades(grades);

    vector<int> result = grading_students(grades);

    cout << '\n';

    cout << "Grades after\n-----------------\n";
    print_grades(result);

    return 0;
}

