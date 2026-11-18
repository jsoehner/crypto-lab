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

    public record KemEnvelope(byte[] encapsulation, byte[] salt, AesGcmExample.Envelope dataEnvelope) {}

    /**
     * KEM-DEM public-key encryption (replaces RSA-OAEP): ML-KEM-768 + HKDF-SHA-256 + AES-256-GCM.
     */
    public static KemEnvelope encryptWithKem(PublicKey recipientPublicKey, byte[] plaintext, byte[] aad) throws Exception {
        KEM.Encapsulated encapsulated = encapsulate(recipientPublicKey);
        byte[] salt = CryptoSupport.randomBytes(16);
        byte[] info = "ml-kem-768-dem-aes-256-gcm".getBytes(StandardCharsets.UTF_8);
        byte[] keyBytes = X25519HkdfExample.hkdfSha256(encapsulated.key().getEncoded(), salt, info, 32);
        SecretKey aesKey = new javax.crypto.spec.SecretKeySpec(keyBytes, "AES");
        AesGcmExample.Envelope envelope = AesGcmExample.encrypt(aesKey, plaintext, aad);
        return new KemEnvelope(encapsulated.encapsulation(), salt, envelope);
    }

    public static byte[] decryptWithKem(PrivateKey recipientPrivateKey, KemEnvelope kemEnvelope, byte[] aad) throws Exception {
        SecretKey sharedSecret = decapsulate(recipientPrivateKey, kemEnvelope.encapsulation());
        byte[] info = "ml-kem-768-dem-aes-256-gcm".getBytes(StandardCharsets.UTF_8);
        byte[] keyBytes = X25519HkdfExample.hkdfSha256(sharedSecret.getEncoded(), kemEnvelope.salt(), info, 32);
        SecretKey aesKey = new javax.crypto.spec.SecretKeySpec(keyBytes, "AES");
        return AesGcmExample.decrypt(aesKey, kemEnvelope.dataEnvelope(), aad);
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
