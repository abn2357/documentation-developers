---
title: Deployment and Invocation
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
## Smart Contract Deployment

Deploying a smart contract is to create a `CreateSmartContract` transaction, which can be created through the Fullnode API [`wallet/deploycontract`](https://developers.tron.network/reference/wallet-deploycontract). After the transaction is created, it needs to be signed, and then broadcasted:

```curl
curl --request POST \
     --url https://api.shasta.trongrid.io/wallet/deploycontract \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data '
{
     "owner_address": "41D1E7A6BC354106CB410E65FF8B181C600FF14292",
     "abi": "[{\"constant\":false,\"inputs\":[{\"name\":\"key\",\"type\":\"uint256\"},{\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"set\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"key\",\"type\":\"uint256\"}],\"name\":\"get\",\"outputs\":[{\"name\":\"value\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]",
     "bytecode": "608060405234801561001057600080fd5b5060de8061001f6000396000f30060806040526004361060485763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416631ab06ee58114604d5780639507d39a146067575b600080fd5b348015605857600080fd5b506065600435602435608e565b005b348015607257600080fd5b50607c60043560a0565b60408051918252519081900360200190f35b60009182526020829052604090912055565b600090815260208190526040902054905600a165627a7a72305820fdfe832221d60dd582b4526afa20518b98c2e1cb0054653053a844cf265b25040029",
     "fee_limit": 1000000,
     "origin_energy_limit": 100000,
     "name": "SomeContract",
     "call_value": 0,
     "consume_user_resource_percent": 100
}
'
```

Result:

```json
{
  "visible": false,
  "txID": "e4eb4df3a64a33565059ee3cef29b93b79f58ece9e7e8153fda3bbfe40fb0524",
  "contract_address": "416c5d359d1836085cdad65788e1ce53d3d7a13dd6",
  "raw_data": {
    "contract": [
      {
        "parameter": {
          "value": {
            "owner_address": "41d1e7a6bc354106cb410e65ff8b181c600ff14292",
            "new_contract": {
              "bytecode": "608060405234801561001057600080fd5b5060de8061001f6000396000f30060806040526004361060485763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416631ab06ee58114604d5780639507d39a146067575b600080fd5b348015605857600080fd5b506065600435602435608e565b005b348015607257600080fd5b50607c60043560a0565b60408051918252519081900360200190f35b60009182526020829052604090912055565b600090815260208190526040902054905600a165627a7a72305820fdfe832221d60dd582b4526afa20518b98c2e1cb0054653053a844cf265b25040029",
              "consume_user_resource_percent": 100,
              "name": "SomeContract",
              "origin_address": "41d1e7a6bc354106cb410e65ff8b181c600ff14292",
              "abi": {
                "entrys": [
                  {
                    "inputs": [
                      {
                        "name": "key",
                        "type": "uint256"
                      },
                      {
                        "name": "value",
                        "type": "uint256"
                      }
                    ],
                    "name": "set",
                    "stateMutability": "Nonpayable",
                    "type": "Function"
                  },
                  {
                    "outputs": [
                      {
                        "name": "value",
                        "type": "uint256"
                      }
                    ],
                    "constant": true,
                    "inputs": [
                      {
                        "name": "key",
                        "type": "uint256"
                      }
                    ],
                    "name": "get",
                    "stateMutability": "View",
                    "type": "Function"
                  }
                ]
              },
              "origin_energy_limit": 100000
            }
          },
          "type_url": "type.googleapis.com/protocol.CreateSmartContract"
        },
        "type": "CreateSmartContract"
      }
    ],
    "ref_block_bytes": "0a49",
    "ref_block_hash": "975853d6629c8702",
    "expiration": 1652153760000,
    "fee_limit": 1000000,
    "timestamp": 1652153701556
  },
  "raw_data_hex": "0a020a492208975853d6629c87024080f2a6e08a305add03081e12d8030a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e437265617465536d617274436f6e747261637412a3030a1541d1e7a6bc354106cb410e65ff8b181c600ff142921289030a1541d1e7a6bc354106cb410e65ff8b181c600ff142921a5c0a2b1a03736574220e12036b65791a0775696e743235362210120576616c75651a0775696e74323536300240030a2d10011a03676574220e12036b65791a0775696e743235362a10120576616c75651a0775696e743235363002400222fd01608060405234801561001057600080fd5b5060de8061001f6000396000f30060806040526004361060485763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416631ab06ee58114604d5780639507d39a146067575b600080fd5b348015605857600080fd5b506065600435602435608e565b005b348015607257600080fd5b50607c60043560a0565b60408051918252519081900360200190f35b60009182526020829052604090912055565b600090815260208190526040902054905600a165627a7a72305820fdfe832221d60dd582b4526afa20518b98c2e1cb0054653053a844cf265b2504002930643a0c536f6d65436f6e747261637440a08d0670b4a9a3e08a309001c0843d"
}
```

The [transaction structure](https://developers.tron.network/docs/tron-protocol-transaction) of different transaction types are actually the same, but the content contained in `raw_data` is different, which is mainly reflected in the `contract.parameter.value` field of the transaction. 

The `contract.parameter.value` in the contract deployment transaction contains the following content:

* `owner_address`: the address of the contract owner, which is the contract deployer's address
* `new_contract`: details of the new smart contract
  * origin\_address: the address of the smart contract owner
  * contract\_address: the address of the smart contract
  * ABI: the ABI of the smart contract
  * bytecode: bytecode of the smart contract
  * call\_value: the amount of TRX sending to the smart contract
  * consume\_user\_resource\_percent: [user Energy payment percentage](#consume_user_resource_percent)
  * name: the name of the smart contract
  * origin\_energy\_limit: the contract owner’s Energy consumption limit for each transaction, in sun
* `call_token_value`: the amount of the TRC-10 token sending to the new smart contract
* `token_id`: the ID of the TRC-10 token

## Smart Contract Invocation & Query

#### triggersmartcontract

The contract call is to create a `TriggerSmartContract` transaction, which can be created through the Fullnode API [`wallet/triggersmartcontract`](https://developers.tron.network/reference/triggersmartcontract). After the transaction is created, it needs to be signed, and then broadcasted to the entire network.

```curl

curl -X POST https://api.shasta.trongrid.io/wallet/triggersmartcontract -d '{
"contract_address":"419E62BE7F4F103C36507CB2A753418791B1CDC182",
"function_selector":"transfer(address,uint256)",
"parameter":"00000000000000000000004115208EF33A926919ED270E2FA61367B2DA3753DA0000000000000000000000000000000000000000000000000000000000000032",
"fee_limit":100000000,
"call_value":0,
"owner_address":"41977C20977F412C2A1AA4EF3D49FEE5EC4C31CDFB"
}'
```

Parameter description:

* contract\_address: the contract address.
* owner\_address: the caller address.
* function\_selector: the contract function.
* parameter: the encoded parameter value of the contract method. In this example, there are two parameters that should be passed in, namely address and uint256 type. For more information about how to encode and decode the parameters, please refer to [Parameter Encoding and Decoding](https://developers.tron.network/docs/parameter-encoding-and-decoding).
* fee\_limit: the upper limit of Energy consumption that the caller is willing to undertake for the transaction. For more information, please refer to [Feelimit](#feelimit).
* call\_value: the amount of TRX sending to the smart contract.

After the above command is executed, the following result will be returned, including a contract calling transaction:

```json
{
	"result": {
		"result": true
	},
	"transaction": {
		"visible": false,
		"txID": "d2ce86097df40287ad45ebc67f0d546ee98c2d7cd7c101e4d4d5b0c8a752d900",
		"raw_data": {
			"contract": [{
				"parameter": {
					"value": {
						"data": "a9059cbb00000000000000000000004115208ef33a926919ed270e2fa61367b2da3753da0000000000000000000000000000000000000000000000000000000000000032",
						"owner_address": "41977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb",
						"contract_address": "419e62be7f4f103c36507cb2a753418791b1cdc182"
					},
					"type_url": "type.googleapis.com/protocol.TriggerSmartContract"
				},
				"type": "TriggerSmartContract"
			}],
			"ref_block_bytes": "1c51",
			"ref_block_hash": "74912b480b7b887c",
			"expiration": 1652169501000,
			"fee_limit": 100000000,
			"timestamp": 1652169442098
		},
		"raw_data_hex": "0a021c51220874912b480b7b887c40c8d2e7e78a305aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb1215419e62be7f4f103c36507cb2a753418791b1cdc1822244a9059cbb00000000000000000000004115208ef33a926919ed270e2fa61367b2da3753da000000000000000000000000000000000000000000000000000000000000003270b286e4e78a30900180c2d72f"
	}
}
```

The `contract.parameter.value` in the contract calling transaction contains the following content:

* owner\_address: the caller address.
* contract\_address: the contract address.
* data: the contract function selector and its parameters - the first 4 bytes are the contract function selector, which is the first 4 bytes of the result obtained by performing the Keccak-256 operation on the contract function name and parameters, and is used by the virtual machine to discover the function. The remaining bytes of data are parameters of the function. For more information about encoding and decoding, please refer to [Parameter Encoding and Decoding](https://developers.tron.network/docs/parameter-encoding-and-decoding).
* call\_value: the amount of TRX sending to the smart contract.
* token\_id: the ID of the TRC-10 token sending to the contract.
* call\_token\_value: the amount of the TRC-10 token sending to the smart contract.

#### triggerconstantcontract

Invoke the constant function of the contract through the Fullnode API [`wallet/triggerconstantcontract`](https://developers.tron.network/reference/triggerconstantcontract). Since this is a query operation and does not need to be chained, no signature or broadcasting is required:

```curl
curl -X POST https://127.0.0.1:8090/wallet/triggerconstantcontract -d '{
"contract_address":"419E62BE7F4F103C36507CB2A753418791B1CDC182",
"function_selector":"balanceOf(address)",
"parameter":"000000000000000000000041977C20977F412C2A1AA4EF3D49FEE5EC4C31CDFB",
"owner_address":"41977C20977F412C2A1AA4EF3D49FEE5EC4C31CDFB"
}'

```

Parameter description:

* contract\_address: the contract address.
* owner\_address: the caller address.
* function\_selector: the triggered contract method.
* parameter: the parameters to be passed in the contract method. For more information about encoding and decoding, please refer to the chapter on parameter encoding and decoding.

Result:

```json
{
	"result": {
		"result": true
	},
	"constant_result": ["0000000000000000000000000000000000000000000000000000000430e1b700"],
	"transaction": {
		"ret": [{}],
		"visible": false,
		"txID": "7f47212aed2fdab232195feece54fc302bde2ce379e92ffd0d0e95206ce7a3bb",
		"raw_data": {
			"contract": [{
				"parameter": {
					"value": {
						"data": "70a08231000000000000000000000041977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb",
						"owner_address": "41977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb",
						"contract_address": "419e62be7f4f103c36507cb2a753418791b1cdc182"
					},
					"type_url": "type.googleapis.com/protocol.TriggerSmartContract"
				},
				"type": "TriggerSmartContract"
			}],
			"ref_block_bytes": "5ab1",
			"ref_block_hash": "f24f075df912f43e",
			"expiration": 1590382815000,
			"timestamp": 1590382762536
		},
		"raw_data_hex": "0a025ab12208f24f075df912f43e4098cecfd1a42e5a8e01081f1289010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412540a1541977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb1215419e62be7f4f103c36507cb2a753418791b1cdc182222470a08231000000000000000000000041977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb70a8b4ccd1a42e"
	}
}
```

* `constant_result`: the result of querying the contract. In this example, the return value is of type uint256. For more information about how to encode and decode the return value, please refer to [Parameter Encoding and Decoding](https://developers.tron.network/docs/parameter-encoding-and-decoding).

### Calling with Data

In addition to directly inputting the function selector and parameters, you can also **encode** them into hexadecimal data according to the **ABI specification**. This encoded data is then concatenated and submitted as the `data` field.

Let's look at calling the standard **TRC-20** `transfer` function on a smart contract. Typically, the function signature is `transfer(address,uint256)`.

We want to transfer `100` tokens to the address `TV3nb5HYFe2xBEmyb3ETe93UGkjAhWyzrs`.

* **Function Signature:** `transfer(address,uint256)`
* **Function Selector:** the first 4 bytes of the Keccak-256 hash of `transfer(address,uint256)`. For this specific function, it's typically `a9059cbb`.
* **Parameter Encoding:**
  * The address `TV3nb5HYFe2xBEmyb3ETe93UGkjAhWyzrs` needs to be encoded as a 32-byte hexadecimal value.
  * The `uint256` value `100` needs to be encoded as a 32-byte hexadecimal value.

The final `data` field is simply the concatenation of the function selector and the encoded parameters.

A typical `data` value for calling `transfer(address,uint256)` to send 100 tokens to `TV3nb5HYFe2xBEmyb3ETe93UGkjAhWyzrs` might look like this (keep in mind this is a simplified example; actual encoding follows specific ABI rules):

`a9059cbb00000000000000000000000041a614f89f8a93d7f8824f607c7b2a3c3e0d5e190000000000000000000000000000000000000000000000000000000000000064`

In this example:

* `a9059cbb` is the function selector for `transfer(address,uint256)`.
* `00000000000000000000000041a614f89f8a93d7f8824f607c7b2a3c3e0d5e19` is the encoded value of the recipient address `TV3nb5HYFe2xBEmyb3ETe93UGkjAhWyzrs` (represented in hexadecimal and padded to 32 bytes).
* `0000000000000000000000000000000000000000000000000000000000000064` is the encoded value of `100` (`64` for hexadecimal, padded to 32 bytes).

**Complete Call:**

```curl curl
curl --request POST \
     --url https://api.shasta.trongrid.io/wallet/triggersmartcontract \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "owner_address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
  "contract_address": "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs",
  "data": "a9059cbb00000000000000000000000041a614f89f8a93d7f8824f607c7b2a3c3e0d5e190000000000000000000000000000000000000000000000000000000000000064",
  "fee_limit": 1000000000,
  "call_value": 0,
  "visible": true
}
'
```

**Result:**

```json
{
	"result": {
		"result": true
	},
	"transaction": {
		"visible": true,
		"txID": "e33c025b615a5125c8a28ec7e012a8b880c5d855f010c07dca45cb2d40609b82",
		"raw_data": {
			"contract": [{
				"parameter": {
					"value": {
						"data": "a9059cbb00000000000000000000000041a614f89f8a93d7f8824f607c7b2a3c3e0d5e190000000000000000000000000000000000000000000000000000000000000064",
						"owner_address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
						"contract_address": "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs"
					},
					"type_url": "type.googleapis.com/protocol.TriggerSmartContract"
				},
				"type": "TriggerSmartContract"
			}],
			"ref_block_bytes": "8e6a",
			"ref_block_hash": "9858ac3fec3262ff",
			"expiration": 1747130115000,
			"fee_limit": 1000000000,
			"timestamp": 1747130056923
		},
		"raw_data_hex": "0a028e6a22089858ac3fec3262ff40b8c7c7c8ec325aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541fd49eda0f23ff7ec1d03b52c3a45991c24cd440e12154142a1e39aefa49290f2b3f9ed688d7cecf86cd6e02244a9059cbb00000000000000000000000041a614f89f8a93d7f8824f607c7b2a3c3e0d5e19000000000000000000000000000000000000000000000000000000000000006470db81c4c8ec3290018094ebdc03"
	}
}
```

## consume\_user\_resource\_percent

Contract invocation can cause the resource fee. In order to encourage users to conduct contract transactions and reduce their invocation costs, the TRON network supports contract deployers to share part of the contract invocation fee. During contract deployment, users' Energy payment ratio can be set through the parameter `consume_user_resource_percent`.

The user Energy payment ratio is the proportion of Energy paid by users for smart contract execution. For example, if the user Energy payment ratio is set to 60, a user pays 60% of the Energy required for a contract execution, and the developer (contract deployer) pays the remaining 40% of the total Energy consumed. This parameter can only be an integer between 0 and 100 (0 and 100 included). Developers are advised to appropriately increase the user Energy payment ratio to prevent users from attacking the contract and exhausting the contract owner's account resources.

After the contract is successfully deployed, the user Energy payment ratio can also be modified. For example, the contract owner can modify it through the Fullnode HTTP API [`wallet/updatesetting`](https://developers.tron.network/reference/wallet-updatesetting).

**Note**: Although contract developers may need to share a certain percentage of the Energy cost of contract invocation, when Energy of a developer's account is not enough to pay for the corresponding part, or Energy of the developer's account consumed by the specific invocation exceeds the value of `origin_energy_limit`, the rest part is still borne by the caller. 

For a more detailed explanation of `consume_user_resource_percent`, please refer to [TRON Energy Sharing Mechanism](https://developers.tron.network/docs/energy-consumption-mechanism#tron-energy-sharing-mechanism).

## feelimit

feelimit refers to the upper limit of the Energy cost that a caller is willing to undertake for the deployment or invocation of a smart contract, in sun (1 TRX = 1e6 sun). Currently, the maximum value of this Energy cost limit is 15,000 TRX. If the feelimit is set to greater than 15,000 TRX, an error will occur.

During contract execution, Energy is calculated and deducted step by step according to the instruction execution. If the Energy usage is exceeded, the contract execution will fail and the deducted Energy will not be refunded.

Before deploying a contract to the Mainnet, the best practice is to set a reasonable feelimit. For example, when deploying large contracts or running complex functions, a larger feelimit can be necessary. However, due to issues like contract execution timeout, infinite loops in contracts, illegal operations, and transfers to non-existent accounts, the feelimit should be kept under control and not excessively high.

* For a more detailed introduction to feelimit, please refer to [Feelimit](https://developers.tron.network/docs/feelimit). 
* For instructions on how to set up feelimit for a transaction, please refer to [Feelimit Parameter Setting](https://developers.tron.network/docs/set-feelimit).
