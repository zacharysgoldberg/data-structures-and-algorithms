def reverse_array(a):
    a.reverse()
    return a


# print(reverseArray([1, 2, 3, 4]))


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
