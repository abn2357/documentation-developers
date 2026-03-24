---
title: Account Resources
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
# getAccountResource

Query the resource information of an account(bandwidth,energy,etc).

### Usage

```
getAccountResource(address)
```

### Parameter

| Parameter | Description                        | Type   |
| :-------- | :--------------------------------- | :----- |
| address   | Address, HEX or Base58check format | String |

### Return

Object - AccountResourceMessage object.

### Example

```
wrapper.getAccountResource("TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b");
```

Execution result：

```
freeNetLimit: 5000
  assetNetUsed {
    key: "1000203"
    value: 0
  }
  assetNetLimit {
    key: "1000203"
    value: 100000
  }
  TotalNetLimit: 43200000000
  TotalNetWeight: 30001829306
  EnergyLimit: 13348
  TotalEnergyLimit: 90000000000
  TotalEnergyWeight: 13485132
```

# getAccountNet

Query bandwidth information.

### Usage

```
getAccountNet(address)
```

### Parameter

| Parameter | Description                        | Type   |
| :-------- | :--------------------------------- | :----- |
| address   | Address, HEX or Base58check format | String |

### Return

Object - AccountNetMessage object.

### Example

```
wrapper.getAccountNet("TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b");
```

Execution result：

```
freeNetLimit: 5000
  assetNetUsed {
    key: "1000203"
    value: 0
  }
  assetNetLimit {
    key: "1000203"
    value: 100000
  }
  TotalNetLimit: 43200000000
  TotalNetWeight: 30001829306
```

# freezeBalance

This interface has been deprecated, please use freezeBalanceV2 to stake TRX to obtain resources.

### Usage

```
freezeBalance(ownerAddress, frozenBalance, frozenDuration, resourceCode, receiveAddress)
```

### Parameter

| Parameter      | Description                                                             | Type   |
| :------------- | :---------------------------------------------------------------------- | :----- |
| ownerAddress   | Owner address, HEX or Base58check format                                | String |
| frozenBalance  | The amount of frozen TRX, the unit is sun                               | long   |
| frozenDuration | TRX stake duration, only be specified as 3 days                         | long   |
| resourceCode   | The type of the acquired resource，0 BANDWIDTH and 1 ENERGY              | int    |
| receiveAddress | Optional, the address that will receive the resource, default hexString | String |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention transaction = wrapper.freezeBalance("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm", 1_000_000L, 3L,1,"TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b");
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
557c9975c5db33d33c634c307a3ce05477c56cb124df94f1cbd8af247d6dd017
```

# unfreezeBalance

Unstake the staked TRX.

### Usage

```
unfreezeBalance(ownerAddress, resourceCode, receiveAddress)
```

### Parameter

| Parameter      | Description                                                             | Type   |
| :------------- | :---------------------------------------------------------------------- | :----- |
| ownerAddress   | Owner address, HEX or Base58check format                                | String |
| resourceCode   | Resource type，0 BANDWIDTH and 1 ENERGY                                  | int    |
| receiveAddress | Optional, the address that will receive the resource, default hexString | String |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention transaction = wrapper.unfreezeBalance("TFRgpvvNTe8bwC666D6orYhEkCcYsbax8U", 0);
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
48f7cd24b548de95d58a65b74aeeb5413e4d8a4638e40ec1fbfb212aeded7419
```

# getDelegatedResource

Returns all resources delegations from an account to another account. The fromAddress can be retrieved from the GetDelegatedResourceAccountIndex API.

### Usage

```
getDelegatedResource(fromAddress, toAddress)
```

### Parameter

| Parameter   | Description                                      | Type   |
| :---------- | :----------------------------------------------- | :----- |
| fromAddress | Resource from address, Hex or Base58check format | String |
| toAddress   | Resource to address, Hex or Base58check format   | String |

### Return

DelegatedResourceList - Delegation information.

### Example

```
wrapper.getDelegatedResource("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm","TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b");
```

Execution result:

```
delegatedResource {
    from: "Aw\326^\303g\274`\360\216\276\327\302k\023\274\226\232S\364\217"
    to: "A\201ok\226\373\273*C\253\307py\242c\312\315\215kSz"
    frozen_balance_for_energy: 2000000
    expire_time_for_energy: 1615020525000
  }
```

# getDelegatedResourceAccountIndex

Query the energy delegation by an account. i.e. list all addresses that have delegated resources to an account.

### Usage

```
getDelegatedResourceAccountIndex(address)
```

### Parameter

| Parameter | Description                                | Type   |
| :-------- | :----------------------------------------- | :----- |
| address   | Account address, Hex or Base58check format | String |

### Return

DelegatedResourceAccountIndex - The resource delegation index object.

### Example

```
DelegatedResourceAccountIndex accountIndex = wrapper.getDelegatedResourceAccountIndex("TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm");
ByteString account = accountIndex.getAccount();
int fromAccountsCount = accountIndex.getFromAccountsCount();
for(int i =0;i<fromAccountsCount;i++){
    ByteString fromAccounts = accountIndex.getFromAccounts(i);
}
int toAccountsCount = accountIndex.getToAccountsCount();
for(int i =0;i<toAccountsCount;i++){
    ByteString toAccounts = accountIndex.getToAccounts(i);
}
```

Execution result:

```
Accounts: TLtrDb1udekjDumnrf3EVeke3Q6pHkZxjm
toAccounts: TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b
```

# freezeBalanceV2

In Stake2.0, Stake an amount of TRX to obtain bandwidth or energy, and obtain equivalent TRON Power(TP) according to the staked amount.

### Usage

```
freezeBalanceV2(ownerAddress, frozenBalance, resourceCode)
```

### Parameter

| Parameter     | Description                                                                          | Type   |
| :------------ | :----------------------------------------------------------------------------------- | :----- |
| ownerAddress  | The address of the account that initiated the transaction, HEX or Base58check format | String |
| frozenBalance | The amount of frozen TRX, the unit is sun                                            | long   |
| resourceCode  | The type of the acquired resource，0 BANDWIDTH and 1 ENERGY                           | int    |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention txnExt =client.freezeBalanceV2("41C9B9110BD5F6697075659AB3AAF6107840A9D96D",10000000,1);
System.out.println("txn id => " + Hex.toHexString(txnExt.getTxid().toByteArray()));
Transaction signedTxn = client.signTransaction(txnExt);
TransactionReturn ret = client.blockingStub.broadcastTransaction(signedTxn);
System.out.println("======== Result ========\n" + ret.toString());
```

Execution result：

```
txn id => 6d5a3492516db8008ce11b8db7c7b1d514e003f4fcb6a7bcbf2c792485eaa746
======== Result ========
result: true
```

# unfreezeBalanceV2

in Stake2.0, Unstake TRX to release bandwidth and energy and at the same time TRON Power will be reclaimed and corresponding votes will be revoked.

### Usage

```
unfreezeBalanceV2(ownerAddress, unfreezeBalance, resourceCode)
```

### Parameter

| Parameter       | Description                                                                          | Type   |
| :-------------- | :----------------------------------------------------------------------------------- | :----- |
| ownerAddress    | The address of the account that initiated the transaction, HEX or Base58check format | String |
| unfreezeBalance | The amount of TRX to unstake, in sun                                                 | long   |
| resourceCode    | Resource type，0 BANDWIDTH and 1 ENERGY                                               | int    |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention txnExt2 =client.unfreezeBalanceV2("41C9B9110BD5F6697075659AB3AAF6107840A9D96D",700000000,1);
System.out.println("txn2 id => " + Hex.toHexString(txnExt2.getTxid().toByteArray()));
Transaction signedTxn2 = client.signTransaction(txnExt2);
TransactionReturn ret2 = client.blockingStub.broadcastTransaction(signedTxn2);
System.out.println("======== Result ========\n" + ret2.toString());
```

Execution result：

```
txn2 id => af0748c673940f71068c5519cf0af582c3d5c7c386d34e9f2d354e6b9e62c197
======== Result ========
result: true
```

# delegateResource

Delegate bandwidth or energy resources to other accounts in Stake2.0.

### Usage

```
delegateResource( ownerAddress,  balance,  resourceCode, receiverAddress, lock)
```

### Parameter

| Parameter       | Description                                                                                                                                                                                                                                                                                                    | Type    |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| ownerAddress    | Owner address, Hex or Base58check format                                                                                                                                                                                                                                                                       | String  |
| balance         | Amount of TRX staked for resources to be delegated, unit is sun                                                                                                                                                                                                                                                | long    |
| resourceCode    | Resource type，0 BANDWIDTH and 1 ENERGY                                                                                                                                                                                                                                                                         | int     |
| receiverAddress | Receiver address of resource to be delegated to, Hex or Base58check format                                                                                                                                                                                                                                     | String  |
| lock            | Whether it is locked, if it is set to true, the delegated resources cannot be undelegated within 3 days. When the lock time is not over, if the owner delegates the same type of resources using the lock to the same address, the lock time will be reset to 3 days. optional, default is 0, 0-lock, 1-unlock | boolean |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention txnExt3 =client.delegateResource("41C9B9110BD5F6697075659AB3AAF6107840A9D96D",100999990,1,"41715AE2D2B73B5B4885F480BFBA04CBE6D61E6824",false);
System.out.println("txn3 id => " + Hex.toHexString(txnExt3.getTxid().toByteArray()));
Transaction signedTxn3 = client.signTransaction(txnExt3);
TransactionReturn ret3 = client.blockingStub.broadcastTransaction(signedTxn3);
System.out.println("======== Result ========\n" + ret3.toString());
```

Execution result：

```
txn3 id => f8f59725c2282d5f25443e32c606c97ec30602ae0310cb562e6529f63decd4bb
======== Result ========
result: true
```

# undelegateResource

Cancel the delegation of bandwidth or energy resources to other accounts in Stake2.0.

### Usage

```
undelegateResource( ownerAddress,  balance,  resourceCode, receiverAddress)
```

### Parameter

| Parameter       | Description                                                                          | Type   |
| :-------------- | :----------------------------------------------------------------------------------- | :----- |
| ownerAddress    | the address of the account that initiated the transaction, Hex or Base58check format | String |
| balance         | Amount of TRX staked for resource to be undelegated, unit is sun                     | long   |
| resourceCode    | Resource type，0 BANDWIDTH and 1 ENERGY                                               | int    |
| receiverAddress | Receiver address of resource to be delegated to, Hex or Base58check format           | String |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention txnExt4 =client.undelegateResource("41C9B9110BD5F6697075659AB3AAF6107840A9D96D",100999940,1,"41715AE2D2B73B5B4885F480BFBA04CBE6D61E6824");
System.out.println("txn4 id => " + Hex.toHexString(txnExt4.getTxid().toByteArray()));
Transaction signedTxn4 = client.signTransaction(txnExt4);
TransactionReturn ret4 = client.blockingStub.broadcastTransaction(signedTxn4);
System.out.println("======== Result ========\n" + ret4.toString());
```

Execution result：

```
txn4 id => 1f7096bb68a4c743e606544cfd58b301bdf6f2a5a8ec81fa20243b1f4fcd802a
======== Result ========
result: true
```

# withdrawExpireUnfreeze

Withdraw unfrozen balance in Stake2.0.

### Usage

```
withdrawExpireUnfreeze(ownerAddress)
```

### Parameter

| Parameter    | Description                                | Type   |
| :----------- | :----------------------------------------- | :----- |
| ownerAddress | Account address, Hex or Base58check format | String |

### Return

Object - TransactionExtention: unsigned transaction information.

### Example

```
TransactionExtention txnExt5 =client.withdrawExpireUnfreeze("41C9B9110BD5F6697075659AB3AAF6107840A9D96D");
System.out.println("txn5 id => " + Hex.toHexString(txnExt5.getTxid().toByteArray()));
Transaction signedTxn5 = client.signTransaction(txnExt5);
TransactionReturn ret5 = client.blockingStub.broadcastTransaction(signedTxn5);
System.out.println("======== Result ========\n" + ret5.toString());
```

Execution result：

```
txn5 id => d09c82ea7aa664dd7a617ee347c2e1664171a84cd674d5bd028a12ec338a2e11
======== Result ========
result: true
```

# getAvailableUnfreezeCount

Remaining times of executing unstake operation in Stake2.0.

### Usage

```
getAvailableUnfreezeCount( ownerAddress)
```

### Parameter

| Parameter    | Description                                | Type   |
| :----------- | :----------------------------------------- | :----- |
| ownerAddress | Account address, Hex or Base58check format | String |

### Return

int - count: remaining times of executing unstake operation.

### Example

```
long count =client.getAvailableUnfreezeCount("41C9B9110BD5F6697075659AB3AAF6107840A9D96D");
System.out.println("count => "+count);
```

Execution result：

```
count => 31
```

# getCanWithdrawUnfreezeAmount

Query the withdrawable balance in Stake2.0.

### Usage

```
getCanWithdrawUnfreezeAmount(ownerAddress)
```

### Parameter

| Parameter    | Description                                | Type   |
| :----------- | :----------------------------------------- | :----- |
| ownerAddress | Account address, Hex or Base58check format | String |

### Return

long - amount: the withdrawable balance.

### Example

```
long amount =client.getCanWithdrawUnfreezeAmount("41C9B9110BD5F6697075659AB3AAF6107840A9D96D");
System.out.println("amount => "+amount);
```

Execution result：

```
amount => 0
```

# getCanDelegatedMaxSize

in Stake2.0, query the amount of delegatable resources share of the specified resource type for an address, unit is sun.

### Usage

```
getCanDelegatedMaxSize(ownerAddress, type)
```

### Parameter

| Parameter    | Description                                | Type   |
| :----------- | :----------------------------------------- | :----- |
| ownerAddress | Account address, Hex or Base58check format | String |
| type         | resource type, 0 is bandwidth, 1 is energy | int    |

### Return

long - maxSize: the amount of delegatable resources share.

### Example

```
long maxSize =client.getCanDelegatedMaxSize("41C9B9110BD5F6697075659AB3AAF6107840A9D96D",1);
System.out.println("maxSize => "+maxSize);
```

Execution result: 

```
maxSize => 321999830
```

# getDelegatedResourceV2

Query the detail of resource share delegated from fromAddress to toAddress in Stake2.0.

### Usage

```
getDelegatedResourceV2(fromAddress, toAddress)
```

### Parameter

| Parameter   | Description                                      | Type   |
| :---------- | :----------------------------------------------- | :----- |
| fromAddress | Resource from address, Hex or Base58check format | String |
| toAddress   | Resource to address, Hex or Base58check format   | String |

### Return

DelegatedResourceList - Delegation information.

### Example

```
Response.DelegatedResourceList delegatedResourceList =client.getDelegatedResourceV2("41C9B9110BD5F6697075659AB3AAF6107840A9D96D","41715AE2D2B73B5B4885F480BFBA04CBE6D61E6824");
System.out.println("delegatedResourceList => "+delegatedResourceList);
```

Execution result:

```
delegatedResourceList => delegatedResource {
 from: "A\311\271\021\v\325\366ipue\232\263\252\366\020x@\251\331m"
 to: "AqZ\342\322\267;[H\205\364\200\277\272\004\313\346\326\036h$"
 frozen_balance_for_energy: 7000169
}
```

# getDelegatedResourceAccountIndexV2

Query the resource delegation index by an account in Stake2.0. Two lists will return, one is the list of addresses the account has delegated its resources(toAddress), and the other is the list of addresses that have delegated resources to the account(fromAddress).

### Usage

```
getDelegatedResourceAccountIndexV2(address)
```

### Parameter

| Parameter | Description                                | Type   |
| :-------- | :----------------------------------------- | :----- |
| address   | Account address, Hex or Base58check format | String |

### Return

DelegatedResourceAccountIndex - The resource delegation index object.

### Example

```
Response.DelegatedResourceAccountIndex delegatedResourceAccountIndex =client.getDelegatedResourceAccountIndexV2("41715AE2D2B73B5B4885F480BFBA04CBE6D61E6824");
System.out.println("delegatedResourceAccountIndex => "+delegatedResourceAccountIndex);
```

Execution result:

```
delegatedResourceAccountIndex => account: "AqZ\342\322\267[H\205\364\200\277\272\004\313\346\326\036h$"
fromAccounts: "A\311\271\021\v\325\366ipue\232\263\252\366\020x@\251\331m"
```
