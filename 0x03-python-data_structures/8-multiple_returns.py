#!/usr/bin/python3
def multiple_returns(sentence):
    output = (len(sentence), (None if len(sentence) == 0 else sentence[0]))
    return output
