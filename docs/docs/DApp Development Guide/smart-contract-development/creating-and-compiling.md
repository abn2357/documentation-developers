---
title: Creating and Compiling a Contract
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
[Tron-IDE](https://www.tronide.io/)   (similar to [Remix IDE](https://remix.ethereum.org) on the Ethereum platform) is a user-friendly IDE for developing contracts. For more information on how to use Tron-IDE, please refer to the [Tron-IDE Introduction](https://developers.tron.network/docs/tron-ide). This guide explains how to create and compile a smart contract in Tron-IDE.

## Prepare Contract Files

After entering the **FILE EXPLORER** tab, click the "Create New File" icon to create a contract file, or select the "Load a local file into current workspace" icon to import pre-written contract code from your local machine.

<br />

![](https://files.readme.io/7764be376502b32ca1b7efaa3eac9e0d06c0cff58f10def92ac02379a6d9ed2c-image.png)

<br />

You can use the [TRC-20 contract template](https://github.com/tronprotocol/tron-contracts/tree/master/contracts/tokens/TRC20) to issue your TRC-20 token.

## Compile Contract

Enter the **SOLIDITY COMPILER** tab in Tron-IDE, select the appropriate compiler version, and configure compilation parameters, such as whether to enable optimization and the number of optimization runs (These parameters will be needed again during contract verification, so please keep them in mind.). After setting up, click the Compile button to compile the contract.

![](https://files.readme.io/f09cf4c14ff24aa74aec91d59ddd0286990eeb2572019bf4903db0a56e627e48-image.png)

<br />

<br />

## View Contract Data

After compilation, click **Compilation Details** to view the data of the smart contract.  
The details contain the contract name, [ABI](https://en.wikipedia.org/wiki/Application_binary_interface), bytecode, Etc.

![](https://files.readme.io/cff31b559d208e35e8f414d8d8e2fafd4bad9d750de4d9d804df177e9872ab19-image.png)