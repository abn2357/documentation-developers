---
title: Get events by contract address
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-events-by-contract-address
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<br />

**Returns**

| Field                           | Type                 | Description                                                                                                       |
| :------------------------------ | :------------------- | :---------------------------------------------------------------------------------------------------------------- |
| data[i].block_number            | Integer              | The block number                                                                                                  |
| data[i].block_timestamp         | Long                 | The block timestamp. (Unit: millisecond)                                                                          |
| data[i].caller_contract_address | String               | Same as data.[0].contract_address for backward compatibility.                                                     |
| data[i].contract_address        | String               | The address of the contract that emitted the event.                                                               |
| data[i].event_index             | String               | The event's index within the transaction's event log.                                                             |
| data[i].event_name              | String               | The event name                                                                                                    |
| data[i].event                   | String               | The event signature used to parse indexed and non-indexed parameters. (e.g., `Transfer(address,address,uint256)`) |
| data[i].transaction_id          | String               | Transaction hash.                                                                                                 |
| data[i].result                  | map\<string, string> | The event's parameters, including both indexed and non-indexed parameters.                                        |
| data[i].result_type             | map\<string, string> | The type of parameter                                                                                             |
| data[i]._unconfirmed            | Boolean              | Whether the transaction is unconfirmed. `true` means unconfirmed.                                                 |
| success                         | Boolean              | Whether the request was successful.                                                                               |
| meta.page_size                  | Integer              | The number of items returned on the current page.                                                                 |
| meta.at                         | Long                 | The response timestamp. (Unit: millisecond)                                                                       |