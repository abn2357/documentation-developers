---
title: Stake TRX for Energy and OUT_OF_ENERGY
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
As explained in the [energy usage model](https://developers.tron.network/docs/energy), developers gain energy either from staking TRX to get dynamically-allocated energy (stake TRX / network total \* total available, currently 90 billion), or from burning TRX directly to obtain fixed energy (currently 1 energy = 280 sun).

Under normal circumstances, both strategies should provide enough energy for smart contract deploy/execution. However, due to the way *fee\_limit* is set up, if a developer stakes too much TRX for energy, this account's energy calculation is bound to the stake model. The max energy this account can use is limited to **fee\_limit (up to 10000 TRX) / total network stake TRX \* 90 billion**. If the upper bound is hit, an **OUT\_OF\_ENERGY** error will be thrown, without burning TRX. If the amount of energy staked isn't too much, it is possible to combine both strategies to account for total used energy.

The specific formula is:

```go
const R = Dynamic Energy Limit
const F = Daily account energy from staking TRX
const E = Remaining daily account energy from staking TRX
const L = Fee limit in TRX set in deploy/trigger call
const T = Remaining usable TRX in account
const C = Energy per TRX if purchased directly

// Calculate M, defined as maximum energy limit for deployment/trigger of smart contract
if F > L*R
	let M = min(E+T*C, L*R)
else
	let M = E+T*C
```

Developers can also use the user-friendly [energy calculator](https://tronstation.io/calculator) to calculate the energy amount an account can use to deploy/execute smart contracts, and how much they will cost.

As general advice, developers are discouraged from staking too much TRX (making it unfair for other developers). Otherwise, they are bound to the lower energy upper cap, rather than from burning TRX directly. If an account is in such a situation and a large contract needs to be deployed, try to either unstake some TRX or transfer TRX to a new account without staking TRX.
