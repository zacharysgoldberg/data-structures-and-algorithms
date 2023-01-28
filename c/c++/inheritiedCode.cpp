#include <iostream>
#include <string>
#include <sstream>
#include <exception>

class BadLengthException {
private:
    int n;

public:
    BadLengthException(int error): n{ error } {}

    int what() {
        return n;
    }
};


bool checkUsername(std::string username) {
    bool isValid = true;
    int n = username.length();
    if (n < 5) {
        throw BadLengthException(n);
    }
    for (int i = 0; i < n - 1; i++) {
        if (username[i] == 'w' && username[i + 1] == 'w') {
            isValid = false;
        }
    }
    return isValid;
}

int main() {
    int T; std::cin >> T;

    while (T--) {
        std::string username;
        std::cin >> username;

        try {
            bool isValid = checkUsername(username);

            if (isValid) {
                std::cout << "Valid" << '\n';
            }
            else {
                std::cout << "Invalid" << '\n';
            }
        }
        catch (BadLengthException e) {
            std::cout << "Too short: " << e.what() << '\n';
        }
    }
}