'''
Create a reverse dict of the given dict i.e if the given dict has (N,C)
then reverse dict will have (C,N) as key-value pair.
Traverse original dict and see if it's key exists in reverse dict
If it doesn't exist then we found our starting point.
After the starting point is found, simply trace the complete path from
the original dict.
'''


def trace_path(my_dict):
    result = []
    reverse_dict = dict()
    keys = my_dict.keys()
    for key in keys:
        reverse_dict[my_dict.get(key)] = key

    current = None
    for city in keys:
        if city not in reverse_dict:
            current = city
            break

    next = my_dict.get(current)
    while next:
        result.append([current, next])
        current = next
        next = my_dict.get(current)

    return result
