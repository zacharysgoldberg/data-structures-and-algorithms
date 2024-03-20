#include "ListNode.h"

class Solution
{
public:

    ListNode* mergeNodes(ListNode* head)
    {
        ListNode* mergedNodes = nullptr;
        ListNode* mergedNodesPtr = mergedNodes;
        ListNode* curr = head;
        int sum = 0;

        while (curr)
        {
            if (curr->val == 0 && sum != 0)
            {
                if (mergedNodes == nullptr)
                {
                    mergedNodes = new ListNode(sum);
                    mergedNodesPtr = mergedNodes;
                }
                else
                {
                    mergedNodes->next = new ListNode(sum);
                    mergedNodes = mergedNodes->next;
                }
                sum = 0;
            }
            else
                sum += curr->val;

            curr = curr->next;
        }
        return mergedNodesPtr;
    }
};