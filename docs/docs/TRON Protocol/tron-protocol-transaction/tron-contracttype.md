---
title: Supported Transaction Types in Detail
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
TRON supports various types of transactions that share a generally consistent structure (see the [Transaction](/docs/tron-protocol-transaction) section for details). However, the specific content within the `raw_data.contract` field varies depending on the transaction type. This article provides a detailed explanation of the structure and meaning of each field within `raw_data.contract` for different transaction types, helping developers construct and parse transaction data more efficiently.

## 1. AccountCreateContract

### Functionality Description

Creates a new basic TRON account, requiring a 1 TRX activation fee.

### Field Description

| Field Name        | Data Type | Description                                        |
| ----------------- | --------- | -------------------------------------------------- |
| `owner_address`   | bytes     | Address of the creator                             |
| `account_address` | bytes     | Newly generated address                            |
| `type`            | enum      | Account type (0 = Normal, 1 = Asset, 2 = Contract) |

***

## 2. TransferContract

### Functionality Description

Executes basic TRX transfer operations.

### Field Description

| Field Name      | Data Type | Description              |
| --------------- | --------- | ------------------------ |
| `owner_address` | bytes     | Sender's address         |
| `to_address`    | bytes     | Recipient's address      |
| `amount`        | int64     | Transfer amount (in SUN) |

***

## 3. TransferAssetContract

### Functionality Description

Executes TRC-10 token transfers.

### Field Description

| Field Name      | Data Type | Description                                             |
| --------------- | --------- | ------------------------------------------------------- |
| `asset_name`    | bytes     | Unique identifier of a token                            |
| `owner_address` | bytes     | Address of the token sender                             |
| `to_address`    | bytes     | Recipient's address (must be activated)                 |
| `amount`        | int64     | Transfer quantity (needs to be multiplied by precision) |

### Rules

1. Precision calculation formula: `Actual quantity = Amount / 10^precision`  
   (Precision is defined during token issuance)

***

## 4. VoteWitnessContract

### Functionality Description

Votes for Super Representatives (SRs).

### Field Description

| Field Name      | Data Type | Description                      |
| --------------- | --------- | -------------------------------- |
| `owner_address` | bytes     | Voter's address                  |
| `votes`         | Vote[]    | List of votes (maximum 30 items) |

### Voting Substructure

| Field Name     | Data Type | Description                             |
| -------------- | --------- | --------------------------------------- |
| `vote_address` | bytes     | SR's address                            |
| `vote_count`   | int64     | Number of votes (1 vote = 1 staked TRX) |

***

## 5. WitnessCreateContract

### Functionality Description

Registers to become an SR candidate.

### Field Description

| Field Name      | Data Type | Description                          |
| --------------- | --------- | ------------------------------------ |
| `owner_address` | bytes     | Applicant's address                  |
| `url`           | bytes     | Official website URL (UTF-8 encoded) |

***

## 6. WitnessUpdateContract

### Functionality Description

Updates the public information of an SR.

### Field Description

| Field Name      | Data Type | Description                             |
| --------------- | --------- | --------------------------------------- |
| `owner_address` | bytes     | SR's address                            |
| `update_url`    | bytes     | New official website URL (can be empty) |

***

## 7. AssetIssueContract

### Functionality Description

Creates and configures a TRC-10-standard token.

### Field Description

| Field Name      | Type           | Description                                               |
| --------------- | -------------- | --------------------------------------------------------- |
| `id`            | string         | Unique identifier of the token                            |
| `owner_address` | bytes          | Address of the token issuer                               |
| `name`          | bytes          | Full token name (UTF-8, maximum 32 bytes)                 |
| `abbr`          | bytes          | Token abbreviation (UTF-8, maximum 16 bytes)              |
| `total_supply`  | int64          | Total token supply (≥1)                                   |
| `frozen_supply` | FrozenSupply[] | List of token freeze plans                                |
| `trx_num`       | int32          | The amount of TRX required to exchange for 1 target token |
| `precision`     | int32          | Decimal precision (0-8)                                   |
| `num`           | int32          | Token issuance batch number                               |
| `start_time`    | int64          | Crowdsale start time (UNIX milliseconds)                  |
| `end_time`      | int64          | Crowdsale end time (UNIX milliseconds)                    |
| `order`         | int64          | Reserved field (currently no practical use)               |
| `vote_score`    | int32          | Voting weight coefficient                                 |
| `description`   | bytes          | Token description text (UTF-8)                            |
| `url`           | bytes          | Token official website URL (UTF-8)                        |

### FrozenSupply Structure

| Sub-field       | Type  | Description                      |
| --------------- | ----- | -------------------------------- |
| `frozen_amount` | int64 | Amount of frozen tokens          |
| `frozen_days`   | int64 | Number of frozen days (≥ 3 days) |

### Rules

1. **Issuance Requirements**
   * The total supply must satisfy: `total_supply ≥ 1`
   * The token name must be unique across the entire network.

***

## 8. ParticipateAssetIssueContract

### Functionality Description

Participates in TRC-10 token crowdsales.

### Field Description

| Field Name      | Data Type | Description                                           |
| --------------- | --------- | ----------------------------------------------------- |
| `owner_address` | bytes     | Participant's address                                 |
| `to_address`    | bytes     | Sending address                                       |
| `asset_name`    | bytes     | ID of the target token                                |
| `amount`        | int64     | TRX amount (in SUN) used to purchase the issued token |

### Rules

1. **Exchange Logic**:
   ```plaintext
   Token amount received = (Invested TRX amount × Token price denominator) / (Token price numerator × 10^Precision)
   ```
2. **Time Limit**:
   * Must be operated within the token crowdsale period `(start_time ≤ Current Time ≤ end_time)`.
3. **Failure Scenarios**:
   * Crowdsale quota is full.
   * Participant's TRX balance is insufficient.

## 9. AccountUpdateContract

### Functionality Description

Updates basic account information.

### Field Description

| Field Name      | Data Type | Description              |
| --------------- | --------- | ------------------------ |
| `owner_address` | bytes     | Operator's address       |
| `account_name`  | bytes     | New account name (UTF-8) |

***

## 10. FreezeBalanceContract

### Functionality Description

Stakes TRX to obtain Bandwidth/Energy resources. (Deprecated, please use `FreezeBalanceV2Contract`)

### Field Description

| Field Name         | Type  | Description                                                        |
| :----------------- | :---- | :----------------------------------------------------------------- |
| `owner_address`    | bytes | Address of the staking operator                                    |
| `frozen_balance`   | int64 | Amount of TRX to be staked (in SUN)                                |
| `frozen_duration`  | int64 | Number of staking days                                             |
| `resource`         | enum  | Resource type:<br />0=Bandwidth (BANDWIDTH)<br />1=Energy (ENERGY) |
| `receiver_address` | bytes | Resource receiving address (can be delegated to another address)   |

### Rules

* The receiving address must be activated.
* If no receiving address is specified, the resources will be sent to the `owner_address` by default.

***

## 11. UnfreezeBalanceContract

### Functionality Description

Unfreezes staked TRX in Stake1.0.

### Field Description

| Field Name         | Type  | Description                                                        |
| :----------------- | :---- | :----------------------------------------------------------------- |
| `owner_address`    | bytes | Address of the unstaking operator                                  |
| `resource`         | enum  | Resource type:<br />0=Bandwidth (BANDWIDTH)<br />1=Energy (ENERGY) |
| `receiver_address` | bytes | Original receiving address of those resources obtained by staking  |

***

## 12. WithdrawBalanceContract

### Functionality Description

Allows SRs to claim block rewards or users to claim voting rewards.  
Super Representatives can withdraw from their account balance; users can receive voting rewards from Super Representatives and deposit them into their account balance.

### Field Description

| Field Name      | Data Type | Description        |
| --------------- | --------- | ------------------ |
| `owner_address` | bytes     | SR or user address |

### Rules

1. **Reward Calculation**:
   * Block reward = Number of blocks produced × Current block reward
   * Voting reward = Number of votes received × Voting reward coefficient
2. **Claiming Limits**:
   * Minimum withdrawal amount: **1 TRX**
   * Limit of **1 withdrawal per 24 hours**

***

## 13. UnfreezeAssetContract

### Functionality Description

Unfreezes frozen TRC-10 token (requires issuer authorization).

### Field Description

| Field Name      | Data Type | Description        |
| --------------- | --------- | ------------------ |
| `owner_address` | bytes     | Operator's address |

***

## 14. UpdateAssetContract

### Functionality Description

Modifies basic parameters of an issued TRC-10 token.

### Field Description

| Field Name         | Type  | Description                                        |
| ------------------ | ----- | -------------------------------------------------- |
| `owner_address`    | bytes | Address of the token issuer                        |
| `description`      | bytes | New token description (UTF-8 encoded)              |
| `url`              | bytes | New token official website link (UTF-8 encoded)    |
| `new_limit`        | int64 | New limit on the number of token-holding addresses |
| `new_public_limit` | int64 | New public offering limit                          |

***

## 15. ProposalCreateContract

### Functionality Description

Creates a new proposal to modify network parameters.

### Field Description

| Field Name      | Data Type          | Description                                       |
| --------------- | ------------------ | ------------------------------------------------- |
| `owner_address` | bytes              | Address of the proposal creator                   |
| `parameters`    | map\<int64, int64> | List of parameter modifications (key-value pairs) |

### Rules

1. **Proposal Content**:
   * Modifiable parameters include: block reward, transaction fee rates, etc.
   * A single proposal can contain a maximum of **20** modifications.
2. **Effectiveness Conditions**:
   * Requires approval from **2/3 + 1** SRs.
   * Takes effect in the next maintenance cycle after approval.

***

## 16. ProposalApproveContract

### Functionality Description

SRs vote on proposals.

### Field Description

| Field Name       | Data Type | Description                       |
| ---------------- | --------- | --------------------------------- |
| `owner_address`  | bytes     | Address of the voting SR          |
| `proposal_id`    | int64     | ID of the target proposal         |
| `is_add_approve` | bool      | Add or remove approval (true=add) |

### Rules

1. **Voting Rights**:
   * Only active SRs in the current cycle can vote.
   * Each SR can vote on each proposal only **once**.
2. **Voting Validity**:
   * Proposals that do not reach the required number of votes within the time limit are automatically rejected.

***

## 17. ProposalDeleteContract

### Functionality Description

Deletes an existing network parameter modification proposal.

### Field Description

| Field Name      | Data Type | Description                               |
| --------------- | --------- | ----------------------------------------- |
| `owner_address` | bytes     | Address of the proposal deletion operator |
| `proposal_id`   | int64     | ID of the target proposal                 |

### Rules

1. **Deletion Rights**:
   * Only the proposal creator or the SR committee can delete a proposal.
   * Proposals that have already taken effect cannot be deleted.
2. **Time Limit**:
   * Proposals can only be deleted after **24 hours** from creation.

***

## 18. SetAccountIdContract

### Functionality Description

Sets a custom unique identifier (Account ID) for an account.

### Field Description

| Field Name      | Data Type | Description              |
| --------------- | --------- | ------------------------ |
| `owner_address` | bytes     | Account address          |
| `account_id`    | bytes     | Custom ID (ASCII string) |

***

## 19. CustomContract

### Functionality Description

Executes legacy custom contract logic (deprecated).

### Field Description

| Field Name      | Data Type | Description                             |
| --------------- | --------- | --------------------------------------- |
| `owner_address` | bytes     | Operator's address (must be an SR node) |
| `contract_data` | bytes     | Custom data (maximum 256 KB)            |

### Rules

1. **Compatibility Limits**
   * Only supports versions ≤ v4.1.2
   * New contracts must use `TriggerSmartContract`.

***

## 20. CreateSmartContract

### Functionality Description

Deploys a smart contract.

### Field Description

| Field Name         | Type          | Description                      |
| ------------------ | ------------- | -------------------------------- |
| `owner_address`    | bytes         | Address of the contract deployer |
| `new_contract`     | SmartContract | Smart contract                   |
| `call_token_value` | int64         | Initial funding amount (TRC-10)  |
| `token_id`         | int64         | TRC-10 token ID                  |

### SmartContract Structure

| Field Name                      | Type   | Required | Description                                                                 |
| ------------------------------- | ------ | -------- | --------------------------------------------------------------------------- |
| `origin_address`                | bytes  | Yes      | Address of the contract creator                                             |
| `contract_address`              | bytes  | Yes      | On-chain address of the contract                                            |
| `abi`                           | ABI    | Yes      | Contract interface definition (including metadata like methods and events)  |
| `bytecode`                      | bytes  | Yes      | EVM bytecode                                                                |
| `call_value`                    | int64  | No       | Amount of TRX transferred during invocation (in SUN, 1 TRX = 1,000,000 SUN) |
| `consume_user_resource_percent` | int64  | Yes      | Percentage of user resource consumption (range 0-100, default 100)          |
| `name`                          | string | Yes      | Contract name                                                               |
| `origin_energy_limit`           | int64  | Yes      | Energy pre-allocated by the creator (minimum: `1_000_000`)                  |
| `code_hash`                     | bytes  | Yes      | Hash of the bytecode                                                        |
| `trx_hash`                      | bytes  | Yes      | Deployment transaction hash                                                 |
| `version`                       | int32  | Yes      | Protocol version                                                            |

***

#### ABI Nested Structure

##### Entry Structure Fields

| Field Name        | Type                | Required | Description                                              |
| ----------------- | ------------------- | -------- | -------------------------------------------------------- |
| `anonymous`       | bool                | No       | Event anonymity identifier (only valid for `Event` type) |
| `constant`        | bool                | No       | ⚠️Deprecated (replaced by `stateMutability`)             |
| `name`            | string              | Yes      | Method/event name (empty for constructor)                |
| `inputs`          | repeated Param      | Yes      | List of input parameters (at least 1)                    |
| `outputs`         | repeated Param      | No       | Output parameters (only valid for `Function`)            |
| `type`            | EntryType           | Yes      | Entry type (see enum tables enum table below)            |
| `payable`         | bool                | No       | ⚠️Deprecated (replaced by `stateMutability`)             |
| `stateMutability` | StateMutabilityType | Yes      | State mutability (see enum tables table below)           |

***

#### Enumeration Type Tables

##### EntryType Enum

| Value | Enum Name        | Corresponding Scenario                 | Solidity Example                  |
| ----- | ---------------- | -------------------------------------- | --------------------------------- |
| 0     | UnknownEntryType | Unknown type (protocol reserved value) | -                                 |
| 1     | Constructor      | Contract constructor                   | `constructor() payable {}`        |
| 2     | Function         | Regular function                       | `function transfer() external {}` |
| 3     | Event            | On-chain event                         | `event Transfer(address indexed)` |
| 4     | Fallback         | Fallback function                      | `fallback() external {}`          |
| 5     | Receive          | Function for receiving TRX             | `receive() external payable {}`   |
| 6     | Error            | Custom error                           | `error InsufficientBalance();`    |

##### StateMutabilityType Enum

| Value | Enum Name             | State Impact                            | Modifier Example |
| ----- | --------------------- | --------------------------------------- | ---------------- |
| 0     | UnknownMutabilityType | Unknown state (protocol reserved value) | -                |
| 1     | Pure                  | Does not read or write state            | `pure`           |
| 2     | View                  | Read-only state                         | `view`           |
| 3     | Nonpayable            | Modifiable state (cannot receive TRX)   | No modifier      |
| 4     | Payable               | Modifies state (can receive TRX)        | `payable`        |

***

## 21. TriggerSmartContract

### Functionality Description

Interacts with a smart contract.

### Field Description

| Field Name         | Type  | Description                                                                                                                        |
| ------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `owner_address`    | bytes | Blockchain address of the caller                                                                                                   |
| `contract_address` | bytes | Address of the contract being called                                                                                               |
| `call_value`       | int64 | Amount of TRX transferred (in SUN, 1 TRX = 1,000,000 SUN)                                                                          |
| `data`             | bytes | ABI-encoded data (includes 4-byte function selector + 32-byte aligned parameter encoding)                                          |
| `call_token_value` | int64 | Amount of TRC-10 token transferred (needs to be multiplied by token precision, e.g., when the precision is 6, 1 token = 1,000,000) |
| `token_id`         | int64 | TRC-10 token ID                                                                                                                    |

***

## 22. GetContract

### Functionality Description

Queries detailed information about a smart contract.

### Parameter Parsing (BytesMessage)

#### Data Structure

```protobuf
message BytesMessage {
  bytes value = 1;
}
```

#### Input Requirements

| Field   | Format           |
| ------- | ---------------- |
| `value` | Contract address |

### Return Value Parsing (SmartContract)

#### Key Field Description

| Field              | Type           | Description                            |
| ------------------ | -------------- | -------------------------------------- |
| `origin_address`   | bytes          | Address of the contract creator        |
| `contract_address` | bytes          | On-chain address of the contract       |
| `abi.entrys`       | repeated Entry | List of contract interface definitions |
| `bytecode`         | bytes          | TVM bytecode                           |

***

## 23. UpdateSettingContract

### Functionality Description

Modifies the user resource consumption ratio of a smart contract (the resource allocation ratio between developers and users).

### Field Description

| Field Name                      | Type  | Description                                                                             |
| ------------------------------- | ----- | --------------------------------------------------------------------------------------- |
| `owner_address`                 | bytes | Address of the contract owner                                                           |
| `contract_address`              | bytes | Target contract address                                                                 |
| `consume_user_resource_percent` | int64 | Percentage of resource consumption borne by the user (valid range: 0-100, default: 100) |

***

## 24. UpdateEnergyLimitContract

### Functionality Description

Modifies the Energy consumption limit of a smart contract.

### Field Description

| Field Name            | Type  | Description              |
| --------------------- | ----- | ------------------------ |
| `owner_address`       | bytes | Contract owner's address |
| `contract_address`    | bytes | Target contract address  |
| `origin_energy_limit` | int64 | Energy limit value       |

***

## 25. AccountPermissionUpdateContract

### Functionality Description

Manages the multi-signature permission configuration of an account.

### Field Description

| Field Name      | Type         | Description                                     |
| --------------- | ------------ | ----------------------------------------------- |
| `owner_address` | bytes        | Account address                                 |
| `owner`         | Permission   | Owner permission configuration                  |
| `witness`       | Permission   | Witness permission configuration (can be empty) |
| `actives`       | Permission[] | Active permission configuration                 |

***

## 26. ClearABIContract

### Functionality Description

Clears the ABI definition of a smart contract.

### Field Description

| Field Name         | Type  | Description              |
| ------------------ | ----- | ------------------------ |
| `owner_address`    | bytes | Contract owner's address |
| `contract_address` | bytes | Target contract address  |

### Rules

**Impact of Clearing**

* External parties cannot parse contract methods via ABI.
* Deployed contracts can still be executed.

***

## 27. UpdateBrokerageContract

### Functionality Description

Adjusts the commission ratio for SRs.

### Field Description

| Field Name      | Type  | Description          |
| --------------- | ----- | -------------------- |
| `owner_address` | bytes | SR's address         |
| `brokerage`     | int32 | New commission ratio |

### Rules

1. **Ratio Range**
   * Minimum: **0%** (all distributed to voters)
   * Maximum: **100%** (no reward distribution)

***

## 28. DelegateResourceContract

### Functionality Description

Implements resource delegation operations (such as Bandwidth and Energy).

### Field Description

| Field Name         | Type         | Description                                                                      |
| ------------------ | ------------ | -------------------------------------------------------------------------------- |
| `owner_address`    | bytes        | Address of the resource owner                                                    |
| `resource`         | ResourceCode | Resource type (0 = Bandwidth, 1 = Energy)                                        |
| `balance`          | int64        | Amount of the resources to be delegated (in SUN, 1 TRX = 1,000,000 SUN)          |
| `receiver_address` | bytes        | Address of the resource recipient                                                |
| `lock`             | bool         | Whether to lock the delegation (true = locked, false = not locked)               |
| `lock_period`      | int64        | Lock period (in block numbers, 1 block ≈ 3 seconds, only valid when lock = true) |

***

## 29. UnDelegateResourceContract

### Functionality Description

Implements resource undelegation operations.

### Field Description

| Field Name         | Type         | Description                                                                                       |
| ------------------ | ------------ | ------------------------------------------------------------------------------------------------- |
| `owner_address`    | bytes        | Address of the resource owner (same as the delegation operation address)                          |
| `resource`         | ResourceCode | Resource type (must be consistent with the type at the time of delegation)                        |
| `balance`          | int64        | Amount of resources to be undelegated (in SUN, the amount must be ≤ the delegated amount)         |
| `receiver_address` | bytes        | Address of the resource recipient (must be consistent with the address at the time of delegation) |

***

## 30. FreezeBalanceV2Contract

### Functionality Description

Used to stake TRX to obtain Bandwidth or Energy resources in Stake 2.0 of the TRON network (the original 1.0 staking method has been deprecated).

### Field Description

| Field Name       | Type         | Description                                                |
| ---------------- | ------------ | ---------------------------------------------------------- |
| `owner_address`  | bytes        | Address of the staking operation initiator                 |
| `frozen_balance` | int64        | Amount of TRX to be staked (in SUN, 1 TRX = 1,000,000 SUN) |
| `resource`       | ResourceCode | Target resource type (0 = Bandwidth, 1 = Energy)           |

### Additional Notes

1. **Resource Acquisition Rules**
   * The amount of resources obtainable per 1 TRX staked is dynamically calculated by the entire network.
   * Staking operations take effect immediately, and resources can be used instantly.

2. **Unstaking Mechanism**
   * Unstaking needs to be done via `UnfreezeBalanceV2Contract`.

3. **Resource Type Mapping**

   | ResourceCode Value | Resource Type | Usage Scenario                           |
   | ------------------ | ------------- | ---------------------------------------- |
   | `0`                | Bandwidth     | Consumption for all transactions         |
   | `1`                | Energy        | Consumption for smart contract execution |

***

## 31. UnfreezeBalanceV2Contract

### Functionality Description

Used to unfreeze staked TRX and return the Bandwidth/Energy resources (used in conjunction with `FreezeBalanceV2Contract`).

### Field Description

| Field Name         | Type         | Description                                                                   |
| ------------------ | ------------ | ----------------------------------------------------------------------------- |
| `owner_address`    | bytes        | Address of the unstaking operation initiator                                  |
| `unfreeze_balance` | int64        | Amount of TRX to be unstaked (in SUN, the amount must be ≤ the staked amount) |
| `resource`         | ResourceCode | Target resource type (0 = Bandwidth, 1 = Energy, 2 = Vote Power)              |

***

### Core Rules

1. **Unstaking Delay Mechanism**
   * After initiating unstaking, it takes **14 days** (on-chain time) before TRX can be withdrawn.

***

## 32. WithdrawExpireUnfreezeContract

### Functionality Description

Used to withdraw TRX funds that have **passed the unstaking waiting period** (must be executed after initiating `UnfreezeBalanceV2Contract`).

### Field Description

| Field Name      | Type  | Description                                   |
| --------------- | ----- | --------------------------------------------- |
| `owner_address` | bytes | Address of the withdrawal operation initiator |

***

## 33. CancelAllUnfreezeV2Contract

### Functionality Description

Used to **cancel all uncompleted unstaking operations** (revokes initiated unstaking requests within the unstaking waiting period).

### Field Description

| Field Name      | Type  | Description                        |
| --------------- | ----- | ---------------------------------- |
| `owner_address` | bytes | Address of the operation initiator |

### Core Mechanism

1. **Operation Impact**
   * Revokes all unstaking requests initiated via `UnfreezeBalanceV2Contract` that have not yet passed the 14-day waiting period (the unstaking waiting period for Stake 2.0 is 14 days, while it was 3 days for 1.0).
   * Restores the staking status of the corresponding TRX and maintains the original resource (Bandwidth/Energy) quota.

2. **Restrictions**
   * Only effective for **unexpired** unstaking records (unstaking that has passed the 14-day waiting period cannot be cancelled).
   * The operation is irreversible; after cancellation, the unstaking process can only be initiated again.
