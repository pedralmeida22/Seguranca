import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def read_from_file():
    f = open("key.txt", "rb")
    #print(f.read())
    return f.read()


# Read key bytes from key file ( into variable key )
key = read_from_file()
# Setup cipher : AES in CBC mode , w/ a random IV and PKCS #7 padding ( similar to PKCS #5)
iv = os.urandom(algorithms.AES.block_size // 8)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
encryptor = cipher.encryptor()
padder = padding.PKCS7(algorithms.AES.block_size).padder()

# Open input file for reading and output file for writing
input_file = open("ex3_input_file.txt", "rb")

# Write the contents of iv in the output file
print("iv: ", iv)

while True:  # Cicle to repeat while there is data left on the input file
    # Read a chunk of the input file to the plaintext variable
    plaintext = input_file.read()

    if not plaintext:
        ciphertext = encryptor.update(padder.finalize())
        # Write the contents of ciphertext in the output file
        print("ciphertext1: ", ciphertext)
        break
    else:
        ciphertext = encryptor.update(padder.update(plaintext))
        # Write the ciphertext in the output file
        print("ciphertext: ", ciphertext)

input_file.close()
