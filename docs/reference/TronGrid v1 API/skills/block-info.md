---
title: Block Info
excerpt: >-
  Query and analyze TRON blocks with producer info, transaction breakdown, and
  resource consumption.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                             |
| :----------- | :---------------------------------------------------------------- |
| **Skill ID** | `trongrid-block-info`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-block-info) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Examine block data including producer information, transaction breakdown, rewards, burns, and resource consumption.

## Workflow

1. Fetch block data
2. Parse block header
3. Identify block producer (SR)
4. Analyze transactions by type
5. Calculate rewards & burns
6. Assess network load
7. Generate block report

## Output Example

```
Block #67890123

Producer: SR_Name
Time: 2026-03-16 04:20:15 UTC
Transactions: 245

Transaction Distribution:
- TRC-20 transfers: 180 (73%)
- TRX transfers: 45 (18%)
- Contract calls: 20 (9%)

Economics:
- Block reward: 16 TRX
- Fees: 1,234 TRX
- TRX burned: 617 TRX

Resource Consumption:
- Energy: 45,000,000
- Bandwidth: 123,456
```

## How to Trigger

**Natural language**:

* "Latest block"
* "Block #67890123 details"
* "What's in the newest block?"

**Direct call**:

```
/trongrid-block-info
/trongrid-block-info 67890123
```

## Related Skills

* [Transaction Info](./transaction-info): Analyze specific transactions in the block
* [Data Insights](./data-insights): Compare block metrics with network trends
