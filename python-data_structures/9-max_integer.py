#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return 
    else:
        sort = sorted(my_list)
        max_num = sort[-1]
        return max_num
