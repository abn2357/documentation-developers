---
title: Programming Language
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
TRON supports Solidity, a developer-friendly smart contract development language, which has the following features:

* Object-oriented, high-level language
* Statically typed
* Supports inheritance, libraries and complex user-defined types.

# Composition of a Smart Contract

A smart contract consists of data and functions.

## Data

Any contract data must be assigned to a location: either to storage or memory. It is costly to modify storage in a smart contract, so you need to consider where your data should live wisely.

### Storage

Persistent data is referred to as storage and is represented by state variables. These values get stored permanently on the blockchain. You need to declare the type so that the contract can keep track of how much storage on the blockchain it needs during compilation.

```solidity
contract SimpleStorage {
    uint storedData; // State variable
    // ...
}
```

Types of variables include: address, boolean, integer, fixed point numbers, fixed-size byte arrays, dynamically-sized byte arrays, rational and integer literals, string literals, hexadecimal literals, and enums.

`address`：In order to be compatible with Ethereum, the data of `address` in Solidity is the value obtained by performing the following operations on the hex-format address of the TRON network account:

1. Remove the prefix `41` from the TRON hex address.
2. Perform [Mixed-case checksum](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md) on the result obtained in the previous step.\
   `Mixed-case checksum` : According to a certain logic, some letters in the address are capitalized, together with the remaining lowercase letters to form a checksum, so that the address has the ability of self-check. On average, there will be 15 check bits per address, and the net probability that a randomly generated address if mistyped will accidentally pass a check is 0.0247%.

For example, for the TRON network account `TA9h822trLafTtsGXQc4g4ehPvyNzkQNsS`, the hex address is: `4101fba20cb405734c6b2e704b9ed67c0b5ea74d9e` , and the value in Solidity is:

```solidity
address newAddress = 0x01fbA20CB405734C6B2e704B9eD67C0b5ea74D9E
```

### Memory

Values that are only stored for the lifetime of a contract function's execution are called memory variables. Since these are not stored permanently on the blockchain, they are much cheaper to use.

### Environment variables

In addition to the variables you defined in your contract, there are some special global variables. They are primarily used to provide information about the blockchain or the current transaction. 

Examples:

| Environment Variable | Type    | Description                                                             |
| -------------------- | ------- | ----------------------------------------------------------------------- |
| block.timestamp      | uint256 | The timestamp of the current block in seconds                           |
| block.number         | uint    | The current block number                                                |
| block.coinbase       | address | The Super Representative's node address that produces the current block |
| msg.sender           | address | The message sender (current smart contract caller)                      |
| msg.value            | uint    | The amount of SUN sent with the message                                 |
| msg.data             | bytes   | Complete call data                                                      |
| msg.sig              | bytes4  | The first 4 bytes of call data (function identifier)                    |
| now                  | uint    | The current block timestamp (block.timestamp)                           |

## Functions

There are two types of function calls:

* `internal` -  these don't create an TVM call
  * Internal functions and state variables can only be accessed internally (i.e., from within the current contract or contracts deriving from it)
* `external` -  these do create an TVM call 
  * External functions are part of the contract interface, which means they can be called from other contracts and via transactions. An external function f cannot be called internally (i.e., for internal calls, f() does not work, but this.f() works).

Functions can also be public or private:

* `public` - public functions can be called internally from within the contract or externally via messages.
* `private` - private functions are only visible for the contract they are defined in and not in derived contracts.

Here is a function for updating a state variable in a contract. The parameter value of the type string is passed into the function: update\_name, which is declared public, meaning anyone can access it. Since the function is not declared view, it can be used to modify the contract state.

```solidity
function update_name(string value) public {
    dapp_name = value;
}
```

### View functions

`view` functions promise not to modify the state of the contract's data, such as query operations. Here is an example of a function that queries account balance:

```solidity
function balanceOf(address _owner) public view returns (uint256 _balance) {
    return ownerPizzaCount[_owner];
}
```

What is considered modifying state:

1. Writing to state variables
2. Emitting events
3. Creating other contracts
4. Using selfdestruct
5. Sending TRX via calls
6. Calling any function not marked as `view` or `pure`
7. Using low-level calls
8. Using inline assembly that contains certain opcodes

### Constructor functions

constructor functions are only executed once when the contract is first deployed. Like constructor in many class-based programming languages, these functions often initialize state variables to their specified values.

```solidity
// Initializes the contract's data, setting the `owner`
// to the address of the contract creator.
constructor() public {
    // All smart contracts rely on external transactions to trigger its functions.
    // `msg` is a global variable that includes relevant data on the given transaction,
    // such as the address of the sender and the trx value included in the transaction.
    owner = msg.sender;
}
```

### Built-in functions

In addition to the variables and functions you define in your contract, there are some special built-in functions. For example, `address.send()`, it allows the contract to send TRX to other accounts.

## Writing Functions

Your function needs:

* parameter variable and type (if it accepts parameters)
* declaration of `public` or `private`
* declaration of `pure` or `view` or `payable`
* returns type (if it returns a value)

A complete contract might look something like this. Here, the constructor function provides an initial value for the dapp\_name variable.

```solidity
pragma solidity >=0.4.0 <=0.6.0;

contract ExampleDapp {
    string dapp_name; // state variable

    // Called when the contract is deployed and initializes the value
    constructor() public {
        dapp_name = "My Example dapp";
    }

    // Get Function
    function read_name() public view returns(string) {
        return dapp_name;
    }

    // Set Function
    function update_name(string value) public {
        dapp_name = value;
    }
}
```

## Events and Logs

Events allow us to easily query "things" that happened when a contract transaction was executed. Logs are used to "write" data to data structures outside smart contracts. Log information cannot be accessed by smart contracts, but can provide information about transactions and what happened in blocks. When a contract transaction is successfully executed, the smart contract can emit events and write logs to the blockchain.

# Smart Contract Library

You don't need to write every smart contract in your project from scratch. There are many open-source smart contract libraries available that provide reusable building blocks for your project that can save you from having to reinvent the wheel.

## What's in a Library

You can usually find two kinds of building blocks in smart contract libraries: reusable behaviors you can add to your contracts, and implementations of various standards.

### Behaviors

When writing smart contracts, there is a good chance you'll find yourself writing similar patterns over and over, like assigning an admin address to carry out protected operations in a contract. Smart contract libraries usually provide reusable implementations of these behaviors as libraries or via inheritance in Solidity.

As an example, following is a simplified version of the Ownable contract from the OpenZeppelin Contracts library, which designates an address as the owner of a contract, and provides a modifier for restricting access to a method only to that owner.

```solidity
contract Ownable {
    address public owner;

    constructor() internal {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "Ownable: caller is not the owner");
        _;
    }
}

```

To use a building block like this in your contract, you would need to first import it, and then extend from it in your own contracts. This will allow you to use the modifier provided by the base Ownable contract to secure your own functions.

```solidity=
import ".../Ownable.sol"; // Path to the imported library

contract MyContract is Ownable {
    // The following function can only be called by the owner
    function secured() onlyOwner public {
        msg.sender.transfer(1 ether);
    }
}

```

Another popular example is [SafeMath](https://docs.openzeppelin.com/contracts/3.x/utilities#math). This library provides arithmetic functions with overflow checks, which are not provided by the language. It's a good practice to use it instead of native arithmetic operations to guard your contract against overflows, which can have disastrous consequences!

### Standards

The TRON community has defined several standards in the form of TRCs: TRC-10, TRC-20, TRC-721 and so on. When including a TRC standard as part of your contracts, it's a good idea to look for standard implementations rather than trying to roll out your own. 

## How to Add a Library

Always refer to the documentation of the library you are including for specific instructions on how to include it in your project. Several Solidity contract libraries are packaged using npm, so you can just npm install them. When including a library, always keep an eye on the language version. For instance, you cannot use a library for Solidity 0.6 if you are writing your contracts in Solidity 0.5.

## When to Use a Library

Using a smart contract library for your project has several benefits. First and foremost, it saves you time by providing you with ready-to-use building blocks for you to include in your system, rather than having to code them yourself. Security is also a major plus. Open-source smart contract libraries are also often heavily scrutinized. Given many projects depend on them, there is a strong incentive by the community to keep them under constant review. It's much more common to find errors in application code than in reusable contract libraries. Some libraries also undergo external audits for additional security.

However, using smart contract libraries also carry the risk of including code you are not familiar with into your project. Without a good understanding of what that contract does, you may be inadvertently introducing an issue in your system due to an unexpected behavior. Always make sure to read the documentation of the code you are importing, and then review the code itself before making it a part of your project!

Last, when deciding on whether to include a library, consider its overall usage. A widely-adopted one has the benefits of having a larger community and more eyes looking into it for issues. Security should be your primary focus when building with smart contracts!
