from functionList import *


def swap (arr,i,j):
    arr[i], arr[j] = arr[j],arr[i]
    return arr

def ksa (key):
    s = [i for i in range(256)]
    
    j = 0
    
    for i in range(256):
        j = (j + s[i] + key[ i % len(key)]) % 256
        swap(s,i,j)
        
    return s
    
def prga(s, plain):
    i = 0
    j = 0
    cipher = []
    
    for idx in range(len(plain)):
        i = (i+1) % 256
        j = (j + s[i]) % 256
        swap(s,i,j)
        t = (s[i] + s[j]) % 256
        u = s[t]
        cipherChar = u ^ plain[idx]
        cipher.append(cipherChar)
    
    print(cipher)
    cipher = binary_to_string(cipher)
        
    return cipher



def rc4(plain,key):
    key = text_to_binary(key)
    plain = text_to_binary(plain)
    
    s = ksa(key)
    result = prga(s,plain)
    
    return result

key = "kenjjio"
plain = "tsawadikap"
ciphertext = ".§Ì{|içb"

hasil = rc4(plain,key)
hasil2 = rc4(hasil,key)
hasil3 = rc4(ciphertext,key)
print(hasil)
print(hasil2)
print(hasil3)

        
    
    