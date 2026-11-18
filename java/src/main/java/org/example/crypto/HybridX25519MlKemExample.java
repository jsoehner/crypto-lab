package org.example.crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyPair;
import java.util.Arrays;
import javax.crypto.KEM;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

/**
 * Hybrid Post-Quantum Key Establishment: X25519 + ML-KEM-768 (FIPS 203) -> HKDF-SHA-256 -> AES-256-GCM.
 * Combines classical ECDH (X25519) and post-quantum ML-KEM-768 so security holds if either primitive remains unbroken.
 */
public final class HybridX25519MlKemExample {
    private HybridX25519MlKemExample() {}

    public record HybridCiphertext(byte[] kemEncapsulation, AesGcmExample.Envelope dataEnvelope) {}

    public static byte[] combineSecrets(byte[] x25519Secret, byte[] mlKemSecret, byte[] salt, byte[] info) throws Exception {
        byte[] ikm = new byte[x25519Secret.length + mlKemSecret.length];
        System.arraycopy(x25519Secret, 0, ikm, 0, x25519Secret.length);
        System.arraycopy(mlKemSecret, 0, ikm, x25519Secret.length, mlKemSecret.length);
        try {
            // HKDF-SHA-256 extract+expand over concatenated classical + PQC shared secrets
            javax.crypto.Mac mac = javax.crypto.Mac.getInstance("HmacSHA256");
            byte[] effectiveSalt = salt == null ? new byte[32] : salt.clone();
            mac.init(new SecretKeySpec(effectiveSalt, "HmacSHA256"));
            byte[] prk = mac.doFinal(ikm);
            byte[] okm = new byte[32];
            mac.init(new SecretKeySpec(prk, "HmacSHA256"));
            if (info != null) mac.update(info);
            mac.update((byte) 1);
            System.arraycopy(mac.doFinal(), 0, okm, 0, 32);
            Arrays.fill(prk, (byte) 0);
            return okm;
        } finally {
            Arrays.fill(ikm, (byte) 0);
        }
    }

    public static HybridCiphertext encryptHybrid(
            KeyPair senderX25519,
            java.security.PublicKey recipientX25519Pub,
            java.security.PublicKey recipientMlKemPub,
            byte[] salt,
            byte[] plaintext,
            byte[] aad
    ) throws Exception {
        byte[] x25519Secret = X25519HkdfExample.sharedSecret(senderX25519, recipientX25519Pub);
        KEM.Encapsulated kemEnc = MlKemExample.encapsulate(recipientMlKemPub);
        byte[] mlKemSecret = kemEnc.key().getEncoded();

        byte[] aesKeyBytes = combineSecrets(
                x25519Secret,
                mlKemSecret,
                salt,
                "hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)
        );
        SecretKey aesKey = new SecretKeySpec(aesKeyBytes, "AES");
        AesGcmExample.Envelope envelope = AesGcmExample.encrypt(aesKey, plaintext, aad);
        return new HybridCiphertext(kemEnc.encapsulation(), envelope);
    }

    public static byte[] decryptHybrid(
            KeyPair recipientX25519,
            java.security.PublicKey senderX25519Pub,
            java.security.PrivateKey recipientMlKemPriv,
            byte[] salt,
            HybridCiphertext payload,
            byte[] aad
    ) throws Exception {
        byte[] x25519Secret = X25519HkdfExample.sharedSecret(recipientX25519, senderX25519Pub);
        SecretKey mlKemKey = MlKemExample.decapsulate(recipientMlKemPriv, payload.kemEncapsulation());
        byte[] aesKeyBytes = combineSecrets(
                x25519Secret,
                mlKemKey.getEncoded(),
                salt,
                "hybrid-x25519-mlkem768-aes256gcm".getBytes(StandardCharsets.UTF_8)
        );
        SecretKey aesKey = new SecretKeySpec(aesKeyBytes, "AES");
        return AesGcmExample.decrypt(aesKey, payload.dataEnvelope(), aad);
    }

    public static void main(String[] args) throws Exception {
        KeyPair aliceX25519 = X25519HkdfExample.generateKeyPair();
        KeyPair bobX25519 = X25519HkdfExample.generateKeyPair();
        KeyPair bobMlKem = MlKemExample.generateKeyPair();

        byte[] salt = CryptoSupport.randomBytes(16);
        byte[] aad = "hybrid-pqc-v1".getBytes(StandardCharsets.UTF_8);
        byte[] message = "hybrid quantum-resistant payload".getBytes(StandardCharsets.UTF_8);

        HybridCiphertext encrypted = encryptHybrid(
                aliceX25519, bobX25519.getPublic(), bobMlKem.getPublic(), salt, message, aad
        );
        byte[] decrypted = decryptHybrid(
                bobX25519, aliceX25519.getPublic(), bobMlKem.getPrivate(), salt, encrypted, aad
        );

        CryptoSupport.require(Arrays.equals(message, decrypted), "Hybrid X25519+ML-KEM-768 round-trip failed");
        System.out.println("HybridX25519MlKemExample OK kemBytes=" + encrypted.kemEncapsulation().length);
    }
}
