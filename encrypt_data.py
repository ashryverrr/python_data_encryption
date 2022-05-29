from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#CREATE KEY.KEY FILE IN CURRENT DIRECTORY
key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()

file = open('key.key', 'rb')

key = file.read()
file.close
print(key)

def encrypt_data(to_encrypt):
    f = Fernet(key)
    message = to_encrypt
    encoded = message.encode()
    encrypted = f.encrypt(encoded)
    encrypted = encrypted.decode("utf-8")
    #print(encrypted)
    #encrypted = bytes(encrypted, "utf-8")
    return encrypted


def decrypt_data(data):
    type(data)
    type(key)
    f = Fernet(key)
    #data = bytes(data,"utf-8")
    #encrypted_data = f.decrypt(data)
    encrypted_data = f.decrypt(bytes(data,"utf-8"))
    decrypted_string = encrypted_data.decode()
    
    return decrypted_string