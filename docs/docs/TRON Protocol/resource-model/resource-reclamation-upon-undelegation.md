---
title: Resource Reclamation Upon Undelegation
deprecated: false
hidden: false
metadata:
  robots: index
---
In the TRON network, the amount of resources an account receives depends on the proportion of its TRX staked relative to the total TRX staked across the entire network.

When a delegator delegates resources to a recipient, it essentially lends a portion of its own staked TRX to the recipient. In resource quota calculations, the system does not distinguish between the sources of TRX. TRX staked by the account itself and TRX delegated from other accounts are aggregated and treated uniformly as the weighting basis for resource allocation.

Based on this mechanism, unless otherwise specified, the term “staked amount” in this document refers to the total staked TRX of an account, including both self-staked TRX and TRX delegated from other accounts, without distinguishing their sources.

# Resource Reclamation

When a Delegator initiates resource delegation, a certain amount of staked TRX is lent to the Recipient, granting them the corresponding resources usage right. When the Delegator cancels the resource delegation, the system not only reclaims the corresponding staked TRX, but also reclaims a proportional amount of the Recipient’s unrecovered resources.

## Reclamation Logic for Unrecovered Resources

### 1. Calculation Formula

The system proportionally reclaims the Recipient's unrecovered resources based on the amount of TRX being undelegated according to the following formula:

```text
Reclaimed unrecovered resources  
= (Canceled delegated TRX amount ÷ Recipient’s total staked TRX amount for that resource)  
× Recipient’s unrecovered resource amount
```

**Note**: The reclaimed unrecovered resources **must not exceed** the maximum resource capacity corresponding to the undelegated TRX amount, calculated in real time based on current network-wide staking.

* **Canceled delegated TRX amount**: The amount of staked TRX reclaimed in the cancel delegation transaction.
* **Recipient's total staked TRX amount for that resource**: The total staked TRX used by the recipient to obtain a specific resource (Energy or Bandwidth), including self-staked TRX (Stake 1.0 and Stake 2.0) and delegated TRX from others. This can be queried via the [wallet/getaccount](https://developers.tron.network/reference/account-getaccount#/) API.
* **Recipient's unrecovered resource amount**: The amount of resources that have already been consumed and are currently in the recovery period on the recipient’s account. This can be queried via [wallet/getaccount](https://developers.tron.network/reference/account-getaccount#/) or [wallet/getaccountresource](https://developers.tron.network/reference/getaccountresource#/).

### 2. Account State Changes

After resource undelegation, the effective resource-related states of both accounts are changed as follows.
The following expressions describe the changes at a logical level. The term “staked amount” represents a computed value rather than a single on-chain field.

**Delegator**

```
Staked amount = Original staked amount + Canceled delegated TRX amount

Unrecovered resource amount = Original unrecovered resource amount + Reclaimed unrecovered resource amount
```

**Recipient**

```
Staked amount = Original staked amount - Canceled delegated TRX amount

Unrecovered resource amount = Original unrecovered resource amount - Reclaimed unrecovered resource amount
```

**Note on Recovery:** Resources recover linearly over a **24-hour period**. If an account uses resources again or reclaims delegated resources during this period, the system performs a weighted merger of the existing recovery progress and the new recovery cycle. 

## Example

Assume the current network resource conversion ratio is 1 TRX Staked = 0.2 Energy, and the total network staking amount remains unchanged. User X delegated 200 TRX worth of Energy to User Y. Before the delegation is canceled, the account states are:

| Account | Role      | Total Staked TRX (for Energy) | Total Energy | Unrecovered Energy |
| ------- | --------- | ----------------------------- | ------------ | ------------------ |
| X       | Delegator | 1000 TRX                      | 200 Energy   | 75 Energy          |
| Y       | Recipient | 500 TRX                       | 100 Energy   | 50 Energy          |

When User X cancels the Energy delegation of 200 TRX to User Y:

```
Reclaimed unrecovered Energy amount = (200 / 500) * 50 = 20 Energy
```

After reclamation, the account states become:

| Account | Role      | Total Staked TRX (for Energy) | Total Energy | Unrecovered Energy |
| :------ | :-------- | :---------------------------- | :----------- | :----------------- |
| X       | Delegator | 1200 TRX (1000+200)           | 240 Energy   | 95 Energy (75+20)  |
| Y       | Recipient | 300 TRX (500-200)             | 60 Energy    | 30 Energy (50-20)  |
