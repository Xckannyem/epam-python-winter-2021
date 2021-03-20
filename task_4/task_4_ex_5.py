"""Implement a function get_digits(args: int) -> Tuple[int] which receives
arbitrary amount of arguments and returns a tuple of digits of given integers.
Example:

python
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

"""


def get_digits(*args):
    """
    Function that glues the elements of a tuple args into one number,
    then splits this number into digits and return tuple of separated digits
    """
    concatenated_numbs = int(''.join(map(str, args)))
    return tuple(int(x) for x in str(concatenated_numbs))
