---
title: GetAccountResource
excerpt: Query the resource information of an account (bandwidth, energy, etc).
api:
  file: full-node-http-api.json
  operationId: getaccountresource
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

| Parameter            | Type                | Description                                                           |
| :------------------- | :------------------ | :-------------------------------------------------------------------- |
| freeNetUsed          | int64               | Amount of free Bandwidth used by the account.                         |
| freeNetLimit         | int64               | Total free Bandwidth limit for the account.                           |
| NetUsed              | int64               | Amount of staked Bandwidth used by the account.                       |
| NetLimit             | int64               | Total Bandwidth obtained by staking.                                  |
| TotalNetLimit        | int64               | Total Bandwidth can be obtained by staking by the entire network.     |
| TotalNetWeight       | int64               | Total amount of TRX staked for Bandwidth by the entire network.       |
| totalTronPowerWeight | int64               | Total TRON Power (votes) in the entire network.                       |
| tronPowerLimit       | int64               | Total TRON Power (votes) obtained by the account.                     |
| tronPowerUsed        | int64               | Amount of TRON Power (votes) used by the account.                     |
| EnergyUsed           | int64               | Account's Energy usage.                                               |
| EnergyLimit          | int64               | Total energy obtained by staking.                                     |
| TotalEnergyLimit     | int64               | Total Energy limit for the entire network.                            |
| TotalEnergyWeight    | int64               | Total amount of TRX staked for energy by the entire network.          |
| assetNetUsed         | map\<string, int64> | Account's free Bandwidth used for TRC-10 tokens, keyed by Token ID.   |
| assetNetLimit        | map\<string, int64> | Account's free Bandwidth limits for TRC-10 tokens, keyed by Token ID. |