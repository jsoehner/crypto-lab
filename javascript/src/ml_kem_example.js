import { hkdfSync, randomBytes } from 'node:crypto';
import { ml_kem768 } from '@noble/post-quantum/ml-kem.js';

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
