---
title: getBlockTransactionCount
excerpt: Retrieves the count of transactions within a block.
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
tronWeb.trx.getBlockTransactionCount()
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
        Block Height
      </td>

      <td>
        The height of the block you wish to obtain transaction count data for.
      </td>

      <td>
        Integer/string
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Object

**Example**

```javascript
tronWeb.trx.getBlockTransactionCount(16012520).then(console.log);
>35
tronWeb.trx.getBlockTransactionCount("0000000000f454e84edbee2365fbf1bf34bc98283ded06e68311bb6e5bea3cf6").then(console.log);
>35
```
