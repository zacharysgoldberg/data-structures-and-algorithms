from time import time
from collections import Counter
import string
from data_structures import queues


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


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10))


# rotate elements right

def rotate_right(lst, k):
    if not lst:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


# print(rotate_right([1, 2, 3, 4, 5], 2))


def rearrange(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


def max_min(lst):
    min_val = 0
    max_val = len(lst) - 1
    res = []
    for _ in range(len(lst) // 2):
        res.append(lst[max_val])
        res.append(lst[min_val])
        min_val += 1
        max_val -= 1
    if len(lst) % 2:
        res.append(lst[len(lst) // 2])
    return res


# print(max_min([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def find_max_sum_sublist(lst):
    res = 0
    temp = 0
    for i in range(len(lst)):
        if temp > res:
            res = temp
        if temp < 0:
            temp = lst[i]
        else:
            temp += lst[i]
    return res


# print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
