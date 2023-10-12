#!/usr/bin/python3
for list_alphabet in range(97, 123):
    if (chr(list_alphabet) is not 'q' and chr(list_alphabet) is not 'e'):
        print("{}".format(chr(list_alphabet)), end="")
