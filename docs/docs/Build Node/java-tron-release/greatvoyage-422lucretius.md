---
title: GreatVoyage-4.2.2(Lucretius)
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
# Core Protocol

## 1. Block Processing optimization

In the versions before GreatVoyage-v4.2.2 (Lucretius), to obtain the witness list during block processing, multiple database queries and deserialization operations were performed, which took up nearly 1/3 of the block processing time.

The GreatVoyage-v4.2.2 (Lucretius) version simplifies the query of witnesses. In the block processing process, the witness list can be obtained by only one query. After testing, this optimization has dramatically improved the block processing performance.

* TIP: [TIP-269](https://github.com/tronprotocol/tips/blob/master/tip-269.md)
* Source code: [#3827](https://github.com/tronprotocol/java-tron/pull/3827)

## 2. Data Query optimization

In the versions before GreatVoyage-v4.2.2 (Lucretius), multiple HTTP or RPC queries for data on the chain are mutually exclusive. If a query request is being processed, a new query request will keep waiting until the previous request is completed. 

However, data query methods never use shared data, and no lock operation is required. This optimization removes unnecessary synchronization locks in the query process and improves the performance of internal queries, HTTP and RPC query requests of nodes.

## 3. Smart Contract ABI Storage optimization

In the version before GreatVoyage-v4.2.2 (Lucretius), the ABI other data of the smart contract are stored together in the contract database, and some high-frequency instructions (SLOAD, SSTORE, Etc.) will read all the data of a smart contract from the contract database. However, the execution of the contract does not use these ABI data, and these frequent readings will impact the execution efficiency of these instructions.

In the version of GreatVoyage-v4.2.2 (Lucretius), smart contract ABIs are transferred to a particular ABI database. The ABI data will no longer be read during the execution of the contract, thus significantly improving the performance of TVM.

* TIP: [TIP-268](https://github.com/tronprotocol/tips/blob/master/tip-268.md)
* Source code: [#3836](https://github.com/tronprotocol/java-tron/pull/3836)

# Other Changes

## 1. System Contract `BatchValidateSign` Initialization Process optimization

* Source code: [#3836](https://github.com/tronprotocol/java-tron/pull/3836)

The version of GreatVoyage-v4.2.2 (Lucretius) introduces three important optimizations. The optimization of block processing effectively improves the execution speed of the block, thereby significantly improving the performance of the TRON network. Efficient HTTP/RPC query and excellent TVM performance will bring a better experience to TRON DAPP users and further prosper the TRON ecosystem.

 \--- *Truths kindle light for truths.* 

<p align="right"> --- Lucretius</p>

# DBReqair.jar User Guide

## Scope

This tool is only for users who have downgraded the java-tron version to [GreatVoyage-v4.2.1(Origen)](https://github.com/tronprotocol/java-tron/releases/tag/GreatVoyage-v4.2.1) or [GreatVoyage-v4.2.0(Plato)](https://github.com/tronprotocol/java-tron/releases/tag/GreatVoyage-v4.2.0) from [GreatVoyage-v4.2.2(Lucretius)](https://github.com/tronprotocol/java-tron/releases/tag/GreatVoyage-v4.2.2) or other higher versions. 

If users meet the above conditions, users need to execute the DBReqair.jar tool to repair the database before users can start FullNode.jar normally.

## Tool Homepage:

[https://github.com/tronprotocol/tools/releases/tag/v1.0.0](https://github.com/tronprotocol/tools/releases/tag/v1.0.0) 

## Steps

1. Download the “DBRepair.jar” and “repair.sh” from the tool homepage and place them in the same directory as “FullNode.jar”.
2. Go to the “FullNode.jar” directory and execute the “repair.sh” file:

```
sh ./repair.sh
```

3. Open the log file “logs/tron.log” and wait for the execution to complete, you will see "Repairment completed!" in log output once execution is complete. (DBRepair will automatically exit after the execution is completed).
4. Now the repair of the database has been completed. users can start the node normally with the latest version  [GreatVoyage-v4.2.2.1(Epictetus)](https://github.com/tronprotocol/java-tron/releases/tag/GreatVoyage-v4.2.2.1) 

## Notes

This tool only needs to be executed once.
