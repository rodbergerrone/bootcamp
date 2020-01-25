import argparse
import os
import pathlib


def folder_tree(path, prefix=''):
    items_count = len(list(path.iterdir()))
    for n, x in enumerate(path.iterdir()):
        if n == items_count - 1:
            marker = '  └ '
            next_marker = '    '
        else:
            marker = '  ├ '
            next_marker = '  │ '
        if x.is_dir():
            if os.access(x, os.R_OK):
                print(prefix + marker + '\033[1m' + f'[{x.name}]' + '\033[0m')
                folder_tree(x, prefix + next_marker)
        else:
            if x.suffix == '.py':
                print(prefix + marker + '\33[94m' + f'{x.name}' + '\33[0m')
            else:
                print(prefix + marker + f'{x.name}')


if __name__ == "__main__":
    # folder_tree(pathlib.Path(r'C:\\Users\\kurs\\workspace\\projects\\bootcamp'))
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    folder_tree(pathlib.Path(args.file))

#TODO: fix colors in terminal version, exeption on certain folders