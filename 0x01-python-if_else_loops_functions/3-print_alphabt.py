#!/usr/bin/python3
for i in range(97, 123):
    asciToLetter = chr(i)
    if i == 101 or i == 113:
        continue
    print("{}".format(asciToLetter), end='')
