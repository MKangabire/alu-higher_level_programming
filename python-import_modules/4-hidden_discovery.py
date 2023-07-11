#!/usr/bin/python3
import hidden_4

def main():
    for content in dir(hidden_4):
        if content[:2] != '__':
        print(f"{:s}".format(content))

        
if __name__ == '__main__':
    print_names()
