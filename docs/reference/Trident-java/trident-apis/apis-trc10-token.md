---
title: TRC10 Token
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
# getAssetIssueByAccount

Query the TRC10 token information issued by an account.

### Usage

```
getAssetIssueByAccount(address)
```

### Parameter

| Parameter | Description                                                  | Type   |
| :-------- | :----------------------------------------------------------- | :----- |
| address   | Address, the Token Issuer account address, default hexString | String |

### Return

AssetIssueList object.

### Example

```
wrapper.getAssetIssueByAccount("TD9tMPSfBJ3To8s71vdBz2BLT2wwBNWyLc");
```

Execution result：

```
assets {
    owner_address: "A\"\355b\226~\320\322\030k/\3069\327\227-\027*\225\310U"
    name: "lsp1"
    abbr: "saf1"
    total_supply: 100000000
    frozen_supply {
      frozen_amount: 1
      frozen_days: 1
    }
    trx_num: 1
    precision: 6
    num: 1000
    start_time: 1609833139923
    end_time: 1610833137923
    description: "newlsp"
    url: "sadf"
    free_asset_net_limit: 1
    public_free_asset_net_limit: 2
    id: "1000204"
  }
```

# getAssetIssueById

Query a token by token id.

### Usage

```
getAssetIssueById(assetId)
```

### Parameter

| Parameter | Description               | Type   |
| :-------- | :------------------------ | :----- |
| assetId   | The ID of the TRC10 token | String |

### Return

AssetIssueContract object.

### Example

```
wrapper.getAssetIssueById("1000200");
```

Execution result：

```
owner_address: "Aw\326^\303g\274`\360\216\276\327\302k\023\274\226\232S\364\217"
  name: "lsp"
  abbr: "saf"
  total_supply: 1
  frozen_supply {
    frozen_amount: 1
    frozen_days: 1
  }
  trx_num: 1
  precision: 1
  num: 1000
  start_time: 1609826985753
  end_time: 1610826983753
  description: "stest-assetissue"
  url: "7777772e6578616d706c652e636f6d"
  free_asset_net_limit: 100000
  public_free_asset_net_limit: 1
  id: "1000200"
```

# getAssetIssueList

Query the list of all the TRC10 tokens.

### Usage

```
getAssetIssueList()
```

### Parameter

None

### Return

AssetIssueList object.

### Example

```
wrapper.getAssetIssueList();
```

Execution result：

```
assets {
    owner_address: "A~\225\344_Z`\314E\362\320\257\343~\351\367\177\270\316\237\377"
    name: "tronlink_token"
    abbr: "tronlink_token"
    total_supply: 1000000000000000
    frozen_supply {
      frozen_amount: 1
      frozen_days: 1
    }
    trx_num: 1
    precision: 6
    num: 1
    start_time: 1574757000000
    end_time: 1757595000000
    description: "Description"
    url: "https://blog.csdn.net/u010270891/article/details/82978260"
    free_asset_net_limit: 1000
    public_free_asset_net_limit: 2000
    id: "1000001"
  }
 ...
```

# getPaginatedAssetIssueList

Query the list of all the tokens by pagination.

### Usage

```
getPaginatedAssetIssueList(offset, limit)
```

### Parameter

| Parameter | Description                   | Type |
| :-------- | :---------------------------- | :--- |
| offset    | The index of the start token  | long |
| limit     | The amount of tokens per page | long |

### Return

AssetIssueList object.

### Example

```
wrapper.getPaginatedAssetIssueList(0,20);
```

Execution result：

```
assets {
    owner_address: "A\250\251\006\315\235^\177\363\344r\323L\245hD\034\356\264\317["
    name: "00Dice"
    abbr: "0x0"
    total_supply: 1000000000000000000
    trx_num: 1000000
    precision: 6
    num: 100000000
    start_time: 1592841600000
    end_time: 1592928000000
    description: "\347\224\250\344\272\216\346\265\213\350\257\225"
    url: "https://www.baidu.com"
    id: "1000052"
  }
  ...
```

# TransferTrc10

Transfers TRC10 Asset.

### Usage

```
transferTrc10(fromAddress, toAddress, tokenId, amount)
```

### Parameter

| Parameter   | Description                                    | Type   |
| :---------- | :--------------------------------------------- | :----- |
| fromAddress | fromAddress is the owner address               | String |
| toAddress   | toAddress is the recipient address             | String |
| tokenId     | Asset name                                     | int    |
| amount      | Amount is the amount of TRX to transfer in SUN | int    |

### Return

TransactionExtention, including execution results.

### Exception

IllegalException, if fail to transfer trc10.

### Example

```
TransactionExtention transactionExtention = wrapper.transferTrc10("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm", "TP8LKAf3R3FHDAcrQXuwBEWmaGrrUdRvzb",
                    1000016, 1_000_000);
Transaction signedTxn = wrapper.signTransaction(transactionExtention);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
ad42e2116d30cd55c9c9bb6b01ba940cdc411ca5c052454c66951f58eef79372
```

# createAssetIssue

Issue a token.

### Usage

```
createAssetIssue(ownerAddress, name, abbr, totalSupply, trxNum, icoNum, startTime, endTime, url, freeAssetNetLimit, publicFreeAssetNetLimit, precision, frozenSupply, description)
```

### Parameter

| Parameter               | Description                                   | Type   |
| :---------------------- | :-------------------------------------------- | :----- |
| ownerAddress            | Owner address, default hexString              | String |
| name                    | Token name, default hexString                 | String |
| abbr                    | Token name abbreviation, default hexString    | String |
| totalSupply             | Token total supply                            | long   |
| trxNum                  | Define the price by the ratio of trx\_num/num | int    |
| icoNum                  | Define the price by the ratio of trx\_num/num | int    |
| startTime               | ICO start time                                | long   |
| endTime                 | ICO end time                                  | long   |
| url                     | Token official website url, default hexString | String |
| freeAssetNetLimit       | total free bandwidth for the token            | long   |
| publicFreeAssetNetLimit | free bandwidth for each token holder          | long   |
| precision               | -                                             | int    |
| frozenSupply            | HashMap\<frozenDay, frozenAmount>             | -      |
| description             | Token description, default hexString          | String |

### Return

TransactionExtention object.

### Exception

IllegalException, if fail to create AssetIssue.

### Example

```
long start = System.currentTimeMillis() + 2000;
long end = System.currentTimeMillis() + 1000000000;
HashMap<String, String> frozenSupply = new HashMap<String, String>();
frozenSupply.put("1","1");
frozenSupply.put("2","1");
frozenSupply.put("3","2");
TransactionExtention transaction = wrapper.createAssetIssue("TJ3Zyr26kzS8wRGz7aWYGgenMcqkUuPzLf","name", "saf1",100000000L, 1, 1000,start,end,"7777772e6578616d706c652e636f6d",
                    100000L,1L,6,frozenSupply,"stest-assetissue");
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
ff88e516799642161ca100bfcd3b67226793f003048c49e04aaaf48b8f5b6477
```

# participateAssetIssue

Participate a token.

### Usage

```
participateAssetIssue(toAddress, ownerAddress, assetName, amount)
```

### Parameter

| Parameter    | Description                                        | Type   |
| :----------- | :------------------------------------------------- | :----- |
| toAddress    | The issuer address of the token, default hexString | String |
| ownerAddress | The participant address, default hexString         | String |
| assetName    | Token id, default hexString                        | String |
| amount       | Participate token amount                           | long   |

### Return

TransactionExtention object.

### Exception

IllegalException, if fail to participate AssetIssue.

### Example

```
TransactionExtention transaction = wrapper.participateAssetIssue("TJ3Zyr26kzS8wRGz7aWYGgenMcqkUuPzLf","TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm","1000251", 1L);
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
8ae5067d3b2b822e7de3cfeb5df19bb9d1c8af2de5d9163ddc96d81baf7af58b
```

# unfreezeAsset

Unstake a token that has passed the minimum stake duration.

### Usage

```
unfreezeAsset(ownerAddress)
```

### Parameter

| Parameter    | Description                      | Type   |
| :----------- | :------------------------------- | :----- |
| ownerAddress | Owner address, default hexString | String |

### Return

TransactionExtention object.

### Exception

IllegalException, if fail to unstake asset.

### Example

```
TransactionExtention transaction = wrapper.unfreezeAsset("TJ3Zyr26kzS8wRGz7aWYGgenMcqkUuPzLf");
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
3baeafe39df63f6125dabfc317977498fb6f30933da2c5e6610dcbee1cfc9437
```

# updateAsset

Update basic TRC10 token information.

### Usage

```
updateAsset(ownerAddress, description, url, newLimit, newPublicLimit)
```

### Parameter

| Parameter      | Description                                 | Type   |
| :------------- | :------------------------------------------ | :----- |
| ownerAddress   | Owner address, default hexString            | String |
| description    | The description of token, default hexString | String |
| url            | The token's website url, default hexString  | String |
| newLimit       | Each token holder's free bandwidth          | int    |
| newPublicLimit | The total free bandwidth of the token       | int    |

### Return

TransactionExtention object.

### Exception

IllegalException, if fail to update asset.

### Example

```
TransactionExtention transaction = wrapper.updateAsset("TD9tMPSfBJ3To8s71vdBz2BLT2wwBNWyLc","newname","sadf", 1,2);
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
9a1234914e3ed5926d4f14584745514006be523adacd5cc208991018d5d31084
```

# getAssetIssueByName

Query a token by token name.

### Usage

```
getAssetIssueByName(name)
```

### Parameter

| Parameter | Description                 | Type   |
| :-------- | :-------------------------- | :----- |
| name      | The name of the TRC10 token | String |

### Return

AssetIssueContract object.

### Example

```
wrapper.getAssetIssueByName("name");
```

Execution result：

```
owner_address: "AX\224.\275P\223\324\313\344\241\365N\300\3470bXx\301{"
  name: "name"
  abbr: "saf1"
  total_supply: 100000000
  frozen_supply {
    frozen_amount: 1
    frozen_days: 1
  }
  ...
  trx_num: 1
  precision: 6
  num: 1000
  start_time: 1614768027088
  end_time: 1615768025088
  description: "stest-assetissue"
  url: "7777772e6578616d706c652e636f6d"
  free_asset_net_limit: 100000
  public_free_asset_net_limit: 1
  id: "1000251"
```

# getAssetIssueListByName

Query the list of all the TRC10 tokens by token name.

### Usage

```
getAssetIssueListByName(name)
```

### Parameter

| Parameter | Description                 | Type   |
| :-------- | :-------------------------- | :----- |
| name      | The name of the TRC10 token | String |

### Return

AssetIssueList object.

### Example

```
wrapper.getAssetIssueListByName("name");
```

Execution result：

```
owner_address: "AX\224.\275P\223\324\313\344\241\365N\300\3470bXx\301{"
  name: "name"
  abbr: "saf1"
  total_supply: 100000000
  frozen_supply {
    frozen_amount: 1
    frozen_days: 1
  }
  ...
  trx_num: 1
  precision: 6
  num: 1000
  start_time: 1614768027088
  end_time: 1615768025088
  description: "stest-assetissue"
  url: "7777772e6578616d706c652e636f6d"
  free_asset_net_limit: 100000
  public_free_asset_net_limit: 1
  id: "1000251"
```
