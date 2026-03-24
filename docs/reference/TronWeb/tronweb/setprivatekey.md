---
title: setPrivateKey
excerpt: >-
  Set a private key used with the TronWeb instance, used for obtaining the
  address, signing transactions, and getting balances.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ WARNING
>
> Do not use this with any web/user facing TronWeb instances. This will leak the private key.

**Usage** 

```javascript
tronWeb.setPrivateKey('da146...f0d0');
```

**Parameters**\
   String

**Returns**\
  No return value

**Example** 

```javascript
>tronWeb.setPrivateKey('AD71C52E0FC0AB0DFB13B3B911624D4C1AB7BDEFAD93F36B6EF97DC955577509');
undefined
> tronWeb.defaultPrivateKey
'AD71C52E0FC0AB0DFB13B3B911624D4C1AB7BDEFAD93F36B6EF97DC955577509'
```

> Note: Currently the tronweb injected by the tronlink chrome extension does not support this interface.
