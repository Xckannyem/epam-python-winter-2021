import argparse

parser = argparse.ArgumentParser(description='Simple arithmetic operations')
parser.add_argument('operand1', type=float, help='first operand')
parser.add_argument('operator', type=str, help='type of operator: +, -, /, *')
parser.add_argument('operand2', type=float, help='second operand')


def calculator(args):
    operand1 = args.operand1
    operator = args.operator
    operand2 = args.operand2

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    if operator not in operations:
        raise NotImplementedError(f'passed operation {operator} is not implemented!')
    return operations[operator](operand1, operand2)


def main():
    args = parser.parse_args()
    print(calculator(args))


if __name__ == '__main__':
    main()
