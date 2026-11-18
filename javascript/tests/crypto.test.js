import test from 'node:test';
import assert from 'node:assert/strict';
import { randomBytes, timingSafeEqual } from 'node:crypto';
import { sha256 } from '../src/hashing.js';
import { computeHmac, verifyHmac } from '../src/hmac_example.js';
import { generateKey, encrypt, decrypt } from '../src/aes_gcm_example.js';
import {
  generateKeyPair as generateKemKeyPair,
  encapsulate,
  decapsulate,
  deriveSessionKey,
  encryptWithKem,
  decryptWithKem,
} from '../src/ml_kem_example.js';
import {
  generateKeyPair as generateDsaKeyPair,
  sign as dsaSign,
  verify as dsaVerify,
} from '../src/ml_dsa_example.js';
import {
  generateX25519KeyPair,
  encryptHybrid,
  decryptHybrid,
} from '../src/hybrid_kem_example.js';
import {
  generateKeyPair as generateSlhKeyPair,
  sign as slhSign,
  verify as slhVerify,
} from '../src/slh_dsa_example.js';

test('SHA-256 produces 32-byte digest and detects changes', () => {
  const d1 = sha256(Buffer.from('test data'));
  const d2 = sha256(Buffer.from('test data '));
  assert.equal(d1.length, 32);
  assert.notDeepEqual(d1, d2);
});

test('HMAC-SHA-256 verifies valid tag and rejects tampered message', () => {
  const key = randomBytes(32);
  const msg = Buffer.from('test message');
  const tag = computeHmac(key, msg);
  assert.equal(verifyHmac(key, msg, tag), true);
  assert.equal(verifyHmac(key, Buffer.from('test message!'), tag), false);
});

test('AES-256-GCM round-trips and rejects wrong AAD or tampered ciphertext', () => {
  const key = generateKey();
  const plaintext = Buffer.from('secret message');
  const aad = Buffer.from('aad');
  const env = encrypt(key, plaintext, aad);
  assert.deepEqual(decrypt(key, env, aad), plaintext);

  assert.throws(() => decrypt(key, env, Buffer.from('wrong-aad')));

  const tampered = {
    nonce: env.nonce,
    ciphertext: Buffer.from(env.ciphertext),
    tag: env.tag,
  };
  tampered.ciphertext[0] ^= 0xff;
  assert.throws(() => decrypt(key, tampered, aad));
});

test('ML-KEM-768 (FIPS 203) encapsulates, decapsulates, and derives identical session key', () => {
  const { publicKey, secretKey } = generateKemKeyPair();
  const { cipherText, sharedSecret: senderSs } = encapsulate(publicKey);
  const receiverSs = decapsulate(cipherText, secretKey);
  assert.equal(timingSafeEqual(senderSs, receiverSs), true);

  const salt = Buffer.from('fixed-test-salt');
  const info = Buffer.from('ml-kem-768-info');
  const k1 = deriveSessionKey(senderSs, salt, info);
  const k2 = deriveSessionKey(receiverSs, salt, info);
  assert.deepEqual(k1, k2);
  assert.equal(k1.length, 32);
});

test('ML-DSA-65 (FIPS 204) signs and verifies, rejecting tampered messages', () => {
  const { publicKey, secretKey } = generateDsaKeyPair();
  const msg = Buffer.from('pqc signed payload');
  const sig = dsaSign(secretKey, msg);
  assert.equal(dsaVerify(publicKey, msg, sig), true);
  assert.equal(dsaVerify(publicKey, Buffer.from('tampered payload'), sig), false);
});

test('ML-KEM-768 KEM-DEM (replaces RSA-OAEP) encrypts/decrypts and rejects wrong AAD', () => {
  const { publicKey, secretKey } = generateKemKeyPair();
  const pt = Buffer.from('confidential kem-dem payload');
  const aad = Buffer.from('context-v1');
  const payload = encryptWithKem(publicKey, pt, aad);
  assert.deepEqual(decryptWithKem(secretKey, payload, aad), pt);
  assert.throws(() => decryptWithKem(secretKey, payload, Buffer.from('wrong-aad')));
});

test('Hybrid X25519 + ML-KEM-768 encrypts/decrypts and rejects wrong AAD', () => {
  const aliceX = generateX25519KeyPair();
  const bobX = generateX25519KeyPair();
  const bobKem = generateKemKeyPair();
  const pt = Buffer.from('hybrid pqc secret');
  const aad = Buffer.from('hybrid-aad');
  const payload = encryptHybrid(aliceX.privateKey, bobX.publicKey, bobKem.publicKey, pt, aad);
  assert.deepEqual(decryptHybrid(bobX.privateKey, aliceX.publicKey, bobKem.secretKey, payload, aad), pt);
  assert.throws(() => decryptHybrid(bobX.privateKey, aliceX.publicKey, bobKem.secretKey, payload, Buffer.from('bad-aad')));
});

test('SLH-DSA (FIPS 205) signs and verifies, rejecting tampered messages', () => {
  const { publicKey, secretKey } = generateSlhKeyPair();
  const msg = Buffer.from('root-ca-payload');
  const sig = slhSign(secretKey, msg);
  assert.equal(slhVerify(publicKey, msg, sig), true);
  assert.equal(slhVerify(publicKey, Buffer.from('tampered-ca-payload'), sig), false);
});
