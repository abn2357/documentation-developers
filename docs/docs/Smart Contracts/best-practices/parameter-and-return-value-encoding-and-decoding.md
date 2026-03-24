---
title: Parameter and return value encoding and decoding
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The main content of this section is the introduction of encoding and decoding of the parameters passed when calling smart contracts in the Tron network.

When calling smart contracts through the HTTPS triggersmartcontract interface, it is necessary to pass the encoded parameter. Here we use the USDT contract as an example to provide JavaScript code to show developers how to encode the parameters. For details about parameter encoding and decoding in solidity, please refer to [solidity document ](https://solidity.readthedocs.io/zh/latest/abi-spec.html#function-selector-and-argument-encoding)and \[tronweb related code] ([https://github.com/TRON-US/tronweb](https://github.com/TRON-US/tronweb)).

# Parameter encoding

**We take the transfer function in USDT contract as an example:**

```text solidity
function transfer (address to, uint256 value) public returns (bool);
```

Suppose you transfer 50000 USDT to the address 412ed5dd8a98aea00ae32517742ea5289761b2710e, and call the triggersmartcontract interface as follows:

```curl
curl -X POST \
-d '{
"contract_address": "412dd04f7b26176aa130823bcc67449d1f451eb98f",
"owner_address": "411fafb1e96dfe4f609e2259bfaf8c77b60c535b93",
"function_selector": "transfer (address, uint256)",
"parameter": "0000000000000000000000002ed5dd8a98aea00ae32517742ea5289761b2710e0000000000000000000000000000000000000000000000000000000ba43b7400",
"call_value": 0,
"fee_limit": 1000000000,
"call_token_value": 0,
"token_id": 0
} '
```

In the above command, the parameter encoding needs to be in accordance with the [ABI rules] 8D # id7), the rules are more complicated, users can use the ethers library to encode, the following is the sample code:

```javascript
//It is recommended to use ethers4.0.47 version
var ethers = require('ethers')

const AbiCoder = ethers.utils.AbiCoder;
const ADDRESS_PREFIX_REGEX = /^(41)/;
const ADDRESS_PREFIX = "41";

async function encodeParams(inputs){
    let typesValues = inputs
    let parameters = ''

    if (typesValues.length == 0)
        return parameters
    const abiCoder = new AbiCoder();
    let types = [];
    const values = [];

    for (let i = 0; i < typesValues.length; i++) {
        let {type, value} = typesValues[i];
        if (type == 'address')
            value = value.replace(ADDRESS_PREFIX_REGEX, '0x');
        else if (type == 'address[]')
            value = value.map(v => toHex(v).replace(ADDRESS_PREFIX_REGEX, '0x'));
        types.push(type);
        values.push(value);
    }

    console.log(types, values)
    try {
        parameters = abiCoder.encode(types, values).replace(/^(0x)/, '');
    } catch (ex) {
        console.log(ex);
    }
    return parameters

}

async function main() {
    let inputs = [
        {type: 'address', value: "412ed5dd8a98aea00ae32517742ea5289761b2710e"},
        {type: 'uint256', value: 50000000000}
    ]
    let parameters = await encodeParams(inputs)
    console.log(parameters)

main()
```

Sample code output:

```text output
0000000000000000000000002ed5dd8a98aea00ae32517742ea5289761b2710e0000000000000000000000000000000000000000000000000000000000000ba43b7400
```

# Parameter decoding

In the above section of the ***parameter encoding*** , the invoked triggersmartcontract generates a transaction object, and then signs the broadcast. After the transaction is successfully chained, the transaction information on the chain can be obtained through gettransactionbyid:

```curl
curl -X POST \
  https://api.trongrid.io/wallet/gettransactionbyid \
  -d '{"value": "1472178f0845f0bfb15957059f3fe9c791e7e039f449c3d5a843aafbc8bbdeeb"}'
```

The results are as follows:

```json
{
    "ret": [
        {
            "contractRet": "SUCCESS"
        }
    ],
    ..........
    "raw_data": {
        "contract": [
            {
                "parameter": {
                    "value": {
                        "data": "a9059cbb0000000000000000000000002ed5dd8a98aea00ae32517742ea5289761b2710e0000000000000000000000000000000000000000000000000000000ba43b7400",
                        "owner_address": "418a4a39b0e62a091608e9631ffd19427d2d338dbd",
                        "contract_address": "41a614f803b6fd780986a42c78ec9c7f77e6ded13c"
                    },
                    "type_url": "type.googleapis.com/protocol.TriggerSmartContract"
                },
    ..........
}
```

The raw\_data.contract \[0] .parameter.value.data field in the above return value is the parameter that calls the transfer (address to, uint256 value) function, but the data field and the encoding of the ***parameters are described in the triggersmartcontract described in the section*** The parameter field is not the same. There are 4 abytes of a9059cbb in front. These 4 bytes are the method ID. This is derived from the first 4 bytes of the Keccak hash signed by transfer (address, uint256) in ASCII format. Used by virtual machines to address functions.

The following code decodes the data field to get the parameters passed by the transfer function:

```javascript
var ethers = require('ethers')

const AbiCoder = ethers.utils.AbiCoder;
const ADDRESS_PREFIX_REGEX = /^(41)/;
const ADDRESS_PREFIX = "41";

//types:Parameter type list, if the function has multiple return values, the order of the types in the list should conform to the defined order
//output: Data before decoding
//ignoreMethodHash：Decode the function return value, fill falseMethodHash with false, if decode the data field in the gettransactionbyid result, fill ignoreMethodHash with true

async function decodeParams(types, output, ignoreMethodHash) {

    if (!output || typeof output === 'boolean') {
        ignoreMethodHash = output;
        output = types;
    }

    if (ignoreMethodHash && output.replace(/^0x/, '').length % 64 === 8)
        output = '0x' + output.replace(/^0x/, '').substring(8);

    const abiCoder = new AbiCoder();

    if (output.replace(/^0x/, '').length % 64)
        throw new Error('The encoded string is not valid. Its length must be a multiple of 64.');
    return abiCoder.decode(types, output).reduce((obj, arg, index) => {
        if (types[index] == 'address')
            arg = ADDRESS_PREFIX + arg.substr(2).toLowerCase();
        obj.push(arg);
        return obj;
    }, []);
}


async function main() {

    let data = '0xa9059cbb0000000000000000000000004f53238d40e1a3cb8752a2be81f053e266d9ecab000000000000000000000000000000000000000000000000000000024dba7580'

    result = await decodeParams(['address', 'uint256'], data, true)
    console.log(result)
}
```

Sample code output:

```text output
['414f53238d40e1a3cb8752a2be81f053e266d9ecab', BigNumber {_hex: '0x024dba7580'}]
```

Note that the third parameter ignoreMethodHash of the decodeParams function must be set to true, so that the decodeParams function skips the first 4 bytes and decodes the subsequent content.

# Return value parameter decoding

**We take the query function in USDT contract as an example:**

```text
balanceOf (address who) public constant returns (uint)
```

Suppose you query the balance of 410583A68A3BCD86C25AB1BEE482BAC04A216B0261 and call the triggersmartcontract interface as follows:

```curl
curl -X POST \
  https://api.trongrid.io/wallet/triggersmartcontract \
  -d '{
    "contract_address": "41a614f803b6fd780986a42c78ec9c7f77e6ded13c",
    "owner_address": "411fafb1e96dfe4f609e2259bfaf8c77b60c535b93",
    "function_selector": "balanceOf (address)",
    "parameter": "0000000000000000000000000583a68a3bcd86c25ab1bee482bac04a216b0261",
    "call_value": 0,
    "fee_limit": 1000000000,
    "call_token_value": 0,
    "token_id": 0
}
```

The results are as follows:

```json
{
    "result": {
        "result": true
    },
    "constant_result": [
        "000000000000000000000000000000000000000000000000000196ca228159aa"
    ],
.........
}
```

The constant\_result in the above return value is the return value of balanceOf. Here is the sample code for decoding constant\_result:

```javascript
async function main() {
  //Must start with 0x
    let outputs = '0x000000000000000000000000000000000000000000000000000196ca228159aa'
    //
    //['uint256 '] is a list of return value types. If there are multiple return values, fill in the types in order
    result = await decodeParams(['uint256'], outputs, false)
    console.log(result)
}
```

Sample code output:

```text output
[BigNumber {_hex: '0x0196ca228159aa'}]
```
