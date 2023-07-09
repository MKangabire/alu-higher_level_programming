#!/usr/bin/python3
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()

    code = dis.Bytecode.from_code(bytecode)
    names = set()

    for instruction in code:
        if instruction.opname == "LOAD_GLOBAL" and not instruction.argval.startswith("__"):
            names.add(instruction.argval)

    for name in sorted(names):
        print(name)
