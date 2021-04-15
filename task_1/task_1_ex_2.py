import argparse
import math
import operator

parser = argparse.ArgumentParser(description='Standard math operations')
parser.add_argument('operand', type=str)
parser.add_argument('numbers', type=float, nargs='*')


def calculator(args):
    operand = args.operand
    numbers = args.numbers

    if operand in dir(math):
        return getattr(math, operand)(*numbers)
    elif operand in dir(operator):
        return getattr(operator, operand)(*numbers)
    raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculator(args))


if __name__ == '__main__':
    main()
