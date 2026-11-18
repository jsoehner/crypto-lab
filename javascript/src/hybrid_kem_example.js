import { diffieHellman, generateKeyPairSync, hkdfSync, randomBytes } from 'node:crypto';
import { ml_kem768 } from '@noble/post-quantum/ml-kem.js';
import { encrypt as aesGcmEncrypt, decrypt as aesGcmDecrypt } from './aes_gcm_example.js';

/**
 * Generate a classical X25519 keypair for hybrid key agreement.
 */
export function generateX25519KeyPair() {
  return generateKeyPairSync('x25519');
}

/**
 * Derive a 256-bit hybrid session key by combining X25519 and ML-KEM-768 shared secrets via HKDF-SHA-256.
 * @param {Buffer|Uint8Array} x25519Secret
 * @param {Buffer|Uint8Array} mlKemSecret
 * @param {Buffer|Uint8Array} salt
 * @param {Buffer|Uint8Array} info
 * @returns {Buffer}
 */
export function combineHybridSecrets(x25519Secret, mlKemSecret, salt, info) {
  const ikm = Buffer.concat([Buffer.from(x25519Secret), Buffer.from(mlKemSecret)]);
  return Buffer.from(hkdfSync('sha256', ikm, salt, info, 32));
}

/**
 * Hybrid X25519 + ML-KEM-768 authenticated encryption (replaces standalone X25519+HKDF).
 */
export function encryptHybrid(senderX25519Priv, recipientX25519Pub, recipientMlKemPub, plaintext, aad) {
  const x25519Secret = diffieHellman({
    privateKey: senderX25519Priv,
    publicKey: recipientX25519Pub,
  });
  const { cipherText: kemCiphertext, sharedSecret: mlKemSecret } = ml_kem768.encapsulate(recipientMlKemPub);
  const salt = randomBytes(16);
  const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');
  const aesKey = combineHybridSecrets(x25519Secret, mlKemSecret, salt, info);
  const envelope = aesGcmEncrypt(aesKey, plaintext, aad);
  return { kemCiphertext, salt, envelope };
}

/**
 * Hybrid X25519 + ML-KEM-768 decryption.
 */
export function decryptHybrid(recipientX25519Priv, senderX25519Pub, recipientMlKemPriv, payload, aad) {
  const x25519Secret = diffieHellman({
    privateKey: recipientX25519Priv,
    publicKey: senderX25519Pub,
  });
  const mlKemSecret = ml_kem768.decapsulate(payload.kemCiphertext, recipientMlKemPriv);
  const info = Buffer.from('hybrid-x25519-mlkem768-aes256gcm', 'utf8');
  const aesKey = combineHybridSecrets(x25519Secret, mlKemSecret, payload.salt, info);
  return aesGcmDecrypt(aesKey, payload.envelope, aad);
}
