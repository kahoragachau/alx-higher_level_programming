#!/usr/bin/python3
def uppercase(str):
    for i in str:
        value = 1
        if ord(i) in range(97, 123):
            value = chr(ord(i) -32)
        print("{}".format(value), end="")
    print()
