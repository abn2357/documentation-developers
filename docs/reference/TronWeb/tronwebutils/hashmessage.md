---
title: message.hashMessage
excerpt: >-
  Computes the
  [TIP-191](https://github.com/tronprotocol/tips/blob/master/tip-191.md)
  personal message digest of message. Personal messages are converted to UTF-8
  bytes and prefixed with "\u0019TRON Signed Message:\n" and the length of
  message.
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
TronWeb.utils.message.hashMessage(message)
```

**Parameters**\
message : String - A string message.

**Return**\
String - The [TIP-191](https://github.com/tronprotocol/tips/blob/master/tip-191.md) digest of message.

**Example**

```javascript
const txJson = TronWeb.utils.message.hashMessage("Hello World");
> '0xa8383a95afcc961b6c36437aff5c8e38a3e35a0ab36ec8630c42fd11f455eac5'
```
