---
title: method.send()
excerpt: >-
  Use `send` to execute a `non-pure` or `modify` smart contract method on a
  given smart contract that modify or change values on the blockchain. These
  methods consume resources(bandwidth and energy) to perform as the changes need
  to be broadcasted out to the network.
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
let abi = [...];
let contract = await tronWeb.contract(abi, 'contractAddress'); 
let result = await contract.function_name(para1,para2,...).send({
	feeLimit:100_000_000,
	callValue:0,
  tokenId:1000036,
  tokenValue:100,
  shouldPollResponse:true
});
```

**Parameters**

<Table align={["left","left","left"]}>
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
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        feeLimit
      </td>

      <td>
        The maximum SUN consumes by calling this contract method.\
        Hard capped at 10000 TRX.\
        (1TRX = 1,000,000SUN)
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        callValue
      </td>

      <td>
        Amount of TRX transferred with this transaction, measured in SUN (1 TRX = 1,000,000 SUN).
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        shouldPollResponse
      </td>

      <td>
        If set to TRUE, this will wait until the transaction is confirmed on the solidity node before returning the result.
      </td>

      <td>
        Boolean
      </td>
    </tr>

    <tr>
      <td>
        tokenId
      </td>

      <td>
        If the function accepts a trc 10 token , then the id of the same
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        tokenValue
      </td>

      <td>
        Amount of token sent with the call.
      </td>

      <td>
        Integer
      </td>
    </tr>
  </tbody>
</Table>

**Parameters**\
No need to pass parameters

**Returns**\
Object 

**Example**

```javascript
async function triggercontract(){
    try {
        let abi = [...];
        let instance = await tronWeb.contract(abi, 'TQQg4EL8o1BSeKJY4MJ8TB8XK7xufxFBvK');
        let res = await instance.transfer('TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh',500).send({
            feeLimit:100_000_000,
            callValue:0,
            shouldPollResponse:true
        });

        console.log(res);

    } catch (error) {
        console.log(error);
    }
}

triggercontract();
```
