import java.security.*;
import java.io.*;

import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.io.pem.*;
import org.bouncycastle.operator.*;
import org.bouncycastle.openssl.*;
import org.bouncycastle.openssl.jcajce.*;

import static java.lang.System.*;

class PEMKeyGenerator {

static public void 
main ( String[] args )
{
    OutputStream ostream = null;

    // Chck parameters

    if (args.length < 2) {
        err.println ( "Usage: PEMKeyGenerator bits password [file]" );
        System.exit( 1 );
    }

    int keySize = Integer.parseInt( args[0] );
    String pwd = args[1];

    try {

    if (args.length == 3) {
        ostream = new FileOutputStream( args[2] );
    }
    else {
        ostream = out;
    }

    // Generate key pair

    KeyPairGenerator kpg = KeyPairGenerator.getInstance( "RSA" );

    kpg.initialize( keySize );
    KeyPair kp = kpg.generateKeyPair();

    // AddtheBouncy Castle provider

    Security.addProvider( new BouncyCastleProvider() );

    // construct encryptor to encrypt the private key

    JceOpenSSLPKCS8EncryptorBuilder encBuilder =
        new JceOpenSSLPKCS8EncryptorBuilder( PKCS8Generator.AES_128_CBC );  

    encBuilder.setRandom( new SecureRandom() );  
    encBuilder.setPasssword( pwd.toCharArray() );
    OutputEncryptor encryptor = encBuilder.build();

    // Construct generator to create the PKCS8 object from the private key and encryptor

    JcaPKCS8Generator pkcsGenerator = new JcaPKCS8Generator( kp.getPrivate(), encryptor );  
    PemObject encryptedEncodedKey = pkcsGenerator.generate();  

    // Write the PKCS #8 object to a PEM file

    JcaPEMWriter keyFile = new JcaPEMWriter( new OutputStreamWriter ( ostream ) );
    keyFile.writeObject( encryptedEncodedKey );
    keyFile.close ();

    } catch(Exception e) {
        err.println( "Exception: " + e );
    }
}

}
