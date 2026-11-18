import { randomBytes } from 'node:crypto';
import { ml_dsa65 } from '@noble/post-quantum/ml-dsa.js';

/**
 * Generate an ML-DSA-65 (NIST FIPS 204) keypair.
 * @returns {{ publicKey: Uint8Array, secretKey: Uint8Array }}
 */
export function generateKeyPair() {
  const seed = randomBytes(32);
  return ml_dsa65.keygen(seed);
}

/**
 * Sign a message using ML-DSA-65.
 * @param {Uint8Array} secretKey
 * @param {Uint8Array} message
 * @returns {Uint8Array}
 */
export function sign(secretKey, message) {
  return ml_dsa65.sign(secretKey, message);
}

/**
 * Verify an ML-DSA-65 signature.
 * @param {Uint8Array} publicKey
 * @param {Uint8Array} message
 * @param {Uint8Array} signature
 * @returns {boolean}
 */
export function verify(publicKey, message, signature) {
  return ml_dsa65.verify(publicKey, message, signature);
}
