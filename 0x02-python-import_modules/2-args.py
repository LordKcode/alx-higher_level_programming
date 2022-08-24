#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    args = argv[1:]
    length = len(argv)
    i = 1

    if (len(argv) > 1):
        if (length == 2):
            print("{} argument:".format(length - 1))
        else:
            print("{} arguments:".format(length - 1))
        while(length - 1):
            for arg in args:
                print("{}: {}".format(i, arg))
                i += 1
                length -= 1
    elif (length == 1):
        print("0 arguments.")
