---
title: Get internal transactions by address
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-internal-transactions-by-address
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

| Field                     | Type    | Description                                                                                                                                                  |
| :------------------------ | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data[i].internal_tx_id`  | String  | The unique ID for the internal transaction.                                                                                                                  |
| `data[i].data.note`       | String  | The type of instruction, such as `call`, `create`, `suicide`, `freezeBalanceV2ForEnergy`, `freezeBalanceV2ForBandwidth`, or `unfreezeBalanceV2ForBandwidth`. |
| `data[i].data.rejected`   | Boolean | Whether the internal transaction failed during execution. `true` signifies failure.                                                                          |
| `data[i].block_timestamp` | Long    | The block timestamp. (Unit: millisecond)                                                                                                                     |
| `data[i].to_address`      | String  | The recipient's address.                                                                                                                                     |
| `data[i].tx_id`           | String  | The transaction hash of the parent transaction that initiated this internal transaction.                                                                     |
| `data[i].from_address`    | tring   | The sender's address.                                                                                                                                        |
| `success`                 | Boolean | Whether the API request was successful.                                                                                                                      |
| `meta.at`                 | Long    | The API response timestamp. (Unit: millisecond)                                                                                                              |
| `meta.page_size`          | Integer | The number of items returned on the current page..                                                                                                           |
| `meta.fingerprint`        | String  | The fingerprint for paginating to the next page.                                                                                                             |
| `meta.links.next`         | String  | The URL for the next page of results.                                                                                                                        |