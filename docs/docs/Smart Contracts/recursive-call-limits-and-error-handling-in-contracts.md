---
title: Recursive Call Limits and Error Handling in Contracts
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
# Recursive Call Limits in Contracts

## Defining Recursive Call

In Solidity, "recursive call" refers to a function's execution leading to a subsequent call to itself, or an indirect call to itself through another contract's function. Similar to typical programming languages, recursion can lead to issues such as excessive stack depth and repeated function execution.

Solidity recursion, however, presents unique constraints compared to traditional programming languages:

* The TRON Virtual Machine (TVM) has a call stack depth limit. Each contract call consumes a portion of the call stack depth (with a default limit of 64 layers).
* Each function call consumes nergy. Excessive recursive calls can easily exceed a transaction’s available Energy limit, resulting in transaction failure.
* Each function execution in a contract is completed in the same execution context. Exhaustion of the transaction's Energy during recursion can trigger an `out of energy` exception, thereby causing a revert.

## Avoiding or Limiting Recursion

Since the TVM call stack and Energy are critical resources, the Solidity community generally recommends developers to avoid deep recursion when designing smart contract logic. When recursion is inevitable, developers must ensure:

1. A clearly defined upper limit on recursion depth is in place to prevent infinite or excessive recursion.
2. Energy consumption for each call is reasonably estimated to prevent transaction reverts due to "insufficient Energy".
3. Alternative solutions (such as loop iteration or other state machine designs) are prioritized to minimize direct dependence on extensive recursive logic within the contract.

## Stack Depth Limit

* The TVM currently limits the call stack depth to 64 layers, including both external contract calls and recursive calls to the contract's own functions.
* If this stack depth is exceeded during recursion, the call will fail, resulting in an exception.

During contract design, it’s crucial to evaluate the deepest possible call path. Extensive nested calls may also trigger a `Stack too deep` compilation error (a Solidity compiler-level limitation), though this error is more commonly associated with excessive local or temporary variables, and is not always directly related to function recursion. Nevertheless, it serves to remind developers to decompose the logic, reduce local variables, or manually manage stacking when writing complex functions.

# Solidity Error Handling Mechanisms

Solidity primarily has four error handling methods: `assert`, `require`, `revert`, and Custom Errors (introduced in version 0.8.4+).

## `assert`

`assert` is generally used to verify internal errors that are not expected to occur or critical invariant violations. An `assert` failure consumes all remaining Energy and throws an exception, so it is used exclusively for detecting critical errors or ensuring conditions that should never occur.

```
assert(x == y);
```

* If an assertion fails, this indicates a major defect or inconsistency in the contract logic.
* `assert` failures will trigger the compiler to insert a `Panic(uint256)` error at compilation (Solidity 0.8.0+).

## `require`

`require` is used to validate external inputs and conditions to ensure that specific prerequisites are met. If the `require` check fails, the transaction reverts, consuming only the Energy that has been used until this point. Any remaining Energy is returned to the caller.

```
require(msg.sender == owner, "Not the owner");
```

* Common use cases include access control, input validity verification, etc.
* Upon `require` failure, more specific information can be conveyed via error message strings or custom errors.

## `revert`

The `revert` keyword can directly abort execution and revert state changes at any point during function execution, providing an explanatory string (reason string or custom errors) to aid in debugging and user interaction.

```
if (someCondition) {  
    revert("Condition not met");  
}
```

* Using `revert` typically aborts function execution and reverts state changes.

## Custom Errors

Solidity 0.8.4 and later introduced custom error syntax. Its advantages include:

1. Enhanced efficiency at the ABI encoding level, typically resulting in Energy saving compared to using strings.
2. The capacity to include parameters in custom errors, allowing callers to capture more specific error causes or context.

```
// Declaration error
error Unauthorized(address caller);

contract MyContract {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function doSomething() external {
        if (msg.sender != owner) {
            // Use custom error
            revert Unauthorized(msg.sender);
        }
        // Other logic
    }
}
```

* Upon triggering `revert Unauthorized(msg.sender)`, the TVM will revert the transaction and return any unused Energy.
* Compared to `require`'s string-based error messages, custom errors are more flexible and space efficient. 

# Best Practices and Energy Considerations

## Analyzing Energy Consumption

On TRON, each transaction consumes a specific amount of Energy. Deep recursion or improper error handling can lead to increased Energy consumption. For instance:

* `assert` failures will result in the consumption of all remaining Energy;
* `require` or `revert` failures only consume Energy used until the point of the error, with the remaining Energy returned to the caller;
* Compared to `require` and `revert` with string information, custom errors save more Energy during encoding/decoding.

Therefore, contract development should prioritize minimizing unnecessary call depth and failure paths. It is recommended to thoroughly check business processes and check inputs and conditions at the start of a call to avoid wasting Energy from extensive subsequent computations.

## Checking Core Invariants with Assertions

Use `assert` for conditions that should never be violated theoretically. Failures indicate design flaws or logical errors in the contract.

## Checking Caller Inputs and External Conditions with `require`/`revert` and Custom Errors

* `require` (and `revert`) is primarily used to validate external inputs or prerequisites, such as permissions, balances, and contract states.
* Custom errors can enhance the efficient communication of error reasons.

## Designing Function Structure to Avoid or Reduce Recursion

Implement recursion depth limits and Energy cost estimations where recursive calls may occur. However, in many cases, deep recursion can be replaced by loop iteration or transaction splitting.

## Security Considerations

Recursive calls may also cause reentrancy attack vulnerabilities, although these vulnerabilities are more associated with external contract calls and `call`. However, unexpected callback paths in external calls, or recursive function calls within the contract itself that modify the same state variable, can lead to security issues like state race conditions. It is advisable to integrate security measures like `ReentrancyGuard` or carefully design call sequences and reentrancy.
