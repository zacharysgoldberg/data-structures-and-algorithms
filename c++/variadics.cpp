#include <iostream>

// Template Function
template <bool...digits>
int reversed_binary_value() {
    int result = 0, product = 1;

    int booleans[] = { digits... };
    for (bool b : booleans) {
        result += (b ? product : 0);
        product *= 2;
    }

    return result;
}



template <int n, bool...digits>
struct CheckValues {
    static void check(int x, int y)
    {
        CheckValues<n - 1, 0, digits...>::check(x, y);
        CheckValues<n - 1, 1, digits...>::check(x, y);
    }
};

template <bool...digits>
struct CheckValues<0, digits...> {
    static void check(int x, int y)
    {
        int z = reversed_binary_value<digits...>();
        std::cout << (z + 64 * y == x);
    }
};

int main()
{
    int t; std::cin >> t;

    for (int i = 0; i != t; ++i) {
        int x, y;
        std::cin >> x >> y;
        CheckValues<6>::check(x, y);
        std::cout << "\n";
    }
}
