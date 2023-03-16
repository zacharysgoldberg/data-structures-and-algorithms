#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

/*
1.  Declare two empty hash maps - r_count and window, to store the requried window count (by counting of the charactes of  strings t) and the sliding window

2.  Update r_count by traversing the chraracters of t

3.  Traverse string str and update the window based on the character we're on

4.  Store the current window size (intialized to 0) in a varaiable called "current".
    Store the minimum window size (which is the length of r_count, meaning the number of unique characters in t) in a variable called required.
    If the count of a character in window is equal to the count of a character in r_count, increment the value of current by 1

5.  If current is equal to required, this means we have a valid window, and we can store its start and end indexes

6.  The length of our window may not be the minimum.
    So, we pop characters from the left side of this window and update the start and end until current becomes less than required.
    During this popping, we also decrement the counts of the characters in the window
*/


string min_window_substring(string str, string t) {


    return "";
}


// Driver code
int main() {



    return 0;
}

