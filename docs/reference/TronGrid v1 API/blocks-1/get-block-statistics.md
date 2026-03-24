---
title: Get block statistics
excerpt: >-
  Retrieves detailed statistical information for a specific block, including
  transaction counts and resource consumption.
api:
  file: trongrid-v1-api.json
  operationId: get-block-statistics
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

| Field                                            | Type      | Description                                                                                                                                                                                              |
| :----------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data[i].txStat`                                 | `object`  | An object containing transaction statistics. Only returned if `get_tx_detail` is set to `true`.                                                                                                          |
| `data[i].txStat.trxAnd10TransferCount`           | `integer` | The number of TRX and TRC-10 transfer transactions.                                                                                                                                                      |
| `data[i].txStat.trc20And721TransferCount`        | `integer` | The number of TRC-20 and TRC-721 transfer transactions.                                                                                                                                                  |
| `data[i].txStat.trc1155TransferCount`            | `integer` | The number of TRC-1155 transfer transactions.                                                                                                                                                            |
| `data[i].txStat.transferCount`                   | `integer` | The number of all transfer-type transactions.                                                                                                                                                            |
| `data[i].txStat.failTxCount`                     | `integer` | The number of failed transactions.                                                                                                                                                                       |
| `data[i].txStat.internalTxCount`                 | `integer` | The number of all internal transactions generated within the block.                                                                                                                                      |
| `data[i].txStat.containInternalTxCount`          | `integer` | The number of transactions that contain at least one internal transaction.                                                                                                                               |
| `data[i].txStat.contractTypeDistribute`          | `object`  | The total count for each transaction type in the block, keyed by enum ID (see [here](https://github.com/tronprotocol/java-tron/blob/develop/protocol/src/main/protos/core/Tron.proto#L338) for details). |
| `data[i].feeStat`                                | `object`  | An object containing fee and resource consumption statistics.                                                                                                                                            |
| `data[i].feeStat.netUsage`                       | `integer` | The total Bandwidth usage in the caller's account.                                                                                                                                                       |
| `data[i].feeStat.energyUsage`                    | `integer` | The amount of Energy consumed in the caller's account.                                                                                                                                                   |
| `data[i].feeStat.otherFee`                       | `integer` | Total fee (excluding Bandwidth and Energy) for all other operations. (Unit: sun)                                                                                                                         |
| `data[i].feeStat.srCandidateRegistrationFee`     | `integer` | Total fee for Super Representative (SR) candidate registration. (Unit: sun)                                                                                                                              |
| `data[i].feeStat.accountActivationFee`           | `integer` | Total fee for account activations. (Unit: sun)                                                                                                                                                           |
| `data[i].feeStat.permissionUpdateFee`            | `integer` | Total fee for updating account permissions. (Unit: sun)                                                                                                                                                  |
| `data[i].feeStat.multiSignatureFee`              | `integer` | Total fee for a multi-signature transaction. (Unit: sun)                                                                                                                                                 |
| `data[i].feeStat.memoFee`                        | `integer` | Total fee for including a memo in a transaction. (Unit: sun)                                                                                                                                             |
| `data[i].feeStat.trc10AssetIssueFee`             | `integer` | Total fee for issuing a TRC-10 token. (Unit: sun)                                                                                                                                                        |
| `data[i].feeStat.dexPairCreateFee`               | `integer` | Total fee for creating a DEX trading pair. (Unit: sun)                                                                                                                                                   |
| `data[i].feeStat.dexOrderSellFee`                | `integer` | Total fee for creating a DEX sell order. (Unit: sun)                                                                                                                                                     |
| `data[i].feeStat.dexOrderCancelFee`              | `integer` | Total fee for cancelling a DEX order. (Unit: sun)                                                                                                                                                        |
| `data[i].feeStat.energyBurnFeeSunAmt`            | `integer` | The total amount of TRX burned for Energy. (Unit: sun)                                                                                                                                                   |
| `data[i].feeStat.bandwidthConsumedFromBurnCnt`   | `integer` | The Bandwidth obtained by burning TRX.                                                                                                                                                                   |
| `data[i].feeStat.freeBandwidthUsageCnt`          | `integer` | The total usage of staked and free Bandwidth.                                                                                                                                                            |
| `data[i].feeStat.bandwidthBurnFeeSunAmt`         | `integer` | The total amount of TRX burned for Bandwidth. (Unit: sun)                                                                                                                                                |
| `data[i].feeStat.energyConsumedFromOwnerBurnCnt` | `integer` | The total Energy usage obtained by the transaction owner burning TRX.                                                                                                                                    |
| `data[i].feeStat.freeEnergyUsageCnt`             | `integer` | The total usage of staked Energy.                                                                                                                                                                        |
| `success`                                        | `boolean` | Whether the request was successful.                                                                                                                                                                      |
| `meta.at`                                        | `long`    | The response timestamp. (Unit: millisecond)                                                                                                                                                              |
| `meta.page_size`                                 | `integer` | The number of items returned on the current page.                                                                                                                                                        |
