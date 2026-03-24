---
title: getChainParameters
excerpt: >-
  Query the parameters of the blockchain used for witnessses to create a
  proposal
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage** 

```javascript
tronWeb.trx.getChainParameters();
```

**Parameters** 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameters
      </th>

      <th>
        Description
      </th>

      <th>
        Data Type
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        N/A
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Arrays

**Example** 

```javascript
tronWeb.trx.getChainParameters();
>[ { key: 'getMaintenanceTimeInterval', value: 21600000 },
  { key: 'getAccountUpgradeCost', value: 9999000000 },
  { key: 'getCreateAccountFee', value: 100000 },
  { key: 'getTransactionFee', value: 10 },
  { key: 'getAssetIssueFee', value: 1024000000 },
  { key: 'getWitnessPayPerBlock', value: 32000000 },
  { key: 'getWitnessStandbyAllowance', value: 115200000000 },
  { key: 'getCreateNewAccountFeeInSystemContract' },
  { key: 'getCreateNewAccountBandwidthRate', value: 1 },
  { key: 'getAllowCreationOfContracts', value: 1 },
  { key: 'getRemoveThePowerOfTheGr', value: -1 },
  { key: 'getEnergyFee', value: 10 },
  { key: 'getExchangeCreateFee', value: 1024000000 },
  { key: 'getMaxCpuTimeOfOneTx', value: 50 },
  { key: 'getAllowUpdateAccountName' },
  { key: 'getAllowSameTokenName', value: 1 },
  { key: 'getAllowDelegateResource', value: 1 },
  { key: 'getTotalEnergyLimit', value: 100000000000 },
  { key: 'getAllowTvmTransferTrc10', value: 1 },
  { key: 'getTotalEnergyCurrentLimit', value: 100000000000 },
  { key: 'getAllowMultiSign' },
  { key: 'getAllowAdaptiveEnergy' },
  { key: 'getTotalEnergyTargetLimit', value: 6944444 },
  { key: 'getTotalEnergyAverageUsage' },
  { key: 'getUpdateAccountPermissionFee', value: 100000000 },
  { key: 'getMultiSignFee', value: 1000000 } ]
```
