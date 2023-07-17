#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result:{:.1f}".format(result, end=""))
    except ZeroDivisionError:
        print("Inside result:None", end="")
        return None
    except (ValueError, TypeError):
        return None
    finally:
        print()
