---
title: Accounts
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
# createAccount

Create an account. Uses an already activated account to create a new account.

### Usage

```
createAccount(ownerAddress, accountAddress)
```

### Parameter

| Parameter      | Type   | Description                                                           |
| :------------- | :----- | :-------------------------------------------------------------------- |
| ownerAddress   | String | owner address, an activated account, default hex string               |
| accountAddress | String | account address, the address of the new account, default in hexString |

If the creator account has sufficient bandwidth obtained through TRX staking, then creating an account will consume only bandwidth; otherwise, 0.1 TRX will be burnt to pay for bandwidth, while also requiring a fixed number of 1 TRX.

### Return

TransactionExtention, including execution results.

### Exception

IllegalException, if fail to create an account.

### Example

```
TransactionExtention transaction = wrapper.createAccount("TMmbeRPnFhXC7BPLaF2M1HCsoE4jwZNB7b","TD9tMPSfBJ3To8s71vdBz2BLT2wwBNWyLc");
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
6f85a7721cc9acd80a3de5e41ffdbc8c1eb65304732836321165daa9efc6e235
```

# getAccount

Get account info by address.

### Usage

```
getAccount(address)
```

### Parameter

| Parameter | Description                | Type   |
| :-------- | :------------------------- | :----- |
| address   | Address, default hexString | String |

### Return

Account object.

### Example

```
wrapper.getAccount("TKwVM5tsELuTE3a5SUCWiQyVtEgxejL5Wj");
```

Execution result：

```
account_name: "123"
  address: "A\"\355b\226~\320\322\030k/\3069\327\227-\027*\225\310U"
  balance: 3876000001
  create_time: 1608876732000
  latest_opration_time: 1611729843000
  asset_issued_name: "lsp1"
  latest_consume_free_time: 1611729843000
  account_resource {
  }
  owner_permission {
    ...
  }
  active_permission {
    ...
  }
  assetV2 {
    ...
  }
  asset_issued_ID: "1000204"
  free_asset_net_usageV2 {
    ...
  }
```

# updateAccount

Modify the account name, you can update it only if the name is empty.

### Usage

```
updateAccount(address, accountName)
```

### Parameter

| Parameter   | Description                      | Type   |
| :---------- | :------------------------------- | :----- |
| address     | Owner address, default hexString | String |
| accountName | The name of the account          | String |

### Return

TransactionExtention, including execution results.

### Exception

IllegalException, if fail to update account name.

### Example

```
TransactionExtention transaction = wrapper.updateAccount("TJ3Zyr26kzS8wRGz7aWYGgenMcqkUuPzLf","name");
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
8178774ae66b12b72fe5c3db6ec864e9a959bfee2c470af56701ae498288c014
```

# accountPermissionUpdate

Update the account permission, including the three privilege levels of the owner, witness, and active privilege.

### Usage

```
accountPermissionUpdate(contract)
```

### Parameter

| Parameter | Description                            | Type                            |
| :-------- | :------------------------------------- | :------------------------------ |
| contract  | AccountPermissionUpdateContract object | AccountPermissionUpdateContract |

### Return

TransactionExtention object.

### Exception

IllegalException, if fail to update account permission.

### Example

```
AccountPermissionUpdateContract.Builder builder = AccountPermissionUpdateContract.newBuilder();
Permission ownerPermission = null;
Permission.Builder builderOwner = Permission.newBuilder();
builderOwner.setTypeValue(0);
builderOwner.setPermissionName("owner");
builderOwner.setThreshold(1);

Common.Key.Builder keyOwner = Common.Key.newBuilder();
keyOwner.setAddress(wrapper.parseAddress("4122ED62967ED0D2186B2FC639D7972D172A95C855"));
keyOwner.setWeight(1);
builderOwner.addKeys(keyOwner);
ownerPermission = builderOwner.build();

Permission activePermissions = null;
Permission.Builder builderActive = Permission.newBuilder();
builderActive.setTypeValue(2);
builderActive.setThreshold(1);
builderActive.setPermissionName("active0");
builderActive.setOperations(wrapper.parseAddress("7fff1fc0037e0000000000000000000000000000000000000000000000000000"));
       
Common.Key.Builder keyActive = Common.Key.newBuilder();
keyActive.setAddress(wrapper.parseAddress("4122ED62967ED0D2186B2FC639D7972D172A95C855"));
keyActive.setWeight(1);

builderActive.addKeys(keyActive);
activePermissions = builderActive.build();

builder.setOwner(ownerPermission);
builder.addActives(activePermissions);
builder.setOwnerAddress(wrapper.parseAddress("4122ED62967ED0D2186B2FC639D7972D172A95C855"));

TransactionExtention transaction = wrapper.accountPermissionUpdate(builder.build());
Transaction signedTxn = wrapper.signTransaction(transaction);
String ret = wrapper.broadcastTransaction(signedTxn);
```

Execution result：

```
f055632620e3c16d6376ecdcee8e3b077e203f4d52e2c5e29228d44d419bed4c
```
