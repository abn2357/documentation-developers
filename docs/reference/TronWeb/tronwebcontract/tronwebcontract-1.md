---
title: tronweb.contract()
excerpt: smart contract instance
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
tronWeb.contract(abi,contractAddress);
```

**Parameters**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameters
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        abi
      </td>

      <td>
        The abi of the smart contract
      </td>

      <td>
        Array
      </td>
    </tr>

    <tr>
      <td>
        contractAddress
      </td>

      <td>
        The contract address(Hex format or Base58 format)
      </td>

      <td>
        String
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Object - smart contract instance

**Example**

```javascript
let abi = [{"inputs":[{"internalType":"string","name":"initMessage","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"message","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"newMessage","type":"string"}],"name":"update","outputs":[],"stateMutability":"nonpayable","type":"function"}];

async function getContract(){
    let res = await tronWeb.contract(abi,"416A2383E04DF36C74A7EA415E554147C3EE0AF4C7");
    console.log(res);
}
getContract();// Execute the function
```
