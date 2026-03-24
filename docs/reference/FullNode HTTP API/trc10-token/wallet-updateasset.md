---
title: UpdateAsset
excerpt: Updates basic TRC-10 token information.
api:
  file: full-node-http-api.json
  operationId: wallet-updateasset
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

`Transaction` object - JSON object: Unsigned transaction. 

Please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. 

For the `UpdateAssetContract` type, the fields within `raw_data.contract[0].parameter.value`  are listed as follows:

| Field            | Type   | Description                                 |
| :--------------- | :----- | :------------------------------------------ |
| owner_address    | string | Token issuer's address                      |
| description      | string | Description of the TRC-10 token.            |
| url              | string | URL of the official website.                |
| new_limit        | int64  | Bandwidth limit for each individual caller. |
| new_public_limit | int64  | Total Bandwidth limit for all callers.      |

<br />
