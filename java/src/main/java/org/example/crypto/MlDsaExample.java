package org.example.crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.NamedParameterSpec;

/**
 * Post-Quantum Digital Signatures using NIST FIPS 204 (ML-DSA-65).
 * Requires Java 24+ (JEP 497) standard JCA provider.
 */
public final class MlDsaExample {
    private MlDsaExample() {}

    public static KeyPair generateKeyPair() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA");
        kpg.initialize(NamedParameterSpec.ML_DSA_65);
        return kpg.generateKeyPair();
    }

    public static byte[] sign(PrivateKey privateKey, byte[] message) throws Exception {
        Signature signature = Signature.getInstance("ML-DSA");
        signature.initSign(privateKey);
        signature.update(message);
        return signature.sign();
    }

    public static boolean verify(PublicKey publicKey, byte[] message, byte[] signatureBytes) throws Exception {
        Signature signature = Signature.getInstance("ML-DSA");
        signature.initVerify(publicKey);
        signature.update(message);
        return signature.verify(signatureBytes);
    }

    public static void main(String[] args) throws Exception {
        KeyPair keys = generateKeyPair();
        byte[] message = "post-quantum signed message".getBytes(StandardCharsets.UTF_8);
        byte[] signature = sign(keys.getPrivate(), message);
        CryptoSupport.require(verify(keys.getPublic(), message, signature), "ML-DSA-65 verification failed");
        System.out.println("MlDsaExample signatureBytes=" + signature.length);
    }
}
