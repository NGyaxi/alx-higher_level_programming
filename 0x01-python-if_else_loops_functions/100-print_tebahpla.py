#!/usr/bin/python3
p = 0
for reverse_string in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(reverse_string - p)), end="")
    i = 32 if p == 0 else 0
