#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    print("{} argument{}:".format(argc, "s" if argc != 1 else ""))
    if argc == 0:
        print("")
    else:
        print()
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
