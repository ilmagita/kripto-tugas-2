# functions.py

def text_to_binary(string):
    s = []
    for i in range(len(string)):
        s.append(char_to_ascii(string[i]))
    
    return s

def char_to_ascii(ch):
    uc = ord(ch)

    return uc

def ascii_to_char(ch):
    uc = chr(ch)

    return uc

def binary_to_string(array):
    string = "".join(ascii_to_char(val) for val in array)
    return string
#print(type(char_to_ascii('a')))