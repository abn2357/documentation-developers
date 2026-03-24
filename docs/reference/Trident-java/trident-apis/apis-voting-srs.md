---
title: Voting & SRs
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
# listWitnesses

List all super representatives. 

### Usage

```
listWitnesses()
```

### Parameter

None.

### Return

Object - WitnessList object.

### Example

```
wrapper.listWitnesses();
```

Execution result:

```
witnesses {
    address: "A\243]\347\020{\304h\231\270\365\273\030\306\036\262\340\334\2649\340"
    voteCount: 1000008562
    url: "http://SR8.com"
    totalProduced: 514523
    totalMissed: 805
    latestBlockNum: 13925240
    latestSlotNum: 538255669
    isJobs: true
  }
  ...
```

# voteWitness

Vote for a super representative.

### Usage

```
voteWitness(ownerAddress, votes)
```

### Parameter

| Parameter    | Description                                                                                                                                                      | Type   |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- |
| ownerAddress | owner address                                                                                                                                                    | String |
| votes        | key: 'vote\_address' stands for the address of the SR you want to vote, default hexString.  value: 'vote\_count' stands for the number of votes you want to vote | Map    |

### Return

Object -TransactionExtention ，unsigned transaction object.

### Example

```
witness.put("TG7RHXaL7E9rqSkBavX7s1vtikoz6np6bD","1");
TransactionExtention transaction = wrapper.voteWitness("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm",witness);
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result:

```
90b1738e0ead46e52f1550d7e5b619136ecf715cc43a728737b86b1a5bf633a3
```
