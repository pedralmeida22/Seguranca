from PyKCS11 import *
from PyKCS11.LowLevel import *

lib = '/usr/local/lib/libpteidpkcs11.so'

pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load(lib)
slots = pkcs11.getSlotList()

classes = {
    CKO_PRIVATE_KEY: 'private key',
    CKO_PUBLIC_KEY: 'public key',
    CKO_CERTIFICATE: 'certificate'
}

for s in slots:
    if 'CARTAO DE CIDADAO' in pkcs11.getTokenInfo(s).label:
        session = pkcs11.openSession(s)
        objs = session.findObjects()

        for obj in objs:
            l = session.getAttributeValue(obj, [CKA_LABEL])[0]
            c = session.getAttributeValue(obj, [CKA_CLASS])[0]
            print('Object with label ' + l + ', of class ' + classes[c])
