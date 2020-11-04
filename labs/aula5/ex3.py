from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import sys


def main():
    # python3 ex2.py [priv_key_file] [ciphertext_file] [output_file]

    if len(sys.argv) != 4:
        print("Usage: filename.py [key] [text] [output]")
        sys.exit(2)

    # Load key pair to a PEM file protected by a password
    key_filename = sys.argv[1]

    password = "wi"

    with open(key_filename, 'rb') as kf:
        priv_key = serialization.load_pem_private_key(kf.read(), 
                                                        bytes(password, "utf-8"), 
                                                        default_backend())


    # Read for ciphertext no more than maxLen bytes from the input file
    f = open(sys.argv[2], "rb")
    ciphertext = f.read()
    f.close()

    # deciphering the ciphertext using OAEP + MGF1 ( SHA256 ) + SHA256
    plaintext = priv_key.decrypt(ciphertext, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))

    # Write ciphertext in the ouput file
    f = open(sys.argv[3], "wb")
    f.write(plaintext)
    f.close()
    print(plaintext)



if __name__ == "__main__":
    main()
