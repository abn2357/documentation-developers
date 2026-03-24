---
title: Token Scanner
excerpt: >-
  Deep dive into specific tokens with supply metrics, holder distribution, and
  safety assessment.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                                |
| :----------- | :------------------------------------------------------------------- |
| **Skill ID** | `trongrid-token-scanner`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-token-scanner) |

## Installation

### Step 1: Install MCP Server

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Analyze individual TRC-20 or TRC-10 tokens with supply metrics, holder distribution, activity data, and safety assessment.

## Workflow

1. Identify token
2. Fetch metadata
3. Analyze holder distribution
4. Examine transaction activity
5. Fetch market data
6. Perform safety assessment
7. Generate token report

## Output Example

```
Token Report: USDT (TR7N...)

Basic Info:
- Name: Tether USD
- Symbol: USDT
- Decimals: 6
- Type: TRC-20

Supply & Market:
- Total supply: 50.2B USDT
- Circulating: 50.2B USDT
- Market cap: $50.2B
- 24h volume: $8.5B

Holder Analysis:
- Total holders: 8.2M
- Top 10 hold: 35% (concentration: Medium)
- Top 100 hold: 68%

Activity Metrics:
- 24h transactions: 3.2M
- 24h active addresses: 450K
- Average transaction: $2,500

Safety Score: ✅ Low Risk
- Official Tether contract
- Verified source code
- Healthy holder distribution
```

## How to Trigger

**Natural language**:

* "Tell me about USDT on TRON"
* "Is this token safe?"
* "Analyze token TR7N..."

**Direct call**:

```
/trongrid-token-scanner USDT
/trongrid-token-scanner TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

## Related Skills

* [Contract Analysis](./contract-analysis): Analyze the token's smart contract
* [Token List](./token-list): Compare with other tokens
