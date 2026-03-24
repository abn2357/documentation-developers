---
title: The Usage of the Function of Smart Contract
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
# 1. constant function and inconstant function

There are two types of function according to whether any change will be made to the properties on the chain: constant function and inconstant function. Constant function uses view/pure/constant to decorate, will return the result on the node it is called and not be broadcasted in the form of a transaction. Inconstant function will be broadcasted in the form of a transaction while be called, the function will change the data on the chain, such as transfer, changing the value of the internal variables of contracts, etc.

Note: If you use create command inside a contract (CREATE instruction), even use view/pure/constant to decorate the dynamically created contract function, this function will still be treated as inconstant function, be dealt in the form of transaction.

# 2. message calls

Message calls can call the functions of other contracts, also can transfer TRX to the accounts of contract and none-contract. Like the common TRON triggercontract, Message calls have initiator, recipient, data, transfer amount, fees and return attributes. Every message call can generate a new one recursively. Contract can define the distribution of the remaining energy in the internal message call. If it comes with OutOfEnergyException in the internal message call, it will return false, but not error. In the meanwhile, only the gas sent with the internal message call will be consumed, if energy is not specified in call.value(energy), all the remaining energy will be used.

# 3. delegate call/call code/library

There is a special type of message call, delegate call. The difference with common message call is the code of the target address will be run in the context of the contract that initiates the call, msg.sender and msg.value remain unchanged. This means a contract can dynamically loadcode from another address while running. Storage, current address and balance all point to the contract that initiates the call, only the code is get from the address being called. This gives Solidity the ability to achieve the 'lib' function: the reusable code lib can be put in the storage of a contract to implement complex data structure library.

# 4. CREATE command

This command will create a new contract with a new address. The only difference with Ethereum is the newly generated TRON address used the smart contract creation transaction id and the hash of nonce called combined. Different from Ethereum, the defination of nonce is the comtract sequence number of the creation of the root call. Even there are many CREATE commands calls, contract number in sequence from 1. Refer to the source code for more detail. Note: Different from creating a contract by grpc's deploycontract, contract created by CREATE command does not store contract abi.

# 5. built-in function and built-in function attribute (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)

1）TVM is compatible with solidity language's transfer format, including:

* accompany with constructor to call transfer
* accompany with internal function to call transfer
* use transfer/send/call/callcode/delegatecall to call transfer

2）Different accouts vote for SuperNode (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
3）SuperNode gets all the reward (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
4）SuperNode approves or disappoves the proposal (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
5）SuperNode proposes a proposal (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
6）SuperNode deletes a proposal (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
7）TRON byte address converts to solidity address (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
8）TRON string address converts to solidity address (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
9）Send token to target address (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
10）Query token amount of target address (Since Odyssey-v3.1.1, TVM built-in function is not supported temporarily)\
11）Compatible with all the built-in functions of Ethereum

Note: Ethereum's RIPEMD160 function is not recommended, because the return of TRON is a hash result based on TRON's sha256, not an accurate Ethereum RIPEMD160.
