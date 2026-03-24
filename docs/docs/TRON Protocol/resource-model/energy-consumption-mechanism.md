---
title: Energy Consumption Mechanism
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
# Energy Consumption Mechanism

## Basic Energy Consumption Rules

When executing smart contract transactions, the system calculates and deducts the Energy required for each instruction sequentially. The consumption of Energy in an account follows these priority principles:

1. Available Energy (obtained through staking or renting) in the account is first used .
2. If that part of Energy is insufficient, the remaining part will be covered by burning TRX from the account at a fixed rate (0.0001 TRX per Energy unit).

## Contract Energy Sharing Mechanism

For smart contract calls, to reduce the caller's costs, TRON allows contract deployers to bear a portion of the Energy consumption. For specific details, please refer to the [Contract Energy Sharing Mechanism](#tron-energy-sharing-mechanism) section.

**Energy Deduction Rules:**

**Portion borne by the contract deployer:**

* Directly deducted from the available Energy in the deployer's account. TRX in the deployer's account will not be burned.

**Portion borne by the contract caller:**

1. Available Energy in the caller’s account is consumed first.
2. If insufficient, the remaining part will be covered by burning TRX from the caller account at a fixed rate.

# TRON Energy Sharing Mechanism

To enrich the application scenarios of smart contracts, the TRON network has innovatively introduced the Contract Energy Sharing Mechanism. This mechanism allows contract deployers to cover part of the execution Energy consumption. The specific rules are as follows:

## 1. Core Parameter Settings

| Parameter Name                   | Description                                                                                                  | Value Range |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| consume\_user\_resource\_percent | The percentage of Energy to be borne by the caller (e.g., 60 means the caller covers 60% of the consumption) | 0-100       |
| origin\_energy\_limit            | The maximum Energy the deployer will pay for a transaction                                                   | > =0        |

**Note**: This feature has been officially supported since Java-Tron Odyssey 3.2. For new smart contracts, the `origin_energy_limit` parameter must be explicitly set, and its value must be an integer greater than 0. For contracts deployed on the Mainnet before Odyssey 3.2, although the stored value of this parameter is 0, the system will treat it as 10,000,000 during execution.

## 2. Cost Sharing Calculation Logic

When contract execution requires X units of Energy:\
① **Theoretical Paying Value:**

* Caller's Payment = X × consume\_user\_resource\_percent%
* Deployer's Payment = X × (100 - consume\_user\_resource\_percent)%

② **Actual Paid Value:**

* Deployer's Actual Payment
  ```
  Deployer's Actual Payment = min ( X × (100 - consume_user_resource_percent)%
                  origin_energy_limit,
                  Deployer's available Energy
              )
  ```
* Caller's Actual Payment = X - Deployer's Actual Payment

The deployer's actual payment is the minimum of the theoretical paying value, the `origin_energy_limit` set in the contract, and the deployer's current available Energy. This ensures that the payment does not exceed the actually available resources. The caller's actual payment covers the remaining portion (total Energy consumption minus the deployer's actual payment), forming a complete cost coverage. An example is provided below:

### **Example**

Suppose a contract call requires a total of 80 units of Energy. If the deployer only has 10 Energy units available, and the contract parameters are set to:

* consume\_user\_resource\_percent = 60
* origin\_energy\_limit = 40

→ Theoretical paying: User: 48 Energy units, Deployer 32 Energy units.\
→ Actual paying: Deployer pays 10 Energy units (limited by deployer's available Energy: 10, and origin\_energy\_limit: 40); User pays 70 Energy units (80-10=70).

## 3. Parameter Adjustment

| Parameter                        | Modification Interface                                                                         | Scope          |
| -------------------------------- | ---------------------------------------------------------------------------------------------- | -------------- |
| consume\_user\_resource\_percent | [wallet/updatesetting](https://developers.tron.network/reference/wallet-updatesetting)         | Contract Level |
| origin\_energy\_limit            | [wallet/updateenergylimit](https://developers.tron.network/reference/wallet-updateenergylimit) | Contract Level |

Note: Adjustments to the above two parameters will affect all non-query transactions of the specific contract. Please proceed with caution.

In the TRON network, in addition to contract-level Energy consumption configurations, contract transactions also introduce the transaction-level parameter `FeeLimit`, which is used to limit the maximum Energy cost that the caller will cover, thereby providing more flexible cost control methods. For details, please refer to the [FeeLimit](https://developers.tron.network/docs/feelimit) section.
