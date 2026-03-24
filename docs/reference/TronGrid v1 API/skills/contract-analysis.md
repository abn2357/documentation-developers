---
title: Contract Analysis
excerpt: >-
  Deep analysis of TRON smart contracts with ABI parsing, energy costs, and
  safety assessment.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                                    |
| :----------- | :----------------------------------------------------------------------- |
| **Skill ID** | `trongrid-contract-analysis`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-contract-analysis) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Inspect smart contracts to understand their functionality, usage patterns, energy costs, and safety profile.

## Workflow

1. Fetch contract basics
2. Parse ABI methods
3. Analyze transaction activity
4. Identify top callers
5. Estimate energy costs
6. Perform safety assessment
7. Generate analysis report

## Output Example

```
Contract Analysis: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t (USDT)

Basic Info:
- Type: TRC-20 token contract
- Deployed: 2019-04-10
- Creator: TXxx...

Method Stats:
- Total methods: 15
- Popular methods: transfer (73%), approve (15%), transferFrom (8%)

Activity Metrics:
- Total transactions: 1.2B+
- Daily average: 500K+
- Unique callers: 8M+

Energy Economics:
- transfer avg cost: 14,631 Energy
- approve avg cost: 8,500 Energy

Safety Score: ✅ Safe
- Verified contract
- Official Tether deployment
- No known vulnerabilities
```

## How to Trigger

**Natural language**:

* "Is this contract safe?"
* "Analyze contract TR7N..."
* "What does this contract do?"

**Direct call**:

```
/trongrid-contract-analysis TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t
```

## Related Skills

* [Token Scanner](./token-scanner): Analyze TRC-20 tokens deployed by this contract
* [Transaction Info](./transaction-info): Investigate contract interactions
