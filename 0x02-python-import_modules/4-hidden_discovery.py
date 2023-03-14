#!/usr/bin/python3
import sys
import hidden_4
for n in dir(hidden_4):
    if n[:2] != "__":
        print(n)
