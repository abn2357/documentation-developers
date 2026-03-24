---
title: updateAccountPermissions
excerpt: ''
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
let ownerAddress = 'your address';
let ownerPk = 'your private key';
let ownerPermission = { type: 0, permission_name: 'owner' };
ownerPermission.threshold = 2;
ownerPermission.keys  = [];

let activePermission = { type: 2, permission_name: 'active0' };
activePermission.threshold = 3;
activePermission.operations = '7fff1fc0037e0000000000000000000000000000000000000000000000000000';
activePermission.keys = [];

ownerPermission.keys.push({ address: 'address1', weight: 1 });
ownerPermission.keys.push({ address: 'address2', weight: 1 });
activePermission.keys.push({ address: 'address1', weight: 1 });
activePermission.keys.push({ address: 'address2', weight: 1 });


const updateTransaction = await tronWeb.transactionBuilder.updateAccountPermissions(ownerAddress, ownerPermission, null, [activePermission]);
```

# Input Parameters

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
        owner\_address
      </td>

      <td>
        The address is the owner who will update permission. If not pass, value will be the default address you set in tronWeb.
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        ownerPermissions
      </td>

      <td>
        \{\
          type: 0,\
          permission\_name: 'owner',\
          threshold: 2,\
          keys: [  
             \{  
               address: 'xxxxxxxx',  
               weight: 1  
             },  
             \{  
               address: 'xxxxxxxx',  
               weight: 1  
             }  
          ]\
        }\
        type:  has to be 0 which means owner.
      </td>

      <td>
        Object
      </td>
    </tr>

    <tr>
      <td>
        witnessPermissions
      </td>

      <td>
        \{\
          type: 1,\
          permission\_name: 'witness'\
        }\
        Normal user has to pass **null** value. This parameter could be used only for super representative who will generate blocks.
      </td>

      <td>
        Object
      </td>
    </tr>

    <tr>
      <td>
        activesPermissions
      </td>

      <td>
        \[\{\
          type: 2,\
          permission\_name: 'active0',\
          threshold: 2,\
          operations: '7fff1fc0037e0000000000000000000000000000000000000000000000000000',\
          keys: [  
             \{  
               address: 'xxxxxxxx',  
               weight: 1  
             },  
             \{  
               address: 'xxxxxxxx',  
               weight: 1  
             }  
          ]\
        }]\
        Type has to be 2 which means active permission.
      </td>

      <td>
        Array
      </td>
    </tr>
  </tbody>
</Table>

# Example Output Data

```json
{
  "visible": false,
  "txID": "7f06b2e887dd9703ad481c6a7cafc1cd8857b354d0c45ebdf5eb82bfd0cf6d68",
  "raw_data": {
    "contract": [
      {
        "parameter": {
          "value": {
            "owner": {
              "keys": [
                {
                  "address": "413dd5ec509f7f5bf381070b7bbac66d24b4631bd4",
                  "weight": 1
                },
                {
                  "address": "410a0e30b7e7a75a0a4f74388e456406edeb557134",
                  "weight": 1
                },
                {
                  "address": "414d66511bf52280f9be386747e53f172e15b01815",
                  "weight": 1
                }
              ],
              "threshold": 3,
              "permission_name": "owner"
            },
            "owner_address": "413dd5ec509f7f5bf381070b7bbac66d24b4631bd4",
            "actives": [
              {
                "operations": "7fff1fc0037e0000000000000000000000000000000000000000000000000000",
                "keys": [
                  {
                    "address": "413dd5ec509f7f5bf381070b7bbac66d24b4631bd4",
                    "weight": 1
                  },
                  {
                    "address": "410a0e30b7e7a75a0a4f74388e456406edeb557134",
                    "weight": 1
                  },
                  {
                    "address": "414d66511bf52280f9be386747e53f172e15b01815",
                    "weight": 1
                  }
                ],
                "threshold": 3,
                "type": "Active",
                "permission_name": "active0"
              }
            ]
          },
          "type_url": "type.googleapis.com/protocol.AccountPermissionUpdateContract"
        },
        "type": "AccountPermissionUpdateContract"
      }
    ],
    "ref_block_bytes": "000b",
    "ref_block_hash": "07653cf4b79aa839",
    "expiration": 1565312682000,
    "timestamp": 1565312624396
  },
  "raw_data_hex": "0a02000b220807653cf4b79aa839409090a09fc72d5abc02082e12b7020a3c747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e4163636f756e745065726d697373696f6e557064617465436f6e747261637412f6010a15413dd5ec509f7f5bf381070b7bbac66d24b4631bd4125a1a056f776e657220033a190a15413dd5ec509f7f5bf381070b7bbac66d24b4631bd410013a190a15410a0e30b7e7a75a0a4f74388e456406edeb55713410013a190a15414d66511bf52280f9be386747e53f172e15b01815100122800108021a0761637469766530200332207fff1fc0037e00000000000000000000000000000000000000000000000000003a190a15413dd5ec509f7f5bf381070b7bbac66d24b4631bd410013a190a15410a0e30b7e7a75a0a4f74388e456406edeb55713410013a190a15414d66511bf52280f9be386747e53f172e15b018151001708cce9c9fc72d"
}
```