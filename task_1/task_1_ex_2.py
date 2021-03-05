import argparse
import math
import operator

parser = argparse.ArgumentParser(description='Standard math operations')
parser.add_argument('expression', nargs='*')


def calculator(args):
    operator_expr = args.expression[0]
    full_expr = args.expression[0] + '(' + ','.join(args.expression[1:]) + ')'

    if operator_expr in dir(math):
        if len(args.expression) == 1:
            return eval('math.' + operator_expr)
        else:
            return eval('math.' + full_expr)
    elif operator_expr in dir(operator):
        if len(args.expression) == 1:
            return eval('operator.' + operator_expr)
        else:
            return eval('operator.' + full_expr)
    else:
        raise NotImplementedError


def main():
    args = parser.parse_args()
    print(calculator(args))


if __name__ == '__main__':
    main()
