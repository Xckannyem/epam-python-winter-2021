"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use string.ascii_lowercase for list of alphabet letters
Note: raise TypeError in case of wrong data type
Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
print(chars_in_one(*test_strings))
print(chars_in_two(*test_strings))
print(not_used_chars(*test_strings))
"""
import itertools
import string


def chars_in_all(*strings):
    """
    return: characters that appear in all strings.
    """
    list_of_sets = []
    for i in strings:
        if isinstance(i, str):
            s = set()
            for char in i:
                s.add(char)
            list_of_sets.append(s)
        else:
            raise TypeError
    return set.intersection(*list_of_sets)


def chars_in_one(*strings):
    """
    return: characters that appear in at least one string.
    """
    for i in strings:
        if isinstance(i, str):
            return set(''.join(strings))
        else:
            raise TypeError


def chars_in_two(*strings):
    """
    return: characters that appear at least in two strings.
    """
    list_of_sets = []
    for i in strings:
        if isinstance(i, str):
            s = set()
            for char in i:
                s.add(char)
            list_of_sets.append(s)
        else:
            raise TypeError
    double_sets = itertools.combinations(list_of_sets, 2)
    # double_sets - this iterator object consists of tuples, each tuple contains two sets
    list_of_intersections = [set.intersection(*tpl) for tpl in double_sets]
    if len(list_of_intersections) > 2:
        return set.union(*list_of_intersections)
    else:
        raise ValueError


def not_used_chars(*strings):
    """
    return: characters of alphabet, that were not used in any string.
    """
    for i in strings:
        if isinstance(i, str):
            s = set()
            for char in string.ascii_lowercase:
                if char not in chars_in_one(*strings):
                    s.add(char.lower())
            return s
        else:
            raise TypeError


if __name__ == '__main__':
    test_strings = ['hello', 'world', 'python']
    print(f'Test strings: {test_strings}')
    print(f'1) characters that appear in all strings: {chars_in_all(*test_strings)}')
    print(f'2) characters that appear in at least one string: {chars_in_one(*test_strings)}')
    print(f'3) characters that appear at least in two strings: {chars_in_two(*test_strings)}')
    print(f'4) characters of alphabet, that were not used in any string: {not_used_chars(*test_strings)}')
