---
title: getTransactionFromBlock
excerpt: >-
  Returns a transaction based on a block hash or number and the transactions
  index position.
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
tronWeb.trx.getTransactionFromBlock()
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
        Block height
      </td>

      <td>
        A block number or hash.
      </td>

      <td>
        Integer / String
      </td>
    </tr>

    <tr>
      <td>
        Number
      </td>

      <td>
        The transactions index position
      </td>

      <td>
        Integer
      </td>
    </tr>
  </tbody>
</Table>

# Example

```javascript
//示例1
tronWeb.trx.getTransactionFromBlock(16213568).then(console.log)
>[{object1},{object2}...]

//示例2
tronWeb.trx.getTransactionFromBlock("0000000000f76640a8735af072da5aa741ea983ceb87888030dc8535daa79362").then(console.log)
>[{object1},{object2}...]

//示例3
tronWeb.trx.getTransactionFromBlock(16213568,1).then(console.log)
>{ ret: [ { contractRet: 'SUCCESS' } ],
  signature:
   [ 'c73ae891ece8d83724d81d19e796f9486b6eb6436e26278cc1ab153c4768f04b5bff5c7f5f49dff1ad08dea6cbde06fbe4d16616033cccefd7e346faf1eeeee901' ],
  txID:
   'df9343f44a38613581335ec9c6a176f533593a0818a6b615e2b8f56a202d9026',
  raw_data:
   { contract: [ [Object] ],
     ref_block_bytes: '662c',
     ref_block_hash: '292dddfd299d380a',
     expiration: 1578896229000,
     fee_limit: 6000000,
     timestamp: 1578896170650 },
  raw_data_hex:
   '0a02662c2208292dddfd299d380a408885b2ecf92d5ab301081f12ae010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412790a1541b22b30c7a270788398579af95fa7e7530c7b517a121541e42d76d15b7ecd27a92cc9551738c2635c63b71c188084af5f2244a3082be900000000000000000000000000000000000000000000000000000000000000580000000000000000000000000000000000000000000000000000000000000000709abdaeecf92d9001809bee02' }
```
