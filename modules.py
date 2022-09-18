# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:20:49 2022

@author: ANJAN
"""

# import other necessery modules
import random
# modules for encryption and decryption
import base64
import onetimepad
import pyDes
import math

def reverseEncrypt(inputMessage):
    strInput = str(inputMessage)
    reversStr = strInput[::-1]
    return str(reversStr)

def reverseDecrypt(inputMessage):
    strInput = str(inputMessage)
    reversStr = strInput[::-1]
    return str(reversStr)

def caeserCipherEncrypt(string, shift):
    cipher = ''
    for char in string:
        if char==' ':
            cipher=cipher+' '
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return str(cipher)

def caeserCipherDecrypt(string, shift):
    cipher = ''
    shift = -shift
    for char in string:
        if char==' ':
            cipher=cipher+' '
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return str(cipher)


def base64Encryption(msg):
    sample_string = (msg)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return str(base64_string)

def base64Decryption(decode_entry):
    base64_string = decode_entry
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")    
    return str(sample_string)

def pydesEncrypt(msg):
    data = msg
    k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    return d

def pydesDecrypt(msg2):
    k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    lmao = k.decrypt(msg2).decode('ASCII')
    return str((bytes(lmao, 'utf-8')).decode("utf-8"))


# Encryption
def columnarEncrypt(msg):
    key = "HIKE"
    cipher = ""
    # track key indices
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    # calculate column of the matrix
    col = len(key)
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
    # add the padding character '_' in empty
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher

# Decryption
def columnarDecrypt(cipher):
    key = "HIKE"
    msg = ""
    # track key indices
    k_indx = 0
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    # calculate column of the matrix
    col = len(key)
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(key))
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot","handle repeating words.")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]
    return msg


def encoding(message):
    return((pydesEncrypt(base64Encryption(columnarEncrypt(caeserCipherEncrypt(reverseEncrypt(message),10))))))

def decoding(message):
    return((reverseDecrypt(caeserCipherDecrypt(columnarDecrypt(base64Decryption(pydesDecrypt(eval(message)))),10))))