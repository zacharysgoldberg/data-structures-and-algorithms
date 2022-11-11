def binary_search(lst, target):
    low = 0
    high = len(lst)

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid

    return None
