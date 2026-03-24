---
title: Blocks
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
A block is a batch of transactions and contains the hash of the previous block in the chain. This link blocks together to form a chain. Each additional block strengthens the verification of the previous block and hence the entire blockchain. The block hash value is calculated based on the block content through the hash algorithm, which makes the block content difficult to tamper with because one change in any block would invalidate all the following blocks as all subsequent hashes would change and everyone running the blockchain would notice.

# Why Blocks

To ensure that all participants on the TRON network maintain a synchronized state and agree on the precise history of transactions, we batch transactions into blocks. This means hundreds of transactions are committed, agreed on, and synchronized all at once.

# How Blocks Work

To preserve the transaction history, blocks are strictly ordered. Every new block created contains the hash of its parent block. At any given time, almost all participants on the network agree on the exact number and history of blocks.

Once a Super Representative (SR) produces a block, it will broadcast the newly produced block to the network, and all nodes in the network will add the received block to the end of their blockchain. The exact block consensus process is specified by the "Proof of Stake" protocol of the TRON network.

# What's in a Block

The block object will look a little like this:

```javascript
{
    "block_header":
    {
        "raw_data": 
        {
            "number": 23345280,
            "txTrieRoot": "b04e2c9fcbc26bff7173968a198f23b8a1e2875b3f24c02f186c70c3e7a3041e",
            "witness_address": "410765bed97bbd836f6e489265fd0d9ca1c888e606",
            "parentHash": "000000000164387f439d804494b10e099751748f0a555ce0e7860fee4e1dc6c6",
            "version": 23,
            "timestamp": 1648717482000
        },
        "witness_signature":"47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800"
    },
    "transactions":[{<->},...,{<->}]
}
```

A block consists of two parts: the block header and the transaction list. The block header includes the following fields:

* `raw_data.number` - The block number, that is, the height of the block on the chain.
* `raw_data.txTrieRoot` - The Merkle root of the block.
* `raw_data.witness_address` - The address of the SR account that produces this block.
* `raw_data.parentHash` - The block ID of the previous block. The block ID is the unique identifier of a block, which consists of the block height and the hash of the raw\_data of the block header. parentHash links blocks together in a chain.
* `raw_data.version` - The version number, used to identify the version of the chain.
* `raw_data.timestamp` - The timestamp when the block was created.
* `witness_signature` - The SR's signature on the block.

`transactions` is a list of transactions that are packaged into the block. For the content of each transaction, please refer to the [transaction](https://developers.tron.network/docs/tron-protocol-transaction) chapter.

# Block Interval

In TRON, every three seconds is regarded as one slot. Under normal circumstances, each SR will produce a block within the corresponding slot time. Therefore, the average block interval of TRON is approximately three seconds. If an SR fails to produce a block for some reasons, the corresponding slot will be vacant and the next SR will produce a block in the following slot. During the maintenance period, block production will skip two slots.

# Block Size

Blocks themselves are limited in size, and the maximum size of a block will not exceed 2,000,000 bytes (about 1.9M).
