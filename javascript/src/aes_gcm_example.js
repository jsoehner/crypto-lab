import { createCipheriv, createDecipheriv, randomBytes } from 'node:crypto';

/**
 * Generate a 256-bit AES key.
 * @returns {Buffer}
 */
export function generateKey() {
  return randomBytes(32);
}

/**
 * Encrypt plaintext using AES-256-GCM with a fresh 96-bit nonce and AAD.
 * @param {Buffer} key
 * @param {Buffer} plaintext
 * @param {Buffer} aad
 * @returns {{ nonce: Buffer, ciphertext: Buffer, tag: Buffer }}
 */
export function encrypt(key, plaintext, aad) {
  if (key.length !== 32) {
    throw new RangeError('AES-256-GCM requires a 32-byte key.');
  }
  const nonce = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', key, nonce);
  if (aad) {
    cipher.setAAD(aad);
  }
  const ciphertext = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  const tag = cipher.getAuthTag();
  return { nonce, ciphertext, tag };
}

/**
 * Decrypt an AES-256-GCM envelope and authenticate AAD.
 * @param {Buffer} key
 * @param {{ nonce: Buffer, ciphertext: Buffer, tag: Buffer }} envelope
 * @param {Buffer} aad
 * @returns {Buffer}
 */
export function decrypt(key, envelope, aad) {
  if (key.length !== 32) {
    throw new RangeError('AES-256-GCM requires a 32-byte key.');
  }
  const decipher = createDecipheriv('aes-256-gcm', key, envelope.nonce);
  decipher.setAuthTag(envelope.tag);
  if (aad) {
    decipher.setAAD(aad);
  }
  return Buffer.concat([decipher.update(envelope.ciphertext), decipher.final()]);
}
