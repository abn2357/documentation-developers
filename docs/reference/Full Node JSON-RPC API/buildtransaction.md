---
title: buildTransaction
excerpt: Creates a transaction, different transaction types have different parameters.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## TransferContract

Creates a TransferContract transaction.

**Parameters**

1. `Object` - the items in object as below:

   | Param Name | Data Type        | Description                             |
   | :--------- | :--------------- | :-------------------------------------- |
   | `from`     | `DATA`, 20 Bytes | Sender's address of the transaction.    |
   | `to`       | `DATA`, 20 Bytes | Recipient's address of the transaction. |
   | `value`    | `DATA`           | Amount of TRX to transfer.              |

**Returns**

* `Object` - Transaction of `TransferContract` or an error.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "id": 1337,
    "jsonrpc": "2.0",
    "method": "buildTransaction",
    "params": [
        {
            "from": "0xC4DB2C9DFBCB6AA344793F1DDA7BD656598A06D8",
            "to": "0x95FD23D3D2221CFEF64167938DE5E62074719E54",
            "value": "0x1f4"
        }]}'
```

Response

```json
{"jsonrpc":"2.0","id":1337,"result":{"transaction":{"visible":false,"txID":"ae02a80abd985a6f05478b9bbf04706f00cdbf71e38c77d21ed77e44c634cef9","raw_data":{"contract":[{"parameter":{"value":{"amount":500,"owner_address":"41c4db2c9dfbcb6aa344793f1dda7bd656598a06d8","to_address":"4195fd23d3d2221cfef64167938de5e62074719e54"},"type_url":"type.googleapis.com/protocol.TransferContract"},"type":"TransferContract"}],"ref_block_bytes":"957e","ref_block_hash":"3922d8c0d28b5283","expiration":1684469286000,"timestamp":1684469226841},"raw_data_hex":"0a02957e22083922d8c0d28b528340f088c69183315a66080112620a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412310a1541c4db2c9dfbcb6aa344793f1dda7bd656598a06d812154195fd23d3d2221cfef64167938de5e62074719e5418f40370d9bac2918331"}}}
```

## TransferAssetContract

Creates a TransferAssetContract transaction.

**Parameters**

1. `Object` - Items in object as below:

   | Param Name   | Data Type        | Description                             |
   | :----------- | :--------------- | :-------------------------------------- |
   | `from`       | `DATA`, 20 Bytes | Sender's address of the transaction.    |
   | `to`         | `DATA`, 20 Bytes | Recipient's address of the transaction. |
   | `tokenId`    | `QUANTITY`       | Token ID.                               |
   | `tokenValue` | `QUANTITY`       | Amount of TRC-10 to transfer.           |

**Returns**

* `Object` - transaction of `TransferAssetContract` or an error.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "method": "buildTransaction",
    "params": [
        {
            "from": "0xC4DB2C9DFBCB6AA344793F1DDA7BD656598A06D8",
            "to": "0x95FD23D3D2221CFEF64167938DE5E62074719E54",
            "tokenId": 1000016,
            "tokenValue": 20
        }
    ],
    "id": 44,
    "jsonrpc": "2.0"
}
'
```

Response

```json
{"jsonrpc":"2.0","id":44,"error":{"code":-32600,"message":"assetBalance must be greater than 0.","data":"{}"}}
```

## CreateSmartContract

Creates a CreateSmartContract transaction.

**Parameters**

1. `Object` - Items in object as below:

   | Param Name                   | Data Type        | Description                          |
   | :--------------------------- | :--------------- | :----------------------------------- |
   | `from`                       | `DATA`, 20 Bytes | Sender's address of the transaction. |
   | `name`                       | `DATA`           | Name of the smart contract.          |
   | `gas`                        | `DATA`           | Fee limit.                           |
   | `abi`                        | `DATA`           | ABI of the smart contract.           |
   | `data`                       | `DATA`           | Byte code of the smart contract.     |
   | `consumeUserResourcePercent` | `QUANTITY`       | Consume user resource percent.       |
   | `originEnergyLimit`          | `QUANTITY`       | Origin energy limit.                 |
   | `value`                      | `DATA`           | Data passed through call_value.      |
   | `tokenId`                    | `QUANTITY`       | Token ID.                            |
   | `tokenValue`                 | `QUANTITY`       | Amount of TRC-10 to transfer.        |

**Returns**

* `Object` - Transaction of `CreateSmartContract` or an error.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{
    "id": 1337,
    "jsonrpc": "2.0",
    "method": "buildTransaction",
    "params": [
        {
            "from": "0xC4DB2C9DFBCB6AA344793F1DDA7BD656598A06D8",
            "name": "transferTokenContract",
            "gas": "0x245498",
            "abi": "[{\"constant\":false,\"inputs\":[],\"name\":\"getResultInCon\",\"outputs\":[{\"name\":\"\",\"type\":\"trcToken\"},{\"name\":\"\",\"type\":\"uint256\"},{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"toAddress\",\"type\":\"address\"},{\"name\":\"id\",\"type\":\"trcToken\"},{\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"TransferTokenTo\",\"outputs\":[],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[],\"name\":\"msgTokenValueAndTokenIdTest\",\"outputs\":[{\"name\":\"\",\"type\":\"trcToken\"},{\"name\":\"\",\"type\":\"uint256\"},{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"constructor\"}]\n",
            "data": "6080604052d3600055d2600155346002556101418061001f6000396000f3006080604052600436106100565763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166305c24200811461005b5780633be9ece71461008157806371dc08ce146100aa575b600080fd5b6100636100b2565b60408051938452602084019290925282820152519081900360600190f35b6100a873ffffffffffffffffffffffffffffffffffffffff600435166024356044356100c0565b005b61006361010d565b600054600154600254909192565b60405173ffffffffffffffffffffffffffffffffffffffff84169082156108fc029083908590600081818185878a8ad0945050505050158015610107573d6000803e3d6000fd5b50505050565bd3d2349091925600a165627a7a72305820a2fb39541e90eda9a2f5f9e7905ef98e66e60dd4b38e00b05de418da3154e7570029",
            "consumeUserResourcePercent": 100,
            "originEnergyLimit": 11111111111111,
            "value": "0x1f4",
            "tokenId": 1000033,
            "tokenValue": 100000
        }
    ]
}
'
```

Response

```json
{"jsonrpc":"2.0","id":1337,"result":{"transaction":{"visible":false,"txID":"598d8aafbf9340e92c8f72a38389ce9661b643ff37dd2a609f393336a76025b9","contract_address":"41dfd93697c0a978db343fe7a92333e11eeb2f967d","raw_data":{"contract":[{"parameter":{"value":{"token_id":1000033,"owner_address":"41c4db2c9dfbcb6aa344793f1dda7bd656598a06d8","call_token_value":100000,"new_contract":{"bytecode":"6080604052d3600055d2600155346002556101418061001f6000396000f3006080604052600436106100565763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166305c24200811461005b5780633be9ece71461008157806371dc08ce146100aa575b600080fd5b6100636100b2565b60408051938452602084019290925282820152519081900360600190f35b6100a873ffffffffffffffffffffffffffffffffffffffff600435166024356044356100c0565b005b61006361010d565b600054600154600254909192565b60405173ffffffffffffffffffffffffffffffffffffffff84169082156108fc029083908590600081818185878a8ad0945050505050158015610107573d6000803e3d6000fd5b50505050565bd3d2349091925600a165627a7a72305820a2fb39541e90eda9a2f5f9e7905ef98e66e60dd4b38e00b05de418da3154e7570029","consume_user_resource_percent":100,"name":"transferTokenContract","origin_address":"41c4db2c9dfbcb6aa344793f1dda7bd656598a06d8","abi":{"entrys":[{"outputs":[{"type":"trcToken"},{"type":"uint256"},{"type":"uint256"}],"payable":true,"name":"getResultInCon","stateMutability":"Payable","type":"Function"},{"payable":true,"inputs":[{"name":"toAddress","type":"address"},{"name":"id","type":"trcToken"},{"name":"amount","type":"uint256"}],"name":"TransferTokenTo","stateMutability":"Payable","type":"Function"},{"outputs":[{"type":"trcToken"},{"type":"uint256"},{"type":"uint256"}],"payable":true,"name":"msgTokenValueAndTokenIdTest","stateMutability":"Payable","type":"Function"},{"payable":true,"stateMutability":"Payable","type":"Constructor"}]},"origin_energy_limit":11111111111111,"call_value":500}},"type_url":"type.googleapis.com/protocol.CreateSmartContract"},"type":"CreateSmartContract"}],"ref_block_bytes":"80be","ref_block_hash":"ac7c3d59c55ac92c","expiration":1634030190000,"fee_limit":333333280,"timestamp":1634030131693},"raw_data_hex":"0a0280be2208ac7c3d59c55ac92c40b0fba79ec72f5ad805081e12d3050a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e437265617465536d617274436f6e7472616374129e050a1541c4db2c9dfbcb6aa344793f1dda7bd656598a06d812fc040a1541c4db2c9dfbcb6aa344793f1dda7bd656598a06d81adb010a381a0e676574526573756c74496e436f6e2a0a1a08747263546f6b656e2a091a0775696e743235362a091a0775696e743235363002380140040a501a0f5472616e73666572546f6b656e546f22141209746f416464726573731a0761646472657373220e120269641a08747263546f6b656e22111206616d6f756e741a0775696e743235363002380140040a451a1b6d7367546f6b656e56616c7565416e64546f6b656e4964546573742a0a1a08747263546f6b656e2a091a0775696e743235362a091a0775696e743235363002380140040a0630013801400422e0026080604052d3600055d2600155346002556101418061001f6000396000f3006080604052600436106100565763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166305c24200811461005b5780633be9ece71461008157806371dc08ce146100aa575b600080fd5b6100636100b2565b60408051938452602084019290925282820152519081900360600190f35b6100a873ffffffffffffffffffffffffffffffffffffffff600435166024356044356100c0565b005b61006361010d565b600054600154600254909192565b60405173ffffffffffffffffffffffffffffffffffffffff84169082156108fc029083908590600081818185878a8ad0945050505050158015610107573d6000803e3d6000fd5b50505050565bd3d2349091925600a165627a7a72305820a2fb39541e90eda9a2f5f9e7905ef98e66e60dd4b38e00b05de418da3154e757002928f40330643a157472616e73666572546f6b656e436f6e747261637440c7e3d28eb0c30218a08d0620e1843d70edb3a49ec72f9001a086f99e01"}}}
```

## TriggerSmartContract

Creates a TriggerSmartContract transaction.

**Parameters**

1. `Object` - the items in object as below:

   | Param Name   | Data Type        | Description                               |
   | :----------- | :--------------- | :---------------------------------------- |
   | `from`       | `DATA`, 20 Bytes | Sender's address of the transaction.      |
   | `to`         | `DATA`, 20 Bytes | Recipient's address of the transaction.   |
   | `data`       | `DATA`           | Invoked contract function and parameters. |
   | `gas`        | `DATA`           | Fee limit.                                |
   | `value`      | `DATA`           | Data passed through `call_value`.         |
   | `tokenId`    | `QUANTITY`       | Token ID.                                 |
   | `tokenValue` | `QUANTITY`       | Amount of TRC-10 to transfer.             |

**Returns**

* `Object` - Transaction of `TriggerSmartContract` or an error.

**Example**

Request

```curl
curl -X POST 'https://api.shasta.trongrid.io/jsonrpc' --data '{"id": 1337,
    "jsonrpc": "2.0",
    "method": "buildTransaction",
    "params": [
        {
            "from": "0xC4DB2C9DFBCB6AA344793F1DDA7BD656598A06D8",
            "to": "0xf859b5c93f789f4bcffbe7cc95a71e28e5e6a5bd",
            "data": "0x3be9ece7000000000000000000000000ba8e28bdb6e49fbb3f5cd82a9f5ce8363587f1f600000000000000000000000000000000000000000000000000000000000f42630000000000000000000000000000000000000000000000000000000000000001",
            "gas": "0x245498",
            "value": "0xA",
            "tokenId": 1000035,
            "tokenValue": 20
        }
    ]

    }
'
```

Response

```json
{"jsonrpc":"2.0","id":1337,"result":{"transaction":{"visible":false,"txID":"c3c746beb86ffc366ec0ff8bf6c9504c88f8714e47bc0009e4f7e2b1d49eb967","raw_data":{"contract":[{"parameter":{"value":{"amount":10,"owner_address":"41c4db2c9dfbcb6aa344793f1dda7bd656598a06d8","to_address":"41f859b5c93f789f4bcffbe7cc95a71e28e5e6a5bd"},"type_url":"type.googleapis.com/protocol.TransferContract"},"type":"TransferContract"}],"ref_block_bytes":"958c","ref_block_hash":"9d8c6bae734a2281","expiration":1684469328000,"timestamp":1684469270364},"raw_data_hex":"0a02958c22089d8c6bae734a22814080d1c89183315a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a1541c4db2c9dfbcb6aa344793f1dda7bd656598a06d8121541f859b5c93f789f4bcffbe7cc95a71e28e5e6a5bd180a70dc8ec5918331"}}}
```
