---
title: getTokensIssuedByAddress
excerpt: Query the TRC10 token issue information of an account.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage**

```javascript
tronWeb.trx.getTokensIssuedByAddress();
```

**Parameters**\
String (HexString或Base58)

**Returns**\
Object

**Example**

```javascript
//example 1
>tronWeb.trx.getTokensIssuedByAddress("TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg").then(result => {console.log(result)});
Promise { <pending> }
> {
  BitTorrent: {
    owner_address: '4137fa1a56eb8c503624701d776d95f6dae1d9f0d6',
    name: 'BitTorrent',
    abbr: 'BTT',
    total_supply: 990000000000000000,
    trx_num: 1,
    precision: 6,
    num: 1,
    start_time: 1548000000000,
    end_time: 1548000001000,
    description: 'Official Token of BitTorrent Protocol',
    url: 'www.bittorrent.com',
    id: '1002000'
  }
}

//example 2
>tronWeb.trx.getTokensIssuedByAddress("4137fa1a56eb8c503624701d776d95f6dae1d9f0d6").then(result => {console.log(result)});
Promise { <pending> }
> {
  BitTorrent: {
    owner_address: '4137fa1a56eb8c503624701d776d95f6dae1d9f0d6',
    name: 'BitTorrent',
    abbr: 'BTT',
    total_supply: 990000000000000000,
    trx_num: 1,
    precision: 6,
    num: 1,
    start_time: 1548000000000,
    end_time: 1548000001000,
    description: 'Official Token of BitTorrent Protocol',
    url: 'www.bittorrent.com',
    id: '1002000'
  }
}
```
