#include <iostream>
#include <vector>
#include <regex>

using namespace std;


/*
1. Initialize two pointers at the opposite ends of the string

2. If the values at the left and right indexes match, move both toward the middle until they meet

3. If a mismatch occurs, skip one of the elements and check the rest of the string for palindrome

4. Skip the other element and check for palindrome

5. If no palindrome is obtained, return False, else if no more than one mismatch occurs throughout the traversal, return True
*/

bool checkOther(string& word, int left, int right) {
    while (left < right) {
        if (word[left] != word[right]) return false;

        left++;
        right--;
    }

    return true;
}

string validPalindrome(string word) {
    int left = 0;
    int right = word.size() - 1;

    while (left <= right) {
        if (word[left] != word[right]) break;

        left++;
        right--;
    }

    if (checkOther(word, left + 1, right) || checkOther(word, left, right - 1)) return word;

    return " ";
}

int main() {

    std::vector<std::string> vec = { "madame", "dead", "abca", "tebbem", "eeccccbebaeeabebccceea", "ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno", "kayak" };

    for (int i = 0; i < vec.size(); i++) {
        string result = validPalindrome(vec[i]);

        cout << result << endl;
    }

    return 0;

}