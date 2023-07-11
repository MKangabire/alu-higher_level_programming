#!/usr/bin/python3
import dis
import types

def get_names():
    with open('hidden_4.pyc', 'rb') as f:
        code = f.read()
    module = types.ModuleType('hidden_4')
    module.__file__ = 'hidden_4.pyc'
    module.__loader__ = None
    module.__package__ = ''
    exec(compile(code, 'hidden_4.pyc', 'exec'), module.__dict__)
    return [name for name in dir(module) if not name.startswith('__')]

for name in sorted(get_names()):
    print(name)
if __name__ == '__main__':
    print_names()
