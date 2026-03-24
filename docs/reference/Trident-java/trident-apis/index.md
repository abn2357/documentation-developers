---
title: APIs
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
## Data decoding for API returns

The type of data returned by calling the API interface is divided into various types. The specific analysis methods for each type of data are described below.

### Address Type

```shell
witness_address: "A\327\261fa\251h\340\271\030\252\245\266\275\3548FF\254\270\330"
```

The analysis method is as follows:

```java
ByteString byteString = block.getBlockHeader().getRawData().getWitnessAddress();
        
String witnessAddress= wrapper.Base58Check.bytesToBase58(byteString.toByteArray());
```

### Transaction.raw\_data.contract.parameter.value

```shell
raw_data {
  ref_block_bytes: "Q\001"
  ref_block_hash: "\033\373\\/\017\261-\'"
  expiration: 1618904781000
  contract {
    type: TransferContract
    parameter {
      type_url: "type.googleapis.com/protocol.TransferContract"
      value: "\n\025A\201ok\226\373\273*C\253\307py\242c\312\315\215kSz\022\025A\220S{\226\371R3\247\\\310\246\036\311\237\270\267\f\214\036O\030\300\204="
    }
  }
  timestamp: 1618904723116
}
```

The analysis method is as follows:

```java
// Contract type is determined by Transaction.raw_data.contract.type 
TransferContract transferContract = contractParameter.unpack(TransferContract.class);
```

### Other Type

```shell
parentHash: "\000\000\000\000\000\347\222\344\"O\017\274\235x\252He\217;\215\270\361v\362\276\037rg\312{yl"
```

The analysis method is as follows:

```java
String parentHash = wrapper.toHex(block.getBlockHeader().getRawData().getParentHash());
```
