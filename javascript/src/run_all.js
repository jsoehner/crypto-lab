import { randomBytes, timingSafeEqual } from 'node:crypto';
import { sha256 } from './hashing.js';
import { computeHmac, verifyHmac } from './hmac_example.js';
import { generateKey, encrypt, decrypt } from './aes_gcm_example.js';
import {
  generateKeyPair as generateKemKeyPair,
  encapsulate,
  decapsulate,
  deriveSessionKey,
} from './ml_kem_example.js';
import {
  generateKeyPair as generateDsaKeyPair,
  sign as dsaSign,
  verify as dsaVerify,
} from './ml_dsa_example.js';

// 1. SHA-256
const digest = sha256(Buffer.from('reference message', 'utf8'));
console.log(`JS Hashing SHA-256=${digest.toString('hex')}`);

// 2. HMAC-SHA-256
const hmacKey = randomBytes(32);
const hmacMsg = Buffer.from('authenticated payload', 'utf8');
const tag = computeHmac(hmacKey, hmacMsg);
if (!verifyHmac(hmacKey, hmacMsg, tag)) {
  throw new Error('HMAC verification failed');
}
console.log(`JS HmacExample tag=${tag.toString('hex')}`);

// 3. AES-256-GCM
const aesKey = generateKey();
const aad = Buffer.from('app=v1;purpose=reference', 'utf8');
const env = encrypt(aesKey, Buffer.from('confidential data', 'utf8'), aad);
const plaintext = decrypt(aesKey, env, aad);
if (plaintext.toString('utf8') !== 'confidential data') {
  throw new Error('AES-GCM round-trip failed');
}
console.log('JS AesGcmExample round-trip OK');

// 4. ML-KEM-768 (NIST FIPS 203) + HKDF-SHA-256
const kemKeys = generateKemKeyPair();
const { cipherText, sharedSecret: senderSecret } = encapsulate(kemKeys.publicKey);
const receiverSecret = decapsulate(cipherText, kemKeys.secretKey);
if (!timingSafeEqual(senderSecret, receiverSecret)) {
  throw new Error('ML-KEM-768 shared secret mismatch');
}
const sessionKey = deriveSessionKey(
  senderSecret,
  randomBytes(16),
  Buffer.from('ml-kem-768-session', 'utf8'),
);
console.log(`JS MlKemExample ciphertextBytes=${cipherText.length} derivedKey=${sessionKey.toString('hex')}`);

// 5. ML-DSA-65 (NIST FIPS 204)
const dsaKeys = generateDsaKeyPair();
const pqcMsg = Buffer.from('post-quantum signed message', 'utf8');
const sig = dsaSign(dsaKeys.secretKey, pqcMsg);
if (!dsaVerify(dsaKeys.publicKey, pqcMsg, sig)) {
  throw new Error('ML-DSA-65 verification failed');
}
console.log(`JS MlDsaExample signatureBytes=${sig.length}`);
