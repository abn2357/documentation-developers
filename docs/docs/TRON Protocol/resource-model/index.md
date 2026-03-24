---
title: Resource Model
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
Voting right, Bandwidth, and Energy are important system resources of the TRON network. Among them, voting rights are used to vote for Super Representatives (SRs). Bandwidth is the unit that measures the size of the transaction bytes stored in the blockchain database. The larger the transaction, the more Bandwidth resources will be consumed. Energy is the unit that measures the amount of computation required by the TRON Virtual Machine (TVM) to perform specific operations on the TRON network. Since executing smart contract transactions requires computing resources, each smart contract transaction can consume Energy as fees.

# Voting Right

Before any account can vote for SRs, it needs to obtain voting rights, that is, TRON Power (TP). Voting rights can be obtained by staking TRX, which means in addition to Bandwidth or Energy, staking TRX can also bring users voting rights at the same time. Voters who stake 1 TRX will receive 1 TP. For more information about how to stake TRX, refer to [Staking on TRON Network](/docs/staking-on-tron-network).

Voters can stake multiple times, and the voting rights obtained by these staking operations will all be added to the voter's account. Voters can query the total number of voting rights owned by an account as well as the number of voting rights already used through the [wallet/getaccountresource](/reference/getaccountresource) interface.

# Bandwidth

Except for query operations, any transaction needs to consume Bandwidth. Transactions are transmitted and stored in the TRON network in the form of byte arrays. One byte requires one unit of Bandwidth, so the Bandwidth amount that a transaction needs to consume is equal to the number of transaction bytes.

When the available Bandwidth is insufficient, TRX needs to be burned to pay for Bandwidth:

```
Burned TRX =  Amount of Bandwidth consumed * Unit price of Bandwidth
```

Currently, the unit price of Bandwidth is 1,000 sun.

## How to Get Bandwidth

Each external account has 600 free Bandwidth per day, and more Bandwidth can be obtained through staking TRX. A fixed amount of Bandwidth is allocated to users according to the number of staked TRX. The total fixed Bandwidth supply for the entire network is 43,200,000,000 per day. The following formula can be used to calculate how much Bandwidth can be obtained by staking a certain amount of TRX:

```
Amount of Bandwidth obtained = Amount of TRX staked for obtaining Bandwidth / Total amount of TRX staked for obtaining Bandwidth on the whole network  * 43_200_000_000
```

You can query the total amount of TRX staked for obtaining Bandwidth on the whole network through the [wallet/getaccountresource](/reference/getaccountresource) interface.

You can send a `FreezeBalanceV2Contract` type of transaction to stake TRX to obtain Bandwidth. The following content uses wallet-cli as an example to create a `FreezeBalanceContract` type of transaction:

```
wallet> freezeBalanceV2 1000000 0
```

## Bandwidth Consumption

Except for query operations, any transaction needs to consume Bandwidth. Here are the rules of Bandwidth consumption: Firstly, if the transaction initiator's Bandwidth obtained by staking TRX is sufficient, this part of Bandwidth is used for consumption. Otherwise, the free Bandwidth of the transaction initiator is then compared with the transaction consumption. If sufficient, the free Bandwidth is consumed instead. If neither of them is sufficient for the transaction, TRX will be burned to pay for the Bandwidth consumption of the transaction based on the unit price of 0.001 TRX per Bandwidth.

## Bandwidth Recovery

After the account's free Bandwidth and the Bandwidth obtained by staking TRX are consumed, they will gradually recover within 24 hours. Developers can retrieve the `net_window_size` field via the [wallet/getaccount ](/reference/account-getaccount) API to monitor the remaining bandwidth recovery time.

## Account Bandwidth Balance Query

First, call the node HTTP interface [`wallet/getaccountresource`](https://developers.tron.network/reference/getaccountresource) to obtain the current resource status of the account, and then calculate the Bandwidth balance through the following formula:

```
Free Bandwidth balance = freeNetLimit - freeNetUsed

Balance of Bandwidth obtained by staking TRX = NetLimit - NetUsed
```

Note: If the result returned by the interface does not contain the parameters in the above formula, it means that the parameter value is 0.

# Energy

The execution of each instruction of a smart contract consumes a certain amount of Energy while running. So contracts of different complexity consume different amounts of Energy. When a contract is executed, Energy is calculated and deducted according to instructions one by one. When the available Energy of an account is insufficient, TRX needs to be burned to pay for the corresponding Energy.

```
Burned TRX = Energy quantity * Unit price of Energy
```

Currently, the unit price of Energy is 100 sun.

## How to Get Energy

Energy is generated through TRX staking. Users can obtain Energy either by staking their own TRX or by receiving delegated Energy from others. The total daily Energy supply across the network is fixed at 180,000,000,000, distributed proportionally based on the amount of TRX staked. 

The amount of Energy obtained can be calculated as:

```
The amount of Energy obtained = (TRX staked for Energy / Total TRX staked for Energy network-wide) * 180_000_000_000
```

You can query the total amount of TRX staked for obtaining Energy on the whole network through the [wallet/getaccountresource](/reference/getaccountresource) interface.

You can stake TRX to obtain energy by initiating a `FreezeBalanceV2Contract` transaction. For example, using `wallet-cli`:

```
wallet> freezeBalanceV2 1000000 1
```

Alternatively, you can delegate energy to others by initiating a `DelegateResourceContract` transaction:

```
wallet> delegateResource 1000000 1 TQ4gjjpAjLNnE67UFbmK5wVt5fzLfyEVs3
```

## Energy Consumption

When a contract is being executed, Energy is calculated and deducted according to instructions one by one. The priority of account Energy consumption is as follows:

* Energy obtained by staking TRX
* Burn TRX

First, the Energy obtained by staking TRX will be consumed. If this part of Energy is not enough, the account's TRX will continue to be burned to pay for the Energy resources required for the transaction, at the unit price of 0.0001 TRX per Energy. 

If the contract exits due to throwing a revert exception while execution, only the Energy consumed by instructions that have already been executed will be deducted. But for abnormal scenarios, such as contract execution timeout or unexpected exit due to a bug, the maximum Energy allowed for this transaction will be deducted. You can limit the maximum Energy cost of this transaction by setting the `fee_limit` parameter of the transaction.

## Energy Recovery

After the Energy resource of the account is consumed, it will gradually recover within 24 hours. Developers can retrieve the `account_resource.energy_window_size` field via the [wallet/getaccount ](/reference/account-getaccount) API to monitor the remaining energy recovery time.

## Account Energy Balance Query

First, call the node HTTP interface [`wallet/getaccountresource`](https://developers.tron.network/reference/getaccountresource) to obtain the current resource status of the account, and then calculate the Energy balance through the following formula: 

```
Energy Balance = EnergyLimit - EnergyUsed
```

Note: If the result returned by the interface does not contain the parameters in the above formula, it means that the parameter value is 0.

# Dynamic Energy Model

The dynamic Energy model is a resource balancing mechanism of the TRON network, which can dynamically adjust the Energy consumption of each contract according to the resource occupancy of the contract, so as to make the allocation of Energy resources on the chain more reasonable and to prevent excessive concentration of network resources on a few popular contracts. For more details, refer to [Introduction to Dynamic Energy Model](https://coredevs.medium.com/introduction-to-dynamic-energy-model-31917419b61a).

## Principle

If a contract uses too many resources in one [maintenance cycle](https://developers.tron.network/docs/glossary#maintenance-time-interval), then in the next maintenance cycle, a certain percentage of punitive consumption will be added, and users who send the same transaction to this contract will spend more Energy than before. When the contract uses resources reasonably, the Energy consumption of calling the contract will gradually return to normal. 

Each contract has an `energy_factor` field, which indicates the increased ratio of the Energy consumption for the smart contract transaction relative to the base Energy consumption. The initial value is 0. When the `energy_factor` of a contract is 0, it means that the contract is using resources reasonably, and there will be no additional Energy consumption for calling this contract. When the `energy_factor` is greater than 0, it means that the contract is currently a popular contract, and additional Energy will be consumed when users call the contract. The `energy_factor` of a contract can be queried through the [getcontractinfo](#api) API.

The calculation formula for the final Energy consumed by a contract invocation transaction is as follows:

```
Energy consumed by a contract invocation transaction  = Basic Energy consumption generated by the transaction * （1 +  energy_factor）
```

The dynamic Energy model introduces the following three parameters of the TRON network, which jointly control the `energy_factor` field of the contract:

* `threshold`: The threshold of a contract's basic Energy consumption. In a [maintenance cycle](https://developers.tron.network/docs/glossary#maintenance-time-interval), if the basic Energy consumption of the contract exceeds this threshold, the Energy consumption of the contract will increase at the next maintenance cycle.
* `increase_factor`: If the basic Energy consumption of the contract exceeds the threshold during a certain maintenance cycle, the `energy_factor` will increase by a certain percentage according to the `increase_factor` in the next maintenance cycle.
* `max_factor`: the maximum value of energy\_factor for a contract.

There is also a variable `decrease_factor` used to reduce the `energy_factor` of a contract:

* `decrease_factor`: 1/4 of the `increase_factor`value. After the basic Energy consumption of the contract falls below the threshold, `energy_factor` will be reduced by a certain percentage according to `decrease_factor`.

When the basic Energy consumption of a contract exceeds `threshold` during a [maintenance cycle](docs/glossary#maintenance-time-interval), its `energy_factor` will increase in the next maintenance cycle, but its maximum value will not exceed that of `max_factor`. The calculation formula is as follows:

```
energy_factor = min((1 + energy_factor) * (1 + increaese_factor)-1, max_factor)
```

When the basic Energy consumption of the contract drops below the threshold in a [maintenance cycle](docs/glossary#maintenance-time-interval), the `energy_factor` will decrease in the next maintenance cycle, but its minimum value will not be lower than 0. The calculation formula is as follows:

```
energy_factor = max((1 + energy_factor) * (1 - decrease_factor)- 1, 0)
```

The dynamic Energy model has been enabled on the Mainnet, and the relevant parameters are set as follows:

* `threshold`：5,000,000,000
* `increase_factor`：0.2
* `max_factor`：3.4

Since the Energy consumption of popular contracts can vary across different maintenance cycles, it is necessary to set an appropriate feelimit value for the transaction when calling the contract. For more information, refer to [Set Transaction Feelimit](/docs/set-feelimit).

## APIs

The following table shows the relevant interfaces of the dynamic Energy model and the corresponding descriptions:

<Table>
  <thead>
    <tr>
      <th>
        API
      </th>

      <th>
        Description
      </th>

      <th>
        Return Value related to Dynamic Energy Model
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        getcontractinfo
      </td>

      <td>
        Query contract information
      </td>

      <td>
        `contract_state.energy_usage` indicates the total amount of basic Energy usage of the contract in the current maintenance cycle; `contract_state.energy_factor` indicates the Energy factor of the contract. 0 indicates a non-popular contract, while a value greater than 0 indicates a popular contract; `contract_state.update_cycle` indicates the number of the current maintenance cycle.
      </td>
    </tr>

    <tr>
      <td>
        triggerconstantcontract
      </td>

      <td>
        Query contract data or estimate Energy
      </td>

      <td>
        `energy_penalty` indicates the penalty Energy;\
        `energy_used` indicates the total Energy (the sum of the base Energy and the penalty Energy).
      </td>
    </tr>

    <tr>
      <td>
        gettransactioninfobyid
      </td>

      <td>
        Query transaction information
      </td>

      <td>
        `receipt.energy_penalty_total` indicates the penalty Energy.
      </td>
    </tr>

    <tr>
      <td>
        gettransactionreceiptbyid
      </td>

      <td>
        Query information such as transaction execution results and fees
      </td>

      <td>
        `receipt.energy_penalty_total` indicates the penalty Energy.
      </td>
    </tr>
  </tbody>
</Table>
