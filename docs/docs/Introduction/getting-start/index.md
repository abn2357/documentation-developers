---
title: Getting Started
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
TRON is an open-source public blockchain platform that supports smart contracts. Since TRON is compatible with Ethereum, you can migrate smart contracts on Ethereum to TRON directly or only with minor modifications. TRON relies on a unique consensus mechanism to realize the network's high TPS, which is far above Ethereum, bringing developers a good experience with faster transactions.

TRON is mainly different from Ethereum in the following aspects:

* **Consensus Mechanism**\
  The Ethereum network uses the POS consensus mechanism, while TRON's consensus mechanism is DPOS. For more information about the TRON consensus mechanism, please refer to [TRON Consensus Mechanism](/docs/concensus).
* **Resource Model**\
  Ethereum transactions require gas fees, and TRON network transactions require Bandwidth and Energy resources, where Bandwidth is a unit to measure the size of a transaction in bytes. The larger a transaction is, the more Bandwidth will be consumed. Energy is a unit that measures the amount of computation required for TRON Virtual Machine (TVM) to perform specific operations on the TRON network, and is calculated in the same way as that of Ethereum. The more instructions a transaction executes, the more Energy it will consume. The amount of Energy consumed by each instruction is also different. For more information about Bandwidth and Energy, please refer to [TRON Resource Model](/docs/resource-model).
* **TVM**\
  TVM of TRON and EVM of Ethereum are compatible but differ in some details, please refer to [Differences between TVM and EVM](/docs/tvm#differences-from-evm).
* **API**\
  Ethereum supports JSON-RPC 2.0 specification APIs, while TRON supports Http and gRPC APIs. Besides, TRON also provides Ethereum-compatible [JSON-RPC 2.0 APIs](/reference/json-rpc-api-overview).

## Overview

This document is designed to help you build Web3 applications on TRON, including the introduction of TRON's basic concepts and core modules, development tools, and various examples. You can choose a topic according to your needs:

* [For DApp Developers](#for-dapp-developers)
* [For Super Representatives and Voters](#for-super-representatives-and-voters)
* [Exchange/Wallet Integration with the TRON network](#exchangewallet-integrate-with-the-tron-network)

## For DApp Developers

If you have Ethereum development experience, you will easily master development on TRON, whose smart contract development language is Solidity. The development tools are also similar to those you have been familiar with on Ethereum (such as Truffle, Remix, and Web3js). Therefore, you will be able to use them proficiently in very little time.

### Tools

The following list contains tools for developing and deploying smart contracts on TRON:

* [TronBox](https://tronbox.io/): a CLI tool used to compile and deploy smart contracts, similar to Ethereum Truffle.
* [Tron-IDE](/docs/tron-ide): a GUI tool used to compile and deploy smart contracts, similar to Ethereum Remix.
* [TronWeb](https://tronweb.network/): a Javascript SDK supporting TRON, similar to Ethereum Web3.js.
* [Trident-java](https://tronprotocol.github.io/trident/): a lightweight Java SDK that includes libraries for working with TRON system contracts and smart contracts. Trident-java makes it easy to build TRON applications with java.
* [TronWallet Adapter](https://walletadapter.org/): it provides a set of wallet adapters and ready-to-use components that help developers easily manage wallet selection, connection, disconnection, as well as message and transaction signing through a unified interface. It offers dApps a simple, secure, and scalable solution for integrating TRON wallets.
* [walletconnect-tron](https://www.npmjs.com/package/@tronweb3/walletconnect-tron): a toolkit that helps dApps connect to the TRON network via the WalletConnect protocol, enabling TRON dApps to quickly connect and interact with wallets just like Ethereum dApps.
* [TronStation](https://tronscan.io/#/tools/tronstation): a resource calculator that can calculate the cost of obtaining a certain amount of resources based on the real-time prices on TRON.
* [TronWidgets](https://www.npmjs.com/package/@tronwidgets/transaction): it is a collection of libraries designed to help developers interact seamlessly with the TRON ecosystem. It provides ready-to-use JavaScript SDKs and upcoming UI components tailored for TRON developers. Currently, the `@tronwidgets/transaction` library has been released, which wraps TronWeb’s transaction-building functionality to simplify transaction operations.

### Wallet

Like MetaMask, TronLink can also be connected to your DApps. Currently, the wallet supports Chrome extension, Android app, and iOS app installation.

* [DApp Integration with TronLink](/docs/introduction)

### Tutorial

If you have zero experience developing DApps on TRON, you can look at the tutorial below, which is beginner friendly by covering the whole set of processes from compiling contracts and UI interaction to deploying and launching DApps. By learning to build a decentralized library as an example, developers can easily master how to deploy their own DApps on the TRON network.

* [Build a Web3 App ](/docs/build-a-web3-app)

### Testnets

You may deploy your DApp on Shasta and Nile testnets as well as the TRON Mainnet. To learn more, please refer to [Network](/docs/networks).

## For Super Representatives and Voters

A Super Representative (SR) is a participant in the network, running a full node for block production. There are 27 SRs in total, who are elected by voting and are responsible for the verification and generation of blocks on the TRON network. In addition, SRs are also responsible for the governance of the network, playing a vital role in ensuring the normal operation of the network.

Voters stake TRX to obtain voting rights and resources (Energy or Bandwidth). Those obtained voting rights can be voted for SRs and then bring voters rewards at the same time.

* [Become an SR](/docs/super-representatives)
* [Run a Fullnode](/docs/deploy-the-fullnode-or-supernode)
* [Reward](/docs/super-representatives#rewards)
* [Brokerage Ratio](/docs/super-representatives#super-representative-brokerage)
* [Committee and Proposals](/docs/super-representatives#committee-and-proposal)

## Exchange/Wallet Integration with the TRON network

If you are running an exchange or providing a wallet service, you can click [here](/docs/exchangewallet-integrate-with-the-tron-network) to learn more about integration with TRON.
