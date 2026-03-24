---
title: ProposalDelete
excerpt: Deletes Proposal Transaction
api:
  file: full-node-http-api.json
  operationId: proposaldelete
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `ProposalDeleteContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                       |
| :------------ | :----- | :-------------------------------- |
| owner_address | string | Account address.                  |
| proposal_id   | int64  | Unique ID for the chain proposal. |