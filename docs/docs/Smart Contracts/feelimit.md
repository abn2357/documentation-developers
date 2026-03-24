---
title: Feelimit
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
In the TRON network, in addition to contract-level Energy consumption configurations, contract transactions also introduce the transaction-level parameter `FeeLimit`, which is used to limit the maximum Energy cost that the caller will cover, thereby providing more flexible cost control methods.

# Transaction Cost Control Parameter: Feelimit

`FeeLimit` refers to the maximum Energy cost that the caller is willing to pay for the current smart contract deployment or call transaction. The value is calculated in  sun (1 TRX = 1,000,000 sun). The current network allows a maximum `FeeLimit` of 15,000 TRX, which is 15,000,000,000 sun.

It is important to note that `FeeLimit` only limits the maximum Energy expenditure that the caller will pay for the current transaction. It does not affect whether the contract deployer participates in Energy cost sharing nor their sharing proportion. However, `FeeLimit` will affect the total transaction Energy limit (`EnergyLimit`) of  the overall transaction execution process because it defines the maximum Energy share that the caller can bear, and the final `EnergyLimit` is composed of the Energy limits that both the caller and the contract deployer are willing to bear.

## Transaction Energy Consumption Limit: EnergyLimit

`EnergyLimit` is the maximum Energy amount that a contract transaction is allowed to consume during its execution. When the actual consumed Energy has already reached this limit and needs more, the transaction will be immediately aborted, and the error code `OUT_OF_ENERGY` will be returned.

Since the TRON network supports the [Contract Energy Sharing Mechanism](https://developers.tron.network/docs/energy-consumption-mechanism#tron-energy-sharing-mechanism), which allows contract deployers to cover part of the Energy cost for contract callers, the `EnergyLimit` of a transaction is the sum of the maximum Energy that the caller and the contract deployer can each bear:

```
EnergyLimit = Maximum Energy bearable by contract deployer + Maximum Energy bearable by caller
```

#### Maximum Energy Bearable by Caller

```
Maximum Energy bearable by caller = min (
    Energy amount corresponding to FeeLimit,
    Caller's available Energy + Energy amount equivalent to the available TRX balance (the TRX available balance here is the balance after deducting transaction costs such as Bandwidth consumption, TRX transferred to the contract, and other transaction fees)
)
```

#### Maximum Energy Bearable by Contract Deployer

```
Maximum Energy bearable by contract deployer = min (
    origin_energy_limit,  // Contract-set Energy limit per transaction
    Deployer's available Energy in the account,      // Deployer's currently available Energy
    consume_user_resource_percent>0 ? Caller's bearable Energy limit * (100-consume_user_resource_percent)/consume_user_resource_percent : ∞  // If the user’s cost sharing proportion is 0, the deployer’s Energy consumption theoretically has no upper limit
)
```

* If `consume_user_resource_percent = 0`, the deployer is theoretically responsible for the entire transaction Energy cost, so the deployer’s bearable Energy limit is only constrained by the contract's `origin_energy_limit` and the deployer's available Energy.
* If `consume_user_resource_percent > 0`, the deployer's theoretical maximum paying value is derived proportionally from the caller's bearable Energy limit and the `consume_user_resource_percent` value: `Theoretical maximum cost sharing value = Caller's bearable Energy limit * (100 - consume_user_resource_percent) / consume_user_resource_percent`. 

Therefore, the deployer's final Energy limit is the minimum of `origin_energy_limit`, the deployer's available Energy in the account, and the theoretical maximum cost sharing value.

**Example:**\
Assume a contract has `consume_user_resource_percent = 20` and `origin_energy_limit = 300`. The caller sets the `FeeLimit` for the transaction to 0.021 TRX (equivalent to 100 Energy units). The caller's available Energy is 1,000, and the deployer's available Energy is 2,000. Then:

* The caller's bearable Energy consumption: `min (100, 1000) = 100`
* The deployer's theoretical maximum cost sharing value: `100 × (100-20) / 20 = 400`
* Therefore, the deployer's actual bearable Energy consumption: `min (300, 2000, 400) = 300`
* The transaction's `EnergyLimit` is `100 + 300 = 400`. If the required Energy exceeds 400, the transaction will fail.

# Significance of Properly Setting FeeLimit

Properly setting `FeeLimit` is crucial for contract callers and developers in the TRON network. Its main purposes and significance include:

* Preventing excessive resource consumption due to malicious contracts or complex logic.
* Reducing resource abuse.
* Achieving predictable transaction costs.
* Providing a clear upper limit strategy to help developers and users control costs.

Developers should flexibly utilize the three parameters: `FeeLimit`, `consume_user_resource_percent`, and `origin_energy_limit`, based on the contract's characteristics, expected Energy consumption, and user scenarios. This enables optimal cost-control strategies, improves user experience, and ensures efficient utilization of network resources.
