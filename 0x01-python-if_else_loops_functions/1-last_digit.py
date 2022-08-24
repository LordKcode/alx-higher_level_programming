#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
if number < 0:
    number = number * -1
    flag = 1
n = number % 10
if flag:
    number = number * -1
    n = n * -1
if n > 5:
    print('Last digit of', number, 'is', n, 'and is greater than 5')
elif n == 0:
    print('Last digit of', number, 'is', n, 'and is 0')
else:
    print('Last digit of', number, 'is', n, 'and is less than 6 and not 0')
