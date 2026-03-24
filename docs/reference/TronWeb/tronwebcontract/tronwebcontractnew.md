---
title: tronweb.contract.new
excerpt: Deploy a smart contract.
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
let abi = 'some abi for contract';
let code = 'bytecode';
async function deploy_contract(){
 	  let contract_instance = await tronWeb.contract().new({
    abi:JSON.parse(abi),
    bytecode:code,
    feeLimit:1000000000,
    callValue:0,
    userFeePercentage:1,
    originEnergyLimit:10000000,
    parameters:[para1,2,3,...]
  });
  console.log(contract_instance.address);
}
```

**Important Note**: for the `userFeePercentage` parameter, it is **strongly recommended** to set the integer value between 1 and 99 (inclusive). Setting as 0 could potentially open the contract developer up to an infinite loop time-out attack.  

**Parameters**

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>

      <th>
        Option
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        abi
      </td>

      <td>
        Smart Contract's Application Binary Interface.
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>
    </tr>

    <tr>
      <td>
        bytecode
      </td>

      <td>
        The compiled contract's identifier, used to interact with the Virtual Machine.
      </td>

      <td>
        String
      </td>

      <td>
        Required
      </td>
    </tr>

    <tr>
      <td>
        feeLimit
      </td>

      <td>
        The maximum SUN consumes by deploying this contract.\
        (1TRX = 1,000,000SUN)
      </td>

      <td>
        Integer, long
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        callValue
      </td>

      <td>
        Amount of SUN transferred to the contract with this transaction.\
        (1TRX = 1,000,000 SUN)
      </td>

      <td>
        Integer
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        userFeePercentage
      </td>

      <td>
        The energy consumption percentage specified for the user calling this contract.
      </td>

      <td>
        Integer between 0 and 100
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        originEnergyLimit
      </td>

      <td>
        The max energy which will be consumed by the owner in the process of execution or creation of the contract, is an integer which should be greater than 0.
      </td>

      <td>
        Integer
      </td>

      <td>
        Optional
      </td>
    </tr>

    <tr>
      <td>
        parameters
      </td>

      <td>
        Parameter passed to the constructor of the contract.
      </td>

      <td>
        Array
      </td>

      <td>
        Optional, required if constructor needs parameters
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Object 

**Example**

```javascript
let abi = 'some abi for contract';
let code = 'bytecode';
async function deploy_contract(){
  	let contract_instance = await tronWeb.contract().new({
    abi:JSON.parse(abi),
    bytecode:code,
    feeLimit:1_00_000_000,
    callValue:0,
    userFeePercentage:1,
    originEnergyLimit:10_000_000  
    //parameters:[para1,2,3,...]
  });
  console.log(contract_instance.address);
}

deploy_contract();// Execute the function
Promise { <pending> }
> 414d137bb7f91e8704d712d3967f6a745b9eedd839
```
