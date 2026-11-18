import { randomBytes } from 'node:crypto';
import { slh_dsa_sha2_128f } from '@noble/post-quantum/slh-dsa.js';

/**
 * Generate an SLH-DSA-SHA2-128f (NIST FIPS 205 / SPHINCS+) stateless hash-based keypair.
 * Ideal for high-assurance root/CA and firmware signatures with zero lattice assumptions.
 * @returns {{ publicKey: Uint8Array, secretKey: Uint8Array }}
 */
export function generateKeyPair() {
  const seed = randomBytes(48);
  return slh_dsa_sha2_128f.keygen(seed);
}

/**
 * Sign a message with SLH-DSA (FIPS 205).
 * @param {Uint8Array} secretKey
 * @param {Uint8Array} message
 * @returns {Uint8Array}
 */
export function sign(secretKey, message) {
  return slh_dsa_sha2_128f.sign(secretKey, message);
}

/**
 * Verify an SLH-DSA (FIPS 205) signature.
 * @param {Uint8Array} publicKey
 * @param {Uint8Array} message
 * @param {Uint8Array} signature
 * @returns {boolean}
 */
export function verify(publicKey, message, signature) {
  return slh_dsa_sha2_128f.verify(publicKey, message, signature);
}
