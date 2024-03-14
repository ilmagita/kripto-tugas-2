# functions.py
import base64
import os

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

def utf8_to_base64(utf8_text):
    return base64.b64encode(utf8_text.encode("utf-8")).decode("utf-8")

def base64_to_utf8(base64_text):
    utf8_text = base64.b64decode(base64_text).decode("utf-8")
    return utf8_text

def binary_data_to_int_array(binary_data):
    array_of_integers = [int(byte) for byte in binary_data]
    return array_of_integers

def int_array_to_binary_data(array_of_integers):
    binary_data = bytes(array_of_integers)
    return binary_data

def read_binary_file(file):
    f = open(file,'rb')
    content = f.read()
    return content

def read_text_file(file):
    f = open(file,'r')
    content = f.read()
    return content

def save_binary_file(cipherText, fileName):
    with open(fileName, 'wb') as f:
        f.write(cipherText)
        
def save_text_file(cipherText, fileName):
    with open(fileName, 'w') as f:
        f.write(cipherText)

def get_file_name(filepath):
    name_without_extension = os.path.splitext(filepath)[0]
    return name_without_extension

def get_file_type(filepath):
    basename = os.path.basename(filepath)
    _, extension = os.path.splitext(basename)

    return extension

def get_base_file_name(filepath):
    basename = os.path.basename(filepath)
    basename_without_extension = os.path.splitext(filepath)[0]
    return basename_without_extension