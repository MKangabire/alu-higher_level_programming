#!/usr/bin/python3
import dis
import marshal
import types

def print_names():
    with open('hidden_4.pyc', 'rb') as file:
        magic = file.read(4)
        timestamp = file.read(4)
        code_object = marshal.load(file)

    instructions = dis.Bytecode(code_object)
    names = set()

    for instruction in instructions:
        if instruction.opname == 'LOAD_NAME':
            name = instruction.argval
            if not name.startswith('__'):
                names.add(name)

    for name in sorted(names):
        print(name)

if __name__ == '__main__':
    print_names()
