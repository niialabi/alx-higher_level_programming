#!/usr/bin/python3
# return highest value's key
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        top_score = 0
        for key, value in a_dictionary.items():
            if value > top_score:
                top_score = value
    top_score_key = {i for i in a_dictionary if a_dictionary[i] == top_score}
    output = "".join(top_score_key)
    return output
