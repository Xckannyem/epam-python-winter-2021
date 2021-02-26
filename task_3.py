import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('formula')

args = parser.parse_args()

for i in range(len(args.formula) - 1):
    if (args.formula[i] == '-' and args.formula[i + 1] == '-') or \
            (args.formula[i] == '+' and args.formula[i + 1] == '+'):
        print(False, None)
        sys.exit(0)
try:
    print(True, eval(args.formula))
except:
    print(False, None)
