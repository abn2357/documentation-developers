---
title: Protobuf Definition
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
TRON VM is compatible with Ethereum's smart contract, using protobuf to define the content of the contract:

```text SmartContract.proto
message SmartContract {
  message ABI {
    message Entry {
      enum EntryType {
        UnknownEntryType = 0;
        Constructor = 1;
        Function = 2;
        Event = 3;
        Fallback = 4;
      }
      message Param {
        bool indexed = 1;
        string name = 2;
        string type = 3;
        // SolidityType type = 3;
      }
      enum StateMutabilityType {
        UnknownMutabilityType = 0;
        Pure = 1;
        View = 2;
        Nonpayable = 3;
        Payable = 4;
      }

      bool anonymous = 1;
      bool constant = 2;
      string name = 3;
      repeated Param inputs = 4;
      repeated Param outputs = 5;
      EntryType type = 6;
      bool payable = 7;
      StateMutabilityType stateMutability = 8;
    }
    repeated Entry entrys = 1;
  }
  bytes origin_address = 1;
  bytes contract_address = 2;
  ABI abi = 3;
  bytes bytecode = 4;
  int64 call_value = 5;
  int64 consume_user_resource_percent = 6;
  string name = 7；
  int64 origin_energy_limit = 8;
}
```

origin\_address: smart contract creator address\
contract\_address: smart contract address\
abi: the api information of the all the function of the smart contract\
bytecode: smart contract byte code\
call\_value: TRX transferred into smart contract while call the contract\
consume\_user\_resource\_percent: resource consumption percentage set by the developer\
name: smart contract name\
origin\_energy\_limit: energy consumption of the developer limit in one call, must greater than 0. For the old contracts, if this parameter is not set, it will be set 0, developer can use updateEnergyLimit api to update this parameter (must greater than 0)

Through other two grpc message types CreateSmartContract and TriggerSmartContract to create and use smart contract.
