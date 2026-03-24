---
title: UpdateWitness
excerpt: Edit the URL of the SR's official website
api:
  file: full-node-http-api.json
  operationId: updatewitness
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `WitnessUpdateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field         | Type   | Description                        |
| :------------ | :----- | :--------------------------------- |
| owner_address | string | Super Representative (SR) address. |
| update_url    | string | SR‘s Updated URL.                  |

<br />