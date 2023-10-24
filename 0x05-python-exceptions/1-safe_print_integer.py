#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            try:
                print(my_list[count], end=' ')
            except:
                pass
            count += 1
        print()
        return count
    except TypeError:
        print("An error occurred.")
        return count
