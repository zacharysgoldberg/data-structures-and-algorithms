from collections import Counter


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
    min = sum(arr[:-1])  # exclusive
    max = sum(arr[1:])  # inclusive

    print(min, max)


# mini_max_sum([1, 2, 3, 4, 5])

def reverse_array(a):
    a.reverse()
    return a


# print(reverseArray([1, 2, 3, 4]))


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


def birthday_cake_candles(candles):
    tallest = candles.count(max(candles))
    return tallest


# print(birthday_cake_candles([3, 2, 1, 3]))


def counting_sort(arr):
    counter = [0] * 100
    for num in arr:
        if counter[num] == 0:
            counter[num] += arr.count(num)

    print(counter)


# counting_sort([63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33])


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


def hourglass_sum(arr):
    max_sum = set()
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            total = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                     + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
                     + arr[i + 2][j + 2])
            # print(total)
            max_sum.add(total)

    return max(max_sum)


# print(hourglass_sum([[-1, -1, 0, -9, -2, -2],
#                      [-2, -1, -6, -8, -2, -5],
#                      [-1, -1, -1, -2, -3, -4],
#                      [-1, -9, -2, -4, -4, -5],
#                      [-7, -3, -3, -2, -9, -9],
#                      [-1, -3, -1, -2, -4, -5]]))


def rotate_left(d, arr):
    lst = arr[d:] + arr[:d]
    return lst


# print(rotate_left(4, [1, 2, 3, 4, 5]))

# =======================================================================================================
    """
    1. Query 1 x y
        1. Let idx = ((x ^ last_answer) % n)
        2. Append the int y to arr[idx]
        
    2. Query 2 x y
        1. Let idx = ((x ^ last_answer) % n)
        2. Assign the value arr[idx][y % size(arr[idx])] to last_answer
        3. Store the new value of last_answer to an answers array or list
    """


def dynamic_array(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    res = []

    for q in queries:
        index = (q[1] ^ last_answer) % n
        if q[2] % n == 0:
            arr[index].append(q[2])
        else:
            pos = q[2] % len(arr[index])
            last_answer = arr[index][pos]
            res.append(last_answer)
    return res

# print(dynamic_array(2, 5))
# =======================================================================================================


def matching_strings(stringList, queries):
    arr = [stringList.count(q) for q in queries]
    return arr


# print(matching_strings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))


def array_manipulation(n, queries):
    arr = [0] * (n + 1)
    for q in queries:
        a = q[0] - 1
        b = q[1]
        k = q[2]
        arr[a] += k
        arr[b] -= k

    max_value, count = 0, 0
    for num in arr:
        count += num
        print(count)
        if count > max_value:
            max_value = count

    # for a, b, k in queries:
    #     if a == b:
    #         arr[a - 1] += k
    #     else:
    #         while a < b:
    #             arr[a - 1] += k
    #             arr[b - 1] += k
    #             a += 1
    #             b -= 1
    print(arr)
    return max_value


# print(array_manipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))
