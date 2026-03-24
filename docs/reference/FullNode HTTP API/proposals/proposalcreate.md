---
title: ProposalCreate
excerpt: Creates a proposal transaction
api:
  file: full-node-http-api.json
  operationId: proposalcreate
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `ProposalCreateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type               | Description                                                      |
| :------------ | :----------------- | :--------------------------------------------------------------- |
| owner_address | string             | Account address                                                  |
| parameters    | map\<int64, int64> | Proposed new values for chain parameters, keyed by parameter ID. |