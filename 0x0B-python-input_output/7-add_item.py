#!/usr/bin/python3
"""json representation"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    op = my_file = load_from_json_file("add_item.json")
except:
    op = []
for i in sys.argv[1:]:
    op.append(i)
save_to_json_file(op, "add_item.json")
