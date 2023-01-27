#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#define INF (unsigned)!((int)0)
#define FUNCTION(name,operator) inline void name(int &current, int candidate) {!(current operator candidate) ? current = candidate : false;}
#define io(v) std::cin >> vec
#define toStr(str) #str
#define forEach(vec, i) for (int i = 0; i < vec.size(); ++i)


FUNCTION(minimum, < )
    FUNCTION(maximum, > )

    int main() {

    int n;
    std::cin >> n;

    std::vector<int> vec(n);
    forEach(vec, i) { io(vec)[i]; }

    int min = INF;
    int max = -INF;
    forEach(vec, i) {
        minimum(min, vec[i]);
        maximum(max, vec[i]);
    }

    int dif = max - min;

    std::cout << toStr(Result = ) << ' ' << dif;
}
