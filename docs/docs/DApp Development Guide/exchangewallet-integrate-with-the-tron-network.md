---
title: Exchange/Wallet Integrate with the TRON Network
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
The following questions are generally considered when wallets and exchanges integrate with the TRON network:

1. How to determine if an address has inbound asset in time?
2. How to get historical transaction records of an address?
3. How to query asset balance and transfer asset?

Some wallets and exchanges may provide users with staking services, and generally need to consider the following questions:

1. How to stake TRX?
2. How to vote for Super Representatives (SRs)?
3. How to withdraw rewards?
4. How to unstake TRX?

The above requirements can be achieved by accessing the TronGrid service or building a TRON full node. Due to limited resources, the TronGrid service will set the access frequency and daily total limit: 20QPS and 100,000 daily requests. So it is recommended to build a full node if you have high access frequency and total requirements.

In addition to providing all the APIs of the full node, the TronGrid API service also provides some more convenient query API, such as querying the historical transaction records of an account. By continuously polling such an API, you can monitor the real-time inbound and outbound transfers of an address, which is a great help for wallet and exchange integration.

After building a FullNode, the historical transaction records of an account can be obtained by parsing historical blocks, and the outbound and inbound transactions of an address can be monitored in real time by parsing the latest block. Full nodes also provide APIs for transferring and broadcasting transactions.

# Deploy a Fullnode of TRON Network

If you want to build your own node, please refer to the [Deploy A Node](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode) tutorial to complete the node deployment.

## Configure the Fullnode

Before starting the node, please check the node configuration file config.conf. Generally, you need to focus on the following configuration items:

* vm.supportConstant  
  Whether the node supports calling read-only contract functions. It is recommended to set it to true, because the business scenarios of general exchanges and wallets involve querying the balance of TRC20 tokens. To query the balance of TRC20 tokens, you must call the `balanceOf` read-only function of the TRC20 token contract.
* vm.saveInternalTx  
  Whether the node stores internal transactions. Calling other contracts in the contract or transferring asset from the contract to other addresses is called internal transactions. It is recommended to set it to true, because the business scenarios of exchanges and wallets involve block parsing. Only this option enabled ensures all transaction records can be obtained.
* vm.maxTimeRatio  
  The node's tolerance for transaction timeout when verifying smart contract transactions. If the configuration of the machine is below the recommended configuration, it is recommended to set it to 20.0 or higher, otherwise it may cause the node to stop synchronizing.

## Query Balance

The following table lists the example query APIs to query TRX, TRC10 and TRC20 token balances.

| Feature                    | Interface                                                                                            | Example                                                                                     |
| :------------------------- | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Query TRX Balance          | [/wallet/getaccount](https://developers.tron.network/reference/account-getaccount)                   | [TRX Balance](https://developers.tron.network/docs/token-standards-trx#querying-trx)        |
| Query TRC-10 Token Balance | [/wallet/getaccount](https://developers.tron.network/reference/account-getaccount)                   | [TRC-10 Balance](https://developers.tron.network/docs/trc10#check-balance)                  |
| Query TRC-20 Token Balance | [/wallet/triggerconstantcontract](https://developers.tron.network/reference/triggerconstantcontract) | [TRC-20 Balance](https://developers.tron.network/docs/trc20-contract-interaction#balanceof) |

## Transfer

The process of sending a transfer transaction includes three steps: creating a transaction, and signing and broadcasting the transaction. For the life cycle of the transaction, please refer to the [Transaction](https://developers.tron.network/docs/tron-protocol-transaction) chapter.

The following table lists APIs and examples for creating transferring TRX, TRC-10, and TRC-20 token transactions. And SDKs in different languages include offline signing methods.

| Feature                | Interface                                                                                     | Example                                                                                     |
| :--------------------- | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Transfer TRX           | [wallet/createtransaction](https://developers.tron.network/reference/createtransaction)       | [Transfer TRX](https://developers.tron.network/docs/token-standards-trx#transferring-trx)   |
| Transfer TRC-10 Tokens | [wallet/transferasset](https://developers.tron.network/reference/transferasset)               | [Transfer TRC-10](https://developers.tron.network/docs/trc10#transfer)                      |
| Transfer TRC-20 Token  | [wallet/triggersmartcontract](https://developers.tron.network/reference/triggersmartcontract) | [Transfer TRC-20](https://developers.tron.network/docs/trc20-contract-interaction#transfer) |

## Parse Blocks to Get Transaction Records

The historical transaction records of an account can be obtained by parsing historical blocks, and the outbound and inbound transactions of an address can be monitored in real time by parsing the latest blocks.

You can refer to the following steps to parse blocks to obtain TRX, TRC10 and TRC20 historical records:

1. Get block information  
   Get block information from the solidified block according to the block number: `/walletsolidity/getblockbynum`

2. Get transactions from the block.

3. Go through all the transactions and get the `raw_data.contract[0]` of each transaction.

4. Check the type of transaction based on `raw_data.contract[0].type`:

   * TRX Transfer Transaction: `raw_data.contract[0].type == transferContract`  
     Check if the recipient address and amount meet the entry criteria.
     * raw_data.contract[0].parameter.value.owner_address is the transfer address
     * raw_data.contract[0].parameter.value.to_address  is the recipient address
     * raw_data.contract[0].parameter.value.amount is the amount of the transfer

   * TRC10 Transfer Transaction: `raw_data.contract[0].type == TransferAssetContract`  
     Check if the token id, recipient address and amount meet the entry criteria.
     * raw_data.contract[0].parameter.value.owner_address is the transfer address
     * raw_data.contract[0].parameter.value.to_address is the recipient address
     * raw_data.contract[0].parameter.value.asset_name is TRC-10 token id or name. Since [The No.14 Committee Proposal](https://tronscan.org/#/proposal/14) allows duplicate token name, therefore, before the proposal takes effect, the token name is used as the unique identifier of a TRC-10 token. After it takes effect, the token id will be used as the unique identifier of a TRC-10 token. That is, in the block before [5537806](https://tronscan.org/#/block/5537806), this field indicates the TRC-10 token name, in [5537806]([https://tronscan.org/#/block](https://tronscan.org/#/block) /5537806) and subsequent blocks, this field indicates the TRC-10 token id.
     * raw_data.contract[0].parameter.value.amount is the amount of the transfer

   * Smart Contract Transaction: `raw_data.contract[0].type == TriggerSmartContract`  
     One smart contract transaction can contain TRC20 Token Transfer, TRX transfer, and TRC10 Token Transfer. The below process shows how to proceed with a smart contract transaction.
     1. Check whether the transaction is successful, and skip the transaction if it is not successful.  
        Call `/walletsolidity/gettransactioninfobyid` to check whether receive.result == SUCCESS, if yes, the transaction is executed successfully.
     2. Determine whether the transaction contains TRC20 transfers:  
        call `/walletsolidity/gettransactioninfobyid` to check whether the smart contract transaction contains "Transfer" events, If yes, parse all the events (There may be multiple TRC20 transfers in a smart contract transaction) one by one to get the contract address, transfer address, and amount in the event. Event parsing rules please refer to [Here](https://developers.tron.network/docs/event#log-decoding).
     3. TRX/TRC10 Token Transfer in smart contract transaction: call `/walletsolidity/gettransactioninfobyid` to check whether the smart contract transaction contains internal transactions. If yes, then traverse the internal transactions:
        * If the internal transaciton's instruction description is "call", that is the internal_transactions.note.equals("63616c6c"), then if  internal_transactions.callValueInfo != null & internal_transactions.callValueInfo[i].tokenId == null then it is a TRX transfer that is performed in the contract. [Example transaction](https://api.nileex.io/wallet/gettransactioninfobyid?value=f66cad4376d4f611135c0a8cff4c0927fa36d4310d3c9aab20e80ddcfc8b7728)
          * internal_transactions.caller is the transfer address
          * internal_transactions.transferTo_address is the recipient address
          * internal_transactions.callValueInfo[i].callValue is the amount of the transfer
        * If internal_transactions.callValueInfo != null & internal_transactions.callValueInfo[0].tokenId != null then a TRC10 transfer was made in the contract. [Example transaction](https://api.nileex.io/wallet/gettransactioninfobyid?value=4c494931e68c567940168d20edf7b39e7709c3d1c8a2e68dc52226dd78545d9e)
          * internal_transactions.caller  is the transfer address
          * internal_transactions.transferTo_address is the recipient address
          * internal_transactions.callValueInfo[i].tokenId is TRC10 token ID
          * internal_transactions.callValueInfo[i].callValue is the transfer amount

# Use TronGrid API Service

The TronGrid API service provides all APIs of the fullnode of the TRON network and its unique extension API. However, in order to ensure the reasonable allocation of requested resources, all requests need to provide [API Key](https://developers.tron.network/reference/api-key). Domain names starting with `https://api.shasta.trongrid.io/v1` are all v1 extension APIs. For details about v1 extension APIs, please refer to [Trongrid v1 API](https://developers.tron.network/reference/background)。

## TronGrid API Endpoint

Mainnet: [https://api.trongrid.io](https://api.trongrid.io)  
Shasta testnet: [https://api.shasta.trongrid.io](https://api.shasta.trongrid.io)  
Nile testnet: [https://nile.trongrid.io](https://nile.trongrid.io)

## Query Balance

The following table lists the query APIs and examples for querying TRX, TRC10 and TRC20 token balances.

| Feature             | API                                                                                                                          | Example                                                                                    |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| Query TRX Balance   | [https://api.trongrid.io//wallet/getaccount](https://developers.tron.network/reference/account-getaccount)                   | [TRX Balance](https://developers.tron.network/docs/token-standards-trx#querying-trx)       |
| Query TRC10 Balance | [https://api.trongrid.io//wallet/getaccount](https://developers.tron.network/reference/account-getaccount)                   | [TRC10 Balance](https://developers.tron.network/docs/trc10#check-balance)                  |
| Query TRC20 Balance | [https://api.trongrid.io//wallet/triggerconstantcontract](https://developers.tron.network/reference/triggerconstantcontract) | [TRC20 Balance](https://developers.tron.network/docs/trc20-contract-interaction#balanceof) |

## Transfer

The process of sending a transfer transaction includes three steps: creating a transaction body, signing, and broadcasting the transaction. For the life cycle of the transaction, please refer to the [Transaction](https://cn.developers.tron.network/docs/tron-protocol-transaction) chapter.

The following table lists APIs for creating TRX, TRC10, and TRC20 token transfer transactions, as well as signing and broadcasting examples. SDKs in different languages all contain offline signing methods.

| Feature        | API                                                                                                                   | Examples                                                                                   |
| :------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| Transfer TRX   | [https://api.trongrid.io/wallet/createtransaction](https://developers.tron.network/reference/createtransaction)       | [Transfer TRX](https://developers.tron.network/docs/token-standards-trx#transferring-trx)  |
| Transfer TRC10 | [https://api.trongrid.io/wallet/transferasset](https://developers.tron.network/reference/transferasset)               | [Transfer TRC10](https://developers.tron.network/docs/trc10#transfer)                      |
| Transfer TRC20 | [https://api.trongrid.io/wallet/triggersmartcontract](https://developers.tron.network/reference/triggersmartcontract) | [Transfer TRC20](https://developers.tron.network/docs/trc20-contract-interaction#transfer) |

## Get Transaction History

The TronGrid v1 extension API supports querying the historical transaction records of an account. By continuously querying the historical transaction records of an address, it is also possible to monitor the real-time inbound and outbound transfer transactions of an address.

The following table lists the APIs for querying the transfer records of TRX, TRC10 and TRC20 tokens on an address.

| Feature                                                 | API                                                                                                                                                      | Description                                                                                                                                                                                                                                                        |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Query account history TRX and TRC10 transaction records | [v1/accounts/\{address}/transactions?only_confirmed=true](https://developers.tron.network/reference/get-transaction-info-by-account-address)             | The return value contains TRX and TRC10 token transaction records. The transaction type is distinguished by the type field in the transaction. `TransferContract` represents TRX transfer, and `TransferAssetContract` represents TRC10 token transaction records. |
| Query account history TRC20 transaction records         | [v1/accounts/\{address}/transactions/trc20?only_confirmed=true](https://developers.tron.network/reference/get-trc20-transaction-info-by-account-address) | The return value contains TRC20 token transaction records                                                                                                                                                                                                          |

# Staking and Voting

Wallets and exchanges may also provide staking services. In addition to obtaining corresponding resources, any user who stakes TRX will also obtain voting rights. Voting rights can be used to vote for SRs to obtain voting rewards. The following are the APIs related to staking and voting .

| Feature                                                                               | API                                                                                          |
| :------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------- |
| Stake TRX                                                                             | [wallet/freezebalancev2](/reference/freezebalancev2-1)                                       |
| Unstake TRX                                                                           | [wallet/unfreezebalancev2](/reference/unfreezebalancev2-1)                                   |
| Unstake the TRX staked during Stake1.0                                                | [wallet/unfreezebalance](/reference/account-resources-unfreezebalance)                       |
| Delegate resources                                                                    | [wallet/delegateresource](/reference/delegateresource-1)                                     |
| Undelegate resources                                                                  | [wallet/undelegateresource](/reference/undelegateresource-1)                                 |
| Withdraw unfrozen balance                                                             | [wallet/withdrawexpireunfreeze](/reference/withdrawexpireunfreeze)                           |
| Query the remaining times of executing unstaking operation                            | [wallet/getavailableunfreezecount](/reference/getavailableunfreezecount-1)                   |
| Query the withdrawable balance                                                        | [wallet/getcanwithdrawunfreezeamount](/reference/getcanwithdrawunfreezeamount-1)             |
| Query the amount of delegatable resources share of the specified resource Type        | [wallet/getcandelegatedmaxsize](/reference/getcandelegatedmaxsize)                           |
| Query the amount of resource delegated by fromAddress to toAddress                    | [wallet/getdelegatedresourcev2](/reference/getdelegatedresourcev2)                           |
| Query the resource delegation index by an account                                     | [wallet/getdelegatedresourceaccountindexv2](/reference/getdelegatedresourceaccountindexv2-1) |
| Query the account staking status, resource share, unstaking status, and voting status | [wallet/getaccount](/reference/account-getaccount)                                           |
| Query the total amount of resources, and the amount of used available resources       | [wallet/getaccountresource](/reference/getaccountresource)                                   |
| Vote for SRs                                                                          | [wallet/votewitnessaccount](https://developers.tron.network/reference/votewitnessaccount)    |
| Query the rewards that the user has not yet withdrawn                                 | [wallet/getReward](https://developers.tron.network/reference/wallet-getreward)               |
| Withdraw voting rewards                                                               | [wallet/withdrawbalance](https://developers.tron.network/reference/withdrawbalance)          |
