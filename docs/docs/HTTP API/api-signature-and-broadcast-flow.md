---
title: API Signature and Broadcast Flow
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
# Introduction

The TRON network has a variety of API calls to allow users to interact with the blockchain. These API calls can be found in the <a href="https://developers.tron.network/reference/signature-validation" target="_blank">API reference page</a>, which lists API calls from Full Node, Solidity Node, and TronWeb. While some of the API calls serve as stand-alone requests to get individual pieces of information, there are also many API calls which modify the user TRX wallet, resulting in a need to sign and broadcast the transaction. This guide walks the user through a TRX Balance staking example to show the API signature and broadcast process flow.  

# Stake Balance Example

### 1. **Create a Transaction**

`/wallet/freezebalancev2` is used to stake a certain amount of TRX of the user's address to obtain bandwidth or energy, as well as voting rights. Calling this API will create a staking TRX transaction. This API has 3 parameters, namely:

* `owner_address` is the account address.
* `frozen_balance` is the amount of TRX staked in denominations of Sun, in integer format.
* `resource` is the type of resource staking for. This can be either `ENERGY` or `BANDWIDTH`, in string format.<br />

![](https://files.readme.io/aac4ba1-image.png)

Below is the sample JSON output. It lists the various attributes associated with the stake balance transaction. This JSON output will be used to sign the transaction. 

```shell
{
    "visible": false,
    "txID": "f947f1283f7b43c111eba662ab5d27b31dc906b77fdb0b3e52ee626335b21108",
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "resource": "ENERGY",
                        "frozen_balance": 1000000,
                        "owner_address": "41e552f6487585c2b58bc2c9bb4492bc1f17132cd0"
                    },
                    "type_url": "type.googleapis.com/protocol.FreezeBalanceV2Contract"
                },
                "type": "FreezeBalanceV2Contract"
            }
        ],
        "ref_block_bytes": "a59c",
        "ref_block_hash": "aef359052c4aa176",
        "expiration": 1681117668000,
        "timestamp": 1681117610802
    },
    "raw_data_hex": "0a02a59c2208aef359052c4aa17640a0c5afd3f6305a59083612550a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e467265657a6542616c616e63655632436f6e7472616374121d0a1541e552f6487585c2b58bc2c9bb4492bc1f17132cd010c0843d180170b286acd3f630"
}
```

### 2. **Sign the Transaction**

A transaction needs to be signed using the sender's private key before sending it. Transaction signature generating process is:

* Calculate the hash of the transaction.
* Sign the transaction hash with the sender's private key.
* Add the generated signature to the transaction instance.

Most SDKs implement the above transaction signature-generating process and encapsulate them into an interface for developers to call. Taking tronweb as an example, users can directly call the sign method to complete the transaction signature.

```shell
const signedTxn = await tronWeb.trx.sign(unsignedTxn, privateKey);
>{  
   "signature":[  
      "8e6582cead9ef92d7731e356b0131dca2dfe18d701bdaecb5591781af5493391127d10b4864cf45a0f56b10ed97af102864cff8205e14c8bf29b0e50d85f681801"
   ],
   "txID":"ddcbaf061eaa2454975ae8faefbeb0b410329ef9e5bb43b64d4065a7d66720c7",
   "raw_data":{  
      "contract":[  
         {  
            "parameter":{  
               "value":{  
                  "resource":"ENERGY",
                  "frozen_duration":3,
                  "frozen_balance":1000000,
                  "owner_address":"41928c9af0651632157ef27a2cf17ca72c575a4d21"
               },
               "type_url":"type.googleapis.com/protocol.FreezeBalanceContract"
            },
            "type":"FreezeBalanceContract"
         }
      ],
      "ref_block_bytes":"ee08",
      "ref_block_hash":"7b2480cc92edd8a2",
      "expiration":1540253364000,
      "timestamp":1540253304828
   }
}
```

### 3. **Broadcast Transaction**

The `/wallet/broadcasttransaction` API call takes in one parameter, which is the JSON output data from signing the transaction. 

![](https://files.readme.io/20e04b4-broadcastTransaction-request.png "broadcastTransaction-request.png")

Below is the sample JSON Output, confirming successful transaction broadcast. 

```shell
{"result": true}
```
