"""
Task_9_1
Implement swap_quotes function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.
Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(some_string: str) -> str:
    single_quotes = '\''
    double_quotes = '\"'
    swap = 'ssss'
    some_string = some_string.replace(single_quotes, swap)
    some_string = some_string.replace(double_quotes, single_quotes)
    some_string = some_string.replace(swap, double_quotes)
    return some_string
