---
title: Contract-to-Contract Calls in TRON Solidity
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
This document outlines how to perform contract-to-contract calls using Solidity on the TRON network, supplemented with code examples.

# Understanding Contract-to-Contract Calls

In smart contract development, a contract can call another contract to execute specific functions or retrieve data. This invocation pattern can improve code reusability, implement complex business logic, and enhance system modularity.

In the TRON ecosystem, contract-to-contract calls are executed via defined interfaces or by directly calling the target contract.

# Calling Methods

## Calling via Interface

This method is recommended as it explicitly defines the function signatures of the contract being called, thereby enhancing code readability and security.

Consider a scenario where `ContractA` calls a function of an existing `ContractB`:

### Defining Interface

```sol
// IContractB.sol  
pragma solidity ^0.8.0;

interface IContractB {  
    function increment(uint256 value) external returns (uint256);  
}
```

### Calling Target Contract

```sol
// ContractA.sol  
pragma solidity ^0.8.0;

import "./IContractB.sol";

contract ContractA {  
    address public contractBAddress;
  
		constructor(address _contractBAddress) {
    		contractBAddress = _contractBAddress;
		}

		function callIncrement(uint256 value) public returns (uint256) {
    		IContractB contractB = IContractB(contractBAddress);
   			uint256 newValue = contractB.increment(value);
    		return newValue;
		}
}
```

## Calling Directly via Address

When the specific interface of a contract is unknown, or when dynamic calls are required, the target contract can be called directly using its address.

```sol
pragma solidity ^0.8.0;

contract ContractA {  
    address public contractBAddress;
  
  	constructor(address _contractBAddress) {
    		contractBAddress = _contractBAddress;
		}

		function callIncrement(uint256 value) public returns (uint256) {
    		(bool success, bytes memory result) = contractBAddress.call(
        		abi.encodeWithSignature("increment(uint256)", value)
    		);
    		require(success, "Call failed");
    		return abi.decode(result, (uint256));
		}
} 
```

## Calling via TRX Transfer to a Contract Address

Directly transferring a specific amount of TRX to a contract address triggers the execution of the target contract's `receiver` or `fallback` function.

```sol
pragma solidity ^0.8.0;

contract ContractA {
    address public contractBAddress;

    constructor(address _contractBAddress) {
        contractBAddress = _contractBAddress;
    }

    function directTransfer() external payable {
        payable(contractBAddress).transfer(msg.value);
    }
}
```

# Considerations for Contract-to-Contract Calling

* **Resource (Energy) Consumption Management**: Calling other contracts incurs additional Energy costs. Ensure sufficient Energy has been allocated.
* **Call Depth Limit**: Solidity call depth on the TRON network is restricted. Avoid excessively deep recursive calls to prevent execution failures.
* **Error Handling**: Use `require` or `assert` statements to validate call success and implement appropriate handling for failed calls.

# Example Scenario

Assume `ContractB` implements a basic counter logic:

```sol
// ContractB.sol
pragma solidity ^0.8.0;

contract ContractB {
    uint256 public counter;

    function increment(uint256 value) external returns (uint256) {
        counter += value;
        return counter;
    }
}
```

As shown above, `ContractA` calls` ContractB`’s  `increment` method, thereby performing a cross-contract call for the counter.

## Deployment Procedure

1. Deploy `ContractB` and record its on-chain address.
2. During `ContractA`’s deployment, provide `ContractB`'s address as a constructor parameter.
3. Test the contract-to-contract call by calling the callIncrement method in `ContractA`, which in turn calls the relevant method in `ContractB`.
