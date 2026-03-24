---
title: AI Agent Skills for TRON
excerpt: >-
  Pre-built workflows that enable AI agents to query TRON blockchain data
  through natural language.
deprecated: false
hidden: false
metadata:
  robots: index
---
## What Are Skills?

Skills are reusable instruction sets that let AI agents query TRON blockchain data through natural language, without manual API calls.

**Key Benefits**:

* 🚀 **Zero Code**: Ask questions in natural language
* 🎯 **Structured Output**: Automatically aggregates multiple API calls into formatted reports
* 🔄 **Reusable**: 8 pre-built workflows covering common analysis scenarios

## Quick Start

### 1. Install MCP Server

Add to your Claude Code MCP config (`~/.claude/mcp.json` or project `.mcp.json`):

```json
{
  "mcpServers": {
    "trongrid": {
      "type": "http",
      "url": "https://mcp.trongrid.io/mcp"
    }
  }
}
```

Optional: Add API key header for higher rate limits:

```json
{
  "mcpServers": {
    "trongrid": {
      "type": "http",
      "url": "https://mcp.trongrid.io/mcp",
      "headers": {
        "TRON-PRO-API-KEY": "your-api-key"
      }
    }
  }
}
```

Get API Key: [https://www.trongrid.io](https://www.trongrid.io)

### 2. Start Asking

Skills activate automatically. Simply ask questions:

```
"Analyze wallet TRfYy..."
"What is the latest block?"
"Tell me about USDT on TRON"
```

## Available Skills

| Skill                                    | Trigger Examples                 | Purpose                                                              |
| ---------------------------------------- | -------------------------------- | -------------------------------------------------------------------- |
| [Account Profiling](./account-profiling) | "Analyze this wallet"            | Comprehensive account analysis with assets, resources, and activity  |
| [Block Info](./block-info)               | "What is the latest block?"      | Block data, rewards, producer info, and transaction breakdown        |
| [Contract Analysis](./contract-analysis) | "Is this contract safe?"         | Smart contract inspection with ABI, callers, and safety assessment   |
| [Data Insights](./data-insights)         | "How is the TRON network doing?" | Network analytics with activity metrics and trending data            |
| [Token List](./token-list)               | "Top TRON tokens"                | Token discovery with market metrics and rankings                     |
| [Token Scanner](./token-scanner)         | "Tell me about USDT on TRON"     | Deep dive into specific tokens with holder analysis and safety score |
| [Transaction Info](./transaction-info)   | "Check transaction [hash]"       | Transaction decoding with resource consumption and event logs        |
| [TRX Info](./trx-info)                   | "TRX price", "TRX burn rate"     | TRX economics with supply dynamics and network metrics               |

## Use Cases

### Investment Analysis

* [Token Scanner](./token-scanner): Research token fundamentals
* [Token List](./token-list): Discover new opportunities
* [TRX Info](./trx-info): Monitor TRX price and staking yield
* [Account Profiling](./account-profiling): Track whale wallets

### Security Audit

* [Contract Analysis](./contract-analysis): Check contract safety
* [Token Scanner](./token-scanner): Assess token safety score
* [Transaction Info](./transaction-info): Investigate suspicious transactions

### Data Research

* [Data Insights](./data-insights): Understand ecosystem health
* [Block Info](./block-info): Study block rewards and resource consumption
* [Account Profiling](./account-profiling): Classify account behavior

## Troubleshooting

### MCP Server Not Connected

**Symptoms**: Skills don't activate, tools not found

**Solutions**:

1. Check `~/.claude/mcp.json` configuration
2. Restart Claude Code
3. Test connection: `npx @trongrid/mcp-server`

### Invalid API Key

**Symptoms**: Authentication errors on tool calls

**Solutions**:

1. Get new API key from [https://www.trongrid.io](https://www.trongrid.io)
2. Update `TRONGRID_API_KEY` in `mcp.json`
3. Restart Claude Code

### Rate Limit Exceeded

**Symptoms**: Requests rejected, rate limit error

**Solutions**:

1. Free tier: Wait 1 second and retry
2. Upgrade to paid API key (1000 req/s)

## Related Resources

* **TronGrid MCP Server**: [https://developers.tron.network/reference/mcp-api](https://developers.tron.network/reference/mcp-api)
* **TronGrid API Documentation**: [https://developers.tron.network/reference](https://developers.tron.network/reference)
* **ClawHub Skills**: [https://clawhub.ai/u/greason](https://clawhub.ai/u/greason)
