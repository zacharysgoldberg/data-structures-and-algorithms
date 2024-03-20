#include "ListNode.h"


class Solution
{
public:

    ListNode* middleNode(ListNode* head)
    {
        ListNode* slowPtr = head->next;
        ListNode* fastPtr = head->next->next;

        while (fastPtr->next)
        {
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
        }

        return slowPtr;
    }
};