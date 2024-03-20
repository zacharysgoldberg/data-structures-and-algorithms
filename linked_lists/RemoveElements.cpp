#include "ListNode.h"
#include <unordered_set>

class Solution
{
public:

    ListNode* removeElements(ListNode* head, int val)
    {
        while (head && head->val == val)
            head = head->next;

        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr)
        {
            if (curr->val == val)
            {
                ListNode* next = curr->next;
                curr->next = nullptr;
                prev->next = next;
                curr = next;
                continue;
            }
            prev = curr;
            curr = curr->next;
        }

        return head;
    }
};