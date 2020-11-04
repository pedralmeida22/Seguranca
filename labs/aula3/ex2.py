import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


def write_to_file(content):
    f = open("key.txt", "wb")
    f.write(content)
    f.close()


def read_from_file():
    f = open("key.txt", "rb")
    print(f.read())


# The PBKDF2 generator of Python receives as input the number of byes to generate ,
# instead of bits

pwd = input("Enter password: ")

salt = b'\ x00 '
kdf = PBKDF2HMAC(hashes.SHA1(), 16, salt, 1000, default_backend())
key = kdf.derive(bytes(pwd, 'UTF -8 '))

# Write key in a file
write_to_file(key)
read_from_file()
