import { createHash } from 'node:crypto';

/**
 * Compute the SHA-256 digest of a Buffer or Uint8Array.
 * @param {Buffer|Uint8Array} data
 * @returns {Buffer}
 */
export function sha256(data) {
  return createHash('sha256').update(data).digest();
}
