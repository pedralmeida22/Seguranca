import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def read_from_file():
    f = open("key.txt", "rb")
    # print(f.read())
    return f.read()


# Read key bytes from key file ( into variable key )
key = read_from_file()

# Open input file for reading and output file for writing
input_file = open("ex3_output_file.txt", "rb") # usar o ficheiro encriptado do ex anterior
output_file = open("ex4_output_file.txt", "wb")

# TODO
# ir buscar iv ao ficheiro (ler primeiro 16 bytes)
iv = input_file.read(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
decryptor = cipher.decryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()


ciphertext = input_file.read()

plaintext = decryptor.update(padder.update(ciphertext))

output_file.write(plaintext)
print("writen in output file -> ", plaintext)

input_file.close()
output_file.close()
