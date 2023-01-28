#include <iostream>
#include <exception>
#include <string>
#include <stdexcept>
#include <vector>
#include <cmath>

class Server {
private:
    static int load;

public:
    static int compute(long long A, long long B) {
        load += 1;

        if (A < 0) {
            throw std::invalid_argument("A is negative");
        }
        std::vector<int> v(A, 0);
        int real = -1, cmplx = sqrt(-1);

        if (B == 0) throw 0;

        real = (A / B) * real;
        int ans = v.at(B);

        return real + A - B * ans;
    }
    static int getLoad() {
        return load;
    }
};
int Server::load = 0;

int main() {
    int T; std::cin >> T;
    while (T--) {
        long long A, B;
        std::cin >> A >> B;

        try {
            std::cout << Server::compute(A, B) << '\n';
        }
        catch (std::bad_alloc& e) {
            std::cout << "Not enough memory" << '\n';
        }
        catch (std::exception& e) {
            std::cout << "Exception: " << e.what() << '\n';
        }
        catch (...) {
            std::cout << "Other Exception" << '\n';
        }

    }
    std::cout << Server::getLoad() << std::endl;
    return 0;
}