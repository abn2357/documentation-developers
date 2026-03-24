---
title: Get contract transaction info by account address
excerpt: >-
  Get the historical TRC20, TRC721 transfer records and authorization records of
  an account.
api:
  file: trongrid-v1-api.json
  operationId: get-trc20-transaction-info-by-account-address
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

| Field                       | Type    | Description                                                                    |
| :-------------------------- | :------ | :----------------------------------------------------------------------------- |
| data[i].transaction_id      | String  | Transaction hash.                                                              |
| data[i].token_info.symbol   | String  | TRC-20 token symbol.                                                           |
| data[i].token_info.address  | String  | TRC-20 contract address.                                                       |
| data[i].token_info.decimals | Integer | TRC-20 token decimals.                                                         |
| data[i].token_info.name     | String  | TRC-20 token name.                                                             |
| data[i].block_timestamp     | Long    | The block timestamp. (Unit: millisecond)                                       |
| data[i].from                | String  | The `from` address of the transaction.                                         |
| data[i].to                  | String  | The `to` address of the transaction.                                           |
| data[i].type                | String  | The name of the TRC-20 contract function called. (e.g., `transfer`, `approve`) |
| data[i].value               | String  | The amount of TRC-20 token transferred in the call. (Unit: sun)                |
| success                     | Boolean | Whether the request was successful.                                            |
| meta.at                     | Long    | The response timestamp. (Unit: millisecond)                                    |
| meta.page_size              | Integer | The number of items returned on the current page.                              |
| meta.fingerprint            | String  | The fingerprint for paginating to the next page.                               |
| meta.links.next             | String  | The URL for the next page of results.                                          |