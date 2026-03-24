---
title: TRX Info
excerpt: >-
  Comprehensive TRX token analysis with price, supply dynamics, burn rate, and
  staking yield.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                           |
| :----------- | :-------------------------------------------------------------- |
| **Skill ID** | `trongrid-trx-info`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-trx-info) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Analyze TRX economics including price, supply dynamics, burn rate, staking yield, and network health.

## Workflow

1. Gather on-chain data (burns, chain params, resource prices)
2. Calculate supply metrics
3. Fetch market data
4. Assess SR reward economics
5. Generate TRX value report

## Output Example

```
TRX Overview

Price & Market:
- Current price: $0.15
- 24h change: +3.2%
- Market cap: $13.2B
- 24h volume: $890M
- Market rank: #12

Supply Dynamics:
- Total supply: 88.0B TRX
- Circulating: 88.0B TRX
- 24h burned: 1.2M TRX
- Annual burn rate: 0.5%

Network Economics:
- Energy price: 420 SUN/Energy
- Bandwidth price: 1,000 SUN/Bandwidth
- Staking APY: 4.2%
- Total staked: 48.5B TRX (55%)

Value Assessment:
- Network activity: High (7.3M daily transactions)
- Ecosystem health: Excellent
- Deflationary pressure: Medium (burn vs issuance)
```

## How to Trigger

**Natural language**:

* "TRX price"
* "TRX burn rate"
* "How is TRX doing?"

**Direct call**:

```
/trongrid-trx-info
```

## Related Skills

* [Data Insights](./data-insights): TRX in network context
* [Account Profiling](./account-profiling): Analyze TRX holders
