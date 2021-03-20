"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    single_quotes = '\''
    double_quotes = '\"'
    result = ''
    for i in string:
        if i == single_quotes:
            i = double_quotes
        elif i == double_quotes:
            i = single_quotes
        result += i
    return result
