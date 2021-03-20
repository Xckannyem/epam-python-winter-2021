"""
Implement a function split_by_index(string: str, indexes: List[int]) -> List[str]
which splits the string by indexes specified in indexes.
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.
"""


def split_by_index(string, indexes):
    result = []
    current_index = 0
    for i in indexes:
        next_index = i
        if type(i) != int or i < 0 or next_index <= current_index or i >= len(string):
            continue
        result.append(string[current_index:next_index])
        current_index = next_index
    result.append(string[current_index:])
    return result
