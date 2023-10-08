#!/usr/bin/python3
import sys

def main(argv):
    argc = len(argv)
    result = 0

    for i in range(1, argc):  # Start from index 1 to skip the script name
        result += int(argv[i])

    print(result)

if __name__ == "__main__":
    main(sys.argv)
