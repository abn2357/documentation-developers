---
title: GetContract
excerpt: >-
  Fetches comprehensive information for a specified smart contract deployed on
  the blockchain. The returned details include the contract's bytecode,
  Application Binary Interface (ABI), and configuration parameters.
api:
  file: full-node-http-api.json
  operationId: wallet-getcontract
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

For a detailed explanation of the fields, please refer to [Contract Deployment and Invocation](/docs/smart-contract-deployment-and-invocation).

| Field                         | Type   | Description                                                                                                    |
| :---------------------------- | :----- | :------------------------------------------------------------------------------------------------------------- |
| origin_address                | string | Address of the contract creator.                                                                               |
| contract_address              | string | Address of the contract.                                                                                       |
| abi                           | ABI    | Smart contract ABI.                                                                                            |
| bytecode                      | string | Bytecode of the smart contract.                                                                                |
| call_value                    | int64  | Amount of TRX transferred into the contract at deployment. (Unit: sun)                                         |
| consume_user_resource_percent | int64  | Percentage of user Energy consumption for a smart contract. (Range: [0-100])                                   |
| name                          | string | Contract name.                                                                                                 |
| origin_energy_limit           | int64  | Maximum energy from the contract deployer's stake that a single transaction is allowed to consume. (Unit: sun) |
| code_hash                     | string | Hash of the contract's bytecode.                                                                               |