---
title: Illegal Operations and Penalties
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
Illegal operations/invalid operation codes compiled from smart contracts not only fail to deploy/execute, but also incur a full penalty of the *fee\_limit*. As users normally set the fee limit to 10000 TRX (max), this is a significant penalty and is even more costly if the user attempts to retry the operations automatically.

There are two common ways invalid operation codes are triggered:

1. User is manually trying to inject arbitrarily invalid operation code into the smart contract bytecode.
2. User is using a newer compiler before new operation codes are supported. Specifically as a past example, before the "TRC-10 token transfer in smart contracts" is allowed ([https://tronscan.org/#/proposal/15](https://tronscan.org/#/proposal/15)), if user happens to use the new compiler to deploy/execute smart contracts, the full *fee\_limit* would be deducted from the user account.

```javascript
pragma solidity ^0.4.24;

contract transferTokenContract {
    constructor() payable public{}
  
    function() payable public{}
  
    function transferTokenTest(address toAddress, uint256 tokenValue, trcToken id) payable public {
        require(id > 1000000);
        toAddress.transferToken(tokenValue, id);
    }
  
    function msgTokenValueAndTokenIdTest() public payable returns (trcToken, uint256) {
        trcToken id = msg.tokenid;
        uint256 value = msg.tokenvalue;
        return (id, value);
    }
  
    function getTokenBalanceTest(address accountAddress) payable public returns (uint256) {
        trcToken id = 1000001;
        require(id > 1000000);
        return accountAddress.tokenBalance(id);
    }
}
```

In the above example, *transferToken* maps to op code *0xd0*, *tokenBalance* maps to op code *0xd1*, *msg.tokenid* maps to op code *0xd2*, *msg.tokenvalue* maps to op code *0xd3*. If any of these is used before network has activated the new TRC-10 transfer proposal, TVM will reject this operation and penalize the entire *fee\_limit*.

The general rule of thumb is to always use the latest Tron-Web/Tron-Box for compiling/deploying/executing contracts. When switching between Testnet and Mainnet, make sure to re-compile all contracts in case of different network parameters deciding different sets of valid operation codes.
