#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except(TypeError, ValueError):
        return None
    finally:
        print("Inside result: {:.1f}".format(result))
    return result
