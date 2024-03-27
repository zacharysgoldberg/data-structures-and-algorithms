#include <queue>

class Solution
{
public:
    int findTheWinner(int n, int k)
    {
        std::queue<int> friends;

        for (int i = 1; i <= n; i++)
            friends.push(i);

        int i = 1;

        while (friends.size() > 1)
        {
            int currFriend = friends.front();
            friends.pop();

            if (i == k)
                i = 0;
            else
                friends.push(currFriend);

            i++;
        }

        return friends.front();
    }
};