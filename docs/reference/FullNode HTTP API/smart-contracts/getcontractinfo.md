---
title: GetContractInfo
excerpt: >-
  Queries and returns the complete information of a contract from the
  blockchain. Unlike the `wallet/getcontract` interface, this endpoint returns
  both the contract's bytecode and its runtime bytecode.
api:
  file: full-node-http-api.json
  operationId: getcontractinfo
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

| Field                        | Type          | Description                                                                                                             |
| :--------------------------- | :------------ | :---------------------------------------------------------------------------------------------------------------------- |
| runtimecode                  | string        | Runtime bytecode of the contract.                                                                                       |
| smart_contract               | SmartContract | Smart contract object. See [GetContract](https://developers.tron.network/reference/wallet-getcontract) for fields.      |
| contract_state               | ContractState | State of the contract. See [Dynamic Energy Model](https://developers.tron.network/docs/resource-model#api) for details. |
| contract_state.energy_usage  | int64         | Total basic energy usage of the contract in the current maintenance cycle.                                              |
| contract_state.energy_factor | int64         | Energy factor of the contract.                                                                                          |
| contract_state.update_cycle  | int64         | Current maintenance cycle number.                                                                                       |