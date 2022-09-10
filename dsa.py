from time import time
from collections import Counter


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


def majority_element(nums):
    cnt = Counter(nums).most_common(1)[0][0]
    print(cnt)


# majority_element([2, 2, 2, 1, 3, 2, 2, 3, 1])


def plus_minus(arr):
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(pos / len(arr))
    print(neg / len(arr))
    print(zero / len(arr))


# plus_minus([-4, 3, -9, 0, 4, 1])


def mini_max_sum(arr):
    arr.sort()
    min = sum(arr[:-1])
    max = sum(arr[1:])

    print(min, max)


# mini_max_sum([1, 2, 3, 4, 5])


def time_conversion(s):
    if s[0:2] == "12" and "PM" in s:
        print(s.replace(s[-2::], ""))
    elif s[0:2] == "12" and "AM" in s:
        time = s.replace("AM", "").replace("12", "00")
        print(time)
    elif s[0:2] != "12" and 'AM' in s:
        print(s.replace("AM", ""))
    else:
        t = str(int(s[0:2]) + 12)
        time = s.replace(s[0:2], t).replace(s[-2::], "")
        print(time)


# time_conversion("06:40:03AM")

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


def diagonal_difference(arr):
    n = 3
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += arr[i][i]

    for i in range(n):
        d2 += arr[i][n - 1 - i]

    return abs(d1 - d2)


print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
