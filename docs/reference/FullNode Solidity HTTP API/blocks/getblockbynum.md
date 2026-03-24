---
title: GetBlockByNum
excerpt: >-
  Returns the block matching the specified height. If the block is returned, it
  indicates that the block has been confirmed (finalized) by the network.
api:
  file: full-node-http-api.json
  operationId: getblockbynum
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

A `Block` object. See [/walletsolidity/getblock](/reference/getblock-2) for details on header and transaction fields.