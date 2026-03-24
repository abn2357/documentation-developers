---
title: Account Permission Management
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Introduction

[Account permission management](https://github.com/tronprotocol/TIPs/blob/master/tip-16.md) allows for permission grading, and each permission is associated with multiple private keys. This makes it possible to achieve multi-person joint control of a single account, with different permissions managed by different people. This guide will walk you through the design and implementation of TRON's account permission management feature.

# Design

This scheme includes three permission levels: **owner**, **witness**, and **active**:

* Owner permission has the authority to execute all contracts;
* Witness permission is used by Super Representatives (SRs);
* Active permission is a custom permission group that can include different permission sets.

## Structure Description

**1. Account Modification**

```
message Account { 
   ... 
   Permission owner_permission = 31;
   Permission witness_permission = 32;
   repeated Permission active_permission = 33;
 }
```

Three permission attributes are added to the account structure, namely `owner_permission`, `witness_permission`, and `active_permission`, where `active_permission` is a list and can include up to 8 items.

**2. Contract Type Modification**

```
message Transaction {
   message Contract {
     enum ContractType { 
       AccountCreateContract = 0; 
       ... 
       AccountPermissionUpdateContract = 46; 
       }
     }  
   }
 }
```

Added a transaction type `AccountPermissionUpdateContract` to update account permissions.

**3. AccountPermissionUpdateContract**

```
message AccountPermissionUpdateContract {
   bytes owner_address = 1;
   Permission owner = 2;   
   Permission witness = 3; 
   repeated Permission actives = 4; 
 }
```

| Parameter       | Description                                                  |
| :-------------- | :----------------------------------------------------------- |
| `owner_address` | The address of the account to be modified                    |
| `owner`         | The modified owner permission                                |
| `witness`       | The modified witness permission (if it is a witness account) |
| `actives`       | The modified active permission                               |

This interface will override the original account permissions, so even if you only want to modify the owner permission, you still need to configure the witness (if it is a witness account) and active permissions.

**4. Permission**

```
message Permission {
   enum PermissionType {
     Owner = 0;
     Witness = 1;
     Active = 2;
   }
   PermissionType type = 1; 
   int32 id = 2;     
   string permission_name = 3;
   int64 threshold = 4;
   int32 parent_id = 5; 
   bytes operations = 6;  
   repeated Key keys = 7;// 
 }
```

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `PermissionType`
      </td>

      <td>
        The permission type. Currently only three types of permissions are supported.
      </td>
    </tr>

    <tr>
      <td>
        `id`
      </td>

      <td>
        This value is automatically set by the system, with owner's id=0 and witness' id=1. Active id is incremented from 2 onwards. When a contract is executed, the id is used to specify which permission to be used. For example, if the owner permission is used, `id` is set to `0`.
      </td>
    </tr>

    <tr>
      <td>
        `permission_name`
      </td>

      <td>
        The permission name, set by the user and limited to 32 bytes in length.
      </td>
    </tr>

    <tr>
      <td>
        `threshold`
      </td>

      <td>
        The threshold. The corresponding operation is allowed only when the sum of the weights of the participating signatures exceeds the threshold. The value cannot exceed the maximum value allowed by the Long type.
      </td>
    </tr>

    <tr>
      <td>
        `parent_id`
      </td>

      <td>
        Currently, this value can only be set to `0`.
      </td>
    </tr>

    <tr>
      <td>
        `operations`
      </td>

      <td>
        A total of 32 bytes (256 bits), each representing the permission of a contract ( `1` indicates the owner permission, i.e., the permission to execute the contract).  
        You can refer to the detailed example below: "Example of operations in active permissions"
      </td>
    </tr>

    <tr>
      <td>
        keys
      </td>

      <td>
        The addresses that jointly assume the permission and the corresponding weights. Up to 5 keys are allowed.
      </td>
    </tr>
  </tbody>
</Table>

**5. Key**

```
message Key {
   bytes address = 1;
   int64 weight = 2;
 }
```

| Parameter | Description                          |
| :-------- | :----------------------------------- |
| `address` | The address that owns the permission |
| `weight`  | The address's corresponding weight   |

**6. Transaction Modification**

```
message Transaction {
      ...
     int32 Permission_id = 5;
 }
```

Add a `Permission_id` field to the transaction, corresponding to `Permission.id`, which specifies which permission to be used. The default value is 0, indicating the owner permission. The value cannot be set to 1, because the witness permission is only used for block production, not transaction signing.

## Owner Permission

`OwnerPermission` is the highest privilege of an account. Users with the owner permission can adjust the ownership and permission structure of the account, as well as execute all contracts.

The owner permission has the following characteristics:

1. The address with `OwnerPermission` can modify the account's permissions.
2. When an account's `OwnerPermission` is empty, the account's address is assumed to have the owner permission by default.
3. When a new account is created, the address of the account is automatically filled into OwnerPermission, with the default threshold set to 1. The keys parameter only contains the account address and the corresponding weight 1.
4. During transaction execution, if `permissionId` is not specified, `OwnerPermission` is used by default.

## Witness Permission

SRs can use this permission to manage the block-producing nodes. Non-SR accounts do not have this permission.

Example of usage scenario: An SR deploys a block-producing node on the cloud server. To enhance account security, the SR can assign the block production permission to another address. Since the address only has the block production permission, even if the private key on the server is leaked, TRX will not be lost because the address has no TRX transfer permission.

SR's block production node configuration:

1. No special configuration is required when the witness permission is not modified.
2. When the witness permission of the SR is modified, the block-producing node needs to be reconfigured. The configuration items are as follows:

```
#config.conf

// Optional.The default is empty.
// It is used when the witness account has set the witnessPermission.
// When it is not empty, the localWitnessAccountAddress represents the address of the witness account,
// and the localwitness is configured with the private key of the witnessPermissionAddress in the witness account.
// When it is empty,the localwitness is configured with the private key of the witness account.
// Optional, default is empty.
// Used to set the durationPermission when the witness account is set.
// When the value is not empty, localWitnessAccountAddress represents the address of the witness account, and localwitness is the private key of the address in the durationPermission.
// When the value is empty, localwitness is configured as the private key of the witness account.

//localWitnessAccountAddress =

localwitness = [
  f4df789d...4c6a4f57 // Private Key, hex, 64 characters total
]
```

## Active Permissions

Active permission is used to provide a set of permission combinations, such as configuring a permission group to allocate an address only account creation and transfer permissions.

Active permission has the following features:

1. The address with `OwnerPermission` can modify active permissions.
2. The address with the permission to execute `AccountPermissionUpdateContract` can also modify active permissions.
3. You can specify up to 8 active permissions.
4. The ID of the permission is automatically incremented from 2.
5. When a new account is created, an active permission is automatically created, and the address of the account is filled. The default threshold is 1, and the keys parameter only contains the account address and the corresponding weight 1.

## Fees

1. The fee for updating account permission is 100 TRX, and the transaction type is `AccountPermissionUpdate`.
2. When a transaction requires multiple accounts' signatures, that is, the transaction includes two or more signatures, in addition to the transaction fee, an additional 1 TRX will be charged.
3. The above fees are dynamic parameters in the TRON network, and SRs can modify values of these fees by initiating a proposal vote.

# APIs

## Modify Permissions

`AccountPermissionUpdateContract`, the steps to modify permissions are as follows:

1. Use the interface `getaccount` to query the account and get the original permissions
2. Modify the permission
3. Create a contract and sign
4. Send a transaction

**http-demo**

```
http://{{host}}:{{port}}/wallet/accountpermissionupdate


{
  "owner_address": "41ffa9466d5bf6bb6b7e4ab6ef2b1cb9f1f41f9700",
  "owner": {
    "type": 0,
    "permission_name": "owner",
    "threshold": 2,
    "keys": [{
        "address": "41F08012B4881C320EB40B80F1228731898824E09D",
        "weight": 1
      },
      {
        "address": "41DF309FEF25B311E7895562BD9E11AAB2A58816D2",
        "weight": 1
      },
      {
        "address": "41BB7322198D273E39B940A5A4C955CB7199A0CDEE",
        "weight": 1
      }
    ]
  },
  "actives": [{
    "type": 2,
    "permission_name": "active0",
    "threshold": 3,
    "operations": "7fff1fc0037e0000000000000000000000000000000000000000000000000000",
    "keys": [{
        "address": "41F08012B4881C320EB40B80F1228731898824E09D",
        "weight": 1
      },
      {
        "address": "41DF309FEF25B311E7895562BD9E11AAB2A58816D2",
        "weight": 1
      },
      {
        "address": "41BB7322198D273E39B940A5A4C955CB7199A0CDEE",
        "weight": 1
      }
    ]
  }]
}

// For the definition and limitations of the parameter fields, please see Structure Description.
```

**Example of operations in active permissions**

"operations" is a hexadecimal-coded sequence (little-endian byte order) in 32 bytes (256 bits), and each bit represents the permission of a system contract type. The nth bit indicates the permission of the system contract type with ID `n` - its value 1 means that the permission to execute the specific type of operation is granted and the value 0 means the permission is not granted. The following table lists ID values of different system contract types:

| System Contract Type              | ID | Description                                                        |
| :-------------------------------- | :- | :----------------------------------------------------------------- |
| `AccountCreateContract`           | 0  | Create an account                                                  |
| `TransferContract`                | 1  | Transfer TRX                                                       |
| `TransferAssetContract`           | 2  | Transfer a TRC-10 token                                            |
| `VoteAssetContract`               | 3  | Unused                                                             |
| `VoteWitnessContract`             | 4  | Vote for an SR                                                     |
| `WitnessCreateContract`           | 5  | Apply to be an SR candidate                                        |
| `AssetIssueContract`              | 6  | Issue a TRC-10 token                                               |
| `WitnessUpdateContract`           | 8  | Update website URLs for an SR candidate                            |
| `ParticipateAssetIssueContract`   | 9  | Buy a TRC-10 token                                                 |
| `AccountUpdateContract`           | 10 | Update an account name                                             |
| `FreezeBalanceContract`           | 11 | Stake in Stake1.0                                                  |
| `UnfreezeBalanceContract`         | 12 | Unstake TRX staked in the Stake1.0                                 |
| `WithdrawBalanceContract`         | 13 | Withdraw rewards                                                   |
| `UnfreezeAssetContract`           | 14 | Unfreeze an issued TRC-10 token                                    |
| `UpdateAssetContract`             | 15 | Update TRC-10 token parameters                                     |
| `ProposalCreateContract`          | 16 | Create a proposal                                                  |
| `ProposalApproveContract`         | 17 | Approve a proposal                                                 |
| `ProposalDeleteContract`          | 18 | Delete a proposal                                                  |
| `SetAccountIdContract`            | 19 | Set an account ID                                                  |
| `CreateSmartContract`             | 30 | Create a smart contract                                            |
| `TriggerSmartContract`            | 31 | Trigger a smart contract                                           |
| `UpdateSettingContract`           | 33 | Update consume_user_resource_percent                               |
| `ExchangeCreateContract`          | 41 | Create an exchange                                                 |
| `ExchangeInjectContract`          | 42 | Inject assets to an exchange                                       |
| `ExchangeWithdrawContract`        | 43 | Withdraw assets from an exchange                                   |
| `ExchangeTransactionContract`     | 44 | Bancor transactions                                                |
| `UpdateEnergyLimitContract`       | 45 | Adjust the Energy limit provided by the smart contract deployer    |
| `AccountPermissionUpdateContract` | 46 | Update account permissions                                         |
| `ClearABIContract`                | 48 | Clear contract ABI                                                 |
| `UpdateBrokerageContract`         | 49 | Update SR Brokerage                                                |
| `ShieldedTransferContract`        | 51 | Shielded transactions                                              |
| `FreezeBalanceV2Contract`         | 54 | Stake TRX                                                          |
| `UnfreezeBalanceV2Contract`       | 55 | Unstake TRX                                                        |
| `WithdrawExpireUnfreezeContract`  | 56 | Withdraw the unstaked principal that has passed the lock-up period |
| `DelegateResourceContract`        | 57 | Delegate resources                                                 |
| `UnDelegateResourceContract`      | 58 | Cancel resource delegation                                         |
| `CancelAllUnfreezeV2Contract`     | 59 | Cancel all unstaking requests                                      |

For better understanding, take the binary big-endian byte order as an example to illustrate how to calculate the value of `operations`: The number of digits starts from 0, and corresponds to the ID of the system contract type from left to right.  Convert a binary big-endian byte sequence to a hexadecimal little-endian byte sequence, which will be the value of `operations`, as listed in the examples below:

| Operations Allowed                            | Binary Code (Big-Endian)       | Binary Code (Little-Endian)     | Hex Code (Little-Endian) |
| :-------------------------------------------- | :----------------------------- | :------------------------------ | :----------------------- |
| TransferContract(1) & VoteWitnessContract(4)  | 01001000 00000000 00000000 ... | 00010010 00000000 00000000 ...  | 12 00 00 ...             |
| TransferContract(1) & UpdateAssetContract(15) | 01000000 00000001 00000000 ... | 000000010 10000000 00000000 ... | 02 80 00 ...             |
| All system contracts                          | 11111110 11111111 11111000 ... | 01111111 11111111 00011111 ...  | 7F FF 1F ...             |

**Example of calculation of operations in active permissions**

```
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.bouncycastle.util.encoders.Hex;

enum ContractType {
  UndefinedType(-1),
  AccountCreateContract(0),
  TransferContract(1),
  TransferAssetContract(2),
  VoteAssetContract(3),
  VoteWitnessContract(4),
  WitnessCreateContract(5),
  AssetIssueContract(6),
  WitnessUpdateContract(8),
  ParticipateAssetIssueContract(9),
  AccountUpdateContract(10),
  FreezeBalanceContract(11),
  UnfreezeBalanceContract(12),
  WithdrawBalanceContract(13),
  UnfreezeAssetContract(14),
  UpdateAssetContract(15),
  ProposalCreateContract(16),
  ProposalApproveContract(17),
  ProposalDeleteContract(18),
  SetAccountIdContract(19),
  CustomContract(20),
  CreateSmartContract(30),
  TriggerSmartContract(31),
  GetContract(32),
  UpdateSettingContract(33),
  ExchangeCreateContract(41),
  ExchangeInjectContract(42),
  ExchangeWithdrawContract(43),
  ExchangeTransactionContract(44),
  UpdateEnergyLimitContract(45),
  AccountPermissionUpdateContract(46),
  ClearABIContract(48),
  UpdateBrokerageContract(49),
  ShieldedTransferContract(51),
  MarketSellAssetContract(52),
  MarketCancelOrderContract(53),
  FreezeBalanceV2Contract(54),
  UnfreezeBalanceV2Contract(55),
  WithdrawExpireUnfreezeContract(56),
  DelegateResourceContract(57),
  UnDelegateResourceContract(58),
  CancelAllUnfreezeV2Contract(59);

  private int num;

  ContractType(int num) { this.num = num; }

  public static ContractType getContractTypeByNum(int num) {
    for(ContractType type : ContractType.values()){
      if(type.getNum() == num)
        return type;
    }
    return ContractType.UndefinedType;
  }
  public int getNum() {
    return num;
  }
}

public class  operationsEncoderAndDecoder{

  // Description: get operations code according to the input contract types
  public static String operationsEncoder(ContractType[] contractId){

    List<ContractType> list = new ArrayList<ContractType>(Arrays.asList(contractId));
    byte[] operations = new byte[32];
    list.forEach(e -> {
      int num = e.getNum();
      operations[num / 8] |= (1 << num % 8);
    });

    return Hex.toHexString(operations);
  }

  // Description: get all allowable contract types according to the operations code
  public static List<String> operationsDecoder(String operations){

    List<String> contractIDs = new ArrayList<>();
    byte[] opArray = Hex.decode(operations);
    for(int i=0;i<32;i++) // 32 bytes
    {
      for(int j=0;j<8;j++)
      {
        if((opArray[i]>>j & 0x1) ==1) {
          contractIDs.add(ContractType.getContractTypeByNum(i*8+j).name());
        }
      }
    }
    return contractIDs;
  }

  public static void main(String[] args) {
    ContractType[] contractID = {ContractType.TransferContract, ContractType.VoteWitnessContract, ContractType.FreezeBalanceV2Contract };
    String operations = operationsEncoder(contractID);
    System.out.println(operations);
    // output: 1200000000004000000000000000000000000000000000000000000000000000

    List<String> contractIDs = operationsDecoder(operations);
    contractIDs.forEach(e ->{
      System.out.print(e + " ");
    });
    // output: TransferContract VoteWitnessContract FreezeBalanceV2Contract
  }
}
```

## Build & Execute a Transaction involving Different Permissions

1. Create a transaction, following the same process as a non-multiple signature transaction.
2. Specify Permission_id. The default value is 0, indicating the owner permission.
3. User A signs the transaction and then sends the signed transaction to B through other means.
4. User B signs the transaction and then sends the signed transaction to C via other means.  
   ...

   n. The last user who completed the signature broadcasts the transaction to the node.
   n+1. The node verifies if the sum of the weights of the signatures is greater than the threshold value and accept the transaction; otherwise, reject the transaction

```
n. The last user who completed the signature broadcasts the transaction to the node.
N+1. The node verifies if the sum of the weights of the signatures is greater than the threshold value and accept the transaction; otherwise, reject the transaction
```

For a detailed process, please refer to [How to create a transaction using different account permissions](/docs/multi-signature-example-process-flow).

## Other Permission-Management related Interfaces

Query APIs related to permission management transactions:

1. Query Signed Address

```
curl -X POST  http://127.0.0.1:8090/wallet/getapprovedlist -d '{"transaction"}'
 
rpc GetTransactionApprovedList(Transaction) returns (TransactionApprovedList) { }
```

2. Query Transaction Signature Weight

```
curl -X POST  http://127.0.0.1:8090/wallet/getsignweight -d '{"transaction"}'
 
rpc GetTransactionSignWeight (Transaction) returns (TransactionSignWeight) {}
```

The owner-permission and an active-permission are automatically generated during account creation. The owner permission contains one key, with the permission and threshold both set to 1. The active permission also contains one key with the permission and threshold set to 1. The operations are "7fff1fc0033efb07000000000000000000000000000000000000000000000000", which means all operations except AccountPermissionUpdateContract are supported.
