#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//
class Matrix {
public:
    std::vector<std::vector<int>> a;

    Matrix& operator + (const Matrix& m) {
        for (int i = 0; i < m.a.size(); i++) {
            for (int j = 0; j < m.a[i].size(); j++) {
                a[i][j] += m.a[i][j];
            }
        }
        return *this;
    }
};


int main() {
    int cases, k;
    cin >> cases;
    for (k = 0;k < cases;k++) {
        Matrix x;
        Matrix y;
        Matrix result;
        int n, m, i, j;
        cin >> n >> m;
        for (i = 0;i < n;i++) {
            vector<int> b;
            int num;
            for (j = 0;j < m;j++) {
                cin >> num;
                b.push_back(num);
            }
            x.a.push_back(b);
        }
        for (i = 0;i < n;i++) {
            vector<int> b;
            int num;
            for (j = 0;j < m;j++) {
                cin >> num;
                b.push_back(num);
            }
            y.a.push_back(b);
        }
        result = x + y;
        for (i = 0;i < n;i++) {
            for (j = 0;j < m;j++) {
                cout << result.a[i][j] << " ";
            }
            cout << endl;
        }
    }
}
