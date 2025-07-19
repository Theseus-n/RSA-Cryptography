import math
import hashlib

def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            ciphertext += chr(shifted + base)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

