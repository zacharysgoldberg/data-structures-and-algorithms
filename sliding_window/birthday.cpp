#include <vector>

// m is window size

void birthday(std::vector<int> chocolate, int d, int m)
{
    int count = 0;
    if (m > chocolate.size())
    {
        m = chocolate.size();
    }
    int window_sum = 0;
    for (int i = 0; i < m; i++)
    {
        window_sum += chocolate[i];
    }

    if (window_sum == d)
    {
        count++;
    }
    for (int i = m; i < chocolate.size(); i++)
    {
        window_sum += chocolate[i] - chocolate[i - m];
        if (window_sum == d)
            count++;
    }
}
