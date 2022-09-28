#!/usr/bin/python3
"""
This module provides a function that reads command
line argument adds them to a list and serialize into
a file
"""
import json
import sys
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file


def add_item(args, filename):
    try:
        list_obj = load(filename)
    except FileNotFoundError:
        list_obj = []
    i = 1
    while i < len(args):
        list_obj.append(args[i])
        i += 1
    save(list_obj, filename)


if __name__ == "__main__":
    add_item(sys.argv, "add_item.json")
