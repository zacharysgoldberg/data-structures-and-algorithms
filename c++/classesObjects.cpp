#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

class Student {
private:
    int scores[5];
    int totalScore;
    
public:
    Student(): totalScore{0} {}
    
    void input() {
        for (int i = 0; i < 5; i++) {
            std::cin >> scores[i];
        }
    }
    
    int calculateTotalScore() {
        for (int i = 0; i < 5; i++) totalScore += scores[i];
        return totalScore;
    }
};

int main() {
    int n;
    std::cin >> n;
    
    Student* students = new Student[n];
    
    for (int i = 0; i < n; i++) {
        students[i].input();
    }
    
    int kristensScore = students[0].calculateTotalScore();
    
    int count = 0;
    
    for (int i = 1; i < n; i++) {
        int totalScore = students[i].calculateTotalScore();
        if(totalScore > kristensScore) count ++;
    }
    
    std::cout << count << std::endl;
    
    return 0;
}
