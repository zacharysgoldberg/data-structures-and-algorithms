#include <iostream>
#include <vector>
#include <string>

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


string min_window(string str1, string str2) {
    int index_s2 = 0;
    string subsequence = "";
    // Initialize length to a larger number than str1 length
    int min_length = str1.length() + 1;
    // Process every character of str1
    for (int index_s1 = 0; index_s1 < str1.length(); index_s1++) {
        // Check if the character pointed by index_s1 in str1
        // is the same as the character pointed by index_s2 in str2
        if (str1[index_s1] == str2[index_s2]) {
            // If the pointed character is the same
            // in both strings increment index_s2
            index_s2++;
            // Check if index_s2 has reached the end of str2
            if (index_s2 == str2.length()) {
                // At this point the str1 contains all characters of str2
                // Initialize end to the index_s1 + 1 where all characters of
                // str2 were present in str1
                int end = index_s1 + 1;
                // Decrement pointer index_s2 and start a reverse loop
                index_s2--;
                while (index_s2 >= 0) {
                    // Decrement pointer index_s2 until all characters of
                    //  str2 are found in str1
                    if (str1[index_s1] == str2[index_s2])
                        index_s2--;
                    // Decrement index_s1 pointer everytime to find the
                    // starting point of the required subsequence
                    index_s1--;
                }
                // Bringing the indexes back from out of bounds
                index_s2++;
                index_s1++;
                // Check if length of subsequence pointed
                // by index_s1 and end pointers is less than current min length
                if (end - index_s1 < min_length) {
                    // Update length if current sub sequence is shorter
                    min_length = end - index_s1;
                    // Update minimum subsequence string
                    // to this new shorter string
                    subsequence = str1.substr(index_s1, min_length);
                }
            }
        }
    }
    return subsequence;
}


int main() {
    vector<string> str1 = { "abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
                                             "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
                                             "beta", "asd", "abcd" };

    vector<string> str2 = { "bde", "kzed", "werty", "abc", "css", "la", "ab", "as", "pp" };

    for (int i = 0; i < str1.size(); i++) {
        cout << (i + 1) << ".\tInput strings: (" << str1[i] << ", " << str2[i] << ")" << endl;
        cout << "\tSubsequence string: " << min_window(str1[i], str2[i]) << endl;
        cout << string(100, '-') << endl;
    }

    return 0;
}