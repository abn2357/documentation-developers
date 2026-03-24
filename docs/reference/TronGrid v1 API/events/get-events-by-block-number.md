---
title: Get events by block number
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-events-by-block-number
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

| Field                              | Type                 | Description                                                                                                       |
| :--------------------------------- | :------------------- | :---------------------------------------------------------------------------------------------------------------- |
| data\[i].block\_number             | Integer              | The block number                                                                                                  |
| data\[i].block\_timestamp          | Long                 | The block timestamp. (Unit: millisecond).                                                                         |
| data\[i].caller\_contract\_address | String               | Same as `data.[0].contract_address` for backward compatibility.                                                   |
| data\[i].contract\_address         | String               | The address of the contract that emitted the event.                                                               |
| data\[i].event\_index              | String               | The event's index within the transaction's event log.                                                             |
| data\[i].event\_name               | String               | The event name                                                                                                    |
| data\[i].event                     | String               | The event signature used to parse indexed and non-indexed parameters. (e.g., `Transfer(address,address,uint256)`) |
| data\[i].transaction\_id           | String               | Transaction hash.                                                                                                 |
| data\[i].result                    | map\<string, string> | The event's parameters, including both indexed and non-indexed parameters.                                        |
| data\[i].result\_type              | map\<string, string> | The type of parameter                                                                                             |
| data\[i].\_unconfirmed             | Boolean              | Whether the transaction is unconfirmed. `true` means unconfirmed.                                                 |
| success                            | Boolean              | Whether the request was successful.                                                                               |
| meta.page\_size                    | Integer              | The number of items returned on the current page.                                                                 |
| meta.at                            | Long                 | The response timestamp. (Unit: millisecond).                                                                      |
| meta.fingerprint                   | String               | The fingerprint for paginating to the next page.                                                                  |
| meta.links.next                    | String               | The URL for the next page of results.                                                                             |