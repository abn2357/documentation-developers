---
title: GetBlockById
excerpt: 'Retrieves a block by its hash (ID). '
api:
  file: full-node-http-api.json
  operationId: getblockbyid-1
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<br />

**Returns**

A `Block` object. See [/walletsolidity/getblock](/reference/getblock-2) for details on header and transaction fields. for the content contained in block. If the result is null, it indicates the block hash does not exist or the block has not yet reached finality.

<Callout icon="📘" theme="info">
  Note: This endpoint only returns blocks that have been **solidified (confirmed)** by the network. 
</Callout>
