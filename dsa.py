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


def majorityElement(nums):
    cnt = Counter(nums).most_common(1)[0][0]
    print(cnt)


# majorityElement([2, 2, 2, 1, 3, 2, 2, 3, 1])


def plusMinus(arr):
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


# plusMinus([-4, 3, -9, 0, 4, 1])
