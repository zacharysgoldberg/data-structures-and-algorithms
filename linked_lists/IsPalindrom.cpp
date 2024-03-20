#include "ListNode.h"


class Solution
{
public:

    bool isPalindrome(ListNode* head)
    {
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* secondHalfReversed = this->reverseList(slow);

        while (head && secondHalfReversed)
        {
            if (head->val != secondHalfReversed->val)
                return false;
            head = head->next;
            secondHalfReversed = secondHalfReversed->next;
        }

        return true;
    }

    ListNode* reverseList(ListNode* head)
    {
        ListNode* curr = head;
        ListNode* prev = nullptr;
        ListNode* next = nullptr;

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

