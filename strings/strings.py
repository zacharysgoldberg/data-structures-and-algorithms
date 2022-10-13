def staircase(n):
    i = 0
    spaces = n - 1
    while i < n:
        print((' ' * spaces) + '#' * (i + 1))
        i += 1
        spaces -= 1

# staircase(6)


def time_conversion(s):
    time = ''
    if 'PM' in s and s[0:2] != '12':
        pm = str(int(s[0:2]) + 12)
        return time + pm + s[2:-2]
    elif 'AM' in s and s[0:2] == '12':
        return time + '00' + s[2:-2]
    else:
        return time + s[:-2]


# print(time_conversion("06:40:03AM"))


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


# [Recursive palindrome detection]
def is_palindrome_r(s):
    print(s[1:-1])
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome_r(s[1:-1])


# print(is_palindrome_r("racecar"))

def is_palindrome(s):
    if s == s[::-1]:
        return s
    return False


# print(is_palindrome('racecar'))


def get_max(operations):
    items = []
    for i in range(len(operations)):
        nums = list(map(int, operations[i].split()))
        if nums[0] == 1:
            items.append(nums[1])
        elif nums[0] == 2:
            items.pop()
        else:
            print(max(items))
    return items


# print(get_max(['1 83', '3', '2', '1 76']))


def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
# fizzBuzz(15)
