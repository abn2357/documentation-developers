---
title: Contract Address Using in Solidity Language
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
Ethereum VM address is 20 bytes, but TRON's VM address is 21 bytes.

# 1. address conversion

Need to convert TRON's address while using in solidity (recommended):

```text TronAddress.sol
/**
  * @dev convert uint256 (HexString add 0x at beginning) tron address to solidity address type
  * @param  tronAddress uint256 tronAddress, begin with 0x, followed by HexString
  * @return Solidity address type
  */
     
function convertFromTronInt(uint256 tronAddress) public view returns(address){
      return address(tronAddress);
}
```

This is similar with the grammar of the conversion from other types converted to address type in Ethereum.

# 2. address judgement

Solidity has address constant judgement, if using 21 bytes address the compiler will throw out an error, so you should use 20 bytes address, like:

```text CompareAddress.sol
function compareAddress(address tronAddress) public view returns (uint256){
     // if (tronAddress == 0x41ca35b7d915458ef540ade6068dfe2f44e8fa733c) { // compile error
     if (tronAddress == 0xca35b7d915458ef540ade6068dfe2f44e8fa733c) { // right
          return 1;
     } else {
          return 0;
     }
}
```

But if you are using wallet-cli, you can use 21 bytes address, like 0000000000000000000041ca35b7d915458ef540ade6068dfe2f44e8fa733c

# 3. variable assignment

Solidity has address constant assignment, if using 21 bytes address the compiler will throw out an error, so you should use 20 bytes address, like:

```text AssignAddress.sol
function assignAddress() public view {
     // address newAddress = 0x41ca35b7d915458ef540ade6068dfe2f44e8fa733c; // compile error
     address newAddress = 0xca35b7d915458ef540ade6068dfe2f44e8fa733c;
     // do something
}
```
