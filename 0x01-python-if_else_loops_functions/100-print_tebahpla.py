#!/usr/bin/python3
for i in range(122, 96, -1):
    asciToLetter = chr(i - 32)
    if i % 2 == 0:
        asciToLetter = chr(i)
    print("{}".format(asciToLetter), end='')
