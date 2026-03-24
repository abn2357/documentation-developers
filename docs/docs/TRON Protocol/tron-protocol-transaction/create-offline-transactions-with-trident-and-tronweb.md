---
title: Creating Offline Transactions with Trident and TronWeb
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
## Preface

Offline transaction construction not only provides users with the ability to securely create and sign transactions in an internet-isolated environment, thus effectively avoiding potential risks such as private key leakage and network attacks in online transactions, but also grants users complete autonomous control over transactions, eliminating reliance on third-party services.

This tutorial will use TRX transfers as an example to explain the principles and practices of offline transaction construction in an accessible manner, demonstrating how to create transactions in a completely offline state using Trident and TronWeb respectively.

## Protobuf Field Descriptions for Transactions

### Transaction Main Structure

```clojure protobuf
message Transaction {
  message raw {
    repeated Contract contract = 1;        // Transaction operations: e.g. TransferContract, VoteWitnessContract types, etc.
    int64 timestamp = 2;                   // Transaction creation time (in milliseconds)
    int64 expiration = 3;                   // Expiration time
    bytes ref_block_bytes = 4;              // Bytes 6 to 8 (exclusive) of reference block height
    bytes ref_block_hash = 5;               // Bytes 8 to 16 (exclusive) of reference block hash
    int64 fee_limit = 6;                    // Maximum fee limit
  }
  raw raw_data = 1;                         // Transaction core data
  repeated bytes signature = 2;             // Signature list
}
```

### Block-related Field Descriptions

| Field             | Description                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ref_block_bytes` | The reference block height. Take the lower 2 bytes of the latest solidified block height (refBlockNum in code).                                              |
| `expiration`      | Transaction expiration time. The value must be greater than that of the latest block time by 1-3 block intervals (3-9 seconds), and must not exceed 24 hours |

### TRX Transfer System Contract Structure

```clojure Protobuf
message TransferContract {
  bytes owner_address = 1;     // Sender address in Base58Check
  bytes to_address = 2;        // Receiver address in Base58Check
  int64 amount = 3;            // Transfer amount (unit: SUN)
}
```

## Build Offline Transactions with Trident-java

Following decentralized design principles, Trident-java natively supports the offline operation mode for transaction construction and signing. Therefore, you can directly call its provided methods to complete offline transaction construction.

### Prepare Development Environment

```Text Groovy
<dependency>
    <groupId>org.tron.trident</groupId>
    <artifactId>trident-core</artifactId>
    <version>Use latest release version</version>
</dependency>
```

### Initialize ApiWrapper

```java java
String privateKey = "xxx";
ApiWrapper client = ApiWrapper.ofNile(privateKey); // Choose according to needs: Mainnet (ofMainnet), Shasta testnet (ofShasta) or Nile testnet(ofNile)
//Initialize with customized grpc endpoint ApiWrapper client = new ApiWrapper("grpc endpoint", "solidity grpc endpoint", "private_key");
```

### Get Block Parameters (Optional)

In Trident-java, enable the local construction mode via:

```java
ApiWrapper.enableLocalCreate(blockId, expiration);
```

Then obtain block information:

```java
BlockExtention blockExtention = client.getNowBlockSolidity();
BlockId blockId = Utils.getBlockId(blockExtention);
```

The above code demonstrates the manual block parameter acquisition. If the local construction mode is not enabled, Trident will automatically query block information from nodes.

Please note that in Trident, transaction creation and signing are offline operations regardless of whether local construction mode is enabled. Therefore, this configuration is optional. This section is intended to help developers understand the transaction structure.

### Build Transaction

In Trident-java, both transaction construction and signing are offline operations, so directly use the transaction methods.

```java
TransactionExtention transaction = client.transfer(fromAddress, toAddress, 10); // Amount unit is SUN. 1TRX = 1,000,000 SUN
Transaction signTransaction = client.signTransaction(transaction);
```

The offline transaction is now fully constructed and must be broadcast before the set expiration time.

## Build Offline Transactions with TronWeb

As the official TRON-recommended JavaScript SDK, TronWeb also provides complete offline transaction methods, achieving the highest security standard of "private keys never touch the network".

### Prepare Development Environment

```c bash
npm install tronweb
```

### Initialize Tronweb Instance

```javascript
const TronWeb = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: fullnode or fullhost parameter, choose either // This field cannot be empty, otherwise initialization will fail
  privateKey: 'Your private key' 
});

```

### Get Block Parameters (Requires Internet Connection)

```javascript
const latestBlock = await tronWeb.trx.getCurrentBlock();
const refBlockNum = latestBlock.block_header.raw_data.number.toString(16).slice(-4).padStart(4, '0');
const refBlockHash = latestBlock.blockID.substring(16, 32);
```

#### Parameter Example

Besides internet-fetched parameters, a current timestamp is also required.

```json
{
  "ref_block_bytes": 48732987,
  "ref_block_hash": "a1b2c3d4e5f6",
  "expiration": 1743594712000 // Unit: millisecond
  "timestamp": 1743591112000
}
```

### Build Offline Transaction

Addresses should be in the Base58Check format. If the original address is in hex, the `toHex` method is unnecessary.

```javascript
function buildOfflineTransaction(
  fromAddress, 
  toAddress, 
  amountInTRX, 
  refBlockParams
) {
  // Construct transaction object
  const transaction = tronWeb.transactionBuilder.sendTrx(
    tronWeb.address.toHex(toAddress),
    tronWeb.toSun(amountInTRX),       // Convert TRX to SUN
    tronWeb.address.toHex(fromAddress),
    refBlockParams                    // Block parameters
  );

  return transaction;
}
```

### Sign Offline

```javascript
function signOfflineTransaction(transaction, privateKey) {
 
  return tronWeb.trx.sign(transaction, privateKey {
    useTronHeader: true, // Must set true
  });
}
```

### Complete Workflow Demo

```javascript
const params = {
  fromAddress: 'Base58CheckSender',
  toAddress: 'Base58CheckReceiver',
  amount: 888,
  refBlockParams: {
    ref_block_bytes: 48732987,
    ref_block_hash: 'a1b2c3d4e5f6',
    expiration: 1743594712000,
    timestamp: 1743591112000 
  },
  privateKey: 'private_key'
};

const rawTx = buildOfflineTransaction(
  params.fromAddress,
  params.toAddress,
  params.amount,
  params.refBlockParams
);

const signedTx = signOfflineTransaction(rawTx, params.privateKey);
```

## Relevant SDK Links

Trident-java：[https://github.com/tronprotocol/trident](https://github.com/tronprotocol/trident)\
TronWeb：[https://github.com/tronprotocol/tronweb](https://github.com/tronprotocol/tronweb)
