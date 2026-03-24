---
title: '[Annotated json]Get account info by address'
api:
  file: trongrid-v1-api.json
  operationId: get_v1accounts{address}-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**

```json
{
  "success": true, // Indicates if the API request was processed successfully.
  "meta": {
    "at": 1734567890123, // Response timestamp in milliseconds.
    "page_size": 1 // Number of items returned in this response.
  },
  "data": {
    "address": "41A61456...", // Account address in Hex format.
    "balance": 1000000, // TRX balance in SUN (1 TRX = 1,000,000 SUN).
    "create_time": 1541719693000, // Account activation timestamp.
    
    /* --- Resource Usage (Dynamic) --- */
    "net_usage": 0, // Currently consumed Bandwidth from staking.
    "free_net_usage": 0, // Currently consumed Free Bandwidth.
    "account_resource": {
      "energy_usage": 500, // Current Energy consumption.
      "energy_window_size": 28800, // Blocks for Energy recovery (3-decimal precision if optimized).
      "latest_consume_time_for_energy": 1698745200000 // Last energy usage timestamp.
    },

    /* --- Stake 2.0 (New Model) --- */
    "frozenV2": [
      {
        "type": "ENERGY", // Resource type: BANDWIDTH or ENERGY.
        "amount": 5000000 // TRX staked for this resource in Stake 2.0 (in sun).
      }
    ],
    "delegated_frozenV2_balance_for_bandwidth": 0, // Bandwidth delegated to others (Stake 2.0).
    "acquired_delegated_frozenV2_balance_for_bandwidth": 2000000, // Bandwidth received from others (Stake 2.0).

    /* --- Permissions (Multi-Sig) --- */
    "owner_permission": {
      "permission_name": "owner", // Name of the owner permission.
      "threshold": 1, // Required weight sum to authorize an action.
      "keys": [
        {
          "address": "41A61456...", // Authorized signer address.
          "weight": 1 // Signature weight of this specific address.
        }
      ]
    },

    /* --- Assets --- */
    "assetV2": [
      {
        "key": "1002000", // TRC-10 Token ID.
        "value": 500 // Token balance.
      }
    ],
    "votes": [
      {
        "vote_address": "41E552...", // Address of the Super Representative.
        "vote_count": 100 // Number of votes cast.
      }
    ]
  }
}
```