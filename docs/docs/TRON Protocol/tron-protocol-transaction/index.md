---
title: Transactions
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
Transactions are cryptographically signed instructions from accounts. An account can initiate a transaction to update the state of the TRON network. The simplest transaction is transferring TRX from one account to another.

Transactions, which can change the state of the chain, need to be broadcast to the whole network. Any node can broadcast a request for a transaction. After the super node receives the transaction, it executes the transaction and includes it in a block, then propagates the block to the whole network.

Only after the transaction is packed into a block by the super node, and the block is confirmed, the transaction is finally confirmed.

The format of a transaction is as below:

```javascript
{
    "raw_data": 
    {
        "contract": [{<-->}],
        "ref_block_bytes": "c145",
        "ref_block_hash": "c56bd8a3b3341d9d",
        "expiration": 1646796363000,
        "data": "74657374",
        "timestamp": 1646796304152,
        "fee_limit":10000000000
    },
    "signature":["47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800" ] 
}
```

A submitted transaction mainly includes the following fields:

* `raw_data.contract` -  The main content of the transaction.`contract` is a list, but only one element is used at present. TRON supports multiple types of transactions. Different types of transactions have different contract content. For example, for a TRX transfer transaction, the contract will include the transfer amount, receiving address, and other information. For the specific content of this field corresponding to different transaction types, please refer to [Details of Supported Transaction Types](/docs/tron-contracttype).
* `raw_data.ref_block_bytes` -  The height of the transaction reference block, using the 6th to 8th (exclusive) bytes of the reference block height, a total of 2 bytes. The reference block is used in the TRON TAPOS mechanism to prevent a replay of a transaction on forks that do not include the referenced block. The valid reference block is the latest 65536 blocks, and generally, the latest solidified block is used as the reference block. For how to set this field in code, please refer to [here](/docs/faq#19-how-to-set-reference-block-information-for-a-transaction).
* `raw_data.ref_block_hash` - The hash of the transaction reference block, using the 8th to 16th (exclusive) bytes of the reference block hash, a total of 8 bytes. The reference block is used in the TRON TAPOS mechanism to prevent a replay of a transaction on forks that do not include the referenced block. Generally, the latest solidified block is used as the reference block.
* `raw_data.expiration` -  The transaction expiration time, beyond which the transaction will no longer be packed. If the transaction is created by calling a java-tron API, its expiration time will be automatically set by the node through adding 60 seconds to the timestamp of the node's latest block. The expiration time interval can be modified in the node's configuration file, but the maximum value cannot exceed 24 hours.
* `raw_data.data` - The transaction memo.
* `raw_data.timestamp` - The transaction timestamp, set as the transaction creation time. But actually, this field does not need to be set, because the timestamp of the block which the transaction is included in is the actual on-chain timestamp of the transaction.
* `raw_data.fee_limit` - The maximum Energy cost allowed for the execution of smart contract transactions. You need to set this parameter only for deploying and triggering smart contract transactions.
* `signature` - The sender's signature for the transaction. This proves that the transaction could only have come from the sender and was not sent fraudulently.

# Transaction Types

On TRON, there are many different types of transactions, such as TRX transfer transactions, TRC10 transfer transactions, deploying smart contract transactions, triggering smart contract transactions, staking TRX transactions, and so on.

To create different types of transactions, you need to call different APIs. For example, the type of smart contract deployment transaction is `CreateSmartContract`, and you need to call the `wallet/deploycontract` API to create a transaction. The type of the staking TRX transaction is `FreezeBalanceV2Contract`, and you need to call the `wallet/freezebalancev2` API to create a transaction.

```json
$ curl -X POST https://api.shasta.trongrid.io/wallet/freezebalancev2 -d '{"owner_address":"TCrkRWJuHP4VgQF3xwLNBAjVVXvxRRGpbA","frozen_balance": 2100000,"resource" : "BANDWIDTH","visible":true}' | jq
{
  "visible": true,
  "txID": "e54bab34838a59e85d5684e46a2e8e512cd11dfb07b35a9728adeaf3d2666fa6",
  "raw_data": {
    "contract": [
      {
        "parameter": {
          "value": {
            "frozen_balance": 2100000,
            "owner_address": "TCrkRWJuHP4VgQF3xwLNBAjVVXvxRRGpbA"
          },
          "type_url": "type.googleapis.com/protocol.FreezeBalanceV2Contract"
        },
        "type": "FreezeBalanceV2Contract"
      }
    ],
    "ref_block_bytes": "7139",
    "ref_block_hash": "d291dee525445093",
    "expiration": 1646902209000,
    "timestamp": 1646902151591
  },
  "raw_data_hex": "0a0271392208d291dee52544509340e8d39598f72f5a58080b12540a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e467265657a6542616c616e6365436f6e7472616374121e0a15411fafb1e96dfe4f609e2259bfaf8c77b60c535b9310a0968001180370a7939298f72f"
}
```

For more transaction types, please refer to: [Types of transactions on TRON](https://github.com/tronprotocol/java-tron/blob/develop/protocol/src/main/protos/core/Tron.proto#L338). For more HTTP APIs, please refer to：[HTTP API](https://developers.tron.network/reference).

# Transaction Lifecycle

A transaction goes through the following stages in its lifecycle:

1. Transaction creation and signing.
2. The transaction is broadcast to the TRON network, and it will be included in a transaction cache pool after being verified and executed by nodes (including the block-producing node).
3. The block-producing node takes out transactions one by one from the transaction cache pool in the order in which they were put in, packages them into a new block, and then broadcasts the new block to the TRON network.
4. The transaction will be "confirmed". A transaction is considered confirmed once the block containing it is confirmed. In TRON, a block is confirmed when, after it is produced, 18 different Super Representatives (SRs) generate subsequent blocks building on top of it. In this case, the block is acknowledged by a total of 19 SRs, including the SR that produced the block itself.

## Create Transaction

A variety of libraries and tools are provided for you to create transactions. The following section takes using TronWeb to create a TRX transfer transaction as an example to illustrate how to create a transaction:

```javascript
const unsignedTxn = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");
 >{
    "visible": false,
    "txID": "9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "amount": 100,
                        "owner_address": "418840e6c55b9ada326d211d818c34a994aeced808",
                        "to_address": "41d3136787e667d1e055d2cd5db4b5f6c880563049"
                    },
                    "type_url": "type.googleapis.com/protocol.TransferContract"
                },
                "type": "TransferContract"
            }
        ],
        "ref_block_bytes": "0add",
        "ref_block_hash": "6c2763abadf9ed29",
        "expiration": 1581308685000,
        "timestamp": 1581308626092
    },
    "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e"
}
```

## Sign Transaction

A transaction needs to be signed using the sender's private key before sending.

**Transaction signature generating process**

1. Calculate the hash of the transaction.
2. Sign the transaction hash with the sender's private key.
3. Add the generated signature to the transaction instance.

Most SDKs implement the above transaction signature-generating process and encapsulate the steps into an interface for developers. Taking TronWeb as an example, users can directly call the signing method to complete the transaction signature.

**Example of signature using TronWeb**  
Use TronWeb to sign the transaction created above:

```javascript
const signedTxn = await tronWeb.trx.sign(unsignedTxn, privateKey);
>{
    "visible": false,
    "txID":"9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",
    "raw_data":
    {
        "contract": [{<-->}],
        "ref_block_bytes": "0add",
        "ref_block_hash": "6c2763abadf9ed29",
        "expiration": 1581308685000,
        "timestamp": 1581308626092 
    },
    "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e",
    "signature": [ "47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800" ] 
 }
```

## Broadcast Transaction

After the node receives a transaction sent by a user, it will try to verify and execute the transaction locally, and broadcasts valid transactions to other nodes, discards invalid transactions, which will effectively prevent spam transactions from invalid broadcast in the network.

To broadcast a signed transaction using TronWeb:

```javascript
const receipt = await tronWeb.trx.sendRawTransaction(signedTxn);
>{ 
    "result": true,
    "transaction":
    { 
        "visible": false,
        "txID": "9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",
        "raw_data":
        {
            "contract": [{<-->}],
            "ref_block_bytes": "0add",
            "ref_block_hash": "6c2763abadf9ed29",
            "expiration": 1581308685000,
            "timestamp": 1581308626092 
        },
        "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e",
        "signature": [ "47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800" ] 
    } 
 }
```

## Transaction Confirmation

Whether a transaction is confirmed depends on whether the block in which the transaction is included is confirmed. TRON's block confirmation mechanism is that after a block is produced, if 19 different super nodes produce subsequent blocks based on this block,  the block is confirmed.

java-tron node provides the `/walletsolidity/*` API, which is convenient for users to query confirmed transactions. The difference between `/walletsolidity/*` and `/wallet/*` is that transactions returned via `/wallet/*` are transactions that have been on the chain but not necessarily confirmed. Transaction returned via `/walletsolidity/*` are transactions that have been on the chain and solidified, that is, the transactions have been confirmed.

For different transactions, there are different ways to determine whether they have been confirmed:

* **System Contract Transaction**  
  All types of transactions other than creating smart contract and triggering smart contract transactions are system contract transactions. The method for confirming system contract transactions:
  * As long as a transaction can be queried through `/walletsolidity/gettransactioninfobyid` or `/walletsolidity/gettransactionbyid`, it is confirmed.
* **Smart Contract Transaction**  
  Include creating smart contracts and triggering smart contract transactions. Since the transactions need to be executed in the TRON virtual machine (TVM), some exceptions may be thrown during the execution. Even if these transactions are on the chain, it does not mean that the transactions are successfully executed. There are two ways to determine whether a smart contract transaction is successfully executed:
  * Find `transactionInfo.receipt.result` equals `success` via calling the `/walletsolidity/gettransactioninfobyid` API
  * Find `transaction.ret.contractRet` equals`success` via calling `/walletsolidity/gettransactionbyid`API
* **Internal Transaction**  
  An internal transaction is a transaction that transfers tokens to other external addresses or contract addresses in a contract. First, the internal transactions can be queried through the `/walletsolidity/gettransactioninfobyid` API, and the `rejected` field in the internal transaction is used to determine whether the internal transaction is confirmed. But things may differ for HTTP and GRPC APIs:
  * HTTP API: For successful transactions, the `rejected` field is not returned by default. For failed transactions, `rejected` equals true.
  * GRPC API: For successful transactions, `rejected` equals false, indicating that the current internal transaction has not been discarded; for failed transactions, `rejected` equals true.

# Transaction Fees

Except for query operations, any on-chain transaction will consume [system resources](/docs/resource-model). All types of transactions need to consume Bandwidth. In addition to Bandwidth, smart contract deployment and calling transactions also consume Energy. When the available Bandwidth or Energy in an account is insufficient, TRX needs to be burned to pay for the corresponding resource fee. In addition to the resource fee, some special transactions require other fees.

## Bandwidth Fee

The amount of Bandwidth consumed by a transaction is equal to the number of bytes occupied by the transaction on-chain, which includes three parts: the raw_data of the transaction, the transaction signature, and the transaction result. The number of bytes occupied by these three parts after protobuf serialization encoding is the amount of Bandwidth consumed by the transaction.

When both the Bandwidth obtained through staking and the daily free Bandwidth in an account are insufficient, TRX needs to be burned to pay for the Bandwidth cost:

```
TRX burned to pay for Bandwidth = Total Bandwidth consumed by the transaction * Bandwidth unit price
```

The current Bandwidth unit price is 1,000 sun.

When the receiving address of TRX and TRC10 transfer transactions is an inactivated address, the transaction will activate the receiving address. In this case, if the caller address does not have enough Bandwidth obtained through staking, the transaction will consume 0.1 TRX as Bandwidth fee.

For how to estimate the Bandwidth consumption of a transaction, please refer to [here](/docs/faq#5-how-to-calculate-the-bandwidth-and-energy-consumed-when-calling-the-contract).

## Energy Fee

In addition to consuming Bandwidth, smart contract deployment and invocation transactions also consume Energy. When the contract is executed, Energy is calculated and deducted by each instruction. The Energy obtained by staking will be consumed first. If this part of the Energy is not enough, the account's TRX will then be burned to pay for the Energy cost required for the transaction.

```
TRX burned to pay for Energy fee = (Total amount of Energy consumed by the transaction - Amount of Energy available in the caller's account) * Energy unit price
```

The current energy unit price is 100 sun. For how to estimate Energy consumption, please refer to [here](/docs/set-feelimit).

## Other Fees

For some special transactions, in addition to resource fees, other fees can be required. If the transaction initiator adds notes to the transaction, an additional transaction note fee of 1 TRX needs to be paid. If the transaction uses multiple signatures, that is, the number of signatures in the transaction is greater than 1, the transaction initiator needs to pay an additional multi-signature fee of 1 TRX. In addition, there are transaction fees for the following specific types of transactions:

| Transaction Type                | Description                                           |    Fee    |
| :------------------------------ | :---------------------------------------------------- | :-------: |
| WitnessCreateContract           | Apply to become a Super Representative (SR) candidate | 9,999 TRX |
| AssetIssueContract              | Issue an TRC10 token                                  | 1,024 TRX |
| AccountCreateContract           | Create a new account, that is, activate an account    |   1 TRX   |
| AccountPermissionUpdateContract | Update account permissions                            |  100 TRX  |
| ExchangeCreateContract          | Create an exchange pair                               | 1,024 TRX |

Note that for `TransferContract` or `TransferAssetContract` transactions, that is, TRX transfers and TRC10 token transfers, if the target address is not activated, the transaction will also trigger the creation of a new account, and a new account creation fee of 1 TRX will be deducted. At the same time, if the Bandwidth obtained through staking in the transaction initiator's account is insufficient, 0.1 TRX needs to be paid as the Bandwidth fee.

# Internal Transactions

The so-called transactions generally refer to transactions triggered by external accounts, such as smart contract call transactions. But during the execution of smart contract transactions, the contract may trigger other contract method invocation, or transfer TRX/TRC10 tokens to external accounts, or it may also perform operations such as staking, voting, resource delegating. Such transactions that occur during a smart contract execution are called internal transactions. Therefore, internal transactions are transactions triggered in the TVM by contract accounts.

## Generation of Internal Transactions

This article takes the exchange of USDT for TRX in a decentralized exchange as an example to illustrate the generation of internal transactions.

The following content is the `tokenToTrxSwapInput` method of [TRX-USDT trading pair contract](https://tronscan.org/#/contract/TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE/code), which can exchange TRX according to the amount of USDT sold by the user:

```
function tokenToTrxSwapInput(uint256 tokens_sold, uint256 min_trx, uint256 deadline) public returns (uint256) {
    return tokenToTrxInput(tokens_sold, min_trx, deadline, msg.sender, msg.sender);
  }
  
function tokenToTrxInput(uint256 tokens_sold, uint256 min_trx, uint256 deadline, address buyer, address payable recipient) private nonReentrant returns (uint256) {
    require(deadline >= block.timestamp && tokens_sold > 0 && min_trx > 0);
    uint256 token_reserve = token.balanceOf(address(this));
    uint256 trx_bought = getInputPrice(tokens_sold, token_reserve, address(this).balance);
    uint256 wei_bought = trx_bought;
    require(wei_bought >= min_trx);
    recipient.transfer(wei_bought);

    require(address(token).safeTransferFrom(buyer, address(this), tokens_sold));
    emit TrxPurchase(buyer, tokens_sold, wei_bought);
    emit Snapshot(buyer,address(this).balance,token.balanceOf(address(this)));

    return wei_bought;
  }
```

We can see that there are four parts of code in this contract function that involve triggering other contracts or transferring tokens to external accounts, which are:

* Line 7: `token.balanceOf(address(this))`, used to query the USDT balance of this contract
* Line 11: `recipient.transfer(wei_bought)`, used to transfer TRX to the invocation account
* Line 13: `address(token).safeTransferFrom(buyer, address(this), tokens_sold))`, used to transfer USDT from the invocation account to this contract
* Line 15: `token.balanceOf(address(this))`, used to query the USDT balance of this contract

The above four parts of code respectively correspond to the internal transactions queried through [TRONSCAN](https://tronscan.org/#/transaction/50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098/internal-transactions) or through the [API](https://api.trongrid.io/wallet/gettransactioninfobyid?value=50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098) interface.

## Use Cases

Internal transactions can provide some vital information for you. Here are a few use cases where internal transaction information can be used inside a DApp:

* Failed Transaction Notifications -The entire transaction will fail if an internal transaction fails. The purpose of notifying users of the exact location of the fault point can be achieved through internal transactions, which helps to quickly locate and solve problems
* Smart Contract Monitoring - Your deployed smart contract can interact with other contracts via internal transactions. To know when and which contracts it interacts with, you can monitor your smart contract address for any internal transactions.
* Smart Contract Analytics - Since internal transactions can be complex, getting insights is helpful. By looking at the number of internal transactions performed by a smart contract, you can understand the performance of that contract.
* Batch Transactions - When sending transactions to multiple recipient addresses, internal transactions offer a convenient and secure way to ensure accurate delivery.

## Storage of Internal Transactions

There are many use cases for internal transactions, which can guide and inform users about the execution of transactions, but the TRON node does not save internal transaction information by default, and needs to be manually enabled through the node configuration file:

```
vm = {
    ...
  saveInternalTx = true
  saveFeaturedInternalTx = true
    ...
}
```

* `saveInternalTx`: Whether to save internal transactions
* `saveFeaturedInternalTx`: When `saveInternalTx` is enabled, whether to save Stake 2.0-related internal transactions

After the internal transaction storage configuration item is enabled, restart the node. From the moment of the restart, the node will save its internal transactions. You can view internal transactions via the transaction ID of the outer transaction. But viewing internal transactions directly through the hash of internal transactions is not supported. You can call  [gettransactioninfobyid](https://cn.developers.tron.network/reference/gettransactioninfobyid) to query internal transactions involved in a transaction.

## Examples of Internal Transactions

An internal transaction saved by a node contains the following information:

* `hash`: the hash value of the internal transaction.
* `caller_address`: the caller address.
* `transferTo_address`: the called contract address or the account address receiving TRX/TRC10 tokens.
* `callValueInfo.callValue`: the amount of TRX/TRC10 tokens transferred.
* `callValueInfo.tokenId`: the TRC10 token name or ID. When TRX is transferred, this field is empty.
* `note`: the instruction type, such as call, create, suicide, freezeBalanceV2ForEnergy, freezeBalanceV2ForBandwidth, and unfreezeBalanceV2ForBandwidth.
* `rejected`: Whether the internal transaction failed. true means the execution failed.
* `extra`: At present, it is mainly used to save voting information and record the voting SR and its number of votes in the JSON format.

Let's look at the information contained in internal transactions based on various examples:

### 1. Smart contract calls other smart contract methods

In this example, the [transaction](https://tronscan.org/#/transaction/50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098/internal-transactions) is an external address calling the "TQn9Y...." contract, and in the "TQn9Y...." contract, the "TR7NHq...." contract is called:

```
{
    "id": "50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098",
    ......
    "internal_transactions": [
        {
            "hash": "380f4d87271b83afcf5e867271ee2d30b36c19d3eeb15a043477bce7fd5b2079",
            "caller_address": "TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE",
            "transferTo_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
            "callValueInfo": [
                {}
            ],
            "note": "63616c6c"
        },
        .......
    ]
}
```

The information contained in the above internal transactions is as follows:

* `internal_transactions.caller_address` is the address of the caller, that is, the contract address directly called by the external address.
* `internal_transactions.transferTo_address` is the address of another contract called in the contract.
* `internal_transactions.callValueInfo` In this example, the contract did not pass TRX/TRC10 token using `value` when calling other contracts, so the value of this field is empty. If `value` information is attached when the contract calls other contract functions, it will be reflected through this field.
* `internal_transactions.note` is the instruction description, in the Hex format. After converting it to a string, you can get the operation information in plain text, which is`call` in this example.

### 2. Smart contract transfers TRX to external accounts

In this example, the [transaction](https://tronscan.org/#/transaction/50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098/internal-transactions) is an external address calling the "TQn9Y...." contract, and in the "TQn9Y...." contract, TRX is transferred to the "TQnpn...." address:

```
{
    "id": "50e6dd05c37b8666cf4a689fe6c0d52053b76b53d8649b256e6b9dca8c9df098",
     ......
    "internal_transactions": [
        ......
        {
            "hash": "f47fede2a45e722e6406421d0df16142e159ae7404525de5a595f4fc0c357e26",
            "caller_address": "TQn9Y2khEsLJW1ChVWFMSMeRDow5KcbLSE",
            "transferTo_address": "TQnpnLZJYMzH5xku535rAiYTnqYXTDTEHQ",
            "callValueInfo": [
                {
                    "callValue": 4514968563
                }
            ],
            "note": "63616c6c"
        },
        ......
    ]
}
```

* `internal_transactions.caller_address`is the address of the caller, that is, the address of the contract directly called by the external address.
* `internal_transactions.transferTo_address` is the target address for transferring TRX.
* `internal_transactions.callValueInfo[0].callValue` is the transfer amount of TRX (in sun).
* `internal_transactions.note` is the instruction description, in the Hex format. After converting it to a string, you can get the operation information in plain text, which is `call` in this example.

### 3. Smart contract transfers TRC10 tokens to external accounts

TRC10 transfer is basically the same as TRX transfer, except for the following two fields:

* `internal_transactions.callValueInfo[0].callValue` is the amount of TRC10 tokens being transferred.
* `internal_transactions.callValueInfo[0].tokenId` is the TRC10 token name or ID. Since [No. 14 Committee Proposal](https://tronscan.org/#/proposal/14) allows the same token name, so before this proposal takes effect (blocks before 5537806), this field indicates the TRC10 token name, and after the proposal takes effect (block 5537806 and later), this field indicates the TRC10 token ID.

### 4. Smart contract stakes TRX

In this example, the [transaction](https://nile.tronscan.io/#/transaction/9d25a4fe417e0c7540cc5c5841e1d8c9215aec556d9b06e18910ed8b5088f0d8) is an external address calling the "TU8Mb...." contract, and in "TU8Mb....", the contract stakes 1,000 TRX to obtain Energy:

```
{
    "id": "9d25a4fe417e0c7540cc5c5841e1d8c9215aec556d9b06e18910ed8b5088f0d8",
    ......
    "internal_transactions": [
        {
            "hash": "a3a4d666e7bf0729bbd8b5e5ad7afb7f8dd20191e7298ea9dbd17af345c96ed5",
            "caller_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "transferTo_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "callValueInfo": [
                {
                    "callValue": 1000000000
                }
            ],
            "note": "667265657a6542616c616e63655632466f72456e65726779"
        }
    ]
}
```

* `internal_transactions.caller_address` is the address of the staking initiator, that is, the address of the contract directly called by the external address.
* `internal_transactions.transferTo_address` is the resource receiving address, that is, the staking initiator address, which is also the address of the contract directly called by the external address.
* `internal_transactions.callValueInfo[0].callValue` is the staked TRX amount (in sun).
* `internal_transactions.note` is the instruction description in the Hex format, and the instruction information in plain text can be obtained after converting it into a string. In this example, it is `freezeBalanceV2ForEnergy`, which means that the contract stakes TRX to obtain Energy. If the contract stakes TRX to obtain Bandwidth, the value of this field is `freezeBalanceV2ForBandwidth`.

### 5. Smart contract unstakes TRX

In this example, the [transaction](https://nile.tronscan.io/#/transaction/dc110091fbd1568f8b264f287c7e0896d1afaf47b906a9e684fd17d57c7a1151) is an external address calling the "TU8Mb...." contract, and the  "TU8Mb...." contract performs the unstaking operation to unstake the 100 TRX staked to obtain Bandwidth:

```
{
    "id": "dc110091fbd1568f8b264f287c7e0896d1afaf47b906a9e684fd17d57c7a1151",
    ......
    "internal_transactions": [
        {
            "hash": "16f73bdad5e9f984e082909b1028fff0b9865952131e681ca887446f8ec89918",
            "caller_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "transferTo_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "callValueInfo": [
                {
                    "callValue": 100000000
                }
            ],
            "note": "756e667265657a6542616c616e63655632466f7242616e647769647468"
        }
    ]
}
```

* `internal_transactions.caller_address` is the address of the unstaking initiator, that is, the address of the contract directly called by the external address.
* `internal_transactions.transferTo_address` is the TRX receiving address, that is, the contract address directly called by the external address.
* `internal_transactions.callValueInfo[0].callValue` is the amount of TRX unstaked (in sun).
* `internal_transactions.note` is the instruction description. In this example, it is `unfreezeBalanceV2ForBandwidth`, which means that the contract unstakes the TRX staked for obtaining Bandwidth. If the contract unstakes the TRX staked for obtaining Energy, the value of this field is `unfreezeBalanceV2ForEnergy`.

### 6. Smart contract delegates resources to other accounts

In this example, the [transaction](https://nile.tronscan.io/#/transaction/342daa21f8865786295c45bb80e2f257740091e4e1a3a546b90daa51bcbcbd18) is an external address calling the "TU8Mb...." contract, and the "TU8Mb...." contract delegated Energy of 500,000,000 sun to "TUznH....":

```
{
    "id": "342daa21f8865786295c45bb80e2f257740091e4e1a3a546b90daa51bcbcbd18",
    ......
    "internal_transactions": [
        {
            "hash": "58382a79c3af68c472383580309a81a9322e7520a48b6463917ba9219ca32a7d",
            "caller_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "transferTo_address": "TUznHJfHe6gdYY7gvWmf6bNZHuPHDZtowf",
            "callValueInfo": [
                {
                    "callValue": 500000000
                }
            ],
            "note": "64656c65676174655265736f757263654f66456e65726779"
        }
    ]
}
```

* `internal_transactions.caller_address` is the resource delegating address, that is, the contract address directly called by the external address.
* `internal_transactions.transferTo_address` is the resource receiving address.
* `internal_transactions.callValueInfo[0].callValue` is the delegated resource amount (in sun).
* `internal_transactions.note` is the instruction description. In this example, it is `delegateResourceOfEnergy`, which means the contract delegates Energy resources. If it is a contract delegating Bandwidth, the field value is `delegateResourceOfBandwidth`

### 7. Smart contract cancels the resource delegation to other accounts

In this example, the [transaction](https://nile.tronscan.io/#/transaction/aa3961ffb0781d8b66d5e22368e92708135dac9c81eac1e2adcaa8546d729bc8) is an external address calling the "TU8Mb...." contract, and the "TU8Mb...." contract cancels the delegation of 200,000,000 sun Energy to "TUznH....":

```
{
    "id": "aa3961ffb0781d8b66d5e22368e92708135dac9c81eac1e2adcaa8546d729bc8",
    ......
    "internal_transactions": [
        {
            "hash": "1a8524704098770d9c6535e1112d1fb91855363c8366c93810f3cb56e8ee12bf",
            "caller_address": "TU8MbhYhurKv4T3xAHQKZCeP4DtFCmWLMt",
            "transferTo_address": "TUznHJfHe6gdYY7gvWmf6bNZHuPHDZtowf",
            "callValueInfo": [
                {
                    "callValue": 200000000
                }
            ],
            "note": "756e44656c65676174655265736f757263654f66456e65726779"
        }
    ]
}
```

* `internal_transactions.caller_address` is the resource delegating address, that is, the contract address directly called by the external address.
* `internal_transactions.transferTo_address` is the resource receiving address, that is, to cancel the resource delegated to this address.
* `internal_transactions.callValueInfo[0].callValue` is the amount of TRX delegation canceled (in sun).
* `internal_transactions.note` is the instruction description. In this example, it is `unDelegateResourceOfEnergy`, which means canceling the Energy delegation. If the contract cancels the Bandwidth delegation, the value of this field is `unDelegateResourceOfBandwidth`.

### 8. Smart contract votes for SRs

In this example, the [transaction](https://nile.tronscan.io/#/transaction/58506325f692eee0bd730d97a0086f8b0c50e8aa5392b9e4b0edd5fb0916a718) is an external address calling the "TNaDY...." contract, and the "TNaDY...." contract votes 200 and 400 for the SRs "TUoHa...." and "TUznH...." respectively:

```
{
    "id": "58506325f692eee0bd730d97a0086f8b0c50e8aa5392b9e4b0edd5fb0916a718",
    ......
    "internal_transactions": [
        {
            "hash": "792b26cb6fbd1c92030721c62f7fd14522a94f412e04b05442d78e1ce743c9f4",
            "caller_address": "TNaDYZaXEpL1LY8Uk4LtGTwwQrGzXTwss9",
            "callValueInfo": [
                {}
            ],
            "note": "766f74655769746e657373",
            "extra": "{\"votes\":[{\"vote_address\":\"TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM\",\"vote_count\":200},{\"vote_address\":\"TUznHJfHe6gdYY7gvWmf6bNZHuPHDZtowf\",\"vote_count\":400}]}"
        }
    ],
    ......
}
```

* `internal_transactions.caller_address`: This is the address voting for the SRs, that is, the contract address directly called by the external address.
* `internal_transactions.transferTo_address`: For contract voting transactions, the value of this field is empty, so this field is not displayed in the returned result.
* `internal_transactions.callValueInfo`: For contract voting transactions, the value of this field is an empty array.
* `internal_transactions.note`: This is the instruction description. In this case, it is `voteWitness`, which means voting for SRs.
* `internal_transactions.extra`: voting details, recording the SR being voted for and the specific vote count in the JSON format: votes[i].vote_address is the SR address, and votes[i].vote_count is the number of votes.

### 9. Smart contract withdraws rewards

In this example, the [transaction](https://nile.tronscan.io/#/transaction/8dc24b5ce1399b553cd173529e77b22172d9abf31e9f50dd32c473bcc5234b71) is an external address calling the "TNaDY...." contract, and the "TNaDY...." contract withdraws the reward of 443,803,418 sun:

```
{
    "id": "8dc24b5ce1399b553cd173529e77b22172d9abf31e9f50dd32c473bcc5234b71",
    ......
    "internal_transactions": [
        {
            "hash": "e5b047a4a3d64407c93a9e667a083fe52c52b24e859e3a44488249436e79c8d4",
            "caller_address": "TNaDYZaXEpL1LY8Uk4LtGTwwQrGzXTwss9",
            "transferTo_address": "TNaDYZaXEpL1LY8Uk4LtGTwwQrGzXTwss9",
            "callValueInfo": [
                {
                    "callValue": 443803418
                }
            ],
            "note": "7769746864726177526577617264"
        }
    ]
}
```

* `internal_transactions.caller_address` is the address that withdraws the reward, that is, the contract address directly called by the external address.
* `internal_transactions.transferTo_address` is the reward receiving address, that is, the contract address directly called by the external address.
* `internal_transactions.callValueInfo[0].callValue` is the withdrawn TRX reward amount (in sun).
* `internal_transactions.note` is the instruction description. In this example, it is `withdrawReward`, which means withdrawing the reward.
