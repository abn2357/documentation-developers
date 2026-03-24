---
title: Interacting with Smart Contracts
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Trident provides methods to interact with deployed smart contracts. There are two types of contract interactions:

## View Functions (Constant Call)

View functions (functions have the modifiers of `view` or `pure` in Solidity) read data from the blockchain without modifying state. These calls are free and don't require transaction signing:

```java
// Call view function (e.g., balanceOf)
Function balanceOfFunction = new Function(
        "balanceOf",
        Collections.singletonList(new Address(accountAddr)),
        Collections.singletonList(new TypeReference<Uint256>() {})
);

String encodedHex = FunctionEncoder.encode(balanceOfFunction);

TransactionExtention txn = client.triggerConstantContract(
        ownerAddress,    // Caller address
        contractAddress, // Contract address
        encodedHex      // Encoded function call
);

// Decode the result
String result = Numeric.toHexString(txnExt.getConstantResult(0).toByteArray());
BigInteger balance = (BigInteger) FunctionReturnDecoder.decode(
        result, 
        balanceOfFunction.getOutputParameters()
).get(0).getValue();
```

## State-Modifying Functions

Functions that modify contract state require a transaction and consume resources:

```java
// Transfer tokens
Function trc20Transfer = new Function(
        "transfer",
        Arrays.asList(
                new Address(toAddress),
                new Uint256(BigInteger.valueOf(10).multiply(BigInteger.valueOf(10).pow(6))) //decimals
        ),
        Collections.singletonList(new TypeReference<Bool>() {})
);
String encodedHex = FunctionEncoder.encode(trc20Transfer);

TransactionExtention transactionExtention = client.triggerContract(
        fromAddr,        // Sender Address
        contractAddress, // Contract Address
        encodedHex,      // Encoded function call
        0,              // call value
        0,              // token value
        null,           // token id
        150_000_000L    // fee Limit
);

// Sign and broadcast
Transaction signedTxn = client.signTransaction(transactionExtention);
String txid = client.broadcastTransaction(signedTxn);
```

### Error Handling

Check the transaction status after execution:

```java
// Check if the constant call was successful
if (!txn.getResult().getResult()) {
    String message = txn.getResult().getMessage().toStringUtf8();
    throw new RuntimeException("Contract call failed: " + message);
}

// For state-modifying functions, you can get the transaction receipt
TransactionInfo info = client.getTransactionInfoById(txid);
if (info.getResult() != SUCCESS) {
    throw new RuntimeException("Transaction failed: " + info.getResMessage().toStringUtf8());
}
```

<br />

<br />

<br />

## Calling Constant Methods

Constant methods are those that read a value in a smart contract and do not alter the state of the smart contract. In Solidity, methods have the modifiers of `view` or `pure` are constant methods.

To call a method in trident-java, first to construct one:

```java
Function name = new Function("name",
                Collections.emptyList(), Arrays.asList(new TypeReference<Utf8String>() {}));
//method name, input params, output params
```

Then, call the method via `ApiWrapper.constantCall`:

```java
TransactionExtention extension = wrapper.constantCall("caller address", "contract address", name);
```

Finally, decode the `constant result` to human-readable text:

```java
String result = Numeric.toHexString(txnExt.getConstantResult(0).toByteArray());

(String)FunctionReturnDecoder.decode(result, name.getOutputParameters()).get(0).getValue();
```

For USDT, the result should be:

```shell
> Tether USD
```

> 📘 Constant Calls
>
> Constant calls are not resource consumption transactions.

## Trigger Calls

Trigger calls change the state (compare with constant calls). The first half of trigger calls are the same as constant calls, and signature and broadcast are required. For example:

```java
Function transfer = new Function("transfer",
                Arrays.asList(new Address(destAddr),
                        new Uint256(BigInteger.valueOf(amount).multiply(BigInteger.valueOf(10).pow(decimals)))),
                Arrays.asList(new TypeReference<Bool>() {}));
```

Call this method via `ApiWrapper.triggerCall`:

```java
TransactionBuilder builder = wrapper.triggerCall("caller address", "contract address", transfer);
```

Rest steps are the same as normal transactions. Refer to Sending Transactions.

> 📘 Fee Limit Setting
>
> Trigger calls require the setting of `feeLimit`, refer to [Resource Model](https://developers.tron.network/docs/resource-model).
