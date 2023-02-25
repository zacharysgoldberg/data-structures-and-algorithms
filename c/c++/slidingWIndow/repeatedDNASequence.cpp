#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;


/*
1.  Iterate the string.

2.  Compute the hash value for the contents of the window.

3.  Add this hash value to the map that keeps count of all substrings of the given k length.

4.  Move the window one step forward and check for a new substring of the given k length.

5.  If the hash value of a window has a count greater than 1, the sequence in this window is repeated, so we add it to our output set.

6.  Once all characters of the string have been traversed, we return the output set.
*/


set<string> find_repeated_sequences(string str, int k) {
    set<string> repeated_seq;
    map<string, int> counter;

    if (str.length() < k)
        return repeated_seq;

    for (int i = 0; i < str.length() - k; i++) {
        counter[str.substr(i, k)] += 1;
    }

    for (auto it : counter) {
        if (it.second > 1)
            repeated_seq.insert(it.first);
    }
    return repeated_seq;
}


ostream& operator << (ostream& out, set<string> seq) {
    out << "{ ";
    for (auto it = seq.begin(); it != seq.end(); it++) {
        out << *it << ", ";
    }
    out << '}';
    return out;
}


// Driver code
int main()
{
    std::vector<std::string> inputsString = {
        "ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC",
        "GGGGGGGGGGGGGGGGGGGGGGGGG", "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",
        "TTTTTGGGTTTTCCA", "", "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT" };

    std::vector<int> inputsK = { 3, 3, 8, 12, 10, 14, 10, 10, 6 };

    for (int i = 0; i < inputsK.size(); i++) {
        std::cout << i + 1 << ".\tInput Sequence: '" << inputsString[i] << "'\n";
        std::cout << "\tk: " << inputsK[i] << "\n";
        std::cout << "\tRepeated Subsequence: " << find_repeated_sequences(inputsString[i], inputsK[i]) << "\n";
        std::cout << std::string(100, '-') << "\n";
    }
}