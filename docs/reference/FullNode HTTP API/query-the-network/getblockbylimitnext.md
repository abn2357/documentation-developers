---
title: GetBlockByLimitNext
excerpt: Retrieves a list of block objects within the specified block height range.
api:
  file: full-node-http-api.json
  operationId: getblockbylimitnext
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Enter the `startNum` and `endNum` (block heights) to define the query range, then click **Try It** to fetch the data. For example, use `1` and `3`.

**Returns**

A list of `Block` objects. See [/wallet/getblock](/reference/getblock-1) for details on header and transaction fields.

<br />
