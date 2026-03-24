---
title: setDefaultBlock
excerpt: >-
  Sets the default block used as a reference for tronWeb.trx.getBlock,
  tronWeb.trx.getBlockTransactionCount, tronWeb.trx.getTransactionFromBlock
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
tronWeb.setDefaultBlock('blockID');
```

**Parameters**\
 Possible input values can be 'latest', 'earliest', left blank or block number.

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
        latest
      </td>

      <td>
        The reference block is the latest block;
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        earliest
      </td>

      <td>
        The reference block is the genesis block;
      </td>

      <td>
        String
      </td>
    </tr>

    <tr>
      <td>
        left blank
      </td>

      <td>
        No reference block
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        block number
      </td>

      <td>
        The reference block is the corresponding block.
      </td>

      <td>
        0 or the positive integer
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
  String

**Example** 

```javascript
>tronWeb.setDefaultBlock('latest');
'latest'

> tronWeb.setDefaultBlock();
false

> tronWeb.setDefaultBlock('earliest');
'Earliest'

> tronWeb.setDefaultBlock(585367);
undefined
```
