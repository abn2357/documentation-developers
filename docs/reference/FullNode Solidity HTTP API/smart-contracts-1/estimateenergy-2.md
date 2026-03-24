---
title: EstimateEnergy
excerpt: >-
  Estimate the energy required for the successful execution of smart contract
  transactions.  (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: estimateenergy-2
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

* This API is closed by default. To enable this interface, both the `vm.estimateEnergy` and `vm.supportConstant `configuration items must be activated simultaneously in the node configuration file.
* `estimateEnergy` performs an estimation only; it does not generate an on-chain transaction or alter the current node's status. The `energy_required` field in its returned value represents the estimated energy amount, allowing the transaction's `fee_limit` to be set as `energy_required` X `energy unit price`.
* While the `triggerconstantcontract` API is sufficient for estimating the energy consumption of calling _most_ on-chain smart contracts (e.g., USDD, BTT, TUSD), the `estimateEnergy` API offers _greater accuracy_ when estimating the energy consumption for a small number of special contracts. Furthermore, the energy estimate returned by `estimateEnergy` is guaranteed to be sufficient for setting the transaction's `fee_limit`.
* Parameter encoding and decoding: [Parameter and return value encoding and decoding](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding)

**Returns**

| Field           | Type                | Description                                                               |
| :-------------- | :------------------ | :------------------------------------------------------------------------ |
| result          | Object              | Result of the contract execution simulation.                              |
| result.result   | bool                | Whether the estimation was successful.                                    |
| result.code     | response_code(enum) | Response code indicating the error type. (Returned only on failure)       |
| result.message  | string              | Response message describing the error details. (Returned only on failure) |
| energy_required | int64               | Estimated Energy required to execute the transaction.                     |