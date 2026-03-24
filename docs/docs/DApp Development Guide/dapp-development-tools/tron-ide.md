---
title: Tron-IDE
excerpt: Online editor of smart contracts
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Overview

[Tron-IDE](https://www.tronide.io/) is an online editor that helps developers develop smart contracts. It has the characteristics of modularity and provides editing, compiling, and deploying smart contracts in the form of plugins.

## What will you learn?

Through this article, you will learn how to compile and deploy contracts to the TRON network through Tron-IDE.

## What will you do?

* Create files on TRON-IDE
* Compile smart contracts
* Deploy smart contracts

## Getting started with Tron-IDE

TRON-IDE is an online IDE focused on developing smart contracts on the TRON network. You can try it [here](https://www.tronide.io/).

### Install TronLink chrome extension

TRON-IDE needs to interact with TRON accounts and nodes through the TronLink wallet. The installation and operation of TronLink are as follows:

* Install [TronLink Chrome Extension](https://www.tronlink.org/)
* Create an account by creating wallet, importing wallet, or linking a hardware wallet
* For testnets, you can obtain test coins through [faucet](https://developers.tron.network/docs/networks)
* Select the corresponding network on the TronLink chrome extension

### Write the HelloWorld contract

To start building the smart contract, click `New File` and name it to HelloWorld.sol:

![](https://files.readme.io/005dd7f40c4358894e4e16364ccc4028833fafe61a72365dcc5d8521667a2c4d-image.png)

<br />

Copy and paste the following code into the newly created HelloWorld.sol file:

```js
// Specifies that the source code is for a version
// of Solidity greater than 0.5.10
pragma solidity ^0.5.10;

// A contract is a collection of functions and data (its state)
// that resides at a specific address on the Ethereum blockchain.
contract HelloWorld {

    // The keyword "public" makes variables accessible from outside a contract
    // and creates a function that other contracts or SDKs can call to access the value
    string public message;

    // A special function only run during the creation of the contract
    constructor(string memory initMessage) public {
        // Takes a string value and stores the value in the memory data storage area,
        // setting `message` to that value
        message = initMessage;
    }

    // A publicly accessible function that takes a string as a parameter
    // and updates `message`
    function update(string memory newMessage) public {
        message = newMessage;
    }
}
```

### Compile the contract

Use the SOLIDITY compiler plugin (Solidity compiler), select the corresponding compiler version, and compile the smart contract. After the compilation is successful, the compilation result information, including the ABI and bytecode will be returned, else, the detailed error information in red will be returned.

Now, we compile the above HelloWorld contract, and for the compiler version, here select 0.5.16:

![](https://files.readme.io/2b064c232365a96e0a6ce50e3d7522b3935ced0bb20346edb94d38655848bba9-image.png)

<br />

### Deploy the contract

After the compilation is successful, using the deployment plugin (DEPLOYMENT) to deploy the compiled HelloWorld contract to the TRON Shasta testnet:

![](https://files.readme.io/870d462b68e4fdd51fbe25e3672aaa12c69d54ac8fea53f5f553608cab723cab-image.png)

<br />

Once TronLink is connected to TRON-IDE, when you click the "Deploy" button on TRON-IDE, TronLink will pop up a signature window for creating a smart contract, then you need to confirm the signature.

![](https://files.readme.io/15a28978b325ff2eafccd5c61b121d0a3a4f99c3b690e85918de89a59f423d7e-image.png)

<br />

After the deployment is successful, the transaction information will be returned on the terminal of TRON-IDE.

![](https://files.readme.io/71a35472de3ecacb4f8e9f47311ac1a0851c57c1c028bad5e996a95e5b56845d-image.png)

So far, you have successfully deployed the HelloWorld contract. Now you can check the deployment status on the [Shasta testnet browser](https://shasta.tronscan.org/#/address/TCPjoPsRm52kBLUYbjrVnwAN57Rj7D6TUo) according to the contract address and interact with the deployed contract.
