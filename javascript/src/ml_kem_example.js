import { hkdfSync, randomBytes } from 'node:crypto';
import { ml_kem768 } from '@noble/post-quantum/ml-kem.js';
import { encrypt as aesGcmEncrypt, decrypt as aesGcmDecrypt } from './aes_gcm_example.js';

/**
 * Generate an ML-KEM-768 (NIST FIPS 203) keypair.
 * @returns {{ publicKey: Uint8Array, secretKey: Uint8Array }}
 */
export function generateKeyPair() {
  const seed = randomBytes(64);
  return ml_kem768.keygen(seed);
}

/**
 * Encapsulate a fresh 32-byte shared secret for the recipient's public key.
 * @param {Uint8Array} publicKey
 * @returns {{ cipherText: Uint8Array, sharedSecret: Uint8Array }}
 */
export function encapsulate(publicKey) {
  return ml_kem768.encapsulate(publicKey);
}

/**
 * Decapsulate the shared secret using the recipient's secret key.
 * @param {Uint8Array} cipherText
 * @param {Uint8Array} secretKey
 * @returns {Uint8Array}
 */
export function decapsulate(cipherText, secretKey) {
  return ml_kem768.decapsulate(cipherText, secretKey);
}

/**
 * Derive a 256-bit symmetric session key from an ML-KEM shared secret using HKDF-SHA-256.
 * @param {Uint8Array} sharedSecret
 * @param {Uint8Array} salt
 * @param {Uint8Array} info
 * @returns {Buffer}
 */
export function deriveSessionKey(sharedSecret, salt, info) {
  const derived = hkdfSync('sha256', sharedSecret, salt, info, 32);
  return Buffer.from(derived);
}

/**
 * KEM-DEM public-key encryption (replaces RSA-OAEP): ML-KEM-768 + HKDF-SHA-256 + AES-256-GCM.
 * @param {Uint8Array} recipientPublicKey
 * @param {Buffer} plaintext
 * @param {Buffer} aad
 */
export function encryptWithKem(recipientPublicKey, plaintext, aad) {
  const { cipherText: kemCiphertext, sharedSecret } = encapsulate(recipientPublicKey);
  const salt = randomBytes(16);
  const key = deriveSessionKey(sharedSecret, salt, Buffer.from('ml-kem-768-dem-aes-256-gcm', 'utf8'));
  const envelope = aesGcmEncrypt(key, plaintext, aad);
  return { kemCiphertext, salt, envelope };
}

/**
 * KEM-DEM public-key decryption.
 * @param {Uint8Array} recipientSecretKey
 * @param {{ kemCiphertext: Uint8Array, salt: Buffer, envelope: { nonce: Buffer, ciphertext: Buffer, tag: Buffer } }} payload
 * @param {Buffer} aad
 * @returns {Buffer}
 */
export function decryptWithKem(recipientSecretKey, payload, aad) {
  const sharedSecret = decapsulate(payload.kemCiphertext, recipientSecretKey);
  const key = deriveSessionKey(sharedSecret, payload.salt, Buffer.from('ml-kem-768-dem-aes-256-gcm', 'utf8'));
  return aesGcmDecrypt(key, payload.envelope, aad);
}
