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
    
        
    return cipher

def rc4(plain,key):
    plain = text_to_binary(plain)
    
    s = ksa(key)
    result = binary_to_string(prga(s,plain))
    
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
    s = ksa(key)
    plain = read_binary_file(fileName)
    plain = binary_data_to_int_array(plain)
    result = prga(s,plain)
    result = int_array_to_binary_data(result)
    save_file(result, f'{filename_ori}_rc4_{filename_type}')

key = "if20"
plain = "ilmagita punya pacar baru, busy and booked"
cipher = "w7fCocK3wrvCtA/DhMOrwqM/w7fDvcO7e8KkwoFLw7rCj8OPw6vCrcKuwpDDjl5cI8Odw4F3wobCoybDngJEVcKtw43CmVE="


ciphertext = encryption(plain,key)
plaintext = decryption(ciphertext,key)

rc4_binary_file('ciphers/foto.png',key)
rc4_binary_file('ciphers/foto_rc4_.png',key)


print(ciphertext)
print(plaintext)







        
    
    