#include "ListNode.h"
#include <unordered_set>


class Solution
{
public:

    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB)
    {
        std::unordered_set<ListNode*> setA, setB;
        ListNode* currA = headA;
        ListNode* currB = headB;

        while (currA || currB)
        {
            if (currA)
            {
                if (setB.find(currA) != setB.end())
                    return currA;
                setA.insert(currA);
                currA = currA->next;
            }

            if (currB)
            {
                if (setA.find(currB) != setA.end())
                    return currB;
                setB.insert(currB);
                currB = currB->next;
            }
        }
        return nullptr;
    }
};