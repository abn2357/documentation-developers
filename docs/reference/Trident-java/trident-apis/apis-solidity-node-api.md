---
title: Solidity Node API
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
# getAccountSolidity

Get solid account info by address.

### Usage

```
getAccountSolidity(address)
```

### Parameter

| Parameter | Description                        | Type   |
| :-------- | :--------------------------------- | :----- |
| address   | address, Base58check or HEX format | String |

### Return

Account object.

### Example

```
wrapper.getAccountSolidity("TKwVM5tsELuTE3a5SUCWiQyVtEgxejL5Wj");
```

Execution result:

```
address: "Am^\021\374\370\025\340@\032\262R\325uO\033d\034j\226\302"
  balance: 10000000
  create_time: 1606470234000
  latest_opration_time: 1607746098000
  latest_consume_free_time: 1607746098000
  account_resource {
    latest_consume_time_for_energy: 1607142153000
  }
  owner_permission {
    ...
  }
  active_permission {
    ...
  }
```

# getNowBlockSolidity

Query the latest solid block information. 

### Usage

```
getNowBlockSolidity()
```

### Parameter

None.

### Return

BlockExtention object.   

### Exception

IllegalException, if fail to get now block.  

### Example

```
wrapper.getNowBlockSolidity();
```

Execution result:

```
transactions {
    transaction {
      raw_data {
        ref_block_bytes: "\334\003"
        ref_block_hash: "&\231d\202\341B\262\341"
        expiration: 1614841962000
        contract {
          type: TransferContract
          parameter {
            type_url: "type.googleapis.com/protocol.TransferContract"
            value: "\n\025A\006\001\273\365u\212\277P3\372\277`\022[L\262\216{\225J\022\025ASd\326\f\244\362\362<\346\025S\375\272/aZ\250\226\2026\030\200\222\364\001"
          }
        }
        timestamp: 1614841903089
      }
      signature: "@\274\032\251\f\364\331=\236\230\204)\371\\uP2l\253\202\201ve\223\304L\314S\244a\r\255Wx\263\322\f\2378\az[#\324\363mS\234IO\252\212J\332\265Is\333\216\213\300\224\300+\000"
      ret {
        contractRet: SUCCESS
      }
    }
    txid: "\227jh\370\252\205]\321\356&\370+!\316W\234K+&\266N/\212\271\260\200D\333\035x\207\241"
    result {
      result: true
    }
  }
  ...
  block_header {
    raw_data {
      timestamp: 1614841905000
      txTrieRoot: "\373\251\002\250tn\315(\224\034\314\3503O\225\225qlr\253g\275C\350\276\332\274\365\364\243\b5"
      parentHash: "\000\000\000\000\000\324\334\003&\231d\202\341B\262\341\302\277\3438j\203\345\240\216\205\203i4\261\016["
      number: 13949956
      witness_address: "A\256w\025\rK\2734\212\303z\217\037&c\373y]\326%S"
      version: 20
    }
    witness_signature: "2G\316h\003\313f\332\327\230\020\376\266g=\344\316\325l\216/\032\312\216\374\002\267\231\006\253\257d\r\236\0260\306\363\027l\311\200\345\321e6\227\001\000\203\204\374-y\340\271\030\247V\"\306ee\313\001"
  }
  blockid: "\000\000\000\000\000\324\334\004p\253\317\222=\352@\266\361\210\3548\305}Ge\247\314\245\347+`\222\020"
```

# getTransactionByIdSolidity

Get transaction receipt info from a transaction id, must be in solid block.  

### Usage

```
getTransactionByIdSolidity(txID)
```

### Parameter

| Parameter | Description                            | Type   |
| :-------- | :------------------------------------- | :----- |
| txID      | Transaction hash, i.e. transaction id. | String |

### Return

Transaction object.  

### Exception

IllegalException, if the parameters are not correct(e.g. the specified transaction has not been solidified).  

### Example

```
wrapper.getTransactionByIdSolidity("3535304212e0090d421ec88cd194d35875b748c0ad453fcde6d7b4d43e852ced");
```

Execution result:

```
raw_data {
    ref_block_bytes: "\033s"
    ref_block_hash: "v7k\340\f\2049I"
    expiration: 1606474623000
    contract {
      type: TriggerSmartContract
      parameter {
        type_url: "type.googleapis.com/protocol.TriggerSmartContract"
        value: "\n\025A\316\270\245#a\242\257\363y\247\263\005\300\263R6\030\233\331\210\022\025A\251\216\262\025\032l\234\'L\a\371\307\344\270n\004\025\367\265o\"$.\032}M\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\017B@"
      }
    }
    timestamp: 1606474566312
    fee_limit: 20000000
  }
  signature: "J\363Af\3045\314;\206\330\f\321\227\026\325\002\a\360w\254P\006\027\310\202\311\376g\210\316\252\230Yu\316\376\331|\206\331\301\017+\355\324\221>N\216\243\343T\243&\021\305j\364\246e\214\252o`\000"
  ret {
    contractRet: REVERT
  }
```

# getRewardSolidity

Get the rewards that the voter has not received. 

### Usage

```
getRewardSolidity(address)
```

### Parameter

| Parameter | Description                                | Type   |
| :-------- | :----------------------------------------- | :----- |
| address   | Account address, Base58check or HEX format | String |

### Return

NumberMessage object.  

### Example

```
wrapper.getRewardSolidity("TKryTFSUB2UY8jMVc3Rz3ofiUPrnR6pRAs");
```

Execution result:

```
num: 3026824349948
```
