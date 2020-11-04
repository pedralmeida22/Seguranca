from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import sys


def main():
    # python3 ex2.py [pub_key_file] [plaintext_file] [output_file]

    if len(sys.argv) != 4:
        print("Usage: filename.py [key] [text] [output]")
        sys.exit(2)

    # Load key pair to a PEM file protected by a password
    key_filename = sys.argv[1]  # output do ex1

    # tem de ser a mesma pwd do ex1 (passada como argumento)
    password = "wi"

    with open(key_filename, 'rb') as kf:
        priv_key = serialization.load_pem_private_key(kf.read(), 
                                                        bytes(password, "utf-8"), 
                                                        default_backend())

    pub_key = priv_key.public_key()

    # Calculate the maximum amount of data we can encrypt with OAEP + SHA256
    maxLen = (pub_key.key_size // 8) - 2 * hashes.SHA256.digest_size - 2

    # Read for plaintext no more than maxLen bytes from the input file
    f = open(sys.argv[2], "rb")
    plaintext = f.read(maxLen)
    f.close()

    # Encrypt the plaintext using OAEP + MGF1 ( SHA256 ) + SHA256
    ciphertext = pub_key.encrypt(plaintext, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))

    # Write ciphertext in the ouput file
    f = open(sys.argv[3], "wb")
    f.write(ciphertext)
    f.close()
    print(ciphertext)



if __name__ == "__main__":
    main()
