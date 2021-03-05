import argparse

parser = argparse.ArgumentParser(description='Bars of gold')
parser.add_argument('-W', type=int, default=-1, help='Capacity of a knapsack')
parser.add_argument('-w', type=int, nargs='*', default=[-1], help='Weight of gold bar')
parser.add_argument('-n', type=int, default=-1, help='Number of gold bars')
max_weight = 1


def bounded_knapsack(args):
    global max_weight
    for bar in args.w[::-1]:
        if max_weight + bar <= args.W:
            max_weight += bar


def main():
    args = parser.parse_args()
    if any(bar < 0 for bar in args.w) or args.n < 0 or args.W < 0 or args.n != len(args.w):
        raise ValueError

    bounded_knapsack(args)
    print(max_weight)


if __name__ == '__main__':
    main()
