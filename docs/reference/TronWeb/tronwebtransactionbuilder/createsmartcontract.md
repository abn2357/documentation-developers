---
title: createSmartContract
excerpt: Create an unsigned transaction that deploy smart contract
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage**

```javascript
const options = {
    feeLimit: 1000000000,//The maximum TRX burns for resource consumption（1TRX = 1,000,000SUN）
    callValue: 0,//The TRX transfer to the contract for each call（1TRX = 1,000,000SUN）
    tokenId:"",//The id of trc10 token transfer to the contract (Optional)
    tokenValue:0,//The amount of trc10 token transfer to the contract for each call (Optional)
    userFeePercentage: 10,//Consume user's resource percentage. It should be an integer between [0, 100]. if 0, means it does not consume user's resource until the developer's resource has been used up
    originEnergyLimit: 10,//The maximum resource consumption of the creator in one execution or creation
    abi:"{\"entrys\":[{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes3[2]\"}],\"name\":\"bar\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"}]}",//Abi string
    bytecode:"608060405234801561001057600080fd5b50d3801561001d57600080fd5b50d2801561002a57600080fd5b5060da806100396000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063fce353f6146044575b600080fd5b348015604f57600080fd5b50d38015605b57600080fd5b50d28015606757600080fd5b5060a9600480360381019080806040019060028060200260405190810160405280929190826002602002808284378201915050505050919291929050505060ab565b005b505600a165627a7a723058202071fb665ee1935fc34d4da0b135d893fe493a26f309e9888084c4842c3ce66b0029",//Bytecode, default hexString
    parameters: "",//The list of the parameters of the constructor, It should be converted hexString after encoded according to ABI encoder. If constructor has no parameter, this can be optional
    name:"Foo",//Contract name string
    permissionId:1//Optional, for multi-signature use
};
tronWeb.transactionBuilder.createSmartContract(options,issuerAddress);
```

**Parameter**\
object(options),   string(issuerAddress,format:hexstring or base58)

**Return**\
object

**Example**

```javascript
const l_args = {
    feeLimit: 1000000000,
    callValue: 0,
    tokenId:"",
    tokenValue:0,
    userFeePercentage: 10,
    originEnergyLimit: 10,
    abi:"{\"entrys\":[{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes3[2]\"}],\"name\":\"bar\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"pure\",\"type\":\"function\"}]}",
    bytecode:"608060405234801561001057600080fd5b50d3801561001d57600080fd5b50d2801561002a57600080fd5b5060da806100396000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063fce353f6146044575b600080fd5b348015604f57600080fd5b50d38015605b57600080fd5b50d28015606757600080fd5b5060a9600480360381019080806040019060028060200260405190810160405280929190826002602002808284378201915050505050919291929050505060ab565b005b505600a165627a7a723058202071fb665ee1935fc34d4da0b135d893fe493a26f309e9888084c4842c3ce66b0029",
    parameters: "",
    name:"Foo",
    permissionId:1
};
tronWeb.transactionBuilder.createSmartContract(l_args,"41BF97A54F4B829C4E9253B26024B1829E1A3B1120").then(result=>console.log(result));
//Return
{
  visible: false,
  txID: '6c3b978b0971bf4692411d73f5cc90c43016540fd43e606d5d07e28e494e4a1d',
  contract_address: '412b676c1e8d4905de6e3b2a8b807aa09ab298e153',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'caa6',
    ref_block_hash: 'f58a2b9828611d88',
    expiration: 1581062694000,
    fee_limit: 1000000000,
    timestamp: 1581062634939
  },
  raw_data_hex: '0a02caa62208f58a2b9828611d8840f0c8b8f5812e5aa803081e12a1030a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e437265617465536d617274436f6e747261637412ec020a1541bf97a54f4b829c4e9253b26024b1829e1a3b112012d2020a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201a1a0a1810011a03626172220b1a096279746573335b325d30024001229302608060405234801561001057600080fd5b50d3801561001d57600080fd5b50d2801561002a57600080fd5b5060da806100396000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063fce353f6146044575b600080fd5b348015604f57600080fd5b50d38015605b57600080fd5b50d28015606757600080fd5b5060a9600480360381019080806040019060028060200260405190810160405280929190826002602002808284378201915050505050919291929050505060ab565b005b505600a165627a7a723058202071fb665ee1935fc34d4da0b135d893fe493a26f309e9888084c4842c3ce66b0029300a3a03466f6f400a280170bbfbb4f5812e90018094ebdc03'
}
```
