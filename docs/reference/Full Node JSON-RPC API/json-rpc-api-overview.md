---
title: Overview
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
JSON-RPC is a stateless, lightweight remote procedure call (RPC) protocol. The JSON-RPC interface supported by the TRON network is compatible with Ethereum's. However, due to the difference in chain mechanism and design, TRON cannot support some interfaces on Ethereum. At the same time, TRON also provides dedicated APIs to create different types of transactions.

**Please pay attention**

* **The JSON-RPC service must be enabled and the port specified in the node configuration file.** If not configured, the service is disabled by default. \*\*

## How to enable or disable the JSON-RPC service of a node

Add the following items in the node's configuration file, then enable or disable them:

```
node.jsonrpc {  
    httpFullNodeEnable = true  
    httpFullNodePort = 50545  
    httpSolidityEnable = true  
    httpSolidityPort = 50555  
}
```

## HEX value encoding

At the moment, there are two key data types that are passed over JSON: unformatted byte arrays and quantities. Both are passed with a hex encoding, however, with different requirements for formatting:

When encoding QUANTITIES (integers, numbers): encode as hex, prefix with “0x”, the most compact representation (slight exception: zero should be represented as “0x0”).\
Examples:

* 0x41 (65 in decimal)
* 0x400 (1024 in decimal)
* WRONG: 0x (should always have at least one digit - zero is “0x0”)
* WRONG: 0x0400 (no leading zeros allowed)
* WRONG: ff (must be prefixed 0x)

When encoding UNFORMATTED DATA (byte arrays, account addresses, hashes, bytecode arrays): encode as hex, prefix with “0x”, two hex digits per byte.\
Examples:

* 0x41 (size 1, “A”)
* 0x004200 (size 3, “\\0B\\0”)
* 0x (size 0, “”)
* WRONG: 0xf0f0f (must be an even number of digits)
* WRONG: 004200 (must be prefixed 0x)
