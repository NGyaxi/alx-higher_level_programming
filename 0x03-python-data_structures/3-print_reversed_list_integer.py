#!/usr/bin/python3
def print_list_integer(my_list=[]):
    my_list.sort(reverse=True)
    for number in my_list:
        print("{:d}".format(number))
