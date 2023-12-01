#!/usr/bin/python3
import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("{} {} {}{}".format(
        ''  if num_arguments != 1 else '',
        num_arguments,
        'argument' if num_arguments == 1 else 'arguments',
        ':' if num_arguments > 0 else '.'
    ))

    for idx, arg in enumerate(arguments, start=1):
        print("{}: {}".format(idx, arg))

if __name__ == "__main__":
    print_arguments()
