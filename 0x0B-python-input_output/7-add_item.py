#!/usr/bin/python3
"""
Module to load add & save
"""
from sys import argv

import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    present = load_from_json_file("add_item.json")
except FileNotFoundError:
    present = []
present.extend(argv[1:])
save_to_json_file(present, "add_item.json")
