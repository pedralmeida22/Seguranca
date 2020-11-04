from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import sys


def main():
    # python3 asym_keys.py 1024 password key.PEM

    if len(sys.argv) != 4:
        print("Usage: filename.py bits pwd [file]")
        sys.exit(2)

    # Set variables key_size and pwd out of the program arguments
    key_size = int(sys.argv[1])
    pwd = sys.argv[2]

    # Use 65537 (2^16 + 1) as public exponent
    priv_key = rsa.generate_private_key(65537, key_size, default_backend())

    # Save the key pair to a PEM file protected by the password saved in variable pwd
    pem_encoding = priv_key.private_bytes(serialization.Encoding.PEM,
                                        serialization.PrivateFormat.PKCS8,
                                        serialization.BestAvailableEncryption(bytes(pwd, "utf-8")))

    #Save the contents of pem_encoding in a file
    file = open(sys.argv[3], 'wb')
    file.write(pem_encoding)
    file.close()
    print(pem_encoding)



if __name__ == "__main__":
    main()
