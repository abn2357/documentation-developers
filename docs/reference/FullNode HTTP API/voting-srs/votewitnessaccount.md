---
title: VoteWitnessAccount
excerpt: Vote for super representatives
api:
  file: full-node-http-api.json
  operationId: votewitnessaccount
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `VoteWitnessContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                                                                                             |
| :------------ | :----- | :------------------------------------------------------------------------------------------------------ |
| owner_address | string | Account address                                                                                         |
| votes         | Vote[] | List of `Vote` objects, each containing `vote_address` (SR address) and `vote_count` (number of votes). |