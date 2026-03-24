---
title: Transactions
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
# Transfer

Transfer TRX. The amount is in SUN.

### Usage

```
transfer(fromAddress, toAddress, amount)
```

### Parameter

| Parameter   | Description                                    | Type   |
| :---------- | :--------------------------------------------- | :----- |
| fromAddress | fromAddress is the owner address               | String |
| toAddress   | toAddress is the recipient address             | String |
| amount      | amount is the amount of TRX to transfer in SUN | int    |

### Return

TransactionExtention, including execution results.

### Exception

IllegalException, if fail to transfer.

### Example

```
TransactionExtention transaction = wrapper.transfer("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm", "TP8LKAf3R3FHDAcrQXuwBEWmaGrrUdRvzb", 1_000_000);
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
e794b5799adbecd5a82a365d3faed5888e9e99eb7bda2f943e3cc46e77a5da7c
```

# getTransactionSignWeight

Query transaction sign weight.

### Usage

```
getTransactionSignWeight(txn)
```

### Parameter

| Parameter | Description        | Type        |
| :-------- | :----------------- | :---------- |
| txn       | Transaction object | Transaction |

### Return

TransactionSignWeight object.

### Example

```
TransactionSignWeight transaction = wrapper.getTransactionSignWeight(wrapper.getTransactionById("786c7516df88941e33ea44f03e637bd8c1ddcfd058634574102c6e3cfb93de0d"));
```

Execution result：

```
permission {
    permission_name: "owner"
    threshold: 1
    keys {
      address: "A,\303\3379\362\325AU\361\\\016\213q)Xr5\346\322X"
      weight: 1
    }
  }
  approved_list: "A,\303\3379\362\325AU\361\\\016\213q)Xr5\346\322X"
  current_weight: 1
  result {
  }
  transaction {
    ...
  }
```

# getTransactionApprovedList

Query transaction approvedList.

### Usage

```
getTransactionApprovedList(txn)
```

### Parameter

| Parameter | Description        | Type        |
| :-------- | :----------------- | :---------- |
| txn       | Transaction object | Transaction |

### Return

TransactionApprovedList object.

### Example

```
TransactionApprovedList transaction = wrapper.getTransactionApprovedList(wrapper.getTransactionById("786c7516df88941e33ea44f03e637bd8c1ddcfd058634574102c6e3cfb93de0d"));
```

Execution result：

```
approved_list: "A,\303\3379\362\325AU\361\\\016\213q)Xr5\346\322X"
  result {
  }
  transaction {
    ...
  }
```

# estimateBandwidth

Calculate the bandwidth of a transaction.

### Usage

```
estimateBandwidth(Transaction txn)
```

### Parameter

| Parameter | Description                     | Type        |
| :-------- | :------------------------------ | :---------- |
| txn       | The transaction to be estimated | Transaction |

### Return

The estimated bandwidth in the type of long.

### Example

```
long bandwidth = wrapper.estimateBandwidth(signedTxn);
```

Execution result：

```
266
```
