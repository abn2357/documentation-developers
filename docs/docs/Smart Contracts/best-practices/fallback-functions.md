---
title: Fallback Functions
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
Fallback functions are safety "default" functions defined within a smart contract, called when no other valid function can handle the request. The original definition from Ethereum's Solidity docs:

> 📘 Fallback Function
>
> A contract can have exactly one unnamed function. This function cannot have arguments and cannot return anything. It is executed on a call to the contract if none of the other functions match the given function identifier (or if no data was supplied at all).
>
> Furthermore, this function is executed whenever the contract receives plain Ether (without data). Additionally, in order to receive Ether, the fallback function must be marked payable. If no such function exists, the contract cannot receive Ether through regular transactions.

For TRON smart contracts, fallback functions *cannot* be triggered when receiving plain TRX. The proposal discussing support has been rejected: [https://github.com/tronprotocol/TIPs/issues/11](https://github.com/tronprotocol/TIPs/issues/11).

TRON supports normal fallback flow when an invalid function is called on a contract:

```javascript
pragma solidity ^0.4.23;

contract Test {
  uint x;
  function() external payable {
    x = x + 1;
  }
  function get() public view returns (uint) {
    return x;
  }
}

contract Caller {
  function callTest(address testAddress) public {
    testAddress.call("invalid");
  }
}
```

In the above example, contract *Test* has a fallback function that increments *x* on each invalid function call. *Caller* demonstrates how to call a non-existing function, incrementing *x* on each call, when *testAddress* is passed in as *Test*'s deployed address.
