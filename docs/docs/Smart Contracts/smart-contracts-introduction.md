---
title: Introduction
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
# Smart Contract

A "smart contract" is an application program that runs on the TRON network. It's a collection of code (its functions) and data (its state) that resides at a specific account address on the TRON network. Smart contracts are a type of TRON account. This means they have a balance and they can send transactions over the network. However, they're not controlled by a user, instead they are deployed to the network and run as programmed. User accounts can then interact with a smart contract by submitting transactions that execute a function defined in the smart contract, but interactions with them are irreversible.

Perhaps the best metaphor for a smart contract is a vending machine. With the right inputs, a certain output is guaranteed. For a vending machine, this logic is programmed: `money + snack selection = snack dispensed`, then the user can get a snack from a vending machine.

A smart contract, like a vending machine, also has logic programmed into it. Here's a simple example of smart contract - vending machine:

```solidity=
pragma solidity 0.8.7;

contract VendingMachine {

    // Declare state variables of the contract
    address public owner;
    mapping (address => uint) public cupcakeBalances;

    // When 'VendingMachine' contract is deployed:
    // 1. set the deploying address as the owner of the contract
    // 2. set the deployed smart contract's cupcake balance to 100
    constructor() {
        owner = msg.sender;
        cupcakeBalances[address(this)] = 100;
    }

    // Allow the owner to increase the smart contract's cupcake balance
    function refill(uint amount) public {
        require(msg.sender == owner, "Only the owner can refill.");
        cupcakeBalances[address(this)] += amount;
    }

    // Allow anyone to purchase cupcakes
    function purchase(uint amount) public payable {
        require(msg.value >= amount * 1 trx , "You must pay at least 1 TRX per cupcake");
        require(cupcakeBalances[address(this)] >= amount, "Not enough cupcakes in stock to complete this purchase");
        cupcakeBalances[address(this)] -= amount;
        cupcakeBalances[msg.sender] += amount;
    }
}
```

Like how a vending machine removes the need for a vendor employee, smart contracts can replace intermediaries in many industries.

# Properties of Smart Contracts

Smart contracts in TRON network have the following properties:

* Premissionless\
  Anyone can write a smart contract and deploy it to the TRON network. You just need to learn how to code in a smart contract language, and have enough TRX to deploy your contract. Deploying a smart contract is technically a transaction, so you need to pay your resource fee in the same way that you need to pay for a simple TRX transfer. However, resources consumed for contract deployment are far higher.

  TRON has a developer-friendly language for writing smart contracts: Solidity. However, a contract must be compiled before it can be deployed, so that the TRON Virtual Machine (TVM) can interpret and store the contract.

* Composability\
  Smart contracts are public on the TRON network and can be thought of as open APIs. That means you can call other smart contracts in your own smart contract to greatly extend what's possible. Contracts can even deploy other contracts. You don't need to write your own smart contract to become a DApp developer, you just need to know how to interact with them. For example, you can use the existing smart contracts of SunSwap, a decentralized exchange, to handle all the token swap logic in your app – you don't need to start from scratch.

# Limitations of Smart Contracts

The TRON network smart contracts have the following limitations:

* Unable to communicate with external systems\
  Smart contracts cannot communicate directly with external systems, so smart contracts themselves cannot get information about "real-world" events, and this bottleneck limits smart contract application scenarios, but this is by design. Relying on external information could jeopardise consensus, which is important for security and decentralization. The oracle can be used to solve this problem.
* Maximum execution time of smart contracts\
  In order to ensure the high throughput and stable operation of the network, TRON sets the maximum execution time of the TVM to 80ms to ensure that the TRON network can generate a new block every 3s. So the maximum execution time allowed for smart contracts is 80ms. The maximum execution time of the TVM is the `#13` dynamic parameter of the TRON network, and the Super Representative (SR) committee can modify this parameter by initiating proposals.

   For complex smart contracts, the execution may time out and trigger an `OUT_OF_TIME` error, and the caller will be deducted the full fee\_limit fee. So, to avoid smart contracts executing overtime, try to split large contracts into smaller ones and reference each other as needed, and be aware of common pitfalls and recursive calls to avoid infinite loops.
