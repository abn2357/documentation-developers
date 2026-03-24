---
title: Transaction Info
excerpt: 'Query and decode TRON transactions with resource consumption and event logs. '
deprecated: false
hidden: false
metadata:
  robots: index
---
## Reference

| Property     | Value                                                                   |
| :----------- | :---------------------------------------------------------------------- |
| **Skill ID** | `trongrid-transaction-info`                                             |
| **ClawHub**  | [View on ClawHub](https://clawhub.ai/greason/trongrid-transaction-info) |

## Installation

Ensure TronGrid MCP Server is connected. See [Quick Start](./skills#quick-start) for setup instructions.

## Purpose

Investigate transactions to understand their status, participants, resource consumption, and event logs.

## Workflow

1. Fetch transaction data + receipt
2. Determine confirmation status
3. Decode transaction type
4. Decode smart contract calls
5. Analyze resource consumption
6. Parse internal transactions
7. Parse event logs
8. Generate transaction report

## Output Example

```
Transaction Report: 7c2d4206c03a883dd9066d620335dc1be272a8dc...

Status: ✅ Success
Confirmations: 2,450 (Confirmed)
Time: 2026-03-16 04:15:30 UTC

Participants:
- From: TRfYy...
- To: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t (USDT contract)

Description:
Transfer 1,000 USDT to TXxx...

Resource Consumption:
- Energy: 14,631 (from stake)
- Bandwidth: 345 (from stake)
- Fee: 0 TRX

Event Logs:
- Transfer(from=TRfYy..., to=TXxx..., value=1000000000)

Internal Transactions: None
```

## How to Trigger

**Natural language**:

* "Check transaction 7c2d42..."
* "Why did my transaction fail?"
* "Transaction status for [hash]"

**Direct call**:

```
/trongrid-transaction-info 7c2d4206c03a883dd9066d620335dc1be272a8dc...
```

## Related Skills

* [Account Profiling](./account-profiling): Analyze transaction participants
* [Contract Analysis](./contract-analysis): Understand contract interactions
