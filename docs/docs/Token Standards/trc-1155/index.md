---
title: TRC-1155
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
TRC-1155 is one of the TRON token standards, which can represent and manage multiple tokens at once, including fungible tokens (TRC-20), non-fungible tokens (TRC-721), and semi-fungible tokens, and it provides batch processing operations.

TRC-1155 is essentially a combination of TRC-20 and TRC-721 standards. In addition to all the functions of TRC-20 and TRC-721, it also takes the best from these two standards to make itself more efficient. The main purpose of TRC-1155 is to issue multiple fungible tokens, multiple non-fungible tokens (NFTs), or multiple fungible tokens and non-fungible tokens at the same time in one contract.

With the popularity of the metaverse concept, games on blockchain have higher requirements for asset generation and processing speed. The TRC-1155 standard can provide great help for the development and operation of games based on the TRON network, especially in the generation and processing of fungible and non-fungible tokens. For example, a game may require fungible tokens - gold coins or game coins, and non-fungible tokens - collectibles or props, then developers can create these two types of tokens based on the TRC-1155 standard and ensure their interoperability, so that players can exchange single or multiple game props for gold coins and vice versa. Therefore, this standard can greatly improve development efficiency and reduce usage costs.

# TRC-1155 Functions and Features

TRC-1155 has the following functions and features:

* Support Both Fungible Tokens and Non-Fungible Tokens

    For this feature, compared with TRC-20 and TRC-721, TRC-1155 has the following advantages:

    Firstly, since each TRC-20 token requires a contract to be deployed, and the contract codes of most tokens are almost the same, plus a single TRC-1155 contract can represent and manage a variety of fungible tokens and non-fungible tokens, so the TRC-1155 standard can greatly reduce on-chain spatial redundancy.

    Secondly, although a TRC-721 contract can contain multiple NFTs, they actually share the same configuration. But a TRC-1155 contract can configure different properties for each NFT, such as metadata, supply, and other properties.

    When the supply is just one, the token is essentially an NFT. And you can define a metadata URL which can be read and modified by clients.

* Batch Transfer\
    In addition to single-token transfer, TRC-1155 also has a batch transfer function. `safeBatchTransferFrom` can transfer multiple different tokens to an address at the same time, which greatly saves resource consumption.

* Batch Approval\
    Different from TRC-20, TRC-1155 does not authorize a specific number of tokens under a single type to an account, but authorizes all tokens managed by the TRC-1155 contract at one time. It does not support single-token authorization, nor can it specify the number of tokens to be authorized. Through the `setApprovalForAll` interface, you can simply authorize or deauthorize an account.

* Batch Balance

    In addition to the balance query of a single token, TRC-1155 also has a batch query function. `balanceOfBatch` can query the balance of multiple tokens of multiple accounts at the same time.

* Hooks

    Since TRC-1155 supports the TIP-165 specification, if a smart contract wants to receive TRC-1155 tokens, it must implement the following TRC-1155 receive hooks, and the hook function must return a predefined 4-byte value. For details, please see the [ TRC1155 Token Receiver](/docs/protocol-interface#trc1155-token-receiver)  chapter.

  ```solidity
  interface TRC1155TokenReceiver {

  function onERC1155Received(address _operator, address _from, uint256 _id, uint256 _value, bytes calldata _data) external returns(bytes4);
  function onERC1155BatchReceived(address _operator, address _from, uint256[] calldata _ids, uint256[] calldata _values, bytes calldata _data) external returns(bytes4);
  }
  ```

    When a TRC-1155 token needs to be transferred to a contract, the hook function will be called. If the correct value is returned, then the contract can normally receive the TRC-1155 token and know how to deal with it. Receive hooks are a key point in achieving safe transfer.

    Note that in order to be fully compatible with Ethereum and facilitate code migration for developers, the interface defined in `TRC1155TokenReceiver` is consistent with that in Ethereum `ERC1155TokenReceiver`.

* Safe Transfer Rules\
    The TRC-1155 standard defines secure transfer specifications in each interface. For details, please refer to [TRC-1155 Specification](https://github.com/tronprotocol/tips/issues/404).
