---
title: Transaction Signature Validation
deprecated: false
hidden: false
metadata:
  robots: index
---
## Transaction Signature Verification Principle

Transaction signature verification is the critical security mechanism used to confirm the identity of the transaction initiator and ensure the integrity of the transaction data.

**Core Verification Flow:**

1. The user signs the raw message (Transaction ID) with their private key to generate the digital signature.
2. On the verification side, the signer's public key is recovered from the signature and the raw message (Transaction ID).
3. The recovered public key is converted into a blockchain address.
4. This address is compared against the initiator address recorded in the transaction's raw data.

If the recovered address perfectly matches the initiator address, the signature verification succeeds; otherwise, it is considered a verification failure.

## Method Examples

Developers can use signature validation methods provided in various language SDKs to perform signature checks. Below are examples using TronWeb and Trident.

### TronWeb

TronWeb provides the [tronWeb.trx.ecRecover](https://tronweb.network/docu/docs/API%20List/trx/ecRecover/) method, which is used to recover the actual signer's address from the signature data. Developers can subsequently compare the recovered address with the transaction initiator's address to determine if the signature validation passes.

```javascript
tronWeb.trx.ecRecover(signedTransaction)
```

If the recovered address matches the transaction initiator's address, the validation passes; otherwise, it fails.

### Trident

Trident provides the [SignatureValidator.verify](https://tronprotocol.github.io/trident/guides/transactions/signing.html?h=verify#signature-validation) method for signature validation based on the Transaction ID, signature, and the initiator address. If the signature verification passes, it returns `true`; otherwise, it returns `false`.

```java
// Verify using raw data
boolean isValid = SignatureValidator.verify(byte[] txid, byte[] signature, byte[] ownerAddress);

// Verify using String format
boolean isValid = SignatureValidator.verify(String txid, String signature, String ownerAddress);
```
