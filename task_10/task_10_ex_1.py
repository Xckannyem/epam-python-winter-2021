"""
Implement a function sort_names(input_file_path: str, output_file_path: str) -> None, which sorts names from
file_path and write them to a new file output_file_path. Each name should start with a new line as in the
following example:
Example:
Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str):
    with open(input_file_path, 'r', encoding='utf-8') as input_f:
        names = input_f.readlines()
        # list of lines with \n at the end of line
        sorted_names = sorted(names)
    with open(output_file_path, 'w', encoding='utf-8') as output_f:
        output_f.writelines(name for name in sorted_names)
        # write the items of a list to the file (character by character, line breaks should be at the end of each item)


if __name__ == '__main__':
    from_ = 'C:/Users/illic/data/unsorted_names.txt'
    to_ = 'C:/Users/illic/data/sorted_names.txt'
    print('First 10 lines of the original file: ')
    with open(from_) as f:
        for i in range(10):
            print(f.readline().rstrip())
    print(f'\nWRITING {to_} FILE...')
    sort_names(from_, to_)
    print('\nFirst 10 lines of new file: ')
    with open(to_) as f:
        for i in range(10):
            print(f.readline().rstrip())
