#include <iostream>
#include <forward_list>
#include <iterator>
#include <vector>

using namespace std;

/*
1.  Initialize both slow and fast pointers to the head of the list

2.  Move slow pointer one node ahead and fast pointer two nodes ahead

3.  Check if both pointers point to the same node at any point.
    If yes, then return True

4.  Else if the fast pointer reaches the end of the linked list, return False
*/

struct LinkedListNode {
    int data;
    LinkedListNode* next;
    LinkedListNode* ptr;
    LinkedListNode(int _data) {
        data = _data;
        next = nullptr;
        ptr = nullptr;
    }
};

class LinkedList {
public:
    LinkedListNode* head;

    LinkedList() { head = nullptr; }
    LinkedList(LinkedListNode* _head): head{ _head } {}

    void insertAtHead(int data) {
        if (head == nullptr)
            head = new LinkedListNode(data);
        else {
            LinkedListNode* newNode = new LinkedListNode(data);
            newNode->next = head;
            head = newNode;
        }
    }

    void insertAtTail(int data) {
        if (head == nullptr) {
            head = new LinkedListNode(data);
        }
        else {
            LinkedListNode* newNode = new LinkedListNode(data);
            LinkedListNode* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    void createLinkedList(vector<int>& vec) {
        for (int i = vec.size() - 1; i >= 0; i--) {
            insertAtHead(vec[i]);
        }
    }

    // returns the number of nodes in the linked list
    int getLength(LinkedListNode* head) {
        LinkedListNode* temp = head;
        int length = 0;
        while (temp != nullptr) {
            length += 1;
            temp = temp->next;
        }
        return length;
    }

    // returns the node at the specified position(index) of the linked list
    LinkedListNode* getNode(LinkedListNode* head, int pos) {
        if (pos != -1) {
            int p = 0;
            LinkedListNode* ptr = head;
            while (p < pos) {
                ptr = ptr->next;
                p += 1;
            }
            return ptr;
        }
        return head;
    }
};


void printLinkedList(LinkedListNode* head) {
    LinkedListNode* temp = head;
    int i = 0;

    while (temp && i < 7) {
        if (i == 0) {
            std::cout << temp->data << " ";
        }
        else {
            std::cout << temp->data << " ";
        }
        temp = temp->next;
        if (i == 6) {
            std::cout << "(...)";
            break;
        }
        if (temp) {
            std::cout << " →  ";
        }
        else {
            std::cout << " →  NULL";
        }
        i += 1;
    }
}

bool DetectCycle(LinkedListNode* head) {
    LinkedListNode* slow = head;
    LinkedListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return true;
    }

    return false;
}

//TODO: Fix iterator for forward_list
bool detectCycle(forward_list<int>* head) {
    forward_list<int>::iterator slow = head->begin();
    forward_list<int>::iterator fast = head->begin();

    while (*fast && *next(fast, 1)) {
        cout << *slow << ' ' << *fast;

        slow = next(slow, 1);
        fast = next(fast, 2);

        if (*slow == *fast)
            return true;
    }

    return false;
}




int main() {

    // forward_list<int> list = { 1, 2, 3, 4, 5 };

    // // int head = list.front();

    // bool result = detectCycle(&list);

    // cout << result << endl;


    std::vector<std::vector<int>> inputs = {
    {2, 4, 6, 8, 10, 12},
    {1, 3, 5, 7, 9, 11},
    {0, 1, 2, 3, 4, 6},
    {3, 4, 7, 9, 11, 17},
    {5, 1, 4, 9, 2, 3}
    };

    std::vector<int> pos = { 0, -1, 1, -1, 2 };

    for (int i = 0; i < inputs.size(); i++) {
        LinkedList* linkedlists = new LinkedList();
        linkedlists->createLinkedList(inputs[i]);
        std::cout << i + 1 << ".\tInput:\n\t";
        printLinkedList(linkedlists->head);
        if (pos[i] != -1) {
            int length = linkedlists->getLength(linkedlists->head);
            LinkedListNode* lastNode = linkedlists->getNode(linkedlists->head, length - 1);
            lastNode->next = linkedlists->getNode(linkedlists->head, pos[i]);
        }
        std::cout << "\n \tProcessing...\n";
        bool cycle = DetectCycle(linkedlists->head);
        std::cout << "\n\tDetected cyle: " << std::boolalpha << cycle << "\n";
        std::cout << std::string(100, '-') << "\n";
    }

    return 0;
}