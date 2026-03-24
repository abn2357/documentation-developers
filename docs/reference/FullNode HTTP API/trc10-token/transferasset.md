---
title: TransferAsset
excerpt: Transfers TRC-10 token.
api:
  file: full-node-http-api.json
  operationId: transferasset
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

**A `Transaction` object - JSON object: Unsigned transaction. **

For general field definitions, please refer to [Transaction](/docs/tron-protocol-transaction). 

For the `TransferAssetContract` type, the fields within `raw_data.contract[0].parameter.value` are listed below:

| Field         | Type   | Description                         |
| :------------ | :----- | :---------------------------------- |
| owner_address | string | Account address.                    |
| asset_name    | string | TRC-10 Token ID to transfer.        |
| to_address    | string | Recipient address.                  |
| amount        | int64  | Amount of TRC-10 token to transfer. |

<br />