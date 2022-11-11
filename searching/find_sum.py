def find_sum(lst, n):
    lst.sort()
    low = 0
    high = len(lst) - 1
    while low != high:
        if lst[low] + lst[high] < n:
            low += 1
        elif lst[low] + lst[high] > n:
            high -= 1
        else:
            return [lst[low], lst[high]]

    return None
