---
title: Account Profiling
excerpt: >-
  Build a comprehensive profile of any TRON account with assets, resources, and
  activity analysis.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                                    |
| :----------- | :----------------------------------------------------------------------- |
| **Skill ID** | `tronggrid-account-profiling`                                            |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-account-profiling) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Analyze TRON accounts to understand their assets, resources, staking behavior, transaction patterns, and overall activity.

## Workflow

1. Validate address
2. Fetch account fundamentals (balance, resources)
3. Analyze token holdings
4. Review staking & voting activity
5. Examine transaction history
6. Assess DeFi participation
7. Generate comprehensive report

## Output Example

```
Account Profile: TRfYy...

Assets:
- TRX: 1,000,000 (worth $150,000)
- USDT: 500,000
- Other tokens: 15 types

Resources:
- Energy: 50,000 / 100,000 (50% used)
- Bandwidth: 1,500 / 5,000

Staking & Voting:
- Staked: 500,000 TRX
- Voting for: SR_Name (500,000 votes)

Classification: Whale
Activity: High (10+ daily transactions)
```

## How to Trigger

**Natural language**:

* "Analyze wallet TRfYy..."
* "What does this address hold?"
* "Profile account TXxx..."

**Direct call**:

```
/trongrid-account-profiling TRfYy...
```

## Related Skills

* [Token Scanner](./token-scanner): Deep dive into specific tokens held
* [Transaction Info](./transaction-info): Investigate specific transactions
* [Data Insights](./data-insights): Compare with network averages
