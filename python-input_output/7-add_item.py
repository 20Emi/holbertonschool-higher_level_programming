#!/usr/bin/python3
"""Task 7"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file,
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    nomb = "add_item.json"

    try:
        js = load_from_json_file(nomb)
    except FileNotFoundError:
        js = []
    js.extend(sys.argv[1:])
    """'extend()' is used to add multiple items to an existing list."""
    save_to_json_file(js, nomb)
