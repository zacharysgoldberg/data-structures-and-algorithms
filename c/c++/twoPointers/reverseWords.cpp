#include <iostream>
#include <vector>
#include <regex>

using namespace std;


/*
1. Reverse the entire string

2. Start iterating over the reversed string using two pointers, start and end

3. While iterating over the strings, check for spaces between the words

4. Once a space is found between words, update the end pointer accordingly

5. Now use the two pointers to reverse characters in the word

6. Once the word has been reversed, update the start and end pointer to the index of the space

7. Repeat the process until the entire string is iterated
*/

//* Helper function to reverse a word/string
void reverseString(string& sentence, int start, int end) {

    while (start < end) {
        char temp = sentence[start];
        sentence[start] = sentence[end];
        sentence[end] = temp;

        start++;
        end--;
    }
}

string reverseWords(string sentence) {
    sentence = regex_replace(sentence, regex("^ +| +$|( ) +"), "$1");   // removing leading and trailing whitespace

    int start = 0, end = sentence.length() - 1;

    reverseString(sentence, start, end);

    for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] == ' ') {
            end = i;                                                    // position of the space
            reverseString(sentence, start, end - 1);
            start = i + 1;                                              // position after the space
            end = sentence.length() - 1;                                // position at end of string
        }
        if (i == sentence.length() - 1)                                 // no more spaces/words. End of sentence
            reverseString(sentence, start, end);
    }
    return sentence;
}


int main() {

    vector<string> stringsToReverse = {
        " Hello World ",
        "We love Python",
        "The quick brown fox jumped over the lazy dog",
        "Hey",
        "To be, or not to be",
        "AAAAA",
        " Hello     World " };

    for (int i = 0; i < stringsToReverse.size(); i++)
    {
        cout << (i + 1) << ".\tActual string:\t\t" << stringsToReverse[i] << endl;
        string result = reverseWords(stringsToReverse[i]);
        cout << "\tReversed string:\t" << result << endl;
        cout << string(100, '-') << endl;
    }


    return 0;
}