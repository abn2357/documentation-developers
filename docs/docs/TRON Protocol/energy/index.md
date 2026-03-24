---
title: Energy
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
# Introduction

The creation and operation of a smart contract consume CPU resources. It takes time for smart contracts to operate in virtual machines (VMs), and the time consumed in the system is calculated in microseconds. CPU resources are consumed in energy, which means 1 Energy = 1 Microsecond (μs). If a contract takes 100 μs to execute in a VM, it needs to consume 100 Energy. The total CPU resources provided by the TRON network are 100,000,000,000 Energy within 24 hours (based on current network parameter [#20](https://tronscan.org/#/sr/committee)).

# Gaining Energy

Energy can only be obtained by freezing the TRX. Energy obtained = the TRX frozen for gaining Energy / the total TRX frozen for gaining Energy in the entire network \* 100,000,000,000, which is the equally-divided fixed Energy for all users based on the frozen TRX.

For example, suppose the total amount of TRX frozen for gaining Energy is 1,000,000,000 TRX in the current network, and one account freezes 1000 TRX, which is one-millionth of the total and equals 100,000 microseconds. If executing a contract takes 1000 microseconds, then the user can trigger the contract 100 times.

**Note**

* Since the total frozen funds in the network and the frozen funds of accounts may change at any time, the CPU resources owned by accounts are not fixed.
* One cannot get both Bandwidth Points and Energy when freezing funds. If you freeze TRX to get bandwidth, then your Energy will not change.

# Energy Consumption

The creation and execution of smart contracts consume Energy, and other normal transactions do not consume Energy. Refer to the <a href="https://developers.tron.network/docs/energy-costs-calculation" target="_blank">Energy Consumption Mechanism guide</a> for details of the consumption process.

# Energy Calculator Tool

For estimating energy from freezing TRX and maximum energy limit to deploy/trigger smart contract, please use **<a href="https://tronstation.io/calculator" target="_blank">Tron Station</a>** energy tool to calculate.
