---
title: CreateWitness
excerpt: Apply to become a super representative candidate
api:
  file: full-node-http-api.json
  operationId: createwitness
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `WitnessCreateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                                                        |
| :------------ | :----- | :----------------------------------------------------------------- |
| owner_address | string | Super Representative (SR) candidate address.                       |
| url           | string | URL of the Super Representative's (SR) candidate official website. |