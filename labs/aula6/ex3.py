from PyKCS11 import *
from PyKCS11.LowLevel import *

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives.asymmetric import (padding, rsa, utils)


lib = '/usr/local/lib/libpteidpkcs11.so'


pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load(lib)
slots = pkcs11.getSlotList()

for s in slots:
    if 'CARTAO DE CIDADAO' in pkcs11.getTokenInfo(s).label:
        data = bytes('data to be signed', 'utf-8')

        session = pkcs11.openSession(s)

        privKey = session.findObjects([(CKA_CLASS, CKO_PRIVATE_KEY),
                                       (CKA_LABEL, 'CITIZEN AUTHENTICATION KEY')])[0]
        signature = bytes(session.sign(privKey, data, Mechanism(CKM_SHA1_RSA_PKCS)))

        pubKeyHandle = session.findObjects([(CKA_CLASS, CKO_PUBLIC_KEY), (CKA_LABEL, 'CITIZEN AUTHENTICATION KEY')])[0]

        pubKeyDer = session.getAttributeValue(pubKeyHandle, [CKA_VALUE], TRUE)[0]

        session.closeSession()

        pubKey = load_der_public_key(bytes(pubKeyDer), default_backend())

        try:
            pubKey.verify(signature, data, padding.PKCS1v15(), hashes.SHA1())
            print('Verification succeeded')
        except:
            print('Verification failed')
            
