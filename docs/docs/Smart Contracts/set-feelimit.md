---
title: FeeLimit Parameter Setting
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
FeeLimit is a parameter of smart contract transactions, which is used to set the upper limit of the Energy cost that the caller is willing to undertake for the deployment or invocation of A smart contract, in sun (1TRX = 1e6 sun). The default value is 0. Currently, the upper limit of feelimit that can be set is 15000 TRX.

When executing a contract, Energy is calculated and deducted sequentially with each instruction. If the Energy usage is exceeded, the contract execution will fail and the deducted Energy will not be refunded. Therefore, before deploying or calling the contract, it is recommended to set an appropriate `feelimit` to ensure the normal execution of smart contract transactions.

The following content will focus on three key aspects to explain in detail how to evaluate the Energy consumption of contract transactions and how to properly set the FeeLimit parameter:

1. [How to estimate the energy consumption of a smart contract transaction?](/docs/set-feelimit#how-to-estimate-energy-consumption)
2. [How to determine a reasonable FeeLimit based on the estimated value?](/docs/set-feelimit#how-to-determine-the-feelimit-parameter)
3. [How to set the FeeLimit for a transaction?](/docs/set-feelimit#how-to-set-the-feelimit-for-a-transaction)

## How to estimate energy consumption?

Developers can call the [wallet/triggerconstantcontract](https://developers.tron.network/reference/triggerconstantcontract) API to estimate the energy consumption value of a contract invocation or deployment transaction. Let's take an example to illustrate:

### How to estimate the energy consumption of a contract calling transaction?

```
$ curl -X POST  https://nile.trongrid.io/wallet/triggerconstantcontract -d '{
    "owner_address": "TTGhREx2pDSxFX555NWz1YwGpiBVPvQA7e",
    "contract_address": "TVSvjZdyDSNocHm7dP3jvCmMNsCnMTPa5W",
    "function_selector": "transfer(address,uint256)",
    "parameter": "0000000000000000000000002ce5de57373427f799cc0a3dd03b841322514a8c00000000000000000000000000000000000000000000000000038d7ea4c68000",
    "visible": true
}'
```

It returns:

```
{
   ……
   "result": {
       "result": true
   },
   "energy_used": 46236,
   "energy_penalty": 32983,
   ……


}
```

In the return result:

* The `result.result` field being `true` indicates that the estimation was executed successfully. If it is `false`, the estimation failed. Please check whether the request parameters are correctly set to ensure the validity of the contract call.
* `energy_used` represents the total estimated energy consumption for the transaction, where:
  * Base energy consumption = `energy_used` - `energy_penalty`
  * Additional consumption = `energy_penalty`

> Note:
>
> The [triggerconstantcontract](https://developers.tron.network/reference/triggerconstantcontract) API can be used to estimate the energy consumption value of calling most smart contracts on the chain, such as USDD, USDT, USDC, TUSD, etc. Meanwhile, starting from java-tron version 4.7.0.1, a new [wallet/estimateenergy](https://developers.tron.network/reference/estimateenergy) interface has been introduced. The new API will be more accurate in estimating the energy consumption of calling a small number of special contract. But for FullNodes, enabling the `wallet/estimateEnergy` API is optional. So please pay attention that when you call `wallet/estimateEnergy`, if the error message shows that "this node does not support estimate Energy", it is recommended to continue using the `wallet/triggerconstantcontract` API to estimate Energy consumption.

Example:

```
$ curl -X POST  https://nile.trongrid.io/wallet/estimateenergy -d '{
    "owner_address": "TTGhREx2pDSxFX555NWz1YwGpiBVPvQA7e",
    "contract_address": "TVSvjZdyDSNocHm7dP3jvCmMNsCnMTPa5W",
    "function_selector": "transfer(address,uint256)",
    "parameter": "0000000000000000000000002ce5de57373427f799cc0a3dd03b841322514a8c00000000000000000000000000000000000000000000000000038d7ea4c68000",
    "visible": true
}'
```

It returns:

```
{
   "result": {
      "result": true
   },
   "energy_required": 34830
}

```

The `result.result = true` in the example stands for the successful execution of estimating operation. The value of `energy_equired` is the estimated energy consumption of the transaction, covering the basic energy consumption and additional energy consumption.

<br />

### How to estimate the Energy consumption of a contract deployment transaction?

For the contract whose constructor has no parameters, when estimating the energy required for its deployment, you only need to put the contract's bytecode into the `data` field of the `wallet/triggerconstantcontract` interface. However, for the contract whose constructor has parameters, you should also pass in the parameters when deploying. The parameters should also be passed in through the `data` field: the parameters should be ABI-encoded and placed after the contract bytecode. For more details, please refer to the following examples.

* To estimate the energy consumption of deploying a contract whose constructor has no parameters.

Contract example:

```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

contract SimpleContract {
    uint storedData;
    
    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

After compiling the contract, we get the contract bytecode:

```
608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5061015b806100355f395ff3fe608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b506004361061004c575f3560e01c806360fe47b1146100505780636d4ce63c1461006c575b5f80fd5b61006a600480360381019061006591906100d2565b61008a565b005b610074610093565b604051610081919061010c565b60405180910390f35b805f8190555050565b5f8054905090565b5f80fd5b5f819050919050565b6100b18161009f565b81146100bb575f80fd5b50565b5f813590506100cc816100a8565b92915050565b5f602082840312156100e7576100e661009b565b5b5f6100f4848285016100be565b91505092915050565b6101068161009f565b82525050565b5f60208201905061011f5f8301846100fd565b9291505056fea26474726f6e58221220ca11b5749b47f126a08ed4dd6de453cf3e3e1d68c1105af0acdd8a38c18b37ac64736f6c63430008140033
```

Put the contract bytecode into the `data` field of the `wallet/triggerconstantcontract` interface. The command for estimation is:

```
curl --request POST \
 --url https://api.shasta.trongrid.io/wallet/triggerconstantcontract \
 --header 'accept: application/json' \
 --header 'content-type: application/json' \
 --data '
{
  "owner_address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
  "data":"608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5061015b806100355f395ff3fe608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b506004361061004c575f3560e01c806360fe47b1146100505780636d4ce63c1461006c575b5f80fd5b61006a600480360381019061006591906100d2565b61008a565b005b610074610093565b604051610081919061010c565b60405180910390f35b805f8190555050565b5f8054905090565b5f80fd5b5f819050919050565b6100b18161009f565b81146100bb575f80fd5b50565b5f813590506100cc816100a8565b92915050565b5f602082840312156100e7576100e661009b565b5b5f6100f4848285016100be565b91505092915050565b6101068161009f565b82525050565b5f60208201905061011f5f8301846100fd565b9291505056fea26474726f6e58221220ca11b5749b47f126a08ed4dd6de453cf3e3e1d68c1105af0acdd8a38c18b37ac64736f6c63430008140033",
  "visible": true
}'
```

It returns:

```
{
	"result": {
		"result": true
	},
	"energy_used": 69558,
	......
}
```

<br />

* To estimate the energy consumption of deploying a contract whose constructor has parameters

Contract example:

```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

contract SimpleContract {
    uint storedData;
    uint public num;

    constructor(uint _num) {
        num = _num;
    }
    
    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
```

After compiling the contract, we get the contract bytecode:

```
608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5060405161024f38038061024f8339818101604052810190610049919061008d565b80600181905550506100b8565b5f80fd5b5f819050919050565b61006c8161005a565b8114610076575f80fd5b50565b5f8151905061008781610063565b92915050565b5f602082840312156100a2576100a1610056565b5b5f6100af84828501610079565b91505092915050565b61018a806100c55f395ff3fe608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5060043610610057575f3560e01c80634e70b1dc1461005b57806360fe47b1146100795780636d4ce63c14610095575b5f80fd5b6100636100b3565b60405161007091906100e2565b60405180910390f35b610093600480360381019061008e9190610129565b6100b9565b005b61009d6100c2565b6040516100aa91906100e2565b60405180910390f35b60015481565b805f8190555050565b5f8054905090565b5f819050919050565b6100dc816100ca565b82525050565b5f6020820190506100f55f8301846100d3565b92915050565b5f80fd5b610108816100ca565b8114610112575f80fd5b50565b5f81359050610123816100ff565b92915050565b5f6020828403121561013e5761013d6100fb565b5b5f61014b84828501610115565b9150509291505056fea26474726f6e582212205d0adb1a1985b9d6f432a9defc416a17dfe1c931bfb8554978c0f37cfe4cc99f64736f6c63430008140033
```

This contract needs to pass in a uint type parameter when deploying. Assuming that the value 2 is passed in during deployment, it will be ABI-encoded to  `000000000000000000000000000000000000000000000000000000000000000000000002`, which is put after the bytecode to get the `data` field value. The command for estimation is:

```
curl --request POST \
 --url https://api.shasta.trongrid.io/wallet/triggerconstantcontract \
 --header 'accept: application/json' \
 --header 'content-type: application/json' \
 --data '
{
  "owner_address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
  "data":"608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5060405161024f38038061024f8339818101604052810190610049919061008d565b80600181905550506100b8565b5f80fd5b5f819050919050565b61006c8161005a565b8114610076575f80fd5b50565b5f8151905061008781610063565b92915050565b5f602082840312156100a2576100a1610056565b5b5f6100af84828501610079565b91505092915050565b61018a806100c55f395ff3fe608060405234801561000f575f80fd5b50d3801561001b575f80fd5b50d28015610027575f80fd5b5060043610610057575f3560e01c80634e70b1dc1461005b57806360fe47b1146100795780636d4ce63c14610095575b5f80fd5b6100636100b3565b60405161007091906100e2565b60405180910390f35b610093600480360381019061008e9190610129565b6100b9565b005b61009d6100c2565b6040516100aa91906100e2565b60405180910390f35b60015481565b805f8190555050565b5f8054905090565b5f819050919050565b6100dc816100ca565b82525050565b5f6020820190506100f55f8301846100d3565b92915050565b5f80fd5b610108816100ca565b8114610112575f80fd5b50565b5f81359050610123816100ff565b92915050565b5f6020828403121561013e5761013d6100fb565b5b5f61014b84828501610115565b9150509291505056fea26474726f6e582212205d0adb1a1985b9d6f432a9defc416a17dfe1c931bfb8554978c0f37cfe4cc99f64736f6c634300081400330000000000000000000000000000000000000000000000000000000000000002",
  "visible": true
}'
```

It returns:

```
{
	"result": {
		"result": true
	},
	"energy_used": 99278,
	......
}
```

<br />

In the above return value, if the `result.result` field is `true`, it means the estimation operation is executed successfully, and `energy_used` is the estimated value of the energy consumption of the transaction. If the `result.result` field is `false`, it means the estimation failed. Please check whether the transaction data is correct.

<br />

## How to determine the FeeLimit parameter?

Due to the [Dynamic Energy Model](/docs/resource-model#dynamic-energy-model) mechanism, the energy consumption of popular contracts changes dynamically, so calling the same contract function in different time periods may result in different energy consumption. Therefore, in different time periods, transactions that call popular contracts need to set different feelimit parameters.

Here we introduce three ways of setting feelimit:

* Estimate energy before each contract call  
  Before each transaction is sent, the total energy consumption of the transaction can be estimated through the `triggerconstantcontract` API, and the FeeLimit parameter of the transaction can be determined according to the estimated energy consumption:

  ```
  FeeLimit of contract transaction = Estimated total energy consumption * EnergyPrice
  ```

  The advantage of this method is that it allows for the most precise FeeLimit setting, enabling dynamic adjustment based on real-time energy consumption. However, its drawback is the added complexity - an additional estimation call is required before sending each transaction.

* Get the contract `energy_factor` once every maintenance cycle  
  First, determine the basic energy consumption of a contract function through the [triggerconstantcontract](https://developers.tron.network/reference/triggerconstantcontract) API or past historical data of the contract, and then update the `energy_factor` parameter of the contract at each [maintenance cycle](https://developers.tron.network/docs/glossary#maintenance-time-interval):
  ```
  FeeLimit of contract transaction = Estimated basic energy consumption * (1 + energy_factor) * EnergyPrice
  ```
  This method maintains high accuracy while reducing the frequency of calls — it only requires retrieving the contract’s `energy_factor` parameter once per maintenance cycle (approximately every 6 hours). However, it still involves a certain level of operational overhead.

* Set `feelimit` according to `max_factor`  
  First, estimate the basic energy consumption, and then calculate the FeeLimit using the on-chain `max_factor` parameter. The `max_factor` represents the maximum value of the energy penalty coefficient — no matter how frequently a contract is invoked, its energy consumption increase will not exceed this upper limit:

  ```
  FeeLimit of contract transaction = Estimated basic energy consumption *（1 + max_factor）* EnergyPrice
  ```

  The main advantage of this approach is its simplicity — there's no need for frequent on-chain parameter retrieval or dynamic calculations. It is well-suited for scenarios where operational convenience is a priority or where ensuring 100% transaction success is critical. However, since `max_factor` represents the maximum possible energy penalty coefficient and is typically higher than the actual `energy_factor`, the FeeLimit calculated based on it tends to be overly high.

## How to Set FeeLimit for a Transaction?

In the transaction structure, the `fee_limit` field is located within the `raw_data` section. A simplified example of the structure is as follows:

```
{
  "raw_data": {
    ...
    "fee_limit": 10000000000
  },
  "signature": [
    "47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800"
  ]
}

```

After estimating and determining the FeeLimit value for a transaction, there are multiple ways to set the FeeLimit. The method varies depending on how the transaction is created:

### Creating Transactions via the Node HTTP API

If you create a transaction using the `/wallet/triggersmartcontract` or the `/wallet/deploycontract` interface, `fee_limit` is a required parameter. You just need to set it to an appropriate value (unit: sun).

### Using TronWeb to Create Transactions

#### Using the send() Method

When calling the send() method, you can set the energy fee limit by passing an options parameter that includes feeLimit. For example, to set the feeLimit to 150 TRX (i.e., 150 × 10⁶ sun):

```
let abi = [...];
let contract = await tronWeb.contract(abi, 'contractAddress');
let result = await contract.function_name(param1, param2, ...).send({
  feeLimit: 150e6,  // 150 TRX
});
```

#### Using the triggerSmartContract() Method

When calling the triggerSmartContract() method, the third parameter is an optional configuration object where you can set feeLimit. For example, to set feeLimit to 150 TRX (i.e., 150 × 10⁶ sun):

```
const functionSelector = 'transfer(address,uint256)';
const parameter = [
  { type: 'address', value: 'ACCOUNT_ADDRESS' },
  { type: 'uint256', value: 100 }
];
const tx = await tronWeb.transactionBuilder.triggerSmartContract(
  'USDT_ADDRESS',
  functionSelector,
  { feeLimit: 150e6 },
  parameter
);
```

### Using Trident to Create Transactions

#### Building Transactions via triggerContract or deployContract

When using `triggerContract` or `deployContract` in Trident to construct smart contract transactions, since the interfaces already include a feeLimit parameter, you only need to pass the desired value directly when calling them.

```
// Transfer tokens
Function trc20Transfer = new Function(
    "transfer",
    Arrays.asList(
        new Address(toAddress),
        new Uint256(BigInteger.valueOf(10).multiply(BigInteger.valueOf(10).pow(6))) // decimals
    ),
    Collections.singletonList(new TypeReference<Bool>() {})
);
String encodedHex = FunctionEncoder.encode(trc20Transfer);

TransactionExtention transactionExtention = client.triggerContract(
    fromAddr,        
    contractAddress, 
    encodedHex,      
    0,               // callValue
    0,               // tokenValue
    null,            // tokenId
    150_000_000L     // feeLimit
);

Transaction signedTxn = client.signTransaction(transactionExtention);
String txid = client.broadcastTransaction(signedTxn);

```

#### Setting feeLimit using TransactionBuilder

If the transaction has already been constructed via Trident, you can also use `TransactionBuilder` to set the feeLimit separately or add other optional parameters such as memo.

```
TransactionBuilder builder = new TransactionBuilder(transaction); // transaction is transactionExtention.getTransaction()
builder.setFeeLimit(100_000_000L);  // set feeLimit
Transaction transaction = builder.build();

```

### Setting FeeLimit via TronBox

When deploying or invoking contracts using TronBox, the feeLimit is typically configured globally in the TronBox configuration file. All contract deployment and invocation transactions share this feeLimit setting by default. However, you can also set it individually per transaction. For detailed configurations, please refer to the [TronBox configuration documentation](https://developers.tron.network/reference/what-is-tronbox).

### Setting FeeLimit via TronIDE

When deploying or invoking smart contracts in [TronIDE](https://developers.tron.network/docs/tron-ide), you can set the transaction’s feeLimit value directly through the `FEE LIMIT` input box in the UI. Simply enter an appropriate value, and it will apply to the current transaction.
