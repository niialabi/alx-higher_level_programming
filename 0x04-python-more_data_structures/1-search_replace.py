#!/usr/bin/python3
# function to search list and replace spec value

def search_replace(my_list, search, replace):
    def rep_formula(x):
        if x == search:
            x = replace
        else:
            x = x
        return (x)
    new_list = list(map(rep_formula, my_list))
    return (new_list)
