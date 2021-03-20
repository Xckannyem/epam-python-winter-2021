"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.
Example,
n = 1234 result = 4
n = 246 result = 0
Write it as function.
Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    result = 0
    if type(n) is int and n > 0:
        while n > 0:
            if (n % 2) == 1:
                result = result + n % 10
            n = n // 10
        return result
    else:
        raise TypeError
