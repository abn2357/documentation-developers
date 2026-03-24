---
title: UnfreezeAsset
excerpt: Unstakes a token that has passed the minimum freeze duration.
api:
  file: full-node-http-api.json
  operationId: unfreezeasset
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

For the `UnfreezeAssetContract` type, the fields within `raw_data.contract[0].parameter.value` are listed as follows:

| Field         | Type   | Description      |
| :------------ | :----- | :--------------- |
| owner_address | string | Account address. |

<br />
