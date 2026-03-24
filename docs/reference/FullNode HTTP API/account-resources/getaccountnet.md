---
title: GetAccountNet
excerpt: Query bandwidth information of an account.
api:
  file: full-node-http-api.json
  operationId: getaccountnet
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

| Field          | Type                | Description                                                           |
| :------------- | :------------------ | :-------------------------------------------------------------------- |
| freeNetUsed    | int64               | Amount of free Bandwidth used by the account.                         |
| freeNetLimit   | int64               | Total free Bandwidth limit for the account.                           |
| NetUsed        | int64               | Amount of staked Bandwidth used by the account.                       |
| NetLimit       | int64               | Total Bandwidth obtained by staking.                                  |
| TotalNetLimit  | int64               | Total Bandwidth can be obtained by staking by the entire network.     |
| TotalNetWeight | int64               | Total amount of TRX staked for Bandwidth by the entire network.       |
| assetNetUsed   | map\<string, int64> | Account's free Bandwidth used for TRC-10 tokens, keyed by Token ID.   |
| assetNetLimit  | map\<string, int64> | Account's free Bandwidth limits for TRC-10 tokens, keyed by Token ID. |