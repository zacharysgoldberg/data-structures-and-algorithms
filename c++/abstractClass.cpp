#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

#include <list>
#define key first
#define value second

class LRUCache {
private:
    int cp;
    map<int, list<pair<int, int>>::iterator> mp;
    list<pair<int, int>> lst;

public:
    LRUCache(int capacity): cp{ capacity } {}

    void set(int key, int value) {
        if (mp.find(key) != mp.end()) {
            mp[key]->key = key;
            mp[key]->value = value;
        }
        else {
            lst.push_front({ key, value });
            mp[key] = lst.begin();
            if (lst.size() > cp) {
                mp.erase(lst.back().key);
                lst.pop_front();
            }
        }
    }

    int get(int key) {
        if (mp.find(key) != mp.end()) return mp[key]->second;
        else return -1;
    }
};

int main() {
    int n, capacity, i;
    cin >> n >> capacity;
    LRUCache l(capacity);
    for (i = 0;i < n;i++) {
        string command;
        cin >> command;
        if (command == "get") {
            int key;
            cin >> key;
            cout << l.get(key) << endl;
        }
        else if (command == "set") {
            int key, value;
            cin >> key >> value;
            l.set(key, value);
        }
    }
}
