#!/usr/bin/python3
""" Module indents text based on set delimiters """

def text_indentation(text):
    """ Function that indents string
    
    Args:
        text: string source 
        
    Returns:
        Prints newstring separated by 2 new lines

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    exceptions = ['.', '?', ':']
    result = []
    new_line = ""

    for let in text:
        new_line += let
        if let in exceptions:
            result.append(newline.strip())
        
    for line in result:
        print(line)
        print()
