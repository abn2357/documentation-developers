---
title: TRON Virtual Machine (TVM)
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
TRON Virtual Machine (TVM) is the runtime environment for TRON smart contracts, and each node in the network maintains a TVM entity. The TRON protocol keeps the continuous, uninterrupted, and immutable operation of this state machine. At any given block in the chain, TRON has one and only one 'canonical' state, and the TVM is what defines the rules for computing a new valid state from block to block.

# From Ledger to State Machine

The analogy of a 'distributed ledger' is often used to describe blockchains like Bitcoin, which enables a decentralized currency using fundamental tools of cryptography. A cryptocurrency behaves like a 'normal' currency by adhering to the rules that govern what can and cannot be done to modify the ledger. For example, a Bitcoin address cannot spend more Bitcoin than it has previously received. These rules underpin all transactions on Bitcoin.

While TRON has its own native cryptocurrency TRX that follows almost exactly the same intuitive rules, it also enables a much more powerful functionality: smart contracts. With this more complex feature, instead of a simple distributed ledger, TRON is actually a distributed state machine. TRON's state is a large data structure which holds not only all accounts information, but also a machine state, which can change from block to block according to a pre-defined set of rules, and can execute arbitrary machine code.

# State Transition Function

The TVM behaves like a mathematical function: Given an input, it produces a deterministic output. It therefore is quite helpful to more formally describe TRON as having a state transition function:

```
Y(S, T) = S'
```

Given an old valid state (S) and a new set of valid transactions (T), the TRON state transition function Y(S, T) produces a new valid output state S'.

## State

In the TRON network, the state is an enormous data structure called Merkle Trie, which keeps all accounts linked by hashes and reducible to a single root hash stored on the blockchain.

## Transactions

Transactions are cryptographically signed instructions from accounts. They are divided into two categories, system contract transactions and smart contract transactions, in which smart contract transactions include those  resulting in contract message calls and contract creation.

Contract creation generates a new contract account containing compiled smart contract bytecode. Whenever another account makes a message call to that contract, it executes the corresponding bytecode on the TVM.

# TVM Instructions

The TVM executes as a stack machine with a depth of 1024 items. Each item is a 256-bit word, which was chosen for the ease of use with 256-bit cryptography (such as Keccak-256 hashes or secp256k1 signatures).

Compiled smart contract bytecode executes as a number of TVM opcodes, which perform standard stack operations like XOR, AND, ADD, and SUB. The TVM also implements a number of blockchain-specific stack operations, such as ADDRESS, BALANCE, and BLOCKHASH. For more opcodes, please refer to [TRON opcodes](https://github.com/tronprotocol/java-tron/blob/develop/actuator/src/main/java/org/tron/core/vm/Op.java)

The below flowchart shows how TVM works:  
![](https://i.imgur.com/zuLOAtU.png)  
The flow involves the following steps：

* The compiler compiles the smart contract into bytecode, which is readable and executable on the TVM.
* The TVM processes data according to the opcode.
* The TVM accesses blockchain data and invokes external data interfaces through the Interoperation layer.
* When the TVM finishes execution, the status is written into the block, and the user can query the execution result and status through the API.

# TVM vs EVM

The TVM exhibits fundamental compatibility with the Ethereum Virtual Machine (EVM), with notable distinctions in the following aspects:

1. The TVM employs an Energy model instead of the gas model. `energyPrice` is a network parameter (it can be changed by committee proposals), currently set at 100 sun on the Mainnet. Unlike the fluctuating gas prices and the presence of a `basefee` in the EVM, the TVM's `GASPRICE` and `BASEFEE` opcodes both return the `energyPrice`.
2. The Energy consumption of the major TVM opcodes aligns with their EVM counterparts, with certain opcodes exhibiting lower Energy costs, such as `SLOAD` and `CALL`.
3. The prefix for contract addresses generated via `CREATE2` on the TVM is different from that of the EVM. The TVM utilizes the `0x41` prefix, determined by the following formula (where ++ represents string concatenation):
   ```
   keccak256(0x41++ address ++ salt ++ keccak256(init_code))[12:]
   ```
4. TRX can be transmitted to contracts through two mechanisms: standard transfers and `TriggerSmartContract` invocations carrying a `callValue`. Standard transfers bypass the execution of the contract's `fallback` function.

## Differences in Instructions

| Instruction         | TVM                             | EVM                                    |
| :------------------ | :------------------------------ | :------------------------------------- |
| `DIFFICULTY` (0x44) | Returns `0`                     | Returns the current block difficulty   |
| `GASLIMIT` (0x45)   | Returns `0`                     | Returns the current block’s `gaslimit` |
| `GASPRICE` (0x3A)   | Returns `energyPrice`           | Returns the current `gasPrice`         |
| `BASEFEE` (0x48)    | Returns `energyPrice`           | Returns the current block’s `baseFee`  |
| `CREATE2` (0xf5)    | Contract address prefix: `0x41` | Contract address prefix: `0xff`        |

## Differences in Precompiled Contracts

| Precompiled Contract Address | TVM                                                                                                                      | EVM                                               |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| `Ripemd160` (0x03)           | Computes `SHA-256` twice                                                                                                 | Computes `SHA-256` once                           |
| 0x09                         | [BatchValidateSign](https://github.com/tronprotocol/tips/blob/master/tip-43.md)  (used for batch signature verification) | [Blake2F](https://eips.ethereum.org/EIPS/eip-152) |

## New Features of the TVM

### Instructions

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Instruction</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
		  <td colspan="2"><b><a href="https://github.com/tronprotocol/documentation/blob/master/English_Documentation/TRON_Virtual_Machine/TRC10_IN_SMARTCONTRACT.MD">TRC-10</a></b></td>
    </tr>
    <tr>
      <td><code>CALLTOKEN</code> (0xd0)</td>
      <td>Invokes contract with TRC-10 token</td>
    </tr>
    <tr>
      <td><code>TOKENBALANCE</code> (0xd1)</td>
      <td>Queries the balance of TRC-10 token for an address</td>
    </tr>
    <tr>
      <td><code>CALLTOKENVALUE</code> (0xd2)</td>
      <td>Retrieves the TRC-10 token value associated with the current call</td>
    </tr>
    <tr>
      <td><code>CALLTOKENID</code> (0xd3)</td>
      <td>Retrieves the ID of the TRC-10 token involved in the current call</td>
    </tr>
    
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-44.md">TIP-44</a></b></td>
    </tr>
    <tr>
      <td><code>ISCONTRACT</code> (0xd4)</td>
      <td>Checks if a given address is a contract address</td>
    </tr>
    
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-467.md">TIP-157</a></b><b> freeze/Unfreeze Functions</b></td>
    </tr>
    <tr>
      <td><code>FREEZE</code>（0xd5）</td>
      <td>Stake TRX to acquire resources</td>
    </tr>
     <tr>
      <td><code>UNFREEZE</code>（0xd6）</td>
      <td>Unstake TRX, releasing acquired resources</td>
    </tr>
    <tr>
      <td><code>FREEZEEXPIRETIME</code>（0xd7）</td>
      <td>Queries the expiration time of a <code>FREEZE</code> operation</td>
    </tr>
    
     <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-467.md">TIP-467</a></b> <b>freezeV2/UnfreezeV2 Functions</b></td>
    </tr>
    <tr>
      <td><code>FREEZEBALANCEV2</code> (0xda)</td>
      <td>Stake TRX to acquire resources (V2)</td>
    </tr>
    <tr>
      <td><code>UNFREEZEBALANCEV2</code> (0xdb)</td>
      <td>Unstake TRX, releasing acquired resources (V2)</td>
    </tr>
    <tr>
      <td><code>CANCELALLUNFREEZEV2</code> (0xdc)</td>
      <td>Cancels all pending <code>UNFREEZE</code> operations (V2)</td>
    </tr>
     <tr>
      <td><code>WITHDRAWEXPIREUNFREEZE</code>(0xdd)</td>
      <td>Withdraws expired unstaked TRX</td>
    </tr>
    <tr>
        <td><code>DELEGATERESOURCE</code> (0xde)</td>
        <td>Delegates resources to another address</td>
    </tr>
    <tr>
        <td><code>UNDELEGATERESOURCE</code> (0xdf)</td>
        <td>Cancels resource delegation</td>
    </tr>
    
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-271.md">TIP-721</a></b> <b>Contract Voting Related Functions</b></td>
    </tr>
    <tr>
      <td><code>VOTEWITNESS</code> (0xd8)</td>
      <td>Votes for a Super Representative</td>
    </tr>
    <tr>
      <td><code>WITHDRAWREWARD</code> (0xd9)</td>
      <td>Withdraws accumulated voting rewards</td>
    </tr>
   </tbody>
</table>
`}</HTMLBlock>

### Precompiled Contracts

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Precompiled Contract</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-60.md">TIP-60</a></b></td>
    </tr>
    <tr>
      <td><code>ValidateMultiSign</code> (0x0a)</td>
      <td>Multi-signature verification</td>
    </tr>
    <tr>
       <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-43.md">TIP-43</a></b></td>
    </tr>
    <tr>
      <td><code>BatchValidateSign</code> (0x09)</td>
      <td>Batch signature verification</td>
    </tr>
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-271.md">TIP-271</a></b> <b>Contract Voting-Related Functions</b></td>
    </tr>
    <tr>
      <td><code>RewardBalance</code> (0x1000005)</td>
      <td>Retrieves voting reward balance</td>
    </tr>
    <tr>
      <td><code>IsSrCandidate</code> (0x1000006)</td>
      <td>Queries whether an address is an <code>srCandidate</code></td>
    </tr>
    <tr>
      <td><code>VoteCount</code> (0x1000007)</td>
      <td>Queries the number of votes a certain address has given to a certain Witness</td>
    </tr>
    <tr>
      <td colspan="2"><b><a href="https://github.com/tronprotocol/tips/blob/master/tip-467.md">TIP-467</a></b> <b>freezeV2/UnfreezeV2 Functions</b></td>
    </tr>
    <tr>
      <td><code>GetChainParameter</code>(0x100000b)</td>
      <td>Queries the specified chain parameters</td>
    </tr>
    <tr>
      <td><code>AvailableUnfreezeV2Size</code> (0x100000c)</td>
      <td>Queries the available length of the unfreeze queue for the target address (V2)</td>
    </tr>
    <tr>
      <td><code>UnfreezableBalanceV2</code> (0x100000d)</td>
      <td>Queries the unfreezable balance of the specified resource type for the target address (V2)</td>
    </tr>
    <tr>
      <td><code>ExpireUnfreezeBalanceV2</code>(0x100000e)</td>
      <td>Queries the withdrawable amount at a specified timestamp for a target address (V2)</td>
    </tr>
     <tr>
      <td><code>DelegatableResource</code>(0x100000f)</td>
      <td>Queries the delegatable amount of the specified resource type for the target address</td>
    </tr>
     <tr>
      <td><code>ResourceV2</code>(0x1000010)</td>
      <td>Queries the amount of the specified resource type delegated from the specified address to the target address (V2)</td>
    </tr>
    <tr>
      <td><code>CheckUnDelegateResource</code>(0x1000011)</td>
      <td>Checks whether the contract can reclaim the specified amount of resources of a specific resource type that have been delegated to the target address</td>
    </tr>
    <tr>
      <td><code>ResourceUsage</code>(0x1000012)</td>
      <td>Queries the usage and recovery time of the specified resource type for the target address.</td>
    </tr>
    <tr>
      <td><code>TotalResource</code>(0x1000013)</td>
      <td>Queries the total amount of available resources of the specified resource type for the target address</td>
    </tr>
     <tr>
      <td><code>TotalDelegatedResource</code> (0x1000014)</td>
      <td>Queries the amount of delegated resources of a specified resource type for the target address</td>
    </tr>
    <tr>
      <td><code>TotalAcquiredResource</code> (0x1000015)</td>
      <td>Queries the total amount of the specified resource type acquired by the target address through delegation</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

Discussions regarding solutions for these compatibility differences are still ongoing. You can join the conversation at [ISSUE-272](https://github.com/tronprotocol/tips/issues/272), or review the related proposal at [TIP-272](https://github.com/tronprotocol/tips/blob/master/tip-272.md).

<br />
