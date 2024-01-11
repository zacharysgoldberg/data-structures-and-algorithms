#include <vector>
#include <string>
#include <cmath>

using namespace std;

// Greatest Common Divisor
int gcd(int testVar1, int testVar2)
{
    if (testVar1 == testVar2)
        return testVar1;
    if (testVar1 > testVar2)
        return gcd(testVar1 - testVar2, testVar2);
    else
        return gcd(testVar1, testVar2 - testVar1);
}


// Pascals Triangle
std::vector<int> printPascal(int testVar)
{
    if (testVar == 0)
    {
        std::vector<int> arr = { 1 };
        return arr;
    }
    else
    {
        std::vector<int> pascalsTriangle = { 1 };
        std::vector<int> prev = printPascal(testVar - 1);

        for (int i = 0; i < prev.size() - 1; i++)
        {
            pascalsTriangle.push_back(prev[i] + prev[i + 1]);

        }
        pascalsTriangle.push_back(1);
        return pascalsTriangle;
    }
}


// Convert decimal number to binary number
std::string decimalToBinary(float testVar)
{
    if (testVar <= 1)
        return std::to_string(testVar);
    else
        return decimalToBinary(std::floor(testVar / 2)) + decimalToBinary(static_cast<int>(testVar) % 2);
}
