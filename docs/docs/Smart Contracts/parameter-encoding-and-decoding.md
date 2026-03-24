---
title: Parameter Encoding and Decoding
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
This article mainly introduces how to encode and decode parameters when triggering a smart contract in the Tron network. The encoding and decoding of parameters follows the Solidity ABI encoding rules.

# ABI Encoding Specification

This chapter mainly introduces the ABI coding rules through examples. For detailed ABI coding rules, please refer to the [ABI Specification](https://docs.soliditylang.org/en/v0.8.13/abi-spec.html) in Solidity documentation.

## Function Selector

The first four bytes of the `data` field of a contract function call are the function selector, specifying the function to be called.

The function selector is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the function signature. The function signature contains only the function name and parameter types, without parameter names and spaces. Take tranfer(address _to, uint256 _value) as an example, its function signature is transfer(address, uint256).

You can get the Keccak-256 hash value of the function signature by calling the [tronweb.sha3](https://developers.tron.network/reference/sha3) interface.

## Argument Encoding

Starting from the fifth byte, the encoded arguments follow. This encoding is also used in other places, e.g. the return values and also event arguments are encoded in the same way, without the four bytes specifying the function.

### Types

We distinguish static and dynamic types. Static types are encoded in-place and dynamic types are encoded at a separately allocated location after the current block.

* Static Types：Fixed-length parameters, such as uint256, bytes32, bool (the boolean type is uint8, which can only be 0 or 1). Taking uint256 as an example, for a parameter whose type is uint256, even if the value is 1, it needs to be padded with 0 to make it 256 bits, that is, 32 bytes, so the length of the static parameter is fixed and has nothing to do with the value.
* Dynamic Types：The length of dynamic parameters is indeterminate. Dynamic parameter types include: bytes, string, T[] for any T, T[k] for any dynamic T and any k >= 0, (T1,...,Tk) if Ti is dynamic for some 1 \<= i \<= k.

### Static Argument Encoding

**Example 1**

```solidity=
function baz(uint32 x, bool y) public pure returns (bool r) { r = x > 32 || y; }
```

The function signature is `baz(uint32,bool)`, Keccak-256 value of function signature is `0xcdcd77c0992ec5bbfc459984220f8c45084cc24d9b6efed1fae540db8de801d2`, Its function selector is 0xcdcd77c0.

The parameter encoding is expressed in hexadecimal, and every two hexadecimal digits occupies one byte. Since the maximum length of static parameters is 256 bits, during encoding, the length of each static parameter is 256 bits, that is, 32 bytes, with a total of 64 hexadecimal digits. When the parameter is less than 256 bits, the left side is filled with 0s.

Pass a set of parameters (69, true) to the baz method, the encoding result is as follows:

* Convert the decimal number 69 to hexadecimal 45, and add 0 to the left to make it occupy 32 bytes, the result is：  
  0x0000000000000000000000000000000000000000000000000000000000000045

* Boolean true is 1 of uint8, its hexadecimal value is also 1, and add 0 to the left to make it occupy 32 bytes, and the result is：  
  0x0000000000000000000000000000000000000000000000000000000000000001

In total:

```
0xcdcd77c000000000000000000000000000000000000000000000000000000000000000450000000000000000000000000000000000000000000000000000000000000001
```

**Example 2**

Similarly, for static type data of `bytes` type, it needs to be padded to 32 bytes when encoding. The difference is that bytes type data needs to be padded on the right. Take the following function as an example

```solidity=
function bar(bytes3[2] memory) public pure {}
```

Function signature is `bar(bytes3[2])`, function selector is: `0xfce353f6`.

Pass a set of parameters `(abc, def)` to this function, the encoding result is as follows:

* The ASCII value of a b c are 97, 98, 99 in decimal, and 61, 62, 63 in hexadecimal. If parameter is less than 32 bytes，it's need to fill with 0 on the right, the result is: 0x6162630000000000000000000000000000000000000000000000000000000000
* The ASCII value of d e f are 100, 101, 102 in decimal, and 64, 65, 66 in hexadecimal. If parameter is less than 32 bytes，it's need to fill with 0 on the right, the result is: 0x6465660000000000000000000000000000000000000000000000000000000000

In total:

```
0xfce353f661626300000000000000000000000000000000000000000000000000000000006465660000000000000000000000000000000000000000000000000000000000
```

### Dynamic Argument Encoding

For dynamic parameters, due to their indeterminate lengths, it is necessary to use a fixed-length offset to occupy the space first, and record the number of offset bytes of the actual position of the dynamic parameters, and then encode the data.

Take the function `f(uint,uint32[],bytes10,bytes)` as an example, when passing the parameters (0x123, [0x456, 0x789], "1234567890", "Hello, world!") to it, the encoding The result is as follows:

* The first static parameter encoding: uints with unmarked lengths are regarded as uint256, and the encoding result of 0x123 is:
  ```
  0x0000000000000000000000000000000000000000000000000000000000000123
  ```
* The offset of the second dynamic parameter: For uint32[], since the array length is unknown，first use the offset to occupy the place, and the offset records the number of bytes at the starting position of this parameter. Before the formal encoding of this uint32 parameter, there are: the encoding of the first parameter uint (32 bytes), the offset of the second parameter uint32[] (32 bytes), and the encoding of the third parameter bytes10 (32 words) section), the offset of the fourth parameter bytes (32 bytes), therefore, the start bytes of the value encoding should be 128, which is 0x80, and the encoding result is:
  ```
  0x0000000000000000000000000000000000000000000000000000000000000080
  ```
* The value encoding of second dynamic parameter : an array [0x456, 0x789] is passed to uint32[]. For dynamic parameters, first record its length, which is 0x2, and then encode the value. The encoding result of this parameter is：
  ```
  0000000000000000000000000000000000000000000000000000000000000002 
  0000000000000000000000000000000000000000000000000000000000000456
  0000000000000000000000000000000000000000000000000000000000000789
  ```
* The third static parameter encoding: "1234567890" is a static bytes10 parameter, convert it to hex format and pad with 0, the result is:
  ```
  0x3132333435363738393000000000000000000000000000000000000000000000
  ```
* The offset of the fourth dynamic parameter: This parameter type is `bytes`, it is a dynamic type, so first use the offset to occupy the place.  The content before the actual content of the parameter is: 1. the encoding of the first parameter uint (32 bytes), 2. the offset of the second parameter uint32[] (32 bytes), 3. the encoding of the third parameter bytes10 (32 bytes) ), 4. the offset of the fourth parameter bytes (32 bytes), 5. the encoding of the second parameter uint32[] (96 bytes). So the offset should be 224 which is 0xe0.
  ```
  0x00000000000000000000000000000000000000000000000000000000000000e0
  ```
* The value encoding of fourth dynamic parameter : For the parameter value of`bytes` type ："Hello, world!", first record its length 13, which is 0xd. Then convert the string to hexadecimal characters, that is : 0x48656c6c6f2c20776f726c642100000000000000000000000000000000000000. The encoding result of this parameter is：

  ```
  000000000000000000000000000000000000000000000000000000000000000d
  48656c6c6f2c20776f726c642100000000000000000000000000000000000000
  ```

  All parameters are encoded, and the final data is

  ```
  0x8be65246 - function selector
  0000000000000000000000000000000000000000000000000000000000000123 - encoding of 0x123
  0000000000000000000000000000000000000000000000000000000000000080 - offset of [0x456, 0x789]
  3132333435363738393000000000000000000000000000000000000000000000 - encoding of "1234567890"
  00000000000000000000000000000000000000000000000000000000000000e0 - offset of "Hello, world!"
  0000000000000000000000000000000000000000000000000000000000000002 - length of [0x456, 0x789]
  0000000000000000000000000000000000000000000000000000000000000456 - encoding of 0x456
  0000000000000000000000000000000000000000000000000000000000000789 - encoding of 0x789
  000000000000000000000000000000000000000000000000000000000000000d - length of "Hello, world!"
  48656c6c6f2c20776f726c642100000000000000000000000000000000000000 - encoding of "Hello, world!"
  ```

# Parameter's Encoding and Decoding

After understanding the ABI encoding rules, you can use the ABI rules to encode and decode parameters in the code. The TRON community provides many SDKs or libraries for developers to use. Some SDKs have already encapsulated the encoding and decoding of parameters. You can call it directly, such as [trident-java](https://developers.tron.network/reference/quickstart). The following will use trident-java SDK and JavaScript libraries to illustrate how to encode and decode parameters in code.

## Parameter Encoding

We take the transfer function in USDT contract as an example:

```solidity=
function transfer(address to, uint256 value) public returns (bool);
```

Suppose you transfer 50000 USDT to the address 412ed5dd8a98aea00ae32517742ea5289761b2710e, and call the triggersmartcontract interface as follows:

```curl=
curl -X POST https://127.0.0.1:8090/wallet/triggersmartcontract -d '{
"contract_address":"412dd04f7b26176aa130823bcc67449d1f451eb98f",
"owner_address":"411fafb1e96dfe4f609e2259bfaf8c77b60c535b93",
"function_selector":"transfer(address,uint256)",
"parameter":"0000000000000000000000002ed5dd8a98aea00ae32517742ea5289761b2710e0000000000000000000000000000000000000000000000000000000ba43b7400",
"call_value":0,
"fee_limit":1000000000,
"call_token_value":0,
"token_id":0
}'
```

In the above command, the parameter's encoding needs to be in accordance with the [ABI rules](#ABI-Encoding-Specification).

### Example of Parameter Encoding Using Javascript

For JavaScript, users can use the `ethers` library, here is the sample code:

```javascript=
// It is recommended to use ethers4.0.47 version
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
}

main()

```

Output:

```
0000000000000000000000002ed5dd8a98aea00ae32517742ea5289761b2710e0000000000000000000000000000000000000000000000000000000ba43b7400
```

### Example of Parameter Encoding Using trident-java

The process of parameter encoding has been encapsulated in trident, just select the parameter type and pass in the parameter value. The type of the parameter is in the `org.tron.trident.abi.datatypes` package, please select the appropriate java class according to the parameter type. The following sample code shows how to use trident to generate `data` information of contract. The main steps are as follows:

1. To construct a `Function` object, three parameters are required: function name, input parameters and output parameters. See [Function code](https://github.com/tronprotocol/trident/blob/main/trident-java/abi/src/main/java/org/tron/trident/abi/datatypes/Function.java) for details.
2. Call the `FunctionEncoder.encode` function to encode the `Function` object and generate the `data` of the contract transaction.

```java=
public void SendTrc20Transaction() {
    ApiWrapper client = ApiWrapper.ofNile("3333333333333333333333333333333333333333333333333333333333333333");

    org.tron.trident.core.contract.Contract contr  = client.getContract("");
    
    // transfer(address,uint256) returns (bool)
    Function trc20Transfer = new Function("transfer",
                                          Arrays.asList(new Address("TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA"),new Uint256(BigInteger.valueOf(10).multiply(BigInteger.valueOf(10).pow(18)))),
                                          Arrays.asList(new TypeReference<Bool>() {})
                                         );

    String encodedHex = FunctionEncoder.encode(trc20Transfer);

    TriggerSmartContract trigger =
            TriggerSmartContract.newBuilder()
                .setOwnerAddress(ApiWrapper.parseAddress("TJRabPrwbZy45sbavfcjinPJC18kjpRTv8"))
                .setContractAddress(ApiWrapper.parseAddress("TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3"))
                .setData(ApiWrapper.parseHex(encodedHex))
                .build();

    System.out.println("trigger:\n" + trigger);

    TransactionExtention txnExt = client.blockingStub.triggerContract(trigger);
    System.out.println("txn id => " + Hex.toHexString(txnExt.getTxid().toByteArray()));
}
```

## Parameter decoding

In the above section of the parameter encoding , the invoked triggersmartcontract generates a transaction object, and then signs and  broadcasts it. After the transaction is successfully on chain, the transaction information on the chain can be obtained through gettransactionbyid:

```curl=
curl -X POST \
  https://api.trongrid.io/wallet/gettransactionbyid \
  -d '{"value" : "1472178f0845f0bfb15957059f3fe9c791e7e039f449c3d5a843aafbc8bbdeeb"}'
```

The results are as follows:

```json=
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

The `raw_data.contract[0].parameter.value.data` field in the return value is the called transfer(address to, uint256 value) function and its parameters. The first four bytes `a9059cbb` of the data field are function selectors, which come from the first 4 bytes after Keccak-256 operation of `transfer(address, uint256)` in ASCII format, which is used for the virtual machine to address the function. The latter part is the parameter, which is the same as the parameter in the `wallet/triggersmartcontract` interface in the parameter encoding chapter.

Function selector，the first four bytes of data, obtained by Keccak-256, cannot be reversed. The function signature can be obtained in two ways:

* If the contract ABI can be obtained, the selector of each contract function can be calculated and compared with the first four bytes of data to judge the function
* The contract generated by the contract may not have ABI on the chain. The contract deployer can also clear the ABI on the chain through the `clearAbi` interface. When the ABI cannot be obtained, you can try to query the functions in the database through `Ethereum Signature Database`.

For parameters decode please refer to below content.

### Example of Parameter Decoding using javascript

#### Decode data

The following JavaScript code decodes the `data` field and obtains the parameters passed by the transfer function:

```javascript=
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

```
[ '414f53238d40e1a3cb8752a2be81f053e266d9ecab', BigNumber { _hex: '0x024dba7580' } ]
```

#### Decode the return value of a contract query operation

We take the query function in USDT contract as an example:

```
balanceOf(address who) public constant returns (uint)
```

Suppose you query the balance of `410583A68A3BCD86C25AB1BEE482BAC04A216B0261` and call the `triggerconstantcontract` interface as follows:

```curl=
curl -X POST https://127.0.0.1:8090/wallet/triggerconstantcontract -d '{
"contract_address":"419E62BE7F4F103C36507CB2A753418791B1CDC182",
"function_selector":"balanceOf(address)",
"parameter":"0000000000000000000000000583A68A3BCD86C25AB1BEE482BAC04A216B0261",
"owner_address":"41977C20977F412C2A1AA4EF3D49FEE5EC4C31CDFB"
}'
```

The results are as follows:

```json=
{
    "result": {
        "result": true
    },
    "constant_result": [
        "000000000000000000000000000000000000000000000000000196ca228159aa"
    ],
   ............
}
```

The `constant_result` is the return value of balanceOf. Here is the sample code for decoding constant_result:

```javascript=
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

```
[ BigNumber { _hex: '0x0196ca228159aa' } ]
```

### Example of Parameter Decoding using trident-java

#### Decode data

The following Java code decodes the `data` field using trident and obtains the parameters passed by the transfer function:

```java=
final String DATA = "a9059cbb0000000000000000000000007fdf5157514bf89ffcb7ff36f34772afd4cdc7440000000000000000000000000000000000000000000000000de0b6b3a7640000";

public void dataDecodingTutorial() {
        String rawSignature = DATA.substring(0,8);
        String signature = "transfer(address,uint256)"; //function signature
        Address rawRecipient = TypeDecoder.decodeAddress(DATA.substring(8,72)); //recipient address
        String recipient = rawRecipient.toString();
        Uint256 rawAmount = TypeDecoder.decodeNumeric(DATA.substring(72,136), Uint256.class); //amount
        BigInteger amount = rawAmount.getValue();

        System.out.println(signature);
        System.out.println("Transfer " + amount + " to " + recipient);
    }
```

#### Decode the return value of a contract query operation

The constant function call will return a `TransactionExtention` object, in which the `constantResult` field is the query result, which is a List\<ByteString>. After converting it to a hex string, you can use the `TypeDecoder` class in the above sample code to decode the return value of the contract query operation. Or you can also use the `decode` method of `org.tron.trident.abi.FunctionReturnDecoder`:

Specify the type of the return value in the `org.tron.trident.abi.FunctionReturnDecoder: decode` method, and it can convert the result to an object of this type.

```java=
public BigInteger balanceOf(String accountAddr) {
        //construct the funtion
        Function balanceOf = new Function("balanceOf",
                Arrays.asList(new Address(accountAddr)), Arrays.asList(new TypeReference<Uint256>() {}));
        //call the function
        TransactionExtention txnExt = wrapper.constantCall(Base58Check.bytesToBase58(ownerAddr.toByteArray()), 
                Base58Check.bytesToBase58(cntrAddr.toByteArray()), balanceOf);
        //Convert constant result to human readable text
        String result = Numeric.toHexString(txnExt.getConstantResult(0).toByteArray());
        return (BigInteger)FunctionReturnDecoder.decode(result, balanceOf.getOutputParameters()).get(0).getValue();
      }
```
