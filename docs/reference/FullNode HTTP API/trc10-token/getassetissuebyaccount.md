---
title: GetAssetIssueByAccount
excerpt: Query the TRC10 token information issued by an account.
api:
  file: full-node-http-api.json
  operationId: getassetissuebyaccount
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

assetIssue - AssetIssueContract[], a list of issued TRC10 token object, which contains the following fields:

| Field                       | Type           | Description                                                                                        |
| :-------------------------- | :------------- | :------------------------------------------------------------------------------------------------- |
| id                          | string         | The TRC-10 Token ID.                                                                               |
| owner_address               | string         | Token issuer address.                                                                              |
| name                        | string         | Token name.                                                                                        |
| abbr                        | string         | The TRC-10 Token Symbol.                                                                           |
| total_supply                | int64          | Total supply.                                                                                      |
| frozen_supply               | FrozenSupply[] | The number of tokens and days to be frozen specified by the issuer of the token when it is issued. |
| trx_num                     | int32          | Define the price by the ratio of trx_num/num. (The unit of 'trx_num' is SUN)                       |
| precision                   | int32          | Token precision, i.e. the number of decimal places the token supports.                             |
| num                         | int32          | Define the price by the ratio of trx_num/num. (The unit of 'trx_num' is sun)                       |
| start_time                  | int64          | ICO start time. (Unit: millisecond)                                                                |
| end_time                    | int64          | ICO end time. (Unit: millisecond)                                                                  |
| vote_score                  | int32          | The vote score of the TRC-10 token.                                                                |
| description                 | string         | Token description.                                                                                 |
| url                         | string         | The URL of the token's official website.                                                           |
| free_asset_net_limit        | int64          | The total number of token free bandwidth limit.                                                    |
| public_free_asset_net_limit | int64          | The total number of token free bandwidth limit for an account.                                     |
| public_free_asset_net_usage | int64          | The total number of token free bandwidth used by all token owner.                                  |
| public_latest_free_net_time | int64          | The timestamp of the last consumption of this token's free bandwidth.                              |