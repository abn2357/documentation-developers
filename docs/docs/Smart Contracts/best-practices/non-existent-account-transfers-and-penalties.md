---
title: Non-Existent Account Transfers and Penalties
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
In addition to illegal operations, transferring TRX/TRC10 to non-existent accounts also incurs a full penalty of the *fee\_limit*. As users normally set the fee limit to 10000 TRX (max), this is a significant penalty and can be even more costly if the user attempts to retry the operations automatically.

# Penalized Contracts Examples

### Transferring TRX into a Non-Existent/Invalid Account

```javascript
pragma solidity ^0.4.23;

contract Invalid {

  function transAddr() public payable {
    address invalid = 0x1234aabb;
    invalid.transfer(10 trx);
  }
  
  function transAddr2(address addr) public payable {
    addr.transfer(10 trx);
  }
}
```

In the above example, *transAddr* always fails and consumes the *fee\_limit*. In the more common case of *transAddr2*, the developer should make sure *addr* is pre-validated in either Tron-Web or some other existing address. Otherwise, the user pays for the *fee\_limit* penalty.

### Transferring TRX into Itself

```javascript
pragma solidity ^0.4.23;

contract Self {

  function transAddr() public payable {
    address(this).transfer(10 trx);
  }

  function transAddr2(address addr) public payable {
    addr.transfer(10 trx);
  }

  function transAddr3(address addr) public payable {
    require(addr != address(this));
    addr.transfer(10 trx);
  }
}
```

Similarly, *transAddr* always incurs the *fee\_limit* penalty. *transAddr2* will fail the self-transfer case if *addr* is the contract's address itself. *transAddr3* protects against the self-transfer penalty but still suffers from the non-existent account problem above.

### TRC10 Token Transfer into a Non-Existent/Invalid Account

```javascript
pragma solidity ^0.4.24;

contract TRC10 {

  function sendBalance(address to) public payable {
    trcToken id = msg.tokenid;
    uint256 value = msg.tokenvalue;
    to.transferToken(value, id);
  }

  function sendBalance2() public payable {
    trcToken id = msg.tokenid;
    uint256 value = msg.tokenvalue;
    address(this).transferToken(value, id);
  }
}
```

Similar to the TRX transfer above, if *to* account does not exist, *sendBalance* fails with a *fee\_limit* penalty. The self-transfer case *sendBalance2* also incurs *fee\_limit*.
