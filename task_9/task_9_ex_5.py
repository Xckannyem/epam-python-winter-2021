"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.
Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
Note: Pay attention to punctuation.
"""
import collections


def count_letters(s: str):
    """
    Function that takes s as parameter and if it is not a string, a TypeError will be thrown.
    Converts s to the dictionary counter and counts the number of each character of the given string.
    return: dictionary letters_counter that only consists of letters of given string as keys
    (by remove all other types of data) and number of their occurrence as values.
    """
    if isinstance(s, str):
        counter = collections.Counter(s)
        letters_counter = {key: value for key, value in counter.items() if key.isalpha()}
        return letters_counter
    else:
        raise TypeError
