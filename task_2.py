import argparse
import operator

parser = argparse.ArgumentParser(description='Standard math operations')

parser.add_argument('operator')
parser.add_argument('first_value')
parser.add_argument('second_value')

args = parser.parse_args()

try:
    print(eval('operator.' + args.operator + '(' + args.first_value + ',' + args.second_value + ')'))
except BaseException:
    raise NotImplementedError
