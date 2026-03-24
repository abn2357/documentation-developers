---
title: Data Insights
excerpt: >-
  Comprehensive TRON network analytics with activity metrics, trending
  contracts, and governance statistics.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                                |
| :----------- | :------------------------------------------------------------------- |
| **Skill ID** | `trongrid-data-insights`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-data-insights) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Understand TRON ecosystem health through activity metrics, trending contracts, hot tokens, and governance statistics.

## Workflow

1. Network activity snapshot
2. Analyze recent blocks
3. Calculate transaction type distribution
4. Identify hot contracts
5. Identify trending tokens
6. Find most active accounts
7. Review governance metrics
8. Generate insights report

## Output Example

```
TRON Network Insights

Network Activity:
- Current TPS: 85
- Daily transactions: 7.3M
- Active addresses: 2.1M

Transaction Distribution:
- TRC-20 transfers: 68%
- TRX transfers: 22%
- Contract calls: 10%

Hot Contracts (24h):
1. USDT (TR7N...): 3.2M transactions
2. SunSwap Router: 450K transactions
3. JustLend: 280K transactions

Trending Tokens:
1. NEW_TOKEN: +450% volume
2. MEME_COIN: +230% holders

Governance:
- Total staked: 48.5B TRX (45% of supply)
- Active SRs: 27
- Average voting rate: 89%
```

## How to Trigger

**Natural language**:

* "How is the TRON network doing?"
* "Network stats"
* "TRON ecosystem overview"

**Direct call**:

```
/trongrid-data-insights
```

## Related Skills

* [Block Info](./block-info): Detailed block-level analysis
* [Token List](./token-list): Explore trending tokens
* [TRX Info](./trx-info): TRX-specific metrics