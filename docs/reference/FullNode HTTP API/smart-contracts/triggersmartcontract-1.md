---
title: '[more layouts]TriggerSmartContract'
excerpt: >-
  Returns a `TransactionExtention` object, which encapsulates the unsigned
  transaction data.
api:
  file: full-node-http-api.json
  operationId: post_wallettriggersmartcontract-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
**Note:**  
Reference examples for encoding and decoding [ABI](https://solidity.readthedocs.io/en/latest/abi-spec.html#examples) parameters: [Parameter and return value encoding and decoding](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding)

**Returns**

**Return Object:** Unsigned Transaction (JSON)

* **General:** See [Transaction Core](/docs/...) for base fields.
* **Specific :** The table below lists the parameters for **TriggerSmartContract** found in:
  `raw_data.contract[0].parameter.value`

Returned Object: Transaction (Unsigned).

General Fields: Refer to the [Transaction](/docs/tron-protocol-transaction) section.

`TriggerSmartContract` Specific Fields: The `raw_data.contract[0].parameter.value` within the transaction contains parameters for the contract invocation:

### Returns (opt2)

> **JSON Object:** Unsigned Transaction.
> For general field definitions, please refer to [Transaction Details](/link).

**Specific Parameters for `TriggerSmartContract`:**
The table below lists the fields found within `raw_data.contract[0].parameter.value`:

| Field | Type | Description |
| :---- | :--- | :---------- |
| ...   | ...  | ...         |

### Returns (opt3)

Returns an **Unsigned Transaction (JSON)**. For the general structure and base fields, please refer to the [Transaction Chapter](/link).

For `TriggerSmartContract` transactions, the parameters within the following path are described below:
`raw_data.contract[0].parameter.value`

| Field | Type | Description |
| :---- | :--- | :---------- |

### Returns(opt4)

**Unsigned Transaction (JSON)**
See [Transaction Docs](/link) for base fields.

**Fields for `raw_data.contract[0].parameter.value` (`TriggerSmartContract`):**

| Field            | Type   | Description                                                                                                                                     |
| :--------------- | :----- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| owner_address    | string | Transaction initiator address.                                                                                                                  |
| contract_address | string | Contract address.                                                                                                                               |
| call_value       | int64  | Amount of TRX transferred into the contract in this call. (Unit: sun)                                                                           |
| data             | string | Function call data, containing the function selector and encoded parameters, specifying which function to execute and how. (Format: hex string) |
| call_token_value | int64  | Amount of TRC-10 token transferred into the contract.                                                                                           |
| token_id         | int64  | TRC-10 token id transferred into the contract.                                                                                                  |

### Returns

Returns an **Unsigned Transaction (JSON)**. For general field definitions, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter.

<details open>
  <summary><strong>Specific Parameters: TriggerSmartContract</strong> (<code>raw\_data.contract\[0].parameter.value</code>)</summary>

  | Field              | Type   | Description                                                                                       |
  | :----------------- | :----- | :------------------------------------------------------------------------------------------------ |
  | `owner_address`    | string | Transaction initiator address.                                                                    |
  | `contract_address` | string | Contract address.                                                                                 |
  | `call_value`       | int64  | Amount of TRX transferred into the contract in this call. (Unit: sun)                             |
  | `data`             | string | Function call data, containing the function selector and encoded parameters. (Format: hex string) |
  | `call_token_value` | int64  | Amount of TRC-10 token transferred into the contract.                                             |
  | `token_id`         | int64  | TRC-10 token id transferred into the contract.                                                    |
</details>

<br />
