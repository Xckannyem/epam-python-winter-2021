import argparse
from functools import reduce

parser = argparse.ArgumentParser(description='Roman and Arabic numeral')
parser.add_argument('N', type=str)
result = 0


def from_roman_numerals(args):
    global result
    user_input = args.N
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}

    try:
        if len(user_input) <= 5:
            result = reduce(lambda x, y: x - y if x > 4 * y else x + y, (numerals[i] for i in user_input[::-1]))
        else:
            raise ValueError
    except KeyError:
        raise ValueError


def main():
    args = parser.parse_args()
    from_roman_numerals(args)

    if result > 100:
        raise ValueError
    print(result)


if __name__ == "__main__":
    main()
