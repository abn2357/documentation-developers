---
title: Get transaction info by account address
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-transaction-info-by-account-address
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

| Field                         | Type        | Description                                                                                                                                      |
| :---------------------------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| data[i].txID                  | String      | Transaction ID (Hash).                                                                                                                           |
| data[i].blockNumber           | Integer     | The block number.                                                                                                                                |
| data[i].block_timestamp       | Long        | The block timestamp. (Unit: millisecond)                                                                                                         |
| data[i].ret.contractRet       | string[]    | Transaction execution results.                                                                                                                   |
| data[i].ret.fee               | Long        | Transaction fee. (Unit: sun)                                                                                                                     |
| data[i].signature             | string[]    | Transaction signature.                                                                                                                           |
| data[i].raw_data_hex          | string      | The transaction's raw data. (Format: hex)                                                                                                        |
| data[i].raw_data              | Transaction | Transaction content. See [here](https://developers.tron.network/docs/tron-protocol-transaction) for details.                                     |
| data[i].energy_fee            | Long        | The amount of TRX burned for Energy. (Unit: sun)                                                                                                 |
| data[i].energy_usage          | Long        | The amount of Energy consumed by the sender's account.                                                                                           |
| data[i].energy_usage_total    | Long        | The total amount of Energy consumed by the transaction.                                                                                          |
| data[i].net_fee               | Long        | The amount of TRX burned to pay for the Bandwidth.                                                                                               |
| data[i].net_usage             | Long        | The amount of Bandwidth consumed.                                                                                                                |
| data[i].internal_transactions | string[]    | An array of internal transactions. See [here](https://developers.tron.network/docs/tron-protocol-transaction#internal-transactions) for details. |
| success                       | Boolean     | Whether the request was successful.                                                                                                              |
| meta.at                       | Long        | The response timestamp. (Unit: millisecond)                                                                                                      |
| meta.page_size                | Integer     | The number of items returned on the current page.                                                                                                |
| meta.fingerprint              | String      | The fingerprint for paginating to the next page.                                                                                                 |
| meta.links.next               | String      | The URL for the next page of results.                                                                                                            |