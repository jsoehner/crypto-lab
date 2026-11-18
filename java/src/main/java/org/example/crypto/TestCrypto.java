package org.example.crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyPair;
import java.util.Arrays;
import javax.crypto.AEADBadTagException;
import javax.crypto.KEM;
import javax.crypto.SecretKey;

public final class TestCrypto {
    public static void main(String[] args) throws Exception {
        // Hashing
        byte[] digest = HashingExample.sha256("test data".getBytes(StandardCharsets.UTF_8));
        CryptoSupport.require(digest.length == 32, "SHA-256 digest length mismatch");

        // HMAC
        byte[] key = CryptoSupport.randomBytes(32);
        byte[] message = "test message".getBytes(StandardCharsets.UTF_8);
        byte[] tag = HmacExample.compute(key, message);
        CryptoSupport.require(HmacExample.verify(key, message, tag), "HMAC verification failed");
        CryptoSupport.require(
                !HmacExample.verify(key, "test message!".getBytes(StandardCharsets.UTF_8), tag),
                "HMAC accepted tampered message"
        );

        // PBKDF2
        char[] password = "test password".toCharArray();
        Pbkdf2Example.DerivedKey stored = Pbkdf2Example.derive(password);
        CryptoSupport.require(Pbkdf2Example.verify(password, stored), "PBKDF2 verification failed");
        CryptoSupport.require(!Pbkdf2Example.verify("wrong password".toCharArray(), stored), "PBKDF2 accepted wrong password");

        // AES-GCM
        SecretKey aesKey = AesGcmExample.generateKey();
        byte[] plaintext = "test message".getBytes(StandardCharsets.UTF_8);
        byte[] aad = "aad".getBytes(StandardCharsets.UTF_8);
        AesGcmExample.Envelope envelope = AesGcmExample.encrypt(aesKey, plaintext, aad);
        CryptoSupport.require(Arrays.equals(plaintext, AesGcmExample.decrypt(aesKey, envelope, aad)), "AES-GCM round-trip failed");
        boolean rejectedBadAad = false;
        try {
            AesGcmExample.decrypt(aesKey, envelope, "wrong-aad".getBytes(StandardCharsets.UTF_8));
        } catch (AEADBadTagException expected) {
            rejectedBadAad = true;
        }
        CryptoSupport.require(rejectedBadAad, "AES-GCM accepted wrong AAD");

        // RSA-OAEP-PSS
        KeyPair keys = RsaOaepPssExample.generateKeyPair();
        byte[] rsaMsg = "rsa message".getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = RsaOaepPssExample.encrypt(keys.getPublic(), rsaMsg);
        CryptoSupport.require(Arrays.equals(rsaMsg, RsaOaepPssExample.decrypt(keys.getPrivate(), ciphertext)), "RSA-OAEP failed");
        byte[] signature = RsaOaepPssExample.sign(keys.getPrivate(), rsaMsg);
        CryptoSupport.require(RsaOaepPssExample.verify(keys.getPublic(), rsaMsg, signature), "RSA-PSS verify failed");
        CryptoSupport.require(!RsaOaepPssExample.verify(keys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), signature), "RSA-PSS accepted tampered message");

        // Ed25519
        KeyPair edKeys = Ed25519Example.generateKeyPair();
        byte[] edMsg = "ed25519 message".getBytes(StandardCharsets.UTF_8);
        byte[] edSig = Ed25519Example.sign(edKeys.getPrivate(), edMsg);
        CryptoSupport.require(Ed25519Example.verify(edKeys.getPublic(), edMsg, edSig), "Ed25519 verify failed");
        CryptoSupport.require(!Ed25519Example.verify(edKeys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), edSig), "Ed25519 accepted tampered message");

        // X25519-HKDF
        KeyPair alice = X25519HkdfExample.generateKeyPair();
        KeyPair bob = X25519HkdfExample.generateKeyPair();
        byte[] salt = CryptoSupport.randomBytes(16);
        byte[] info = "info".getBytes(StandardCharsets.UTF_8);
        byte[] aliceKey = X25519HkdfExample.hkdfSha256(X25519HkdfExample.sharedSecret(alice, bob.getPublic()), salt, info, 32);
        byte[] bobKey = X25519HkdfExample.hkdfSha256(X25519HkdfExample.sharedSecret(bob, alice.getPublic()), salt, info, 32);
        CryptoSupport.require(CryptoSupport.constantTimeEquals(aliceKey, bobKey), "X25519-HKDF mismatch");

        // AES-KeyWrap
        SecretKey kek = AesKeyWrapExample.generateAesKey();
        SecretKey contentKey = AesKeyWrapExample.generateAesKey();
        byte[] wrapped = AesKeyWrapExample.wrap(kek, contentKey);
        SecretKey recovered = AesKeyWrapExample.unwrap(kek, wrapped);
        CryptoSupport.require(Arrays.equals(contentKey.getEncoded(), recovered.getEncoded()), "AES-KeyWrap failed");

        // ML-KEM-768 (FIPS 203)
        KeyPair mlKemKeys = MlKemExample.generateKeyPair();
        KEM.Encapsulated encapsulated = MlKemExample.encapsulate(mlKemKeys.getPublic());
        SecretKey decapsulated = MlKemExample.decapsulate(mlKemKeys.getPrivate(), encapsulated.encapsulation());
        CryptoSupport.require(
                CryptoSupport.constantTimeEquals(encapsulated.key().getEncoded(), decapsulated.getEncoded()),
                "ML-KEM-768 shared secret mismatch"
        );

        // ML-DSA-65 (FIPS 204)
        KeyPair mlDsaKeys = MlDsaExample.generateKeyPair();
        byte[] mlDsaMsg = "pqc message".getBytes(StandardCharsets.UTF_8);
        byte[] mlDsaSig = MlDsaExample.sign(mlDsaKeys.getPrivate(), mlDsaMsg);
        CryptoSupport.require(MlDsaExample.verify(mlDsaKeys.getPublic(), mlDsaMsg, mlDsaSig), "ML-DSA-65 verify failed");
        CryptoSupport.require(
                !MlDsaExample.verify(mlDsaKeys.getPublic(), "tampered".getBytes(StandardCharsets.UTF_8), mlDsaSig),
                "ML-DSA-65 accepted tampered message"
        );

        System.out.println("All Java tests passed!");
    }
}
