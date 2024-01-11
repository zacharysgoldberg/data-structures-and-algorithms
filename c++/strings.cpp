#include <cmath>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>


int main() {
    std::string a;
    std::string b;
    std::cin >> a >> b;
    std::cout << a.size() << " " << b.size() << std::endl;
    
    std::string c = a + b;
    std::cout << c << std::endl;
    
    std::string a1 = b[0] + a.substr(1, a.size());
    std::string b1 = a[0] + b.substr(1, b.size());
    std::cout << a1 << " " << b1 << std::endl;
    
    return 0;
}