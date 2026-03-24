---
title: Feelimit and energy calculation(user must read)
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
## 1. How to Set Fee Limit (Caller Must Read)

Within the scope of this section, the smart contract developer will be called "developer", the users or other contracts which call the smart contract will be called "caller."

The amount of energy consumed while calling the contract can be converted to TRX or SUN, so within the scope of this section when referring to the consumption of the resource, there's no strict difference between Energy, TRX and SUN unless they are used as a number unit.

Set a rational fee limit can guarantee the smart contract execution. And if the execution of the contract cost great energy, it will not consume too much energy from the caller. Before you set the fee limit, you need to know several conceptions:

1. The legal fee limit is an integer between 0 - 10^9, and the unit is SUN.

2. Different smart contracts consume different amount of energy due to their complexity. The same trigger in the same contract almost consumes the same amount fo energy\[1]. When the contract is triggered, the commands will be executed one by one and consume energy. If it reaches the fee limit, commands will fail to be executed, and energy is not refundable.

3. Currently fee limit only refers to the energy converted to SUN that will be consumed from the caller. The energy consumed by triggering contract also includes the developer's share.

4. For a vicious contract, if it encounters execution timeout or bug crash, all its energy will be consumed.

5. The developer may undertake a proportion of energy consumption(like 90%). But if the developer's energy is not enough for consumption, the rest of the energy consumption will be undertaken by caller completely. Within the fee limit range, if the caller does not have enough energy, then it will burn an equivalent amount of TRX.

To encourage the caller to trigger the contract, usually, the developer has enough energy.

## 2. Energy Calculation (Developer Must Read)

1.In order to punish the vicious developer, for the abnormal contract, if the execution times out (more than 50ms) or quits due to bug (revert not included), the maximum available energy will be deducted. If the contract is executed normally or reverted, it only costs the energy needed.

2. The developer can set the proportion of the energy consumption it undertakes during the execution, and this proportion can be changed later. If the developer's energy is not enough, it will consume the caller's energy.

3. Currently, the total energy available when trigger a contract is composed of caller fee limit and developer's share

**Note:**

* If the developer is not sure if the contract will work, do not set caller's energy consumption proportion to 0%, in case all developer's energy will be deducted due to vicious execution.
* We recommend setting caller's energy consumption proportion to 10% \~ 100%.

If contract executes successfully without any exception, the energy needed for the execution will be deducted. Generally, it is far less than the amount of energy this trigger can use.

If Assert-style error comes out, it will consume the whole number of energy set for fee limit.

Assert-style error introduction, refer to：[Exception Handling](https://developers.tron.network/docs/exception-handling) 

10% - 100% is recommended to set for consume\_user\_resource\_percent to avoid unnecessary loss.
