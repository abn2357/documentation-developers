---
title: sha3
excerpt: Helper function that will sha3 any value using keccak256
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
tronWeb.sha3(string, prefix=true)
```

**Parameters**\
1.string -String :The string that needs to be hashed using Keccak-256 SHA3 algorithm.\
2.prefix - Boolean :Optional, default is true. true means the return value will have the prefix 0x, false means the return value will not have the prefix 0x.

**Returns**\
String-The result hashed using the Keccak-256 SHA3 algorithm.

**Example** 

```javascript
var hash = tronWeb.sha3("some string to be hashed");
console.log(hash)
>0xc4b9bbe7eb8797cf2818085dbcd6ea6662b3261c28810c318e079c8d0c691da6
var hashOfHash = tronWeb.sha3(hash,true)
console.log(hashOfHash)
>0xfbb2fed40430ff0be9383df03e5a92a8a59eaec7a1a54cf6e1e681d69106e969
var hash1 = tronWeb.sha3("some string to be hashed",false);
console.log(hash1)
>c4b9bbe7eb8797cf2818085dbcd6ea6662b3261c28810c318e079c8d0c691da6
```
