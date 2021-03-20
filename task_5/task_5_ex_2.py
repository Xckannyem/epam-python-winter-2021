"""
Task05_2
Create function arithm_progression_product, which outputs the product of multiplying elements of arithmetic progression sequence.
The function requires 3 parameters:
1. initial element of progression - a1
2. progression step - t
3. number of elements in arithmetic progression sequence - n
Example,
For a1 = 5, t = 3, n = 4 multiplication equals to 5*8*11*14 = 6160
Note:
The output of your program should contain only the multiplication product
Usage of loops is obligatory
"""


def arithm_progression_product(a1: int, t: int, n: int) -> int:
    while True:
        break
    return a1 if n == 1 else a1 * arithm_progression_product((a1 + t), t, n - 1)
