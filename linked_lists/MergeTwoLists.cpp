#include "ListNode.h"

class Solution
{
public:

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2)
    {
        ListNode* mergedList = new ListNode();
        ListNode* curr = mergedList;

        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                curr->next = list1;
                list1 = list1->next;
            }
            else
            {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }

        curr->next = list1 == nullptr ? list2 : list1;

        return mergedList->next;
    }
};