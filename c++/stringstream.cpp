#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>

std::vector<int> parseInts(std::string str) {
    std::stringstream ss(str);
    std::vector<int> vec;
    int tmp;
    char ch;
    while (ss >> tmp) {
        vec.push_back(tmp);
        ss >> ch;
    }
    return vec;
}

void printLn(std::vector<int> vec) {
    for (int i = 0; i < vec.size(); i++)
        std::cout << vec[i] << std::endl;
}       

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    std::string str;
    std::cin >> str;
    
    std::vector<int> res = parseInts(str);
    
    printLn(res);
    return 0;
}
