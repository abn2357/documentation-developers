---
title: The Special Constants Differ from Ethereum
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Currency**

Like solidity supports ETH, TRON VM supports trx and sun, 1 trx = 1000000 sun, case sensitive, only support lower case. Tron-IDE supports trx and sun, remix does not support trx and sun.\
We recommend to use Tron-IDE instead of remix to build TRON smart contract.

**Block**

* block.blockhash (uint blockNumber) returns (bytes32): specified block hash, can only apply to the latest 256 blocks and current block excluded
* block.coinbase (address): SuperNode address that produced the current block
* block.difficulty (uint): current block difficulty, not recommended, set 0
* block.gaslimit (uint): current block gas limit, not supported, set 0
* block.number (uint): current block number
* block.timestamp (uint): current block timestamp
* gasleft() returns (uint256): remaining gas
* msg.data (bytes): complete call data
* msg.gas (uint): remaining gas - since 0.4.21, not recommended, replaced by gesleft()
* msg.sender (address): message sender (current call)
* msg.sig (bytes4): first 4 bytes of call data (function identifier)
* msg.value (uint): the amount of SUN send with message
* now (uint): current block timestamp (block.timestamp)
* tx.gasprice (uint): the gas price of transaction, not recommended, set 0
* tx.origin (address): transaction initiator\
  Each command of smart contract consume system resource while running, we use 'Energy' as the unit of the consumption of the resource.
