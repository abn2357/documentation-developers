---
title: UpdateEnergyLimit
excerpt: Update the smart contract's `origin_energy_limit` parameter.
api:
  file: full-node-http-api.json
  operationId: wallet-updateenergylimit
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Origin Energy Limit
>
> Starting with the Java-Tron **Odyssey 3.2 release**, this parameter is mandatory for deploying new contracts, and the value **must be greater than 0**. For contracts already deployed on the Mainnet before Odyssey 3.2, the value is stored as 0 but is functionally treated as the maximum allowed value, which is 10,000,000.

**Returns**

Returned Object:  Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`UpdateEnergyLimitContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

| Field               | Type   | Description                                                                |
| :------------------ | :----- | :------------------------------------------------------------------------- |
| owner_address       | string | Transaction initiator address.(Format: Base58 or Hex)                      |
| contract_address    | string | Contract address. (Format: Base58 or Hex)                                  |
| origin_energy_limit | int    | Adjusted maximum energy provided by the contract deployer per transaction. |

<br />