'''
Check if there are no common elements 
between two lists.
'''


def is_disjoint(list1, list2):
    table = set(list1)
    for el in list2:
        if el in table:
            return False
    return True
