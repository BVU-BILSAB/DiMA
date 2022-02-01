import argparse
import re
from os import getcwd
import fileinput

from git import Repo, Git

VERSION_PATTERN = re.compile(r'version\s=\s\"[^\s]*')
VERSION_FILES = ['pyproject.toml', 'Cargo.toml']

arg_parser = argparse.ArgumentParser(description='A simple script to start working on a new DiMA version.')
arg_parser.add_argument('-v', '--version', type=str, help='The new version number')


def main():
    args = arg_parser.parse_args()
    current_repo = Repo(getcwd())
    new_branch = args.version

    print(f'New version number is {new_branch}.')
    print(f'Current branch is {current_repo.active_branch}.')
    print(f'Creating new branch..')

    Git().checkout('-b', f'v{new_branch}')

    print(f'Current branch is {current_repo.active_branch}.')

    for file in VERSION_FILES:
        print(f'Updating the version in {file}.')

        for line in fileinput.input(file, inplace=True):
            match = VERSION_PATTERN.match(line)

            if not match:
                print(line, end='')
                continue

            print(f'version = "{new_branch}"')

    print('All done.')


if __name__ == '__main__':
    main()
