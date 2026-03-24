---
title: Get account info by address
excerpt: ''
api:
  file: trongrid-v1-api.json
  operationId: get-account-info-by-address
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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Field
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        data.address
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Account address. (Format: hex)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.balance
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        TRX balance. (Unit: `sun`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_name
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Account name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.create\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp for when the account was created. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.is\_witness
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates if the account is a Super Representative (SR), an SR Partner or an SR candidate.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.allowance
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of rewards that can be withdrawn by the account. (Unit: `sun`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.latest\_withdraw\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp of the account's last withdrawal of rewards. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.latest\_opration\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp of the account's last operation. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.latest\_consume\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp of the account's last Bandwidth consumption. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.latest\_consume\_free\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp of the account's last free Bandwidth consumption. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.net\_window\_size
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The duration, in blocks, required for staked Bandwidth to fully recover.\
        Note: The value has a decimal precision of 3 if `net_window_optimized` is `true`, otherwise 0.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.net\_window\_optimized
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the Bandwidth recovery window optimization is enabled.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.latest\_consume\_time\_for\_energy
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp of the account's last Energy consumption. (Unit: millisecond)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.acquired\_delegated\_frozen\_balance\_for\_energy
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by other accounts for this account's energy. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.delegated\_frozen\_balance\_for\_energy
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by this account for other accounts' energy. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.energy\_window\_size
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The duration, in blocks, required for Energy to fully recover.  

        Note: The value has a decimal precision of 3 if `energy_window_optimized` is `true`, otherwise 0.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.acquired\_delegated\_frozenV2\_balance\_for\_energy
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by other accounts for this account's Energy. (Unit: sun, For Stake 2.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.delegated\_frozenV2\_balance\_for\_energy
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by this account for other accounts' Energy. (Unit: sun, For Stake 2.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.energy\_window\_optimized
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the Energy recovery window optimization is enabled.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.frozen[0].frozen\_balance
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked for Bandwidth by this account. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.frozen[0].expire\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp when the `unstake` operation becomes available for the staked Bandwidth. (Unit: millisecond, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.frozen\_balance\_for\_energy.frozen\_balance
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked for Energy by this account. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.frozen\_balance\_for\_energy.expire\_time
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The timestamp when the `unstake` operation becomes available for the staked Energy. (Unit: millisecond, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.account\_resource.energy\_usage
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of Energy used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.owner\_permission.permission\_name
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Owner permission name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.owner\_permission.threshold
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The minimum combined weight of signatures required to validate an operation using this permission.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.owner\_permission.keys.address
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The address associated with the owner permission.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.owner\_permission.keys.weight
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The signature weight of the corresponding address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.type
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The type of the permission. (Value: `Active`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.id
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        Active Permission ID. (Automatically assigned from 2)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.permission\_name
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Permission name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.threshold
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The minimum combined weight of signatures required to validate an operation using this permission.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.operations
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        A string representing the operations allowed by this permission. Note: This is a 32-byte hex string where each bit corresponds to a specific operation. See details [here](https://developers.tron.network/docs/multi-signature#active-permissions) .
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.keys.address
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The address associated with this active permission.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.active\_permission.keys.weight
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The signature weight of the address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.type
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The type of the permission. (Value: `Witness`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.id
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The fixed ID for the witness permission. (Value: `1`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.permission\_name
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        Permission name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.threshold
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        Witness Permission threshold.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.keys.address
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The address of the key associated with this witness permission.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.witness\_permission.keys.weight
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The signature weight of the address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.frozenV2.[i].amount
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked to obtain the resource type specified by `data.frozenV2[i].type`. (Unit: sun, For Stake 2.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.frozenV2.[i].type
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The type of resource obtained through staking. (Enum: `BANDWIDTH` or `ENERGY`)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.acquired\_delegated\_frozenV2\_balance\_for\_bandwidth
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by other accounts for this account's Bandwidth. (Unit: sun, For Stake 2.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.delegated\_frozenV2\_balance\_for\_bandwidth
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by this account for other accounts' Bandwidth. (Unit: sun, For Stake 2.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.acquired\_delegated\_frozen\_balance\_for\_bandwidth
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by other accounts for this account's Bandwidth. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.delegated\_frozen\_balance\_for\_bandwidth
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total amount of TRX staked by this account for other accounts' Bandwidth. (Unit: sun, For Stake 1.0)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.assetV2[i].key
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        TRC-10 Token ID.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.assetV2[i].value
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        TRC-10 Token balance.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.net\_usage
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of Bandwidth used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.free\_net\_usage
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of free Bandwidth used.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.free\_asset\_net\_usageV2[i].key
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The TRC-10 Token ID.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.free\_asset\_net\_usageV2[i].value
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The total free Bandwidth usage attributed to this TRC-10 token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.trc20
      </td>

      <td style={{ textAlign: "left" }}>
        List
      </td>

      <td style={{ textAlign: "left" }}>
        TRC-20 balance held by this account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.votes.vote\_address
      </td>

      <td style={{ textAlign: "left" }}>
        String
      </td>

      <td style={{ textAlign: "left" }}>
        The address of the Super Representative (SR) that this account has voted for.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        data.votes.vote\_count
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The number of votes cast for the the SR address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        success
      </td>

      <td style={{ textAlign: "left" }}>
        Boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the request was successful.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.page\_size
      </td>

      <td style={{ textAlign: "left" }}>
        Integer
      </td>

      <td style={{ textAlign: "left" }}>
        The number of items returned on the current page.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.at
      </td>

      <td style={{ textAlign: "left" }}>
        Long
      </td>

      <td style={{ textAlign: "left" }}>
        The response timestamp. (Unit: millisecond)
      </td>
    </tr>
  </tbody>
</Table>