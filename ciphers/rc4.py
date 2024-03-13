from functionList import *

def swap (arr,i,j):
    arr[i], arr[j] = arr[j],arr[i]
    return arr

def ksa (key):
    s = [i for i in range(256)]
    
    j = 0
    
    for i in range(256):
        j = (j + s[i] + ord(key[ i % len(key)])) % 256
        swap(s,i,j)
        
    return s
    
def playfair_ksa(key):
        key_ksa = ksa(key)
        key_ksa = utf8_to_base64(binary_to_string(key_ksa))
        ency_key = playfair_encryption(key_ksa,key)
        ency_key = text_to_binary(ency_key)
        return ency_key

def prga(s, plain, key):
    i = 0
    j = 0
    cipher = []
    
    for idx in range(len(plain)):
        i = (i+1) % 256
        j = (j + s[i]) % 256
        swap(s,i,j)
        playfair = playfair_encryption(key[ idx % len(key)],key)
        t = (s[i] + s[j] + ord(playfair[0])) % 256
        u = s[t]
        cipherChar = u ^ plain[idx]
        cipher.append(cipherChar)
    
        
    return cipher

def rc4(plain,key):
    plain = text_to_binary(plain)
    

    
    return result

def encryption(plain,key):
    hasil = rc4(plain,key)
    hasil = utf8_to_base64(hasil)
    return hasil

def decryption(plain,key):
    "Hanya dapat menerima text dengan tipe base 64"
    plain = base64_to_utf8(plain)
    hasil = rc4(plain,key)
    return hasil


def rc4_binary_file(fileName,key):
    filename_type = fileName[-4:]
    filename_ori = fileName[:-4]


key = "if20"
plain = "ilmagita S.T 2004?"
cipher = "w7fCocK3wrvCtA/DhMOrwqM/w7fDvcO7e8KkwoFLw7rCj8OPw6vCrcKuwpDDjl5cI8Odw4F3wobCoybDngJEVcKtw43CmVE="


#ciphertext = encryption(plain,key)
#plaintext = decryption(ciphertext,key)

#rc4_binary_file('ciphers/ESP32 (2)_rc4_.png',key)
#rc4_binary_file('ciphers/foto_rc4_.png',key)

#rc4_enc_text_file('ciphers/tes.txt',key)
#rc4_dec_text_file('ciphers/tes_rc4.txt',key)

#print(ciphertext)
#print(plaintext)

rc4_binary_file('ciphers/foto.png',key)
rc4_binary_file('ciphers/foto_rc4_.png',key)









        
    
    