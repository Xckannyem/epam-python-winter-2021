"""
Task04_3
Implement a function which works the same as str.split
Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=' ') -> list:
    if isinstance(str_to_split, str):
        str_to_split = str_to_split.lstrip(delimiter)
        if delimiter in str_to_split:
            pos = str_to_split.index(delimiter)
            found = str_to_split[:pos]
            result = split_alternative(str_to_split[pos + 1:])
            result.insert(0, found)
            return result
        else:
            return [str_to_split]
    else:
        raise ValueError
