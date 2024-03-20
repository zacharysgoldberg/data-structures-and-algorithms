#include "ListNode.h"
#include <unordered_set>


class Solution {
public:

    // slower
    bool hasCycle(ListNode* head)
    {
        std::unordered_set<ListNode*> set;
        ListNode* curr = head;

        while (curr)
        {
            if (set.find(curr) != set.end())
                return true;

            set.insert(curr);
            curr = curr->next;
        }

        return false;
    }

    // faster
    bool hasCycle(ListNode* head)
    {
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
                return true;
        }

        return false;
    }
};