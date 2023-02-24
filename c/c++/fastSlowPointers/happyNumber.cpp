#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;



/*
1.  Initialize a variable "slow" with the input number and "fast" with the squared sum of the input numbers digits

2.  If "fast" is not 1 and also not equal to "slow", increment "slow" by one iteration and "fast" by two iterations.
    Essentially, set "slow" to sumOfDigits(slow) and "fast" to sumOfDigits(sumOfDigits(fast))

3.  If "fast" converges to 1, reuturn True, else return False
*/


int sumOfDigits(int number) {
    int sum = 0;
    while (number > 0) {
        // last digit
        int digit = number % 10;
        // remaining digit(s)
        number = std::floor(number / 10);
        sum += digit * digit;
    }

    return sum;
}


bool isHappyNumber(int num) {
    int slow = num;
    int fast = sumOfDigits(num);

    while (fast != 1 && fast != slow) {
        slow = sumOfDigits(slow);
        fast = sumOfDigits(sumOfDigits(fast));
    }
    if (fast == 1)
        return true;

    else
        return false;
}


int main() {
    std::vector<int> inputs = { 1, 5, 19, 25, 7 };
    for (int i = 0; i < inputs.size(); i++)
    {
        std::cout << i + 1 << ".\tInput Number: " << inputs[i] << "\n";
        bool result = isHappyNumber(inputs[i]);
        std::cout << "\n\tIs it a happy number? ";
        if (result)
            std::cout << "True\n";
        else
            std::cout << "False\n";
        std::cout << std::string(100, '-') << "\n";
    }


    return 0;
}