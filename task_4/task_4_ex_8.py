"""
Task 04-Task 1.8
Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
Pairs should be formed as in the example. If there is only one element in the list return None
instead.
Using zip() is prohibited.
"""


def get_pairs(lst: list) -> list:
    result = []
    if len(lst) > 1:
        while len(lst) > 1:
            result.append(lst[:2])
            lst = lst[1:]
        return list(map(tuple, result))
    else:
        return None
