#!/usr/bin/python3
def no_c(my_string):
    phrase = my_string.translate({ord('C'): None})
    phrase = phrase.translate({ord('c'): None})
    return phrase
