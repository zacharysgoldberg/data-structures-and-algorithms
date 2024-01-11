'''
If list2 is a subset of list1,
return True, otherwise return False
'''


def is_subset(list1, list2):
    table = set(list1)
    for el in list2:
        if el not in table:
            return False
    return True
