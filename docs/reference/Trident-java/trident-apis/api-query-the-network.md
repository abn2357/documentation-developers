---
title: Query the Network
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
# getBlockByNum

Returns the Block Object corresponding to the 'Block Height' specified (number of blocks preceding it).

### Usage

```
getBlockByNum(blockNum)
```

### Parameter

| Parameter | Description  | Type |
| :-------- | :----------- | :--- |
| blockNum  | Block height | long |

### Return

Object - Block object。

### Example

```
wrapper.getBlockByNum(10);
```

Execution result:

```
block_header {
    raw_data {
      timestamp: 1572510150000
      txTrieRoot: "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
      parentHash: "\000\000\000\000\000\000\000\t\210\236\253\326\027\343\241\240\324\030\255\243\330\203\241\002\217\372 \354\261\'{H"
      number: 10
      witness_address: "A\324\244\374\'C\357\b\310\216\265\256\316|\304\255\0327D\222\220"
      version: 9
    }
    witness_signature: "\354_\342^31\231\022\201\366\333S\335\324\334\317\034O\036\3439\347\344\377\252\371\251\020\264\277lj\032\005\241\261\255Tt\261\363\252v\250\0008\227W\356\371\rT\335\263;>=\314\366V\021\372?\003\001"
  }
```

# getBlockByLatestNum

Get some latest blocks.  

### Usage

```
getBlockByLatestNum(num)
```

### Parameter

| Parameter | Description                                           | Type |
| :-------- | :---------------------------------------------------- | :--- |
| num       | Number of latest blocks. It must be between 1 and 99. | long |

### Return

Object - BlockListExtention object。

### Example

```
wrapper.getBlockByLatestNum(2);
```

Execution result:

```
block {
    transactions {
      transaction {
        raw_data {
          ref_block_bytes: "w\v"
          ref_block_hash: "\307\3062\245\312;G\257"
          expiration: 1614763632000
          contract {
            type: TriggerSmartContract
            parameter {
              type_url: "type.googleapis.com/protocol.TriggerSmartContract"
              value: "\n\025A\006\001\273\365u\212\277P3\372\277`\022[L\262\216{\225J\022\025AN\034~z\227\027A\330T=\231\006\255\321\361\232\330\031KT\"D\251\005\234\273\000\000\000\000\000\000\000\000\000\000\000ASd\326\f\244\362\362<\346\025S\375\272/aZ\250\226\2026\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\017B@"
            }
          }
          timestamp: 1614763575881
          fee_limit: 5000000
        }
        signature: "?\360\325:\305@\017\340\244\265\026$\276\004\247\316\355\265\035\037m\343J\361H\367\224\211\333\341\317\037\002\350\215V\310\235c\023W\371?\322\v&\245k\356\a\230\323\032\234\370\034v\203\333\302/\252\340I\000"
        ret {
          contractRet: SUCCESS
        }
      }
      txid: "0\036\246\245\356!3\305A\a\270*;by$qPR\317\2517n\366Uc\377\017\034-\261\a"
      result {
        result: true
      }
    }
    ...
block_header {
    raw_data {
      timestamp: 1614763578000
      txTrieRoot: "\212\332@\257\327\224fU\304k%\206\325O(\230Z@L\325!\353n>4\326+\377I\302\357\033"
      parentHash: "\000\000\000\000\000\324w\f\023y\365\200\350\2676\277\276e\266#\230\300\311Eh2u\330\021\346\276\205"
      number: 13924109
      witness_address: "Aw\024\200\351\353\2102\232\t9g\262\350\234\t\325K\273\023>"
      version: 20
    }
    witness_signature: "\2260\\\003\307\315\2213>\265\320\004@\303\002<\244\234\2326\261%2\004\027\324\033\240d\v\031\371\021\213\323g\353jGc;\024\226nL\"6U\033\336\002\021\336\274\b\232\037o42\370\304D\335\000"
  }
  blockid: "\000\000\000\000\000\324w\rI<\363\300\345\251\024F\001i\016\231\267*I\200\316e\005\a\f\250\253\025"
}
...
```

# getBlockByLimitNext

Returns the list of Block objects included in the 'Block Height' range specified.

### Usage

```
getBlockByLimitNext(startNum, endNum)
```

### Parameter

| Parameter | Description                                        | Type |
| :-------- | :------------------------------------------------- | :--- |
| startNum  | Number of start block height, including this block | long |
| endNum    | Number of end block height, excluding this block   | long |

### Return

Object - BlockListExtention object。Note:  If the parameters are not correct or the difference between startNum and endNum is greater than 100, it will throw IllegalException exception.

### Example

```
wrapper.getBlockByLimitNext(0,2);
```

Execution result:

```
block {
    transactions {
      transaction {
        raw_data {
          contract {
            type: TransferContract
            parameter {
              type_url: "type.googleapis.com/protocol.TransferContract"
              value: "\n\0270x000000000000000000000\022\025A~\225\344_Z`\314E\362\320\257\343~\351\367\177\270\316\237\377\030\200\200\216\306\233\377\355\257\001"
            }
          }
        }
      }
      txid: "\037\332\245\273v\343\301\245C\017}\211 \376,\353\310\022\n\024\310{:\234\2726\340\241\033h\265~"
      result {
        result: true
      }
    }
    ...
block_header {
    raw_data {
      txTrieRoot: "eV\251h($\215k\211\317\320H}L\357\202\2614\265TM\304(\310\242\030\276\262\333\205\253$"
      parentHash: "\345\2173\371\272\3710]\306\370+\237\0314\352\217\n\336-\357\271Q%\215P\026p(\307\2005\037"
      witness_address: "A new system must allow existing systems to be linked together without requiring any central control or coordination"
    }
  }
  blockid: "\000\000\000\000\000\000\000\000\326\230\324\031,V\313k\347$\245XD\216&\204\200-\344\326\315\206\220\334"
}
```

# getNowBlock

Query the latest block information.

### Usage

```
getNowBlock()
```

### Parameter

None

### Return

Object - Block object。  

### Example

```
wrapper.getNowBlock();
```

Execution result:

```
transactions {
    raw_data {
      ref_block_bytes: "vy"
      ref_block_hash: "f\005\240\236L\371\307\221"
      expiration: 1614763188000
      contract {
        type: TriggerSmartContract
        parameter {
          type_url: "type.googleapis.com/protocol.TriggerSmartContract"
          value: "\n\025A\006\001\273\365u\212\277P3\372\277`\022[L\262\216{\225J\022\025AN\034~z\227\027A\330T=\231\006\255\321\361\232\330\031KT\"D\251\005\234\273\000\000\000\000\000\000\000\000\000\000\000ASd\326\f\244\362\362<\346\025S\375\272/aZ\250\226\2026\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\017B@"
        }
      }
      timestamp: 1614763131403
      fee_limit: 5000000
    }
    signature: "H\0312\345e\227\033g\316\304\313\016R\275Sh\"N4\213\002S%\363q\252\373\rh\006\363\t|\263\225Q\001d?`R\2765 +#>\343\024\363\3107\371e\374\271\216rS\321\016H\325\364\001"
    ret {
      contractRet: SUCCESS
    }
  }
  ...
  block_header {
    raw_data {
      timestamp: 1614763134000
      txTrieRoot: "\000\275AwP\a\001f\344#\"\245\307\037\277\342\367\257\360\333\201\032]N\024Y+\341ac\2240"
      parentHash: "\000\000\000\000\000\324vz\003\0200\022\340\272\361A\337\245\212\341\035Q^2^\004M\325\201\347e}"
      number: 13923963
      witness_address: "A\fLd \037f\243\'\031\317\232\264\346\364\256\3263\vH\275"
      version: 20
    }
    witness_signature: "\315\002\203>\v\254\310\363\'M\332\315`bJ\\\263\023\317\034B\251\032\363\303i\276\246\2269\325Ee\211v\375k9\003X\tZ\3756\266\237\r4\025\257\362\3270\276\032\212-\026\266}\347d\260\037\000"
  }
```

# getTransactionById

Query transaction information by transaction id.

### Usage

```
getTransactionById(txID)
```

### Parameter

| Parameter | Description                            | Type   |
| :-------- | :------------------------------------- | :----- |
| txID      | Transaction hash, i.e. transaction id. | String |

### Return

Object - Transaction object. If the parameter is not correct, it will throw IllegalException exception.

### Example

```
wrapper.getTransactionById("786c7516df88941e33ea44f03e637bd8c1ddcfd058634574102c6e3cfb93de0d");
```

Execution result:

```
raw_data {
    ref_block_bytes: "T("
    ref_block_hash: "\236\255\354O\002\260\333\266"
    expiration: 1606991088000
    contract {
      type: TriggerSmartContract
      parameter {
        type_url: "type.googleapis.com/protocol.TriggerSmartContract"
        value: "\n\025A,\303\3379\362\325AU\361\\\016\213q)Xr5\346\322X\022\025A \343\347\200\310\016\373\362#\310\371\266\334\310\f\016\336\v\033\345\"\244\002\365W#Z\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000 \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\316{\'\346\270\270\346\210\217\347\274\226\345\217\267\':\'GN001208300ZK\',\'\346\270\270\346\210\217\345\271\263\345\217\260\':\'AG\346\227\227\350\210\260\345\216\205\',\'\346\270\270\346\210\217\347\261\273\345\236\213\':\'\347\231\276\345\256\266\344\271\220\',\'\346\270\270\346\210\217\347\273\223\346\236\234\':\'\345\272\2048\351\227\2623\',\'\345\210\233\345\273\272\346\227\266\351\227\264\':\'Mon Aug 31 01:55:24 PST 2020\',\'\346\210\252\346\255\242\346\227\245\346\234\237\':\'Mon Aug 31 01:55:49 PST 2020\'}\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
      }
    }
    timestamp: 1606991030518
    fee_limit: 1000000
  }
  signature: "\271\325\213%\214\256\316\3778\304\206m\346\363!h\355i\374\304\212\337\332\227\032\271\363\261\300\262\362*S\306\272{\027\264\003\302\271\335)\210\017\360\243\"\216\325\335\333\360Wu\2265\205y\356\336\344F\000\001"
  ret {
    contractRet: SUCCESS
  }
```

# getTransactionInfoById

Query the transaction fee, block height by transaction id.

### Usage

```
getTransactionInfoById(txID)
```

### Parameter

| Parameter | Description                            | Type   |
| :-------- | :------------------------------------- | :----- |
| txID      | Transaction hash, i.e. transaction id. | String |

### Return

Object - Transaction object. If the parameter is not correct, it will throw IllegalException exception.\
\###Example

```
wrapper.getTransactionInfoById("786c7516df88941e33ea44f03e637bd8c1ddcfd058634574102c6e3cfb93de0d");
```

Execution result:

```
id: "xlu\026\337\210\224\0363\352D\360>c{\330\301\335\317\320XcEt\020,n<\373\223\336\r"
  fee: 202080
  blockNumber: 11359274
  blockTimeStamp: 1606991034000
  contractResult: ""
  contract_address: "A \343\347\200\310\016\373\362#\310\371\266\334\310\f\016\336\v\033\345"
  receipt {
    energy_fee: 179280
    energy_usage_total: 4482
    net_fee: 22800
    result: SUCCESS
  }
  log {
    address: " \343\347\200\310\016\373\362#\310\371\266\334\310\f\016\336\v\033\345"
    topics: "\262tu\a\244n\032\274\354\241\234N\271W)&\301\206\342\fd\2204\250\r\321\254.\302\034\262q"
    data: "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000 \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\316{\'\346\270\270\346\210\217\347\274\226\345\217\267\':\'GN001208300ZK\',\'\346\270\270\346\210\217\345\271\263\345\217\260\':\'AG\346\227\227\350\210\260\345\216\205\',\'\346\270\270\346\210\217\347\261\273\345\236\213\':\'\347\231\276\345\256\266\344\271\220\',\'\346\270\270\346\210\217\347\273\223\346\236\234\':\'\345\272\2048\351\227\2623\',\'\345\210\233\345\273\272\346\227\266\351\227\264\':\'Mon Aug 31 01:55:24 PST 2020\',\'\346\210\252\346\255\242\346\227\245\346\234\237\':\'Mon Aug 31 01:55:49 PST 2020\'}\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
  }
```

# getTransactionInfoByBlockNum

Get transactionInfo from block number. 

### Usage

```
getTransactionInfoByBlockNum(blockNum)
```

### Parameter

| Parameter | Description  | Type |
| :-------- | :----------- | :--- |
| blockNum  | Block height | long |

### Return

Object - TransactionInfoList object. An IllegalException is thrown when the Parameter is incorrect or the transaction cannot be found. 

### Example

```
wrapper.getTransactionInfoByBlockNum(11359274);
```

Execution result:

```
transactionInfo {
    id: "xlu\026\337\210\224\0363\352D\360>c{\330\301\335\317\320XcEt\020,n<\373\223\336\r"
    fee: 202080
    blockNumber: 11359274
    blockTimeStamp: 1606991034000
    contractResult: ""
    contract_address: "A \343\347\200\310\016\373\362#\310\371\266\334\310\f\016\336\v\033\345"
    receipt {
      energy_fee: 179280
      energy_usage_total: 4482
      net_fee: 22800
      result: SUCCESS
    }
    log {
      address: " \343\347\200\310\016\373\362#\310\371\266\334\310\f\016\336\v\033\345"
      topics: "\262tu\a\244n\032\274\354\241\234N\271W)&\301\206\342\fd\2204\250\r\321\254.\302\034\262q"
      data: "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000 \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\316{\'\346\270\270\346\210\217\347\274\226\345\217\267\':\'GN001208300ZK\',\'\346\270\270\346\210\217\345\271\263\345\217\260\':\'AG\346\227\227\350\210\260\345\216\205\',\'\346\270\270\346\210\217\347\261\273\345\236\213\':\'\347\231\276\345\256\266\344\271\220\',\'\346\270\270\346\210\217\347\273\223\346\236\234\':\'\345\272\2048\351\227\2623\',\'\345\210\233\345\273\272\346\227\266\351\227\264\':\'Mon Aug 31 01:55:24 PST 2020\',\'\346\210\252\346\255\242\346\227\245\346\234\237\':\'Mon Aug 31 01:55:49 PST 2020\'}\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
    }
  }
 ...
```

# listNodes

List all nodes that current API node is connected to. 

### Usage

```
listNodes()
```

### Parameter

None.

### Return

Object - NodeList object. An IllegalException is thrown when it fails to get node list.

### Example

```
wrapper.listNodes();
```

Execution result:

```
nodes {
    address {
      host: "47.252.73.173"
      port: 18888
    }
  }
  ...
```

# getNodeInfo

Get current API node’ info. 

### Usage

```
getNodeInfo()
```

### Parameter

None.

### Return

Object - NodeInfo object.  An IllegalException is thrown when it fails to get nodeInfo.  

### Example

```
wrapper.getNodeInfo();
```

Execution result:

```
beginSyncNum: 13924273
  block: "Num:13924292,ID:0000000000d477c4eb847d840e2be648712eaaccdc965f90c70d14a4f68b1bcf"
  solidityBlock: "Num:13924274,ID:0000000000d477b281ec179f56a8f5bdeeb1a8ab7e2531fe139ca2b82e4a9a1e"
  currentConnectCount: 30
  activeConnectCount: 3
  passiveConnectCount: 27
  totalFlow: 5258156
  peerInfoList {
    ...
  }
  ...
 configNodeInfo {
  ...
 }
 machineInfo {
  ...
  }
  ...
}
```

# getChainParameters

All parameters that the blockchain committee can set.  

### Usage

```
getChainParameters()
```

### Parameter

None.

### Return

Object - ChainParameters object. An IllegalException is thrown when it fails to get chain parameters. 

### Example

```
wrapper.getChainParameters();
```

Execution result:

```
chainParameter {
    key: "getMaintenanceTimeInterval"
    value: 600000
  }
  ...
```
