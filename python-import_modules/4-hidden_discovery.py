#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = marshal.load(file)

    names = [name for name in code.co_names if not name.startswith("__")]

    for name in sorted(names):
        print(name)

