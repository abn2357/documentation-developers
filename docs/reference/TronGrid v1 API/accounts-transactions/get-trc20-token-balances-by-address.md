---
title: Get TRC20 token balances by address
api:
  file: trongrid-v1-api.json
  operationId: get_v1-accounts-address-trc20-balance
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**

| Field            | Type    | Description                                                                        |
| :--------------- | :------ | :--------------------------------------------------------------------------------- |
| data             | Array   | An array of objects, each object representing a TRC-20 token address–balance pair. |
| success          | Boolean | Whether the request was successful.                                                |
| meta.at          | Long    | The response timestamp. (Unit: millisecond)                                        |
| meta.page_size   | Integer | The number of items returned on the current page.                                  |
| meta.fingerprint | String  | The fingerprint for paginating to the next page.                                   |
| meta.links.next  | String  | The URL for the next page of results.                                              |

<br />