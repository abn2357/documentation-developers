---
title: Accounts
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
TRON uses an account model. The address of an account is the unique identifier for it, and a private key signature is required for operating the account. An account has many attributes, such as TRX & TRC-10 token balances, Bandwidth amount, and Energy amount. An account can send transactions to increase or reduce its TRX or TRC-10 token balances, deploy smart contracts, and trigger the smart contracts released by itself or others. All TRON accounts can apply to be Super Representatives (SRs) or vote for the elected SRs. Accounts are the basis of all activities on TRON.

# Account Types

TRON has two account types:

* Externally Owned Account (EOA, also known as general account): an account controlled by anyone with the corresponding private key.
* Contract Account: a smart contract deployed on the TRON network and controlled through the code. No one owns the private key of a contract account.

Both account types have the ability to:

* Receive, hold, and send TRX or other tokens
* Interact with deployed smart contracts

# Accounts & Key Pairs

An account consists of a cryptographic pair of keys: a public key and a private key. The public key can be mapped to an address, while the private key is used to sign transactions. This key pair helps prove that a transaction was actually signed by the sender and prevents forgeries.

This can prevent malicious actors from broadcasting fake transactions because the sender of a transaction can always be verified.

For example, when Alice wants to send TRX from her account to Bob's, she needs to create a transaction and send it to the TRON network for verification. With the key pair, Alice can prove that she originally initiated the transaction request. However, without the encryption mechanism, the malicious actor Eve might be able to publicly broadcast a similar request, "send 5 TRX from Alice's account to Eve's account", while no one can validate whether or not the transaction is requested by Alice herself.

# Externally-Owned Account Creation

TRON’s key pair generation algorithm is exactly the same as that of Ethereum, which uses the Elliptic Curve Digital Signature Algorithm (ECDSA) with secp256k1. The process of key pair generation is:

1. Generate a random private key, which consists of 64 hexadecimal characters.
2. A public key is generated from the private key according to the EDCSA.
3. Take the last 20 bytes of the Keccak-256 output of the public key and add `41` in front of the hex format address.

### Account Address Formats

In addition to the `Hex` format, addresses on the TRON network also have a `Base58Check` format.

* Hex  
  For addresses generated from the same private key, except for the digits `41` in the header part, the remaining parts are identical for the generated addresses on both TRON and Ethereum.
  ```
  418840E6C55B9ADA326D211D818C34A994AECED808
  ```
  Note: For a TRON address in the hex format, you can remove the `41` prefix to get the corresponding Ethereum address.
* Base58Check  
  A Base58Check address can be obtained through the base check encoding of a hex address. All Base58Check addresses begin with `T`. For example:

  ```
  TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL
  ```

  The following section describes address format conversion between hex and Base58Check using TronWeb:

  ```javascript
  tronWeb.address.toHex("TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")
  > "418840E6C55B9ADA326D211D818C34A994AECED808"

  tronWeb.address.fromHex("418840E6C55B9ADA326D211D818C34A994AECED808")
  > "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"
  ```

### Ways to Create Accounts

Users can create an account in the following ways. The essence is to generate a private key and the corresponding address.

* Create an account offline using the command line wallet [wallet-cli](https://github.com/tronprotocol/wallet-cli).
  ```json
  wallet> GenerateAddress
  {
      "address": "TU6JdEDQ...4FQrXPCa", // TRON Address, Base58Check, 34 total chars
      "privateKey": "b1ba1db5...74376176" // Private Key, Hex, 64 total chars
  }
  ```

* Create an account offline using the SDK, taking TronWeb as an example:
  ```javascript
  tronWeb.createAccount()
  > address:
  {
      base58: "TDpBe64D...hw2wDacE", // TRON Address, Base58Check, 34 total chars
      hex: "412A2B9F...8106524B", // TRON Address, Hex, 42 total chars
      privateKey: "427139B4...24960091", // Private Key, Hex, 64 total chars
      publicKey: "0404B604...89ED9731" // Public Key, Hex, 130 total chars
  }
  ```

* Create a private key and the corresponding address via a wallet application, such as [TronLink](https://www.tronlink.org/).

# Account Activation

Newly created accounts do not exist on the chain and need to be activated before they can be found via API queries or in the chain explorer. Accounts can be activated in the following ways:

**Standard Activation Methods**

* Send any amount of TRX or TRC-10 tokens from an existing account to the new account;
* Call Java-tron's `wallet/createaccount`API to create a transaction from an existing account, then sign the transaction and broadcast it to the TRON network.

An account creation fee of **1 TRX** is charged to activate a new account. Additionally, the initiator of the above two types of transactions should have enough Bandwidth resources, which can be obtained by staking TRX. Otherwise, **0.1 TRX** will be burned to pay for the Bandwidth consumption.

**Contract Activation Method**

Transferring TRX or TRC-10 tokens to an unactivated address from a contract will also activate that account. Account activation via a contract incurs an extra **25,000 Energy** cost.

# Contract Accounts

After a smart contract is deployed on the TRON network, the corresponding contract account address is then returned, which is calculated based on the ID of the deployed contract transaction and the sender's account address. The format of a contract account address is the same as that of an external account, that is, in hex or Base58Check. For example:

```
Base58Check: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
Hex:    41A614F803B6FD780986A42C78EC9C7F77E6DED13C
```
