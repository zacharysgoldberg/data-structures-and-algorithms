'''

'''


def find_max_sum_sublist(lst: list) -> int:
    max_val = lst[0]
    curr_max = lst[0]
    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if curr_max > max_val:
            max_val = curr_max

    return max_val
