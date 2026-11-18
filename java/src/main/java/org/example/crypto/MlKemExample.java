package org.example.crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.spec.NamedParameterSpec;
import javax.crypto.KEM;
import javax.crypto.SecretKey;

/**
 * Post-Quantum Key Encapsulation Mechanism using NIST FIPS 203 (ML-KEM-768).
 * Requires Java 24+ (JEP 496) standard JCA/JCE provider.
 */
public final class MlKemExample {
    private MlKemExample() {}

    public static KeyPair generateKeyPair() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM");
        kpg.initialize(NamedParameterSpec.ML_KEM_768);
        return kpg.generateKeyPair();
    }

    public static KEM.Encapsulated encapsulate(PublicKey recipientPublicKey) throws Exception {
        KEM kem = KEM.getInstance("ML-KEM");
        KEM.Encapsulator encapsulator = kem.newEncapsulator(recipientPublicKey);
        return encapsulator.encapsulate();
    }

    public static SecretKey decapsulate(PrivateKey recipientPrivateKey, byte[] encapsulation) throws Exception {
        KEM kem = KEM.getInstance("ML-KEM");
        KEM.Decapsulator decapsulator = kem.newDecapsulator(recipientPrivateKey);
        return decapsulator.decapsulate(encapsulation);
    }

    public static void main(String[] args) throws Exception {
        KeyPair recipientKeys = generateKeyPair();

        KEM.Encapsulated encapsulated = encapsulate(recipientKeys.getPublic());
        byte[] senderShared = encapsulated.key().getEncoded();
        byte[] ciphertext = encapsulated.encapsulation();

        SecretKey receiverSecret = decapsulate(recipientKeys.getPrivate(), ciphertext);
        byte[] receiverShared = receiverSecret.getEncoded();

        CryptoSupport.require(
                CryptoSupport.constantTimeEquals(senderShared, receiverShared),
                "ML-KEM-768 shared secret mismatch"
        );

        // Derive an AES-256-GCM key from the ML-KEM shared secret using HKDF-SHA-256
        byte[] salt = CryptoSupport.randomBytes(16);
        byte[] info = "ml-kem-768-aes-256-gcm".getBytes(StandardCharsets.UTF_8);
        byte[] derivedKeyBytes = X25519HkdfExample.hkdfSha256(senderShared, salt, info, 32);

        System.out.println("MlKemExample ciphertextBytes=" + ciphertext.length
                + " derivedKey=" + CryptoSupport.hex(derivedKeyBytes));
    }
}
