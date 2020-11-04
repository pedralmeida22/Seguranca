import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def main():
    if len(sys.argv) < 3:
        print ( "Usage: PEMKeyGenerator bits password [file]\n" )
        sys.exit( 1 )

    key_size = int( sys.argv[1] )
    pwd = sys.argv[2]

    if len(sys.argv) == 4:
        key_file = open( sys.argv[3], "wb" )
    else:
        key_file = sys.stdout.buffer;

    # Use 65537 (2^16 + 1) as public exponent

    keyPair = rsa.generate_private_key( 65537, key_size, default_backend() )

    # Save key pair to a PEM file protected by a password
    # (PKCS #8 password-based, private key encryption)

    pemEncoding = keyPair.private_bytes( serialization.Encoding.PEM,
                                            serialization.PrivateFormat.PKCS8,
                                            serialization.BestAvailableEncryption( bytes( pwd, "utf-8" ) ) )

    key_file.write( pemEncoding )

if __name__ == "__main__":
    main()
