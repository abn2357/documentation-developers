---
title: Transferring TRC-10 in Smart Contracts
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
# Introduction

Compared to TRC-20 tokens, TRC-10 tokens face a user experience flexibility issue. In Odyssey 3.2, developers and their smart contract callers can interact with TRC-10 tokens via smart contracts according to the contract logic, and conduct TRC-10 token transfers in smart contracts, giving them more control on implementing their tokens in business scenarios. Unlike TRC-20 tokens, sending TRC-10 tokens is like transferring TRX in a contract. TRON developers added interfaces specifically for TRC-10 transfers and queries in Solidity.

**Example of transferring a TRC-10 token in a contract**

```javascript Solidity
pragma solidity ^0.5.0;

contract transferTokenContract {
    constructor() payable public{}
    
    function() payable external {}
    
    function transferTokenTest(address payable toAddress, uint256 tokenValue, trcToken id) payable public    {
        toAddress.transferToken(tokenValue, id);
    }
    
    function msgTokenValueAndTokenIdTest() public payable returns(trcToken, uint256){
        trcToken id = msg.tokenid;
        uint256 value = msg.tokenvalue;
        return (id, value);
    }
    
    function getTokenBalanceTest(address accountAddress) payable public returns (uint256){
        trcToken id = 1000001;
        return accountAddress.tokenBalance(id);
    }
}
```

**TRC-10 token type**\
Odyssey\_v3.2 defines a new type (trcToken) for TRC-10 tokens, which represents the tokenId in a token transfer operation. TRC-10 tokens can be converted to the uint256 type and vice versa.

```javascript
trcToken id = 1000001;
```

**TRC-10 transfer in contract** 

```javascript
address.transferToken(uint256 tokenValue, trcToken tokenId)
```

**Query TRC-10 balance in contract**

```
address.tokenBalance(trcToken) returns(uint256 tokenAmount)
```

Odyssey\_v3.2 defines a new tokenBalance function for TRC-10 token balance query.

**TokenValue & TokenID**\
Msg.tokenvalue, represents the token value in the current msg call, with a default value of 0. Msg.tokenid, represents the token ID in the current msg call, with a default value of 0.
