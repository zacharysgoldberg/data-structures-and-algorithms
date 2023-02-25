#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;


/*
1.  Initialize two pointers, index_s1 and index_s2, to zero for iterating both strings.

2.  If the character pointed by index_s1 in str1 is the same as the character pointed by index_s2 in str2, increment both pointers. Otherwise, only increment index_s1.

3.  Create two new pointers (start and end) once index_s2 reaches the end of str2. With these two pointers, we’ll slide the window in the opposite direction.

4.  Set the start to the value of index_s1 and end to start + 1.

5.  Decrement index_s2 if the character pointed by the start pointer in str1 is equal to the character pointed to by index_s2 in str2 and decrement the start pointer until index_s2 becomes less than zero.

6.  Calculate the length of a substring by subtracting values of the end and start variables.

7.  If this length is less than the current minimum length, update the length variable and min_subsequence string

8.  Repeat until index_s1 reaches the end of str1.
*/


string minWindow(string str1, string str2) {
    // Initialize length to a very large number (infinity)
    int length = INT_MAX;
    // Initialize pointers to zero and the min_subsequence to an empty string
    int indexS1 = 0, indexS2 = 0;
    string minSubsequence = "";

    // Process every character of str1
    while (indexS1 < str1.length()) {
        // Check if the character pointed by indexS1 in str1
        // is the same as the character pointed by indexS2 in str2
        if (str1[indexS1] == str2[indexS2]) {
            // If the pointed character is the same
            // in both strings increment indexS2
            indexS2++;
            // Check if indexS2 has reached the end of str2
            if (indexS2 == str2.length()) {
                // At this point the str1 contains all characters of str2
                int start = indexS1, end = start + 1;
                // Initialize start to the index where all characters of
                // str2 were present in str1
                indexS2--;
                // Decrement pointer indexS2 and start a reverse loop
                while (indexS2 >= 0) {
                    // Decrement pointer indexS2 until all characters of
                    //  str2 are found in str1
                    if (str1[start] == str2[indexS2])
                        indexS2--;

                    // Decrement start pointer everytime to find the
                    // starting point of the required subsequence
                    else
                        start--;
                }
                start++;
                // Check if length of sub sequence pointed
                // by start and end pointers is less than current min length
                if (end - start < length) {
                    // Update length if current sub sequence is shorter
                    length = end - start;
                    // Update minimum subsequence string
                    // to this new shorter string
                    minSubsequence = str1.substr(start, length);
                }
                // Set indexS1 to start to continue checking in str1
                // after this discovered subsequence
                indexS1 = start;
                indexS2 = 0;
            }
        }
        // Increment pointer indexS1 to check next character in str1
        indexS1++;
    }
    return minSubsequence;
}


int main() {
    vector<string> str1 = { "abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
                                             "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
                                             "beta", "asd", "abcd" };

    vector<string> str2 = { "bde", "kzed", "werty", "abc", "css", "la", "ab", "as", "pp" };

    for (int i = 0; i < str1.size(); i++) {
        cout << (i + 1) << ".\tInput strings: (" << str1[i] << ", " << str2[i] << ")" << endl;
        cout << "\tSubsequence string: " << minWindow(str1[i], str2[i]) << endl;
        cout << string(100, '-') << endl;
    }

    return 0;
}