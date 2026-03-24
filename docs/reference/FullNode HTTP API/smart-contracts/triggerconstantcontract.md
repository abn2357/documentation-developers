---
title: TriggerConstantContract
excerpt: >-
  This interface is used for pre-execution (or simulation) of smart contracts on
  the blockchain: it can call a contract's read-only functions for data queries,
  call non-read-only functions to predict transaction success or estimate
  required Energy consumption
api:
  file: full-node-http-api.json
  operationId: triggerconstantcontract
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Note:**

* TriggerConstantContract operation will not generate an on-chain transaction, nor will it change the status of the current node.

**Returns**

| Field           | Type        | Description                                                                                                                      |
| :-------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------- |
| result          | Return      | Run result, for detailed parameter definition, refer to [EstimateEnergy](/reference/estimateenergy)                              |
| energy_used     | int64       | Total energy consumption, including basic and penalty energy consumption.                                                        |
| energy_penalty  | int64       | Penalty Energy consumption.                                                                                                      |
| constant_result | string[]    | List of results from a constant contract call.                                                                                   |
| transaction     | Transaction | Transaction object, see [GetTransactionByID](https://developers.tron.network/reference/wallet-gettransactionbyid) for structure. |

Conclusion:

* The  energy consumption: `energy_used`
* The penalty energy consumption: `energy_penalty`
* The basic energy consumption:  `energy_used` - `energy_penalty`