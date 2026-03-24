---
title: Debugging with TronBox Runtime Environment Network
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
TronBox comes built-in with TronBox Runtime Environment Network, a local TRON network designed for development. It allows you to deploy your contracts, run your tests and debug your code on your local environment. When using this network on TronBox, you need to use Docker to pull the image. For the specific usage process, please refer to the [documentation](https://developers.tron.network/reference/tronbox-quickstart).

```text Text
Note：This function requires TronBox V3.4.0 or later.
```

## Solidity `console.log`

When running your contracts and tests on TronBox Runtime Environment Network, you can print logging messages and contract variables calling `console.log` from your Solidity code. To use it, you have to import `tronbox/console.sol` in your contract code.

This is what it looks like:

```javascript solidity
pragma solidity {LATEST_PRAGMA};

import "tronbox/console.sol";

contract Token {
  //...
}
```

Then you can just add some `console.log` calls to the `transfer()` function as if you were using it in JavaScript:

```javascript solidity
function _transfer(address _sender, address _recipient, uint256 _amount) internal {
    require(_recipient != address(0), "TRANSFER_TO_ZERO_ADDRESS");
    uint256 balanceOfSender = balance[_sender];
    require(balanceOfSender >= _amount, "NO_ENOUGH_BALANCE_TO_TRANSFER");

    console.log(
        "Transferring from %s _recipient %s %s tokens",
        msg.sender,
        _recipient,
        _amount
    );

    balanceOfSender -= _amount;
    balance[_sender] = balanceOfSender;
    balance[_recipient] += _amount;
    emit Transfer(_sender, _recipient, _amount);
}

```

The logging output will show when you run your tests:

```shell shell
$  tronbox migrate
Compiling ./contracts/Token.sol...
Compiling tronbox/console.sol...
Writing artifacts to ./build/contracts

Using network 'development'.

Running migration: 1_deploy_token.js
  Running step...
  Deploying Token...
  Token:
    (base58) TDyL9kXC7BUCcQLmxpDV5nsN4CtBDrSGij
    (hex) 412be678b6f7bf51bde302c5ac1120806b4979fe8d
Transferring from TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC _recipient TDvSsdrNM5eeXNL3czpa6AxLDHZA9nwe9K 10000000 tokens
Saving artifacts...

```
