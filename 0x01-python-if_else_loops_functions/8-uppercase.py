#!/usr/bin/python3
def uppercase(str):
    alph = ""
    for ch in str:
        if ord(ch) in range(97, 123):
            alph += chr(ord(ch) - 32)
        else:
            alph += ch
    print("{}".format(alph))
