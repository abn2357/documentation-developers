---
title: Bandwidth Points
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: energy
      title: Energy
---
# Introduction

Scaling up any blockchain's network may lead to delays on transaction confirmation, as seen in the Ethereum and Bitcoin networks. To ensure smooth network operation, the TRON network grants every account a free pool of `Bandwidth Points` for free transactions every 24 hours. To engage in transactions more frequently requires freezing TRX for additional bandwidth points, or paying the fee in TRX. Transactions are transmitted and stored in the network in byte arrays. Bandwidth points consumed in a transaction equals the size of its byte array. 

# Bandwidth Points Calculation

Bandwidth points are the number of usable bytes for an account per day. In any given period, the entire network handles a fixed amount of bandwidth. The ratio of bandwidth points in an account to the bandwidth capacity of TRON’s network equals the rate of frozen balance in an account to frozen balance on the entire network. For example, if the frozen asset on the entire network totals 1,000,000 TRX and one given account froze 1,000 TRX (0.1% of total TRX frozen), then the account can perform roughly 300 transactions per day. **Note:** Since the amount of frozen asset on the entire network and for a certain account are subject to change, bandwidth points held by an account isn’t always fixed.

## Normal Transaction

In a normal transaction, bandwidth points are consumed as the following sequence:

1. Consume the bandwidth points the transaction initiator gained through frozen assets. 

2. Consume the transaction initiator's free bandwidth points.

3. Consume the transaction initiator's TRX, calculated as the number of bytes in the transaction \* 10 SUN.

## Create Account Transaction

If a transaction creates a new account, the bandwidth Points are consumed as follows:

1. Consume the bandwidth points the transaction initiator obtained from frozen TRX.

2. Consume the transaction initiator's 0.1TRX.

## TRC-10 Transfer

1. Consume the public free Bandwidth Point set by the token issuer.

2. Consume the bandwidth points obtained by the transaction initiator through frozen assets. 

3. Consume the transaction initiator's free bandwidth points. 

4. Consume the transaction initiator's TRX, calculated as the number of bytes in the transaction \* 10 SUN.

There's another situation: When you transfer(TRX or token) to an account that does not exist, this operation will create an account then do the transfer. It only consumes Bandwidth points for account creation and free for transfer.

# Bandwidth Points Sources 

There are 5000 bandwidth points for free per account per day. When an account hasn’t frozen any balance, or when its bandwidth points have run out, complimentary bandwidth points can be used. Each transaction in the TRON network is about 200 bytes, so each account enjoys about 25 transactions for free each day.  

Bandwidth points can be gained in two ways:

* Freezing TRX. The quota = the TRX frozen for gaining bandwidth points / the total TRX frozen in the network for gaining bandwidth points \* 43\_200\_000\_000, which is the equally-divided fixed bandwidth points quota for all users based on the frozen TRX.

* Fixed 5,000 free TRX quota for each account.

Use `wallet/freezebalance` to freeze an account's TRX and gain bandwidth and votes. 

# Query Account Bandwidth Points

Use an RPC call to query an account's available bandwidth points.

* `/wallet/getaccountnet` retrieves the bandwidth points information for an account. If a key isn't present, then the value is 0.

```json
{“freeNetUsed”: 557,“freeNetLimit”: 5000,“NetUsed”: 353,“NetLimit”: 5239157853,“TotalNetLimit”: 43200000000,“TotalNetWeight”: 41228}
```

# Bandwidth Points Calculator

For estimating BP from freezing TRX and maximum BP limit, please use **<a href="https://tronstation.io/bpcalc" target="_blank">Tron Station</a>** bandwidth points tool to calculate.

# Automatic Recovery of Bandwidth Points

If the total network locks funds and the account locked funds remain unchanged, the account bandwidth points consumed amount is proportionally attenuated with time and is attenuated to 0 at 24 hours. For example, between time T1 and T1+12 hours, the user consumes U amount of account bandwidth points. The account then uses bandwidth u again, resulting in a consumption of U/2 + u bandwidth points. The formula follows below:

<Image title="bandwidthRestoreEqn.gif" alt={220} src="https://files.readme.io/6097ba9-bandwidthRestoreEqn.gif">
  Bandwidth Points Restoration Equation
</Image>

Thus, the user consumed bandwidth value is reset to 0 every 24 hours.
