---
title: Committee and Proposal
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
# Committee

The committee can modify the TRON network parameters, like transaction fees, block producing reward amount, etc. Committee is composed of the current 27 super representatives. Every super representative has the right to start a proposal. A proposal will be effective when receiving at least 18 votes and will become valid in the next maintenance period.

# Proposal

Only SRs, Partners and Candidates can create a proposal.\
The network parameters can be modified(\[min, max]).\
\{0,1}: 1 means 'allowed' or 'actived', 0 means no.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        #
      </td>

      <td>
        Command
      </td>

      <td>
        Value
      </td>
    </tr>

    <tr>
      <td>
        0
      </td>

      <td>
        getMaintenanceTimeInterval\
        (To modify the maintenance interval of SR)
      </td>

      <td>
        6 Hours\
        [3 * 27, 24 * 3600] s
      </td>
    </tr>

    <tr>
      <td>
        1
      </td>

      <td>
        getAccountUpgradeCost\
        (To modify the cost of applying for SR account)
      </td>

      <td>
        9999 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        getCreateAccountFee\
        (To modify the account creation fee)
      </td>

      <td>
        0.1 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        getTransactionFee\
        (To modify the amount of TRX used to gain extra bandwidth)
      </td>

      <td>
        40 Sun/Byte\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        getAssetIssueFee\
        (To modify asset issuance fee)
      </td>

      <td>
        1024 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        getWitnessPayPerBlock\
        (To modify SR block generation reward)
      </td>

      <td>
        16 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        6
      </td>

      <td>
        getWitnessStandbyAllowance\
        (To modify the rewards given to the top 27 SRs and\
        the following 100 partners)
      </td>

      <td>
        115200 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        7
      </td>

      <td>
        getCreateNewAccountFeeInSystemContract\
        (To modify the cost of account creation)
      </td>

      <td>
        0 TRX
      </td>
    </tr>

    <tr>
      <td>
        8
      </td>

      <td>
        getCreateNewAccountBandwidthRate\
        (To modify the consumption of bandwith of account creation)
      </td>

      <td>
        1 Bandwith/Byte
      </td>
    </tr>

    <tr>
      <td>
        9
      </td>

      <td>
        getAllowCreationOfContracts\
        (To activate the Virtual Machine (VM))
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        10
      </td>

      <td>
        getRemoveThePowerOfTheGr\
        (To remove the GR Genesis votes)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        11
      </td>

      <td>
        getEnergyFee\
        (To modify the fee of 1 energy)
      </td>

      <td>
        40 Sun\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        12
      </td>

      <td>
        getExchangeCreateFee\
        (To modify the cost of trading pair creation)
      </td>

      <td>
        1024 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        13
      </td>

      <td>
        getMaxCpuTimeOfOneTx\
        (To modify the maximum execution time of one transaction)
      </td>

      <td>
        80 ms\
        [0, 1000] ms
      </td>
    </tr>

    <tr>
      <td>
        14
      </td>

      <td>
        getAllowUpdateAccountName\
        (To allow to change the account name)
      </td>

      <td>
        0\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        15
      </td>

      <td>
        getAllowSameTokenName\
        (To allow the same token name)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        16
      </td>

      <td>
        getAllowDelegateResource\
        (To allow resource delegation)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        18
      </td>

      <td>
        getAllowTvmTransferTrc10\
        (To allow the TRC-10 token transfer in smart contracts)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        19
      </td>

      <td>
        getTotalEnergyCurrentLimit\
        (To modify current total energy limit)
      </td>

      <td>
        50000000000
      </td>
    </tr>

    <tr>
      <td>
        20
      </td>

      <td>
        getAllowMultiSign\
        (To allow the initiation of multi-signature)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        21
      </td>

      <td>
        getAllowAdaptiveEnergy\
        (To allow adaptive adjustment for total Energy)
      </td>

      <td>
        0\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        22
      </td>

      <td>
        getUpdateAccountPermissionFee\
        (To modify the fee for updating account permission)
      </td>

      <td>
        100 TRX
      </td>
    </tr>

    <tr>
      <td>
        23
      </td>

      <td>
        getMultiSignFee\
        (To modify the fee for multi-signature)
      </td>

      <td>
        1 TRX
      </td>
    </tr>

    <tr>
      <td>
        24
      </td>

      <td>
        getAllowProtoFilterNum\
        (To enable protocol optimization)
      </td>

      <td>
        0\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        26
      </td>

      <td>
        getAllowTvmConstantinople\
        (To support the new commands of Constantinople)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        27
      </td>

      <td>
        getAllowShieldedTransaction\
        (To enable shielded transaction)
      </td>

      <td>
        0\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        28
      </td>

      <td>
        getShieldedTransactionFee\
        (To modify shielded transaction fee)
      </td>

      <td>
        10 TRX\
        [0, 10000] TRX
      </td>
    </tr>

    <tr>
      <td>
        29
      </td>

      <td>
        getAdaptiveResourceLimitMultiplier\
        (To modify the adaptive energy limit multiplier)
      </td>

      <td>
        1000\
        [1, 10000]
      </td>
    </tr>

    <tr>
      <td>
        30
      </td>

      <td>
        getChangeDelegation\
        (Propose to support the decentralized vote dividend)
      </td>

      <td>
        1\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        31
      </td>

      <td>
        getWitness127PayPerBlock\
        (Propose to modify the block voting rewards given to\
        the top 27 SRs and the following 100 partners)
      </td>

      <td>
        160 TRX\
        [0, 100000000000] TRX
      </td>
    </tr>

    <tr>
      <td>
        32
      </td>

      <td>
        getAllowTvmSolidity059\
        (To allow TVM to support solidity compiler 0.5.9)
      </td>

      <td>
        0\
        \{0, 1}
      </td>
    </tr>

    <tr>
      <td>
        33
      </td>

      <td>
        getAdaptiveResourceLimitTargetRatio\
        (To modify the target energy limit)
      </td>

      <td>
        10\
        [1, 1000]
      </td>
    </tr>
  </tbody>
</Table>

## Create a Proposal

Example (Using wallet-cli):

```shell
createproposal id value  
id: the serial number (0 ~ 18)  
value: the parameter value
```

> 📘 Note
>
> * In TRON network, 1 TRX = 1000\_000 SUN 

## Vote for a Proposal

Proposal only support YES vote. Since the creation time of the proposal, the proposal is valid within 3 days. If the proposal does not receive enough YES votes within the period of validity, the proposal will be invalid beyond the period of validity. Yes vote can be cancelled.

Example (Using wallet-cli):

```shell
approveProposal id is_or_not_add_approval
id: proposal id  
is_or_not_add_approval: YES vote or cancel YES vote
```

## Cancel Proposal

Proposal creator can cancel the proposal before it is passed.\
Example (Using wallet-cli):

```shell
deleteProposal id
id: proposal id
```

## Query Proposal

<a href="https://developers.tron.network/reference/wallet-listproposals" target="_blank">List Proposals Full Node HTTP API</a>

<a href="https://developers.tron.network/reference/listproposals" target="_blank">List Proposals TronWeb API</a>

<a href="https://developers.tron.network/reference/getproposalbyid" target="_blank">Get Proposal by ID Full Node HTTP API</a>
