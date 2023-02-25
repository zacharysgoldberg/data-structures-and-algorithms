#include <iostream>
#include <vector>

#include "linkedList.h"

using namespace std;


/*
1.  Initialize both the slow and fast pointers at the head

2.  Traverse linked list using both pointers at different increments.
    At each iteration, the slow pointer increments by one node,
    and the fast pointer increments by two nodes

3.  Continue doing so until the fast pointer reaches the end of the linked list.
    At this instance, the slow pointer will be pointing at the MIDDLE of the linked list

4.  Reverse the second half of the linked list and compare it with the first half

5. If both halves are the same then it is a palindrome
*/

bool palindrome(LinkedListNode* head) {
    LinkedListNode* slow = head;
    LinkedListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    //Middle/Second half of list
    LinkedListNode* secondHalf = reverseLinkedList(slow);
    while (head && secondHalf) {
        if (head->data != secondHalf->data)
            return false;
        secondHalf = secondHalf->next;
        head = head->next;
    }

    return true;
}




int main() {
    std::vector<std::vector<int>> inputs = {
    {2, 4, 6, 4, 2},
    {0, 3, 5, 5, 0},
    {9, 7, 4, 4, 7, 9},
    {5, 4, 7, 9, 4, 5},
    {5, 9, 8, 3, 8, 9, 5}
    };

    for (int i = 0; i < inputs.size(); i++) {
        LinkedList* linkedlists = new LinkedList();
        linkedlists->createLinkedList(inputs[i]);

        std::cout << i + 1 << ".\tLinked List: ";
        printLinkedList(linkedlists->head);

        std::cout << "\n\tIs it a palindrome?: " << (palindrome(linkedlists->head) == true ? "Yes" : "No") << "\n";
        std::cout << std::string(100, '-') << "\n";
    }

    return 0;
}