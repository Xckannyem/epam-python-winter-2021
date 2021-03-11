import argparse

parser = argparse.ArgumentParser(description='Equal values')
parser.add_argument('number', type=int)


def calculate(args):
    num = args.number

    if num > 0:
        return num * num
    elif num < 0:
        return abs(num)
    else:
        return num


def main():
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()
