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
    d1 = sum(arr[i][i] for i in range(n))
    d2 = sum(arr[i][n - 1 - i] for i in range(n))
    # for i in range(n):
    #     d1 += arr[i][i]

    # for i in range(n):
    #     d2 += arr[i][n - 1 - i]

    return abs(d1 - d2)


# print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


def counting_sort(arr):
    counter = [0] * 100
    for num in arr:
        if counter[num] == 0:
            counter[num] += arr.count(num)

    print(counter)


# counting_sort([63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32,
#               18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33])


def flipping_matrix(matrix):
    n = len(matrix)
    maximal = 0
    for i in range(n // 2):
        for j in range(n // 2):
            maximal += max(matrix[i][j],
                           matrix[i][n - j - 1],
                           matrix[n - i - 1][j],
                           matrix[n - i - 1][n - j - 1])
    print(maximal)


# flipping_matrix([[112, 42, 83, 119],
#                  [56, 125, 56, 49],
#                 [15, 78, 101, 43],
#                 [62, 98, 114, 108]])


def find_zig_zag_sequence(a, n):
    a.sort()
    mid = int((n + 1) / 2 - 1)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


# find_zig_zag_sequence([1, 2, 3, 4, 5, 6, 7], 7)


def tower_breakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2

    return 1


# print(tower_breakers(2, 6))

def caesar_cipher(s, k):
    # res = s[k:] + s[:k]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in range(len(s)):
        if s[char].isalpha():
            i = alphabet.index(s[char].lower())
            tmp = alphabet[(i + k) % len(alphabet)]
            res = res + tmp if s[char].islower() else res + tmp.upper()
        else:
            res = res + s[char]

    print(res)


# caesar_cipher("middle-Outz", 2)

def palindrome_index(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            newstr = s[:i] + s[i + 1:]
            if newstr == newstr[::-1]:
                return i
            return -(i + 1) + len(s)
    return -1


# print(palindrome_index("reefer"))


def grid_challenge(grid):
    n = len(grid)
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))
    for i in range(n - 1):
        for j in range(len(grid[i])):
            print(j)
            if grid[i][j] > grid[i + 1][j]:
                return "NO"
    return "YES"


# print(grid_challenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
# print(grid_challenge(['abc', 'lmp', 'qrt']))
# print(grid_challenge(['abc', 'hjk', 'mpq', 'rtv']))


def super_digit(n, k):
    res = 0
    if len(n) == 1 and k == 1:
        return int(n)
    else:
        res = sum(map(int, n))
        return super_digit(str(res * k), 1)


# print(super_digit('148', 3))
# print(super_digit('9785', 4))


def minimum_bribes(q):
    bribes = 0
    for i, el in enumerate(q):
        if el - i > 3:
            print('Too chaotic')
            return
        for j in range(max(0, el - 2), i):  # optimized
            if q[j] > el:
                bribes += 1
    print(bribes)


# minimum_bribes([2, 1, 5, 3, 4])
# minimum_bribes([2, 5, 1, 3, 4])


def truck_tour(petrolpumps):
    n = len(petrolpumps)
    fuel, start = 0, 0
    i = start
    while i < n:
        fuel += petrolpumps[i][0] - petrolpumps[i][1]
        # print(fuel)
        if fuel < 0:
            start += 1
            i = start
            fuel = 0
        else:
            i += 1

    return start


# print(truck_tour([[1, 5], [10, 3], [3, 4]]))


def merge_linked_lists(head1, head2):

    return


# print(merge_linked_lists())
