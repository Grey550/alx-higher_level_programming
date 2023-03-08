#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 5:
    print('last digit of', number ,'and is 5 and is less than 6 and not 0')
elif number == 0:
    print('last digit of', number , 'and is 0')
elif number > 6 and not 0:
    print('lst digit of', number ,  'and is less than 6 and not 0')

