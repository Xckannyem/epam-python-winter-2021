import argparse

parser = argparse.ArgumentParser(description='Simple arithmetic operations')
parser.add_argument('operand1', type=float, help='first operand')
parser.add_argument('operator', type=str, help='type of operator: +, -, /, *')
parser.add_argument('operand2', type=float, help='second operand')


def calculator(args):
    if args.operator == '+':
        return args.operand1 + args.operand2
    elif args.operator == '-':
        return args.operand1 - args.operand2
    elif args.operator == '/':
        return args.operand1 / args.operand2
    elif args.operator == '*':
        return args.operand1 * args.operand2
    else:
        raise NotImplementedError(f"passed operation {args.operator} not implemented!")


def main():
    args = parser.parse_args()
    print(calculator(args))


if __name__ == '__main__':
    main()
