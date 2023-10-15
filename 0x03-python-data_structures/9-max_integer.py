#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        n_list = [my_list[0]]
        for i in my_list:
            if i > n_list[0]:
                n_list[0] = i
        return(n_list[0])
    return(None)
