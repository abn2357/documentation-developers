---
title: TRC-20 Contract Interaction
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
In this article, we use [the USDT contract on the Shasta testnet](https://shasta.tronscan.org/#/token20/TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs/code)  as an example to demonstrate how to interact with its TRC-20 interface via the Node HTTP API, TronWeb, and Wallet-CLI, respectively.

# name

Call the name function to get the name of the token.

#### HTTP API

```curl curl
// Node HTTP API: /wallet/triggerconstantcontract
// Description: Trigger the constant of the smart contract, the transaction is off the blockchain

curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"name()",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.

        let result = await instance.name().call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs name() # false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description:**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.

# symbol

Call the symbol function to get the symbol of the token.

#### HTTP API

```curl curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"symbol()",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.

        let result = await instance.symbol().call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs symbol() # false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.

# decimals

Call the decimals function to get the precision of the token.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"decimals()",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.

        let result = await instance.decimals().call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs decimals() # false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.

# totalSupply

Call the totalSupply function to get the total supply of the token.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"totalSupply()",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.

        let result = await instance.totalSupply().call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs totalSupply() # false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.

# balanceOf

Call the balanceOf function to get the token balance of the specified account.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"balanceOf(address)",
"parameter":"000000000000000000000041977C20977F412C2A1AA4EF3D49FEE5EC4C31CDFB",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try 
    {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
			let address = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR";
     	let result = await instance.balanceOf(address).call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs balanceOf(address) "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR" false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.

# transfer

Call the transfer function for token transfer.

#### HTTP API

```curl
// Node HTTP API: /wallet/triggersmartcontract
// Description: Trigger smart contract

curl -X POST  https://api.shasta.trongrid.io/wallet/triggersmartcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"transfer(address,uint256)",
"parameter":"00000000000000000000004115208EF33A926919ED270E2FA61367B2DA3753DA0000000000000000000000000000000000000000000000000000000000000032",
"fee_limit":100000000,
"call_value":0,
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

'parameter' is the encoded value of `address` and `uint256` in `transfer (address,uint256)`. For more information, please refer to [the parameter encoding and decoding document](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding).\
Note: After calling this HTTP API, you also need to call the signing and broadcasting APIs.

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi.
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modify or change values on the blockchain.
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
        let result = await instance.transfer(
                    "TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh", // to address
                    1000000   // amount
                ).send({
                              feeLimit:100_000_000,
                              callValue:0,
                              shouldPollResponse:true
                          });
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs transfer(address,uint256) "TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh",1000000 false 100000000 0 0 #
```

**Usage ：**\
TriggerContract [ownerAddress] [contractAddress] \[method] \[args] [isHex] \[fee\_limit] \[value] \[token\_value] \[token\_id]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.
* fee\_limit: the maximum TRX consumption allowed in this calling. Unit: sun.
* value: the amount of TRX to be transferred to the contract during contract calling. Unit: sun.
* token\_value: the amount of the TRC-10 asset to be transferred to the contract during contract calling.
* token\_id: the ID of the TRC-10 asset to be transferred to the contract during contract calling.

**Transaction Confirmation：**\
After the above steps, check whether the TRC-20 transfer is successful via the getTransactionInfoById API.

# approve

Call the approve function to authorize the use right of a specific amount of tokens to another address.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggersmartcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"approve(address,uint256)",
"parameter":"0000000000000000000000410FB357921DFB0E32CBC9D1B30F09AAD13017F2CD0000000000000000000000000000000000000000000000000000000000000064",
"fee_limit":100000000,
"call_value":0,
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

Note: After calling this HTTP API, you also need to call the signing and broadcasting APIs.

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi
    
    //User A allows user B to use 10USDT of A: A calls approve (B,10)
                 
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modify or change values on the blockchain.
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
        let result = await instance.approve(
                    "TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh", // address _spender
                    10000000   // amount
                ).send({
                              feeLimit:100_000_000,
                              callValue:0,
                              shouldPollResponse:true
                          });
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs  approve(address,uint256) "TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh",10000000 false 100000000 0 0 #
```

**Usage ：**\
TriggerContract [ownerAddress] [contractAddress] \[method] \[args] [isHex] \[fee\_limit] \[value] \[token\_value] \[token\_id]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.
* fee\_limit: the maximum TRX consumption allowed in this calling. Unit: sun.
* value: the amount of TRX to be transferred to the contract during contract calling. Unit: sun.
* token\_value: the amount of the TRC-10 asset to be transferred to the contract during contract calling.
* token\_id: the ID of the TRC-10 asset to be transferred to the contract during contract calling.

**Transaction Confirmation**\
After the above steps, check whether the TRC-20 transfer is successful via the getTransactionInfoById API.

# transferFrom

The authorized address can call the transferFrom function to transfer tokens from the authorizer's account.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggersmartcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"transferFrom(address,address,uint256)",
"parameter":"00000000000000000000004109669733965A37BA3582E70CCC5302F8D254675D0000000000000000000000410FB357921DFB0E32CBC9D1B30F09AAD13017F2CD0000000000000000000000000000000000000000000000000000000000000032",
"fee_limit":100000000,
"call_value":0,
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

Note: After calling this HTTP API, the signing and broadcasting APIs also need to be called.

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi
    
    // Address B transfers 10 USDT from address A to C: B calls transferFrom (A, C, 10)
                 
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modify or change values on the blockchain.
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
        let result = await instance.transferFrom(
                    "TApuyuazZnGgxvbNbaGcrUijEFn1oidsAH", //address _from
                    "TBQDyqoJ2ZJHTRDsrGQasyqBm4nUVLbWee", //address _to
                    10000000   // amount
                ).send({
                              feeLimit:100_000_000,
                              callValue:0,
                              shouldPollResponse:true
                          });
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs  transferFrom(address,address,uint256) "TApuyuazZnGgxvbNbaGcrUijEFn1oidsAH","TBQDyqoJ2ZJHTRDsrGQasyqBm4nUVLbWee",10000000, false 100000000 0 0 #
```

**Usage ：**\
TriggerContract [ownerAddress] [contractAddress] \[method] \[args] [isHex] \[fee\_limit] \[value] \[token\_value] \[token\_id]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.
* fee\_limit: the maximum TRX consumption allowed in this calling. Unit: sun.
* value: the amount of TRX to be transferred to the contract during contract calling. Unit: sun.
* token\_value: the amount of the TRC-10 asset to be transferred to the contract during contract calling.
* token\_id: the ID of the TRC-10 asset to be transferred to the contract during contract calling.

**Transaction Confirmation**\
After the above steps, check whether the TRC-20 transfer is successful via the getTransactionInfoById API.

# allowance

The authorized address can call the allowance function to query its remaining quota from the authorizer's account.

#### HTTP API

```curl
curl -X POST  https://api.shasta.trongrid.io/wallet/triggerconstantcontract -d '{
"contract_address":"TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
"function_selector":"allowance(address,address)",
"parameter":"00000000000000000000004109669733965A37BA3582E70CCC5302F8D254675D000000000000000000000041A245B99ECB47B18C6A90ED1D51100C5A9F0641A7",
"owner_address":"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n",
"visible":true
}'
```

#### TronWeb

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.shasta.trongrid.io',
  headers: { 'TRON-PRO-API-KEY': 'your trongrid api key' },
  privateKey: 'your private key'
});

async function triggerSmartContract() {
    const trc20ContractAddress = "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs";//contract address
    const abi = [...]; // Please replace it with the token's abi
    
    //Query the USDT balance that Account A can use for Account B: Account B calls allowance (A, B)
                 
    try {
        let instance = await tronWeb.contract(abi, trc20ContractAddress);
        // Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let result = await instance.allowance(
                    "TApuyuazZnGgxvbNbaGcrUijEFn1oidsAH", //address _owner
                    "TBQDyqoJ2ZJHTRDsrGQasyqBm4nUVLbWee", //address _spender
                ).call();
        console.log('result: ', result);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
```

#### Wallet-CLI

```shell wallet-cli command
TriggerConstantContract TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs allowance(address,address) "TApuyuazZnGgxvbNbaGcrUijEFn1oidsAH","TBQDyqoJ2ZJHTRDsrGQasyqBm4nUVLbWee" false
```

**Usage :** TriggerConstantContract [ownerAddress] [contractAddress] \[method] \[args] [isHex]\
**Parameter Description：**

* ownerAddress: the caller address.
* contractAdress: the TRC-20 contract address.
* method: the contract function.
* args: the function parameters. If there is no parameter, use # as the placeholder.
* isHex: specifies whether the address of the command parameter is in the hex format.
