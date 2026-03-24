---
title: getTransactionsToAddress
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

Gets all the confirmed transactions sent to an address. This will not return any unconfirmed transactions.

Note: this is no longer supported by TronGrid. Please refer to our v1 API <a href="https://developers.tron.network/reference#transaction-information-by-account-address">/accounts/address/transactions</a> or use <a href="https://developers.tron.network/docs/trongridjs">TronGrid JS</a>.

```javascript
tronWeb.trx.getTransactionsToAddress("TNDFkUNA2TukukC1Moeqj61pAS53NFchGF", 30, 0);
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
        address
      </td>

      <td>
        Address to query.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        limit
      </td>

      <td>
        Limit amount of returned tx.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        offset
      </td>

      <td>
        Offset to return from
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# Example Output Output
