#!/usr/bin/python3
import sys

def main(argv):
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num_args == 1:
        print("Number of argument(s): 1.")
        print("1:", argv[0])
    else:
        print("Number of arguments:", num_args, ".")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main(sys.argv[1:])
