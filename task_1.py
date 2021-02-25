import argparse

parser = argparse.ArgumentParser(description='Simple arithmetic operations')

operations = ('+', '-', '/', '*')

parser.add_argument('first_value')
parser.add_argument('operator', help='type of operator: +, -, /, *')
parser.add_argument('second_value')

args = parser.parse_args()

if args.operator in operations and args.first_value.isnumeric() and args.second_value.isnumeric():
    print(eval(args.first_value + args.operator + args.second_value))
else:
    raise NotImplementedError
