# functions.py

def text_to_binary(string):
    s = []
    for i in range(len(string)):
        s.append(char_to_ascii(string[i]))
    
    return s

def char_to_ascii(ch):
    uc = ord(ch)

    return uc

print(type(char_to_ascii('a')))