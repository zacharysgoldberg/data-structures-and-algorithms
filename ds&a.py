from time import time
from collections import Counter
import string


class Solution(object):
    def __init__(self):
        self.found = []

    def first_and_last(self, nums, target):
        low = 0
        high = len(nums)

        while high >= low:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                self.found.append(mid)
                low = mid + 1

        return self.found


nums = [2, 2, 3, 4, 3]
target = 3

res = Solution()
# print(res.first_and_last(nums=nums, target=target))


def lonely_integer(a):
    low = 0
    high = len(a) - 1
    while low <= high:
        i = a.count(a[low])
        j = a.count(a[high])
        if i == 1:
            return a[low]
        elif j == 1:
            return a[high]
        else:
            low += 1
            high -= 1


# print(lonely_integer([1, 2, 3, 4, 3, 2, 1]))


def tower_breakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2

    return 1


# print(tower_breakers(2, 6))
