---
title: setAddress
excerpt: Sets the address used with all TronWeb API's. Will not sign any transactions.
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
tronWeb.setAddress();
```

**Parameters**\
   String(HexString or Base58)

**Returns**\
  No return value

**Example** 

```javascript
//example 1
>tronWeb.setAddress('TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2');
…
>tronWeb.defaultAddress
{
  hex: '41d3fd1b6f3f3a86303e2925844456c49876c4561f',
  base58: 'TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2'
}

//example 2
>tronWeb.setAddress('41d3fd1b6f3f3a86303e2925844456c49876c4561f');
…
>tronWeb.defaultAddress
{
  hex: '41d3fd1b6f3f3a86303e2925844456c49876c4561f',
  base58: 'TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2'
}
```

> Note: Currently the tronweb injected by the tronlink chrome extension does not support this interface.
