---
title: ParticipateAssetIssue
excerpt: Participate in an asset issue.
api:
  file: full-node-http-api.json
  operationId: participateassetissue
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

Transaction object - JSON object: Unsigned transaction.

For general field definitions, please refer to [Transaction](/docs/tron-protocol-transaction).

For the  type `ParticipateAssetIssueContract`, the fields within`raw_data.contract[0].parameter.value` are listed follows:

| Field         | Type   | Description                                           |
| :------------ | :----- | :---------------------------------------------------- |
| owner_address | string | Account address.                                      |
| to_address    | string | Issuer's address.                                     |
| asset_name    | string | Token ID.                                             |
| amount        | int64  | Amount of TRX used to purchase the token. (Unit: sun) |