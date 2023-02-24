#include <iostream>
#include <vector>

#include "linkedList.h"

using namespace std;

/*
1.  Initialize two pointers, slow and fast at the head of the linked list

2.  Traverse the linked list, moving the slow pointer forward and fast pointer two steps forward

3.  When the fast pointer reaches the last node or NULL,
    then the slow pointerd will point to the middle node of the linked list

4.  Return the slow pointer
*/

LinkedListNode* getMiddleNode(LinkedListNode* head) {
    LinkedListNode* slow = head;
    LinkedListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}


int main() {
    std::vector<std::vector<int>> inputs = {
    {1, 2, 3, 4, 5},
    {1, 2, 3, 4, 5, 6},
    {3, 2, 1},
    {10},
    {1, 2}
    };

    for (int i = 0; i < inputs.size(); i++) {
        LinkedList* linkedlists = new LinkedList();
        linkedlists->createLinkedList(inputs[i]);

        std::cout << i + 1 << ".\tLinked list: ";
        printLinkedList(linkedlists->head);

        LinkedListNode* middle = getMiddleNode(linkedlists->head);
        std::cout << "\n\tMiddle of the linked list: " << middle->data << "\n";
        std::cout << std::string(100, '-') << "\n";
    }

    return 0;
}