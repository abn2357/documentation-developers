---
title: getEventResult
excerpt: Returns all events matching the filters.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 🚧 API Change
>
> ***Applies Starting From TronWeb 2.1.31***
>
> This new API function differs from the previous function in that it takes in an additional 3 parameters in the optional object input. These additional 3 parameters are onlyConfirmed, onlyUnconfirmed, and fingerprint.

**Usage**

```javascript
tronWeb.getEventResult(contractAddress, options);
```

**Parameter**\
contractAddress - String : Contract address.\
options - Object :  (optional) The filter conditions, including the following fields:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Options Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        sinceTimestamp
      </td>

      <td>
        Specifies the starting timestamp of the query, in milliseconds, default value is the current time. The query can be forward or reverse lookup specified by the `sort` parameter.
      </td>
    </tr>

    <tr>
      <td>
        eventName
      </td>

      <td>
        Name of the event to filter by.
      </td>
    </tr>

    <tr>
      <td>
        blockNumber
      </td>

      <td>
        Specific block number to query
      </td>
    </tr>

    <tr>
      <td>
        size
      </td>

      <td>
        maximum number returned
      </td>
    </tr>

    <tr>
      <td>
        onlyConfirmed
      </td>

      <td>
        If set to true, only returns confirmed transactions.
      </td>
    </tr>

    <tr>
      <td>
        onlyUnconfirmed
      </td>

      <td>
        If set to true, only returns unconfirmed transactions.
      </td>
    </tr>

    <tr>
      <td>
        fingerprint
      </td>

      <td>
        When the data volume of the query result is large, the returned result of one query will not contain all the data, and it takes multiple queries to obtain the complete data. Therefore, the `fingerprint` field will appear in the last piece of data in the returned result. After specifying this field as the content of the `fingerprint` in the result of the previous query in the next query, the query will return subsequent data. If there is no such field in the last data of the query result, it means that there is no more data
      </td>
    </tr>

    <tr>
      <td>
        sort
      </td>

      <td>
        Specify the query order, whether to query forward or backward from the `sinceTimestamp`. The value can be 'block\_timestamp' for time sequence or '-block\_timestamp' for the reverse. Default is '-block\_timestamp'.
      </td>
    </tr>
  </tbody>
</Table>

**Return**\
Promise Object(Array) : Contract events.

**Example**

```javascript
> tronWeb.getEventResult("TUPz3wD356e3iV337s4cnjQS2weUdhX5ci",{eventName:"RNGIterated",size:2}).then(result => {console.log(result)})
Promise { <pending> }
> [
  {
    block: 615212,
    timestamp: 1577440164000,
    contract: 'TUPz3wD356e3iV337s4cnjQS2weUdhX5ci',
    name: 'RNGIterated',
    transaction: 'a8929bcfb8a7337d6c8c5850b5ed63cdd09ff17bbde46dad07b2c1f20c427e89',
    result: {
      index: '41796',
      rng: '3f7bf1c50a01cbcb980360effa904e0e11880af8daeeb2f8da686b7b3e5d9a50',
      timestamp: '1577440164'
    },
    resourceNode: 'solidityNode'
  },
  {
    block: 615205,
    timestamp: 1577440143000,
    contract: 'TUPz3wD356e3iV337s4cnjQS2weUdhX5ci',
    name: 'RNGIterated',
    transaction: 'fa9e91282de9eb462efabea838c2d0465602312a87ded06524c87d8afafd743d',
    result: {
      index: '41795',
      rng: 'bf190910aa5293ab12f644eb723b5460340e3ec11ac073124147e5fc92ca44d2',
      timestamp: '1577440143'
    },
    resourceNode: 'solidityNode',
    fingerprint: '2TBTeOqO3x2kJDyxT'
  }
]
```
