---
title: Token List
excerpt: >-
  Browse and discover TRC-20/TRC-10 tokens with market metrics, rankings, and
  activity data.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                             |
| :----------- | :---------------------------------------------------------------- |
| **Skill ID** | `trongrid-token-list`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-token-list) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Discover tokens on TRON with market metrics, rankings, and activity data.

## Workflow

1. Fetch TRC-10 asset list
2. Fetch TRC-20 token data
3. Enrich with holder and activity data
4. Rank and categorize tokens
5. Generate token list report

## Output Example

```
TRON Token List

By Market Cap:
1. USDT: $50.2B market cap, 8.2M holders
2. USDC: $3.1B market cap, 450K holders
3. BTT: $890M market cap, 2.3M holders

Top Gainers (24h):
1. TOKEN_A: +125%
2. TOKEN_B: +89%

Most Active (24h):
1. USDT: 3.2M transactions
2. SUN: 450K transactions

Newly Launched (7d):
1. NEW_TOKEN: Launched 2 days ago, 15K holders
```

## How to Trigger

**Natural language**:

* "Top TRON tokens"
* "Trending TRC-20"
* "New tokens on TRON"

**Direct call**:

```
/trongrid-token-list
```

## Related Skills

* [Token Scanner](./token-scanner): Deep dive into specific tokens
* [Data Insights](./data-insights): Token activity in network context
