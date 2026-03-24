---
title: Smart Contract Interaction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Now that you have deployed the Hello World smart contract on the TRON blockchain. You can interact with your contract by calling functions defined in `HelloWorld.sol` in Tron-IDE.

![1314](https://files.readme.io/d1d3b63-QQ20200225112146.png "QQ截图20200225112146.png")

> 📘 Note
>
> Enter the contract address (`TAbsq7DzmrFriHZ5Vk2cK4npCcYPvtWhZ8`) into **"At Address"** to call smart contract functions.

The contract contains two functions: `postMessage` and `getMessage`.

The `postMessage` function is a state-changing one because it changes the message variable within the contract. The calling of this function needs a signature and consumes Energy. The `getMessage` function is a read-only one, because it only returns the message variable (reading the contract, not changing the state) and no signature or resource consumption is needed.

A successful call of `getMessage` returns the _**id**_ and _**contract_result**_ and the transaction receipt. The _**id**_ is the hash of the transaction broadcasted to the blockchain, and the _**contract_result**_ is the output of the function call. The `getMessage` function returns the variable message, which is an empty string in this example. You can make a change by calling `postMessage`.

![1395](https://files.readme.io/6ca0f73-QQ20200225114058.png "QQ截图20200225114058.png")

You have successfully created, compiled, deployed, and interacted with the HelloWorld smart contract on the TRON blockchain.
