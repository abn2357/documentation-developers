---
title: ClearAbi
excerpt: Remove or delete the ABI information associated with the smart contract.
api:
  file: full-node-http-api.json
  operationId: clearabi
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Note
>
> Even after executing the `ClearAbi` operation, the contract's ABI information is not fully deleted from the chain's historical record. Users can still retrieve the ABI by querying the original contract creation transaction.

**Returns**

Returned Object: Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`ClearABIContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

| Field            | Type   | Description                                           |
| :--------------- | :----- | :---------------------------------------------------- |
| owner_address    | string | Transaction initiator address.(Format: Base58 or Hex) |
| contract_address | string | Contract address. (Format: Base58 or Hex)             |