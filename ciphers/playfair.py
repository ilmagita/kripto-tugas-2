## MODIFIED PLAYFAIR CYPHER
from functionList import text_to_binary, char_to_ascii
from math import ceil

## HELPER FUNCTIONS
def str_to_playfair_key(string):
    """
    Function to arrange a string of a cipherkey to the Playfair square of 16x16.
    """

    # remove duplicate letters
    ch_list = []
    for i in range(len(string)):
        if (ord(string[i])) not in ch_list:
            ch_list.append(ord(string[i]))

    # initialize matrix
    matr = [i for i in range(1, 257)]

    for i in range(len(matr)):
        if matr[i] not in ch_list:
            ch_list.append((matr[i]))

    playfair_key = [[ch_list[i * 16 + j] for j in range(16)] for i in range(16)]
    return playfair_key

def str_to_playfair_bigram_list(string, substitute_ch='X'):
    """
    Function to arrange plaintext to an array of bigrams intended for Playfair cipher.
    """

    # handle repeating letters in a bigram - insert substitute character between
    new_string = [ord(char) for char in string]
    bigram_check_list = []
    i = 0

    while i < (len(new_string)):
        el = [0, 0]
        bigram = new_string[i:i+2]

        if i < len(new_string) - 1:
            if bigram[0] == bigram[1]:
                el[0] = bigram[0]
                el[1] = ord(substitute_ch)

                i = i + 1
            else:
                el[0] = bigram[0]
                el[1] = bigram[1]

                i = i + 2
        else:
            el[0] = bigram[0]
            el[1] = ord(substitute_ch)

            i = i + 1

        bigram_check_list.append(el)
   
    return bigram_check_list

def find_el_in_matrix(matrix, el):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == el:
                return i, j
    return None

## ENCRYPTION FUNCTIONS
def playfair_encrypt_bigram(playfair_key, bigram):
    first_el_position = find_el_in_matrix(playfair_key, bigram[0])
    second_el_position = find_el_in_matrix(playfair_key, bigram[1])

    if first_el_position is not None and second_el_position is not None:
        first_el_row, first_el_col = first_el_position
        second_el_row, second_el_col = second_el_position

        cipher_bigram = [0, 0]

        if (first_el_row == second_el_row):
            # if both elements in same row
            cipher_bigram[0] = playfair_key[first_el_row][(first_el_col + 1) % 16]
            cipher_bigram[1] = playfair_key[second_el_row][(second_el_col + 1) % 16]

        elif (first_el_col == second_el_col):
            # if both elements in same column
            cipher_bigram[0] = playfair_key[(first_el_row + 1) % 16][first_el_col]
            cipher_bigram[1] = playfair_key[(second_el_row + 1) % 16][second_el_col]

        else:
            cipher_bigram[0] = playfair_key[first_el_row][second_el_col]
            cipher_bigram[1] = playfair_key[second_el_row][first_el_col]

        return cipher_bigram

def playfair_encryption(plaintext_input, cipherkey_input):
    plaintext_bigram_list = str_to_playfair_bigram_list(plaintext_input)
    cipherkey_matrix = str_to_playfair_key(cipherkey_input)

    cipher_list = []

    for i in range(len(plaintext_bigram_list)):
        cipher_list.append(playfair_encrypt_bigram(cipherkey_matrix, plaintext_bigram_list[i]))
    
    ch_list = [[chr(num) for num in inner] for inner in cipher_list]
    ch_str = ''.join([''.join(inner) for inner in ch_list])
    return ch_str

## DECRYPTION FUNCTIONS
def playfair_decrypt_bigram(playfair_key, bigram):
    first_el_position = find_el_in_matrix(playfair_key, bigram[0])
    second_el_position = find_el_in_matrix(playfair_key, bigram[1])

    if first_el_position is not None and second_el_position is not None:
        first_el_row, first_el_col = first_el_position
        second_el_row, second_el_col = second_el_position

        cipher_bigram = [0, 0]

        if (first_el_row == second_el_row):
            # if both elements in same row
            cipher_bigram[0] = playfair_key[first_el_row][(first_el_col - 1) % 16]
            cipher_bigram[1] = playfair_key[second_el_row][(second_el_col - 1) % 16]

        elif (first_el_col == second_el_col):
            # if both elements in same column
            cipher_bigram[0] = playfair_key[(first_el_row - 1) % 16][first_el_col]
            cipher_bigram[1] = playfair_key[(second_el_row - 1) % 16][second_el_col]

        else:
            cipher_bigram[0] = playfair_key[first_el_row][second_el_col]
            cipher_bigram[1] = playfair_key[second_el_row][first_el_col]

        return cipher_bigram
    
def playfair_decryption(plaintext_input, cipherkey_input):
    plaintext_bigram_list = str_to_playfair_bigram_list(plaintext_input)
    cipherkey_matrix = str_to_playfair_key(cipherkey_input)

    cipher_list = []

    for i in range(len(plaintext_bigram_list)):
        cipher_list.append(playfair_decrypt_bigram(cipherkey_matrix, plaintext_bigram_list[i]))

    ch_list = [[chr(num) for num in inner] for inner in cipher_list]
    ch_str = ''.join([''.join(inner) for inner in ch_list])
    return ch_str

#playfair_key = test
playfair_key = [[116, 101, 115, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
                [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61],
                [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77],
                [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93],
                [94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                [111, 112, 113, 114, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128],
                [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
                [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160],
                [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176],
                [177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192],
                [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208],
                [209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                [225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240],
                [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]]

# result = playfair_encryption('perginya ke pasar', 'test')
# print(f'-{result}-')
# result_d = playfair_decryption(result, 'test')
# print(result_d)
