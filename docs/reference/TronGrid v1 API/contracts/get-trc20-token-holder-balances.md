---
title: Get TRC-20 token holder balances
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-trc20-token-holder-balances
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

| Field            | Type    | Description                                                                                 |
| :--------------- | :------ | :------------------------------------------------------------------------------------------ |
| data\[]          | Array   | The banlance of the TRC20 holder.                                                           |
| success          | Boolean | Whether the request was successful.                                                         |
| meta.at          | Long    | The timestamp for when the API response was generated. (Unit: millisecond)                  |
| meta.page\_size  | Integer | The number of items returned on the current page.                                           |
| meta.fingerprint | String  | A fingerprint of the last transaction on this page, used to fetch the next page of results. |
| meta.links.next  | String  | The complete URL to request the next page of results. `null` if this is the last page.      |