---
title: listExchangesPaginated
excerpt: Query the list of the exchange pairs by pagination.
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
tronWeb.trx.listExchangesPaginated(Limit, Offset);
```

**Parameter**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Parameter Description
      </th>

      <th>
        Data Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Limit
      </td>

      <td>
        The amount of exchanges returned.
      </td>

      <td>
        Number
      </td>
    </tr>

    <tr>
      <td>
        Offset
      </td>

      <td>
        The index of the start exchange.
      </td>

      <td>
        Number
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
Array

**Example**

```javascript
> tronWeb.trx.listExchangesPaginated(2, 0).then(result => console.log(result));
Promise { <pending> }
> [
  {
    exchange_id: 1,
    creator_address: '41f596e85bfd042744f76880979a133da0728679d9',
    create_time: 1539673398000,
    first_token_id: '31303030353634',
    first_token_balance: 174,
    second_token_id: '5f',
    second_token_balance: 85199
  },
  {
    exchange_id: 2,
    creator_address: '41cd3444bd2d493628b14d6dcec93181e15f94d169',
    create_time: 1541678472000,
    first_token_id: '31303031333035',
    first_token_balance: 128,
    second_token_id: '5f',
    second_token_balance: 15102
  }
]
```
