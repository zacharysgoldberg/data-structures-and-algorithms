#include "ListNode.h"

class Solution
{
public:

    ListNode* reverseList(ListNode* head)
    {
        ListNode* prev = nullptr;
        ListNode* next = nullptr;
        ListNode* curr = head;

        while (curr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
};