'''

'''


def find_symmetric(my_list):
    result = []
    pairs = set()
    for pair in my_list:
        pair_tuple = tuple(pair)
        pair.reverse()
        reverse_tuple = tuple(pair)
        if reverse_tuple in pairs:
            result.append(list(reverse_tuple))
            result.append(pair)
        else:
            pairs.add(pair_tuple)

    return result
