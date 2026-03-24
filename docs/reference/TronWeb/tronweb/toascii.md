---
title: toAscii
excerpt: Convert HEX string to ASCII3 string
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
tronWeb.toAscii()
```

**Parameters**\
hexString-a hexadecimal string.

**Returns**\
String-The ASCII value corresponding to the given hexadecimal string.

**Example**

```javascript
var str = tronWeb.toAscii("0x74726f6e")
console.log(str)
>”tron”
```
