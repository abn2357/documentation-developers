---
title: Get assets by name
excerpt: 'NOTE: Multiple assets may have the same name.'
api:
  file: trongrid-v1-api.json
  operationId: get-asset-by-name
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

| Field                   | Type    | Description                                                                    |
| :---------------------- | :------ | :----------------------------------------------------------------------------- |
| data\[i].id             | Long    | The TRC-10 Token ID.                                                           |
| data\[i].abbr           | String  | The TRC-10 Token Symbol.                                                       |
| data\[i].description    | String  | Token description.                                                             |
| data\[i].name           | String  | Token name.                                                                    |
| data\[i].num            | Integer | Define the price by the ratio of trx\_num/num. (The unit of 'trx\_num' is sun) |
| data\[i].precision      | Long    | Token precision, i.e. the number of decimal places the token supports.         |
| data\[i].url            | String  | The URL of the token's official website.                                       |
| data\[i].total\_supply  | String  | Total supply.                                                                  |
| data\[i].trx\_num       | String  | Define the price by the ratio of trx\_num/num. (The unit of 'trx\_num' is SUN) |
| data\[i].vote\_score    | Integer | The vote score of the TRC-10 token.                                            |
| data\[i].owner\_address | String  | Token issuer address.                                                          |
| data\[i].start\_time    | Long    | ICO start time. (Unit: millisecond)                                            |
| data\[i].end\_time      | Long    | ICO end time. (Unit: millisecond)                                              |
| success                 | Boolean | Whether the request was successful.                                            |
| meta.at                 | Long    | The response timestamp. (Unit: millisecond)                                    |
| meta.page\_size         | Integer | The number of items returned on the current page.                              |
| meta.fingerprint        | String  | The fingerprint for paginating to the next page.                               |
| meta.links.next         | String  | The URL for the next page of results.                                          |