---
title: Event Log
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
The Event Log is one of the most important features of the TRON Virtual Machine (TVM), used to output specific binary data and record it in TransactionInfo when TVM is running a contract. The Event Log can help developers confirm, check, and quickly retrieve specific states of a smart contract. This article introduces basics of the Event mechanism and how to decode the Event Log.

# How to Define and Trigger Events in Contracts

In a Solidity contract, you can define an Event via the `event` keyword, and trigger an Event via the `emit` keyword. When defining an Event, you can specify not only the Event name, but also several parameters to output specific data. Take the Transfer Event of the TRC20 contract as an example:

```solidity=
contract ExampleContractWithEvent {
    event Transfer(address indexed from，address indexed to, uint256 value);
    constructor() payable public{}
    function contractTransfer(address toAddress, uint256 amount){
        toAddress.transfer(amount);
        emit Transfer(msg.sender，toAddress, amount);
    }
}
```

* `event Transfer(address indexed from，address indexed to, uint256 value)` defines a `Transfer` Event containing three parameters: The first parameter is `from`, indicating the sender address, the second one is `to`, indicating the recipient address, and the third one is `value`, indicating the transfer amount.
* `emit Transfer(msg.sender，toAddress, amount)` specifies to trigger the corresponding Event after the transfer is completed. The Event contains the sender address, the recipient address, and the amount.

**Note**：The Solidity specification generally requires that the Event name be capitalized to distinguish it from the corresponding function. For example, distinguish the Event "Transfer" and the function "transfer".

# LOG

Solidity uses the LOG instruction to record Event information in TransactionInfo. The Event information is in the log field of TransactionInfo. The following section uses a TransactionInfo snippet obtained through the `gettransactioninfobyid` API to illustrate the structure of an Event:

```json=
{
    "id": "88c66d08f15b983183c7f7d23e3fafec0320bcc837d67957a8bda58d04ca53e1",
    
    ......
    
    "log": [
        {
            "address": "a614f803b6fd780986a42c78ec9c7f77e6ded13c",
            "topics": [
                "ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "00000000000000000000000079309abcff2cf531070ca9222a1f72c4a5136874",
                "00000000000000000000000081b64b1c09d448d25c9eeb3ee3b8f3348a694c96"
            ],
            "data": "00000000000000000000000000000000000000000000000000000000b2d05e00"
        }
    ]
}
```

`log` ： The list of Events triggered in the transaction. For each Event, it contains the following three parts:

* `address`: Contract address. In order to be compatible with the EVM, the address in the TVM is a hex format address without the prefix `0x41`. So if you want to parse the address in the log, you need to add `41` to the beginning of the log address , and then convert it to the Base58 format .
* `topics`: The topic of the Event, including the Event itself and parameters marked as `indexed`. The reason for using `topics` to save the `indexed` parameters is that blockchain always uses key-value storage engines such as LevelDB or RockDB. These engines generally support the `prefix-scan` operation. So putting the `indexed` parameters into `topics` enables quickly retrieving the `Transfer` Event or retrieving a specific `Transfer` Event with a target `toAddress`. 
* `data`:  Non-indexed parameters of Events, such as `amount`.

# LOG Decoding

For Events in the above LOG section, if you want to decode them, you must first know the ABI of the Event. The following is the ABI of the above Transfer Event:

```json=
{
    "anonymous":false,
    "inputs":
    [
        {"indexed":true,"name":"from","type":"address"},
        {"indexed":true,"name":"to","type":"address"},
        {"indexed":false,"name":"value","type":"uint256"}
    ],
    "name":"Transfer",
    "type":"event"
}
```

Check the Event log along the ABI to decode the data:

* `topics[0]`：ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef is the Event itself. This value is the calculation result of `keccak256('Transfer(address,address,uint256)')`, so the Event is a Transfer Event. The keccak256 hash value of the Event can be calculated via [tronweb.sha3()](https://developers.tron.network/reference/sha3). Note: The parameter of keccak256 must be a string without any spaces; otherwise, the calculated hash value will be different.
* `topics[1]`：00000000000000000000000079309abcff2cf531070ca9222a1f72c4a5136874 is the first indexed parameter, `from`. The address here is the 20-byte address with the prefix 0x41 removed. Therefore, for this parameter, get the last 40 bits of data, and add `41` in the front to get the TRON hex address.
* `topics[2]`：00000000000000000000000081b64b1c09d448d25c9eeb3ee3b8f3348a694c96 is the second indexed parameter, `to`, indicating the recipient account address. The parsing logic is the same as above.
* `data` ： 00000000000000000000000000000000000000000000000000000000b2d05e00 is the value of a non-indexed parameter. If there are multiple non-indexed parameters, they are listed in the order according to the ABI coding rules. For details, please refer to [ABI coding rules](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding). For this example, there is only one non-indexed parameter, namely `value`, the transfer amount. The hexadecimal data can be directly converted to decimal.
