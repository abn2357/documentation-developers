---
title: Get internal transactions by contract address
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-internal-transactions-by-contract-address
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
| data\[i].internal\_tx\_id | String  | The unique identifier (ID) for the internal transaction.                                                                                                     |
| data\[i].data.note        | String  | The type of instruction, such as `call`, `create`, `suicide`, `freezeBalanceV2ForEnergy`, `freezeBalanceV2ForBandwidth`, or `unfreezeBalanceV2ForBandwidth`. |
| data\[i].data.rejected    | Boolean | Whether the internal transaction failed during execution. `true` means the execution failed.                                                                 |
| data\[i].block\_timestamp | Long    | The Unix timestamp for when the transaction was confirmed. (Unit: millisecond)                                                                               |
| data\[i].to\_address      | String  | The recipient's address.                                                                                                                                     |
| data\[i].tx\_id           | String  | The unique identifier (ID) of the parent transaction that initiated this internal transaction.                                                               |
| data\[i].from\_address    | tring   | The sender's address.                                                                                                                                        |
| success                   | Boolean | Whether the request was successful.                                                                                                                          |
| meta.at                   | Long    | The timestamp for when the API response was generated. (Unit: millisecond)                                                                                   |
| meta.page\_size           | Integer | The number of items returned on the current page.                                                                                                            |
| meta.fingerprint          | String  | A fingerprint of the last transaction on this page, used to fetch the next page of results.                                                                  |
| meta.links.next           | String  | The complete URL to request the next page of results. `null` if this is the last page.                                                                       |