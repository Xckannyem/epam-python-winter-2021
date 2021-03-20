"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python
foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
foo([3, 2, 1])
[2, 3, 6]`
"""
from typing import List


def product_array(num_list: List[int]) -> List[int]:
    product = 1
    num_zeroes = 0
    pos_zero = -1
    # Multiply all and set positions
    for i, x in enumerate(num_list):
        if x != 0:
            product *= x
            num_list[i] = 1.0 / x
        else:
            num_zeroes += 1
            pos_zero = i
    if num_zeroes > 0:
        num_list = [0] * len(num_list)
        if num_zeroes == 1:
            num_list[pos_zero] = product
    else:
        # Now set the definitive elements
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i] * product)
    return num_list


if __name__ == "__main__":
    print(product_array([1, 2, 3, 4, 5]))
