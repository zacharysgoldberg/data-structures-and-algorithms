#ifndef LINKEDLIST_HEADER
#define LINKEDLIST_HEADER

#include <iostream>
#include <vector>

using namespace std;

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

//TODO: Reverse linked list


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
        i++;
    }
}


#endif