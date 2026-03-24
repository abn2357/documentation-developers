---
title: getBrokerage
excerpt: Get SR brokerage ratio
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
tronWeb.trx.getBrokerage()
```

# Parameters

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
        address
      </td>

      <td>
        account address
      </td>

      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

**Example** 

```javascript
tronWeb.trx.getBrokerage("TBtrUZ2DXdsBGhpquSPkoEcD2KbWx2rZvE").then(console.log)
>20
```
