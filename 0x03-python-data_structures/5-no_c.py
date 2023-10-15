#!/usr/bin/python3
def no_c(my_string):
    myNew_string = ""
    for char in my_string:
        if char != "c" and char != "C":
            myNew_string += char
    print(myNew_string)
