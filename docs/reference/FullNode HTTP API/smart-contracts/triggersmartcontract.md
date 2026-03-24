---
title: TriggerSmartContract
excerpt: >-
  Returns a `TransactionExtention` object, which encapsulates the unsigned
  transaction data.
api:
  file: full-node-http-api.json
  operationId: triggersmartcontract
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
Reference examples for encoding and decoding [ABI](https://solidity.readthedocs.io/en/latest/abi-spec.html#examples) parameters: [Parameter and return value encoding and decoding](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding)

**Returns**

Returned Object: Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`TriggerSmartContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

| Field            | Type   | Description                                                                                                                                     |
| :--------------- | :----- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| owner_address    | string | Transaction initiator address.                                                                                                                  |
| contract_address | string | Contract address.                                                                                                                               |
| call_value       | int64  | Amount of TRX transferred into the contract in this call. (Unit: sun)                                                                           |
| data             | string | Function call data, containing the function selector and encoded parameters, specifying which function to execute and how. (Format: hex string) |
| call_token_value | int64  | Amount of TRC-10 token transferred into the contract.                                                                                           |
| token_id         | int64  | TRC-10 token id transferred into the contract.                                                                                                  |