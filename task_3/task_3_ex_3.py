import argparse
import fnmatch
import os
from os import stat
from stat import filemode


def finder(path, pattern):
    """Searches for files by a given pattern.
    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    found_files = []
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                found_files.append(os.path.join(root, file))
    return found_files


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    for file_path in file_paths:
        print(file_path, filemode(os.stat(file_path).st_mode))
    print(f"Found {len(file_paths)} file(s).")


def main():
    parser = argparse.ArgumentParser(description='Working with files')
    parser.add_argument('path')
    parser.add_argument('-p', nargs='?', default='*')
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()
