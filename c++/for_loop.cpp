#include <iostream>
#include <cstdio>
#include <array>
#include <string>

int main()
{
    std::string numWords[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    int a, b;
    std::cin >> a >> b;

    for (int n = a; n <= b; n++)
    {
        if (1 <= n && n <= 9)
            std::cout << numWords[n - 1] << std::endl;
        else
            (n % 2 == 0) ? std::cout << "even\n" : std::cout << "odd\n";
    }

    return 0;
}