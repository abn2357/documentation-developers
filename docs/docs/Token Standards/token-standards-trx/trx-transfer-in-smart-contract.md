---
title: Transferring TRX in Smart Contracts
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
In a smart contract, you can transfer TRX stored in the contract to another address by calling Solidity’s built-in address member functions.

In Solidity, there are three primary methods for initiating TRX transfers from a contract: `transfer()`, `send()`, and `call()`.

* For simple TRX transfers, the safest method, `transfer()`, is recommended.
* For detailed technical explanations and differences between these methods, please refer to the [Solidity Official Documentation](https://docs.soliditylang.org/en/v0.8.30/types.html#members-of-addresses).

This section uses the `transfer()` method as an example.

```solidity
pragma solidity ^0.8.0;

contract SimpleTransfer {

    receive() external payable {}
    fallback() external payable {}

    event TRXTransferred(address indexed recipient, uint amount);

    // Function: Safely transfer a specified amount of TRX to a given address
    function safeTransferTRX(address payable _recipient, uint _amount) external payable {
        // Ensure the transfer amount is greater than 0
        require(_amount > 0, "Amount must be greater than zero.");
        
        // Ensure the contract has sufficient TRX balance
        require(address(this).balance >= _amount, "Insufficient TRX balance in contract.");

        // Perform the transfer using transfer()
        // If the transfer fails (e.g., the target contract rejects), the transaction will automatically revert
        _recipient.transfer(_amount); 

        // Emit an event for the transfer
        emit TRXTransferred(_recipient, _amount);
    }

    // Function: Get the current TRX balance of the contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
```
