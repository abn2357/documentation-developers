---
title: CreateAssetIssue
excerpt: Issues a TRC-10 token. An account can only issue a TRC-10 token once.
api:
  file: full-node-http-api.json
  operationId: createassetissue
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

Transaction object - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `AssetIssueContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

| Field                       | Type           | Description                                                                                |
| :-------------------------- | :------------- | :----------------------------------------------------------------------------------------- |
| owner_address               | string         | Issuer address.                                                                            |
| name                        | string         | TRC-10 token name.                                                                         |
| abbr                        | string         | TRC-10 token symbol.                                                                       |
| total_supply                | int64          | Total supply.                                                                              |
| frozen_supply               | FrozenSupply[] | List of frozen token supply objects, specified by the issuer at token issuance.            |
| trx_num                     | int32          | Define the price by the ratio of `trx_num/num`. (Unit of `trx_num` is sun)                 |
| precision                   | int32          | Token precision, i.e. number of decimal places the token supports.                         |
| num                         | int32          | Define the price by the ratio of `trx_num/num`. (Unit of `trx_num` is sun)                 |
| start_time                  | int64          | ICO start time. (Unit: millisecond)                                                        |
| end_time                    | int64          | ICO end time. (Unit: millisecond)                                                          |
| description                 | string         | TRC-10 token description.                                                                  |
| url                         | string         | URL of the token's official website. (Default: Hex)                                        |
| free_asset_net_limit        | int64          | Account's free Bandwidth limit for TRC-10 token transfers.                                 |
| public_free_asset_net_limit | int64          | Total free Bandwidth limit for the TRC-10 token.                                           |
| public_free_asset_net_usage | int64          | Amount of free Bandwidth used for the TRC-10 token.                                        |
| public_latest_free_net_time | int64          | Timestamp of the last free Bandwidth consumption for the TRC-10 token. (Unit: millisecond) |