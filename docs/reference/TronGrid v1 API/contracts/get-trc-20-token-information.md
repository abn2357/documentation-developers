---
title: Get smart contract token information
excerpt: Supports retrieving information for TRC-20, TRC-721, and TRC-1155 tokens.
api:
  file: trongrid-v1-api.json
  operationId: get_v1-trc20-info
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**

| Field                    | Type    | Description                                       |
| :----------------------- | :------ | :------------------------------------------------ |
| data[i].contract_address | String  | Contract address.                                 |
| data[i].symbol           | String  | Token symbol.                                     |
| data[i].name             | String  | Token name                                        |
| data[i].decimals         | String  | Token decimals.                                   |
| data[i].type             | String  | Token type.                                       |
| data[i].total_supply     | String  | Token total supply.                               |
| success                  | Boolean | Whether the request was successful.               |
| meta.at                  | Long    | The response timestamp. (Unit: millisecond)       |
| meta.page_size           | Integer | The number of items returned on the current page. |
| meta.fingerprint         | String  | The fingerprint for paginating to the next page.  |
| meta.links.next          | String  | The URL for the next page of results.             |