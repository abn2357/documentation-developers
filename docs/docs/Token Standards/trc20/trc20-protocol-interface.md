---
title: Protocol Interface
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
# TRC-20 Contract Standard

TRC-20 is a set of contract standards for the issuance of token assets. Contracts written in compliance with this standard are considered to be a TRC-20 contract. When wallets and exchanges are docking the assets of a TRC-20 contract, they can know which functions and events are defined by the contract based on this standard set, so as to facilitate docking.

## Optional Items

Token Name

```
string public name = "TRONEuropeRewardCoin";
```

Token Abbreviation

```
string public symbol = "TERC";
```

Token Precision (Decimals)

```
uint8 public decimals = 6;
```

## Required Items

```javascript
contract TRC20 {
             function totalSupply() constant returns (uint theTotalSupply);
             function balanceOf(address _owner) constant returns (uint balance);
             function transfer(address _to, uint _value) returns (bool success);
             function transferFrom(address _from, address _to, uint _value) returns (bool success);
             function approve(address _spender, uint _value) returns (bool success);
             function allowance(address _owner, address _spender) constant returns (uint remaining);
             event Transfer(address indexed _from, address indexed _to, uint _value);
             event Approval(address indexed _owner, address indexed _spender, uint _value);
}
```

**totalSupply()**\
This function returns the total supply of the token.

**balanceOf()**\
This function returns the token balance of a specific account.

**transfer()**\
This function is used to transfer a specific number of tokens to a specific address.

**approve()**\
This function is used to authorize a third party (like a DApp smart contract) to transfer the token from the token owner’s account.

**transferFrom()**\
This function is used to enable the third party to transfer the token from the owner account to a recipient account. The owner account must approve to be called by the third party.

**allowance()**\
This function is used to query the remaining quota of tokens the third party can transfer.

## Event Functions

When the token is successfully transferred, the contract will trigger a Transfer Event.

```
event Transfer(address indexed _from, address indexed _to, uint256 _value)
```

When `approval()` is successfully called, the contract will trigger an `Approval` Event.

```
event Approval(address indexed _owner, address indexed _spender, uint256 _value)
```
