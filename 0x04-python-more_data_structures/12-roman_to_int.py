#!usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    temp = 0
    ret_value = 0
    rom = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    for i in reversed(roman_string):
        if i.upper() not in rom:
            return None
        i = rom[i.upper()]
        if i >= temp:
            ret_value += i
        else:
            ret_value -= i
        temp = i
    return ret_value
