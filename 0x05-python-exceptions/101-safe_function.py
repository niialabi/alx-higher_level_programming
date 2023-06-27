#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as x:
        sys.stderr.write("Exception: " + str(x) + "\n")
        return None
