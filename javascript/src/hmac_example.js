import { createHmac, timingSafeEqual } from 'node:crypto';

/**
 * Compute an HMAC-SHA-256 authentication tag.
 * @param {Buffer|Uint8Array} key
 * @param {Buffer|Uint8Array} message
 * @returns {Buffer}
 */
export function computeHmac(key, message) {
  return createHmac('sha256', key).update(message).digest();
}

/**
 * Verify an HMAC-SHA-256 tag in constant time.
 * @param {Buffer|Uint8Array} key
 * @param {Buffer|Uint8Array} message
 * @param {Buffer|Uint8Array} tag
 * @returns {boolean}
 */
export function verifyHmac(key, message, tag) {
  const expected = computeHmac(key, message);
  if (expected.length !== tag.length) {
    return false;
  }
  return timingSafeEqual(expected, tag);
}
