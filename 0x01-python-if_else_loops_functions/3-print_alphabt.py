#!/usr/bin/python3
for alph in range(97, 123):
    if alph == ord('e') or alph == ord('q'):
        continue
    print("{:c}".format(alph), end='')
