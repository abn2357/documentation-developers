---
title: isConnected
excerpt: Checks if TronWeb is connected to the nodes and event server.
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
tronWeb.isConnected()
```

**Parameters**\
No need to pass parameters

**Returns**\
  Object

**Example**

```javascript
tronWeb.isConnected();
> …
>[[PromiseStatus]]: "resolved"
[[PromiseValue]]: Object
fullNode: true
solidityNode: true
eventServer: true
...
```
