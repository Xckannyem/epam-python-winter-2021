import argparse

parser = argparse.ArgumentParser(description='Formula')
parser.add_argument('user_input')


def check_formula(args):
    for i in range(len(args.user_input) - 1):
        if (args.user_input[i] == '-' and args.user_input[i + 1] == '-') or \
                (args.user_input[i] == '+' and args.user_input[i + 1] == '+'):
            return False, None
    try:
        return True, eval(args.user_input)
    except:
        return False, None


def main():
    args = parser.parse_args()
    print(check_formula(args))


if __name__ == '__main__':
    main()
