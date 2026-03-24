---
title: triggerConfirmedConstantContract
excerpt: >-
  Trigger the read-only function of the contract ( they are the contract
  function which decorated by the pure and view modifiers), the query result is
  a non-solidified state.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Usage

```javascript
// Format
tronWeb.transactionBuilder.triggerConfirmedConstantContract(contractAddress,functions, options,parameter,issuerAddress);
```

**Arguments**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Argument
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
        contractAddress
      </td>

      <td>
        The smart contract address.
      </td>

      <td>
        hexString
      </td>
    </tr>

    <tr>
      <td>
        function
      </td>

      <td>
        Function call, must not leave a blank space
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        options
      </td>

      <td>
        Permission id,feeLimit,callValue
      </td>

      <td>
        Object
      </td>
    </tr>

    <tr>
      <td>
        parameter
      </td>

      <td>
        The parameter passed to 'function'
      </td>

      <td>
        Array
      </td>
    </tr>

    <tr>
      <td>
        issuerAddress
      </td>

      <td>
        Address that triggers the contract
      </td>

      <td>
        hexString
      </td>
    </tr>
  </tbody>
</Table>

# Return

Object

# Example

```javascript
const parameter = []
const options = {
  feeLimit:100000000,
  callValue:0
}
const transaction = await tronWeb.transactionBuilder.triggerConfirmedConstantContract("419e62be7f4f103c36507cb2a753418791b1cdc182", "name()", options,
    parameter,"417946F66D0FC67924DA0AC9936183AB3B07C81126");
>{
    "result": {
        "result": true
    },
    "transaction": {
        "visible": false,
        "txID": "72db144b8594a3f0ae01e89bc04f72eaede81d6b8ab3898f7c49279c9e8dcdac",
        "raw_data": {
            "contract": [
                {
                    "parameter": {
                        "value": {
                            "data": "a9059cbb000000000000000000000000d148171f1ceeeb40d668c47d70e7e94e679775590000000000000000000000000000000000000000000000000000000000000064",
                            "owner_address": "417946f66d0fc67924da0ac9936183ab3b07c81126",
                            "contract_address": "419e62be7f4f103c36507cb2a753418791b1cdc182"
                        },
                        "type_url": "type.googleapis.com/protocol.TriggerSmartContract"
                    },
                    "type": "TriggerSmartContract"
                }
            ],
            "ref_block_bytes": "0cc5",
            "ref_block_hash": "d250de868585420b",
            "expiration": 1581310149000,
            "fee_limit": 1000000000,
            "timestamp": 1581310092216
        },
        "raw_data_hex": "0a020cc52208d250de868585420b408883b8eb822e5aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a15417946f66d0fc67924da0ac9936183ab3b07c811261215419e62be7f4f103c36507cb2a753418791b1cdc1822244a9059cbb000000000000000000000000d148171f1ceeeb40d668c47d70e7e94e67977559000000000000000000000000000000000000000000000000000000000000006470b8c7b4eb822e90018094ebdc03"
    }
}
```
