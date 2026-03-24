---
title: getBlockRange
excerpt: Query the block information by range.
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
tronWeb.trx.getBlockRange(Starting Block,Ending Block);
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
        Starting Block
      </td>

      <td>
        Block number of the beginning of the range.
      </td>

      <td>
        Integer
      </td>
    </tr>

    <tr>
      <td>
        Ending Block
      </td>

      <td>
        Block number of the end of the range.
      </td>

      <td>
        Integer
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
  Object array

**Example** 

```javascript
> tronWeb.trx.getBlockRange(15816492,15816493).then(result => {console.log(result)});
Promise { <pending> }
> [
  {
    blockID: '0000000000f1572c60fe671e379f4cb3dcc4245aa6eca50edbfb64c66a3672c7',
    block_header: {
      raw_data: [Object],
      witness_signature: 'f7b17ae291128adde41f0349b70f2b1fba72b2f7260650e27e231e9a8ceae112353bce76237409d7f256c4f401114234abf521e666890e9f3d090bcc99ae723501'
    },
    transactions: [
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object]
    ]
  },
  {
    blockID: '0000000000f1572d90c32bcaec30eb2fb72df772c5c4fda23b5a79ddba6c3e62',
    block_header: {
      raw_data: [Object],
      witness_signature: 'eba61099d8e498f43ab57de081dbefb28cee9b6a4ceb1a298830969b47877c4538d771232eb8e68a01e651f4a256c0611f32fc29a039cd838a9d96bc42e4eb6300'
    },
    transactions: [
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object],
      [Object], [Object], [Object], [Object], [Object]
    ]
  }
]
```
