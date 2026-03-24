---
title: GetBlockByLatestNum
excerpt: >-
  Retrieves a list of the most recent blocks. Starting from the latest
  solidified block, the method returns the specified number (num) of blocks in
  descending order of height.
api:
  file: full-node-http-api.json
  operationId: wallet-getblockbylatestnum
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Returns**

A list of `Block` objects. See [/wallet/getblock](/reference/getblock-1) for details on header and transaction fields.