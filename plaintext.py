import math

def columnar_transposition_encrypt(plaintext, key):
   
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    
    col = len(key)
    row = math.ceil(len(plaintext) / col)

    
    matrix = [['' for _ in range(col)] for _ in range(row)]
    index = 0
    for r in range(row):
        for c in range(col):
            if index < len(plaintext):
                matrix[r][c] = plaintext[index]
                index += 1

    
    key_order = sorted(list(key))
    ciphertext = ""

    for char in key_order:
        col_index = key.index(char)
        for r in range(row):
            if matrix[r][col_index] != '':
                ciphertext += matrix[r][col_index]

    return ciphertext



plaintext = input("Enter the Plaintext: ")
key = input("Enter the Key: ")

ciphertext = columnar_transposition_encrypt(plaintext, key)
print("\nEncrypted Ciphertext:", ciphertext)
