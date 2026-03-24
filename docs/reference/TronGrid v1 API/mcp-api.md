---
title: MCP API
deprecated: false
hidden: false
metadata:
  robots: index
---
# TronGrid MCP Server Guide

## 1. Introduction

TronGrid MCP Server is a service based on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) that exposes the query and operation capabilities on TRON blockchain as standardized MCP tools. This enables AI clients (such as Claude, Cursor, custom Agents, etc.) to directly interact with TRON network.

## 2. Quick Start

### MCP Service URL

| Environment | URL                                                        |
| ----------- | ---------------------------------------------------------- |
| Production  | [https://mcp.trongrid.io/mcp](https://mcp.trongrid.io/mcp) |

### Protocol

* **MCP Protocol Version**: 2025-11-25
* **Transport Protocol**: Streamable HTTP

## 3. Client Configuration

### 3.1 Claude Desktop

Edit the configuration file:

* macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
* Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```
{
  "mcpServers": {
    "trongrid": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.trongrid.io/mcp"
      ]
    }
  }
}
```

To pass an API Key:

```
{
  "mcpServers": {
    "trongrid": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.trongrid.io/mcp",
        "--header",
        "TRON-PRO-API-KEY:<your-api-key>"
      ]
    }
  }
}
```

### 3.2 Claude Code

#### Option 1: CLI Command

```
claude mcp add --transport http trongrid https://mcp.trongrid.io/mcp
```

#### Option 2: Project Configuration File

Create `.mcp.json` in the project root directory:

```
{
  "mcpServers": {
    "trongrid": {
      "type": "http",
      "url": "https://mcp.trongrid.io/mcp"
    }
  }
}
```

## 4. MCP Protocol Basics

MCP uses Streamable HTTP for transport, with all communication performed via the `POST /mcp` endpoint. The protocol is **stateful** and requires a sequential handshake:

```text
┌──────────┐                      ┌──────────┐
│  Client  │                      │  Server  │
└────┬─────┘                      └────┬─────┘
     │  1. initialize                  │
     │ ──────────────────────────────► │
     │ ◄── mcp-session-id ──────────── │
     │                                 │
     │  2. notifications/initialized   │
     │ ──────────────────────────────► │
     │ ◄── 202 Accepted ────────────── │
     │                                 │
     │  3. tools/list                  │
     │ ──────────────────────────────► │
     │ ◄── tool list ───────────────── │
     │                                 │
     │  4. tools/call                  │
     │ ──────────────────────────────► │
     │ ◄── tool execution result ───── │
     └                                 ┘

```

All requests must carry the following headers:

| Header           | Value                                 | Description                                      |
| ---------------- | ------------------------------------- | ------------------------------------------------ |
| `Content-Type`   | `application/json`                    | Required                                         |
| `Accept`         | `application/json, text/event-stream` | Required                                         |
| `mcp-session-id` | `<session-id>`                        | Required for requests after handshake completion |

## 5. Manual Testing with curl

### Step 1 — Initialization (Obtain Session ID)

```bash
curl -v -X POST https://mcp.trongrid.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2026-03-06",
      "capabilities": {},
      "clientInfo": { "name": "curl-test", "version": "1.0" }
    }
  }'

```

Find the `mcp-session-id` in the response and save it for subsequent requests.

### Step 2 — Send initialized Notification

```bash
curl -X POST https://mcp.trongrid.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <your-session-id>" \
  -d '{
    "jsonrpc": "2.0",
    "method": "notifications/initialized",
    "params": {}
  }'

```

A return of `202 Accepted` indicates success.

### Step 3 — View Available Tools

```bash
curl -X POST https://mcp.trongrid.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <your-session-id>" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'

```

### Step 4 — Call a Tool

Take querying block statistics as an example:

```bash
curl -X POST https://mcp.trongrid.io/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <your-session-id>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
      "name": "getBlockStatistics",
      "arguments": { "blockNum": 68000000 }
    }
  }'

```

## 6. Available Tool Categories

The server exposes a total of **151 MCP tools**, covering major queries and operations on the TRON network:

### 6.1 HTTP REST API Query Tools (18 tools)

Query on-chain data through the TronGrid REST API.

#### Blocks (1)

| Tool Name            | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `getBlockStatistics` | Get statistics for a specific TRON block by block number |

#### Accounts (6)

| Tool Name                       | Description                                             |
| ------------------------------- | ------------------------------------------------------- |
| `getAccountInfo`                | Get account information for a TRON address              |
| `getAccountTransactions`        | Get recent transactions for a TRON account address      |
| `getAccountTrc20Transactions`   | Get TRC-20 token transfer history for a TRON account    |
| `getInternalTransactions`       | Get internal transactions for a TRON account address    |
| `getInternalTransactionsByTxId` | Get internal transactions for a specific transaction ID |
| `getTrc20Balance`               | Get TRC-20 token balances for a TRON account address    |

#### Assets (3)

| Tool Name              | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `listAllAssets`        | List all TRC-10 assets (tokens) on the TRON blockchain |
| `getAssetByName`       | Get TRC-10 assets by name                              |
| `getAssetByIdentifier` | Get a TRC-10 asset by its numeric ID or issuer address |

#### Contracts (3)

| Tool Name                         | Description                                             |
| --------------------------------- | ------------------------------------------------------- |
| `getContractTransactions`         | Get transactions for a smart contract address           |
| `getContractInternalTransactions` | Get internal transactions for a smart contract          |
| `getTrc20TokenHolders`            | Get TRC-20 token holder balances for a contract address |

#### Events (4)

| Tool Name                    | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| `getEventsByTransactionId`   | Get events emitted by a specific transaction   |
| `getEventsByContractAddress` | Get events emitted by a smart contract address |
| `getEventsByBlockNumber`     | Get events from a specific block number        |
| `getEventsByLatestBlock`     | Get events from the latest block               |

#### TRC-20 Tokens (1)

| Tool Name      | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| `getTrc20Info` | Get token info (name, symbol, decimals) for TRC-20/721/1155 tokens |

### 6.2 Wallet Operation Tools (75 tools)

Full Node `/wallet/*` API endpoints for transaction creation & broadcast, account management, resource staking & delegation, smart contracts, Super Representatives, and governance proposals.

#### Address Validation & Transaction Broadcast (3)

| Tool Name              | Description                                        |
| ---------------------- | -------------------------------------------------- |
| `validateAddress`      | Validate a TRON address format                     |
| `broadcastTransaction` | Broadcast a signed transaction to the TRON network |
| `broadcastHex`         | Broadcast a signed hex-encoded transaction to TRON |

#### Account Management (5)

| Tool Name                 | Description                                                |
| ------------------------- | ---------------------------------------------------------- |
| `createAccount`           | Activate an account on the TRON network                    |
| `getAccount`              | Query account on-chain info (TRX balance, assets, staking) |
| `updateAccount`           | Update account name on TRON                                |
| `accountPermissionUpdate` | Update account permissions                                 |
| `getApprovedList`         | Get list of approved signers for a transaction             |

#### TRX Transfer (1)

| Tool Name           | Description                       |
| ------------------- | --------------------------------- |
| `createTransaction` | Create a TRX transfer transaction |

#### Account Resource Queries (3)

| Tool Name            | Description                                   |
| -------------------- | --------------------------------------------- |
| `getAccountBalance`  | Get account balance at a specific block       |
| `getAccountResource` | Get account resource info (bandwidth, energy) |
| `getAccountNet`      | Get account bandwidth info                    |

#### Resource Staking & Delegation — Stake 1.0 (4)

| Tool Name                          | Description                                             |
| ---------------------------------- | ------------------------------------------------------- |
| `freezeBalance`                    | [Deprecated] Stake TRX for bandwidth/energy (Stake 1.0) |
| `unfreezeBalance`                  | [Deprecated] Unstake TRX (Stake 1.0)                    |
| `getDelegatedResource`             | Query resource delegation info                          |
| `getDelegatedResourceAccountIndex` | Query delegation index                                  |

#### Resource Staking & Delegation — Stake 2.0 (11)

| Tool Name                            | Description                                  |
| ------------------------------------ | -------------------------------------------- |
| `freezeBalanceV2`                    | Stake TRX for bandwidth/energy (Stake 2.0)   |
| `unfreezeBalanceV2`                  | Unstake TRX (Stake 2.0)                      |
| `cancelAllUnfreezeV2`                | Cancel all pending unstaking in Stake 2.0    |
| `delegateResource`                   | Delegate bandwidth/energy to another account |
| `unDelegateResource`                 | Undelegate bandwidth/energy                  |
| `withdrawExpireUnfreeze`             | Withdraw expired unstaked TRX                |
| `getAvailableUnfreezeCount`          | Get remaining unstaking slots                |
| `getCanWithdrawUnfreezeAmount`       | Get withdrawable unstaked TRX amount         |
| `getCanDelegatedMaxSize`             | Get max delegatable resource amount          |
| `getDelegatedResourceV2`             | Query Stake 2.0 delegation info              |
| `getDelegatedResourceAccountIndexV2` | Query Stake 2.0 delegation index             |

#### Block Queries (3)

| Tool Name                      | Description                                    |
| ------------------------------ | ---------------------------------------------- |
| `getBlock`                     | Get TRON block header or full block            |
| `getBlockBalance`              | Get all balance-changing operations in a block |
| `getTransactionInfoByBlockNum` | Get all transaction info in a block            |

#### Transaction Queries (5)

| Tool Name                       | Description                              |
| ------------------------------- | ---------------------------------------- |
| `getTransactionById`            | Get transaction info by ID               |
| `getTransactionInfoById`        | Get transaction fee & receipt info by ID |
| `getTransactionListFromPending` | Get pending transaction IDs              |
| `getTransactionFromPending`     | Get a specific pending transaction       |
| `getPendingSize`                | Get pending transaction pool size        |

#### Network & Chain Parameters (5)

| Tool Name            | Description                     |
| -------------------- | ------------------------------- |
| `listNodes`          | List all TRON network nodes     |
| `getNodeInfo`        | Get TRON node information       |
| `getChainParameters` | Get TRON chain parameters       |
| `getEnergyPrices`    | Get historical energy prices    |
| `getBandwidthPrices` | Get historical bandwidth prices |

#### Other Chain Queries (1)

| Tool Name    | Description                 |
| ------------ | --------------------------- |
| `getBurnTrx` | Get total burned TRX amount |

#### TRC-10 Asset Management (11)

| Tool Name                    | Description                                |
| ---------------------------- | ------------------------------------------ |
| `getAssetIssueByAccount`     | Get TRC-10 assets issued by an account     |
| `getAssetIssueById`          | Get TRC-10 asset by token ID               |
| `getAssetIssueByName`        | Get TRC-10 asset by name                   |
| `getAssetIssueList`          | Get all TRC-10 assets                      |
| `getAssetIssueListByName`    | Get TRC-10 assets by name (list)           |
| `getPaginatedAssetIssueList` | Get TRC-10 assets with pagination          |
| `createAssetIssue`           | Issue a new TRC-10 token                   |
| `participateAssetIssue`      | Participate in a TRC-10 token issuance     |
| `transferAsset`              | Create a TRC-10 token transfer transaction |
| `unfreezeAsset`              | Unfreeze TRC-10 tokens                     |
| `updateAsset`                | Update TRC-10 token parameters             |

#### Smart Contracts (9)

| Tool Name                 | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `getContract`             | Get smart contract bytecode and ABI                 |
| `getContractInfo`         | Get smart contract info including energy settings   |
| `triggerSmartContract`    | Trigger a smart contract function call              |
| `triggerConstantContract` | Pre-execute (simulate) a smart contract call        |
| `deployContract`          | Deploy a new smart contract on TRON                 |
| `updateSetting`           | Update smart contract consume_user_resource_percent |
| `updateEnergyLimit`       | Update smart contract origin_energy_limit           |
| `clearAbi`                | Clear a smart contract's ABI                        |
| `estimateEnergy`          | Estimate energy required for a contract call        |

#### Super Representative (SR) Management (8)

| Tool Name                | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `createWitness`          | Apply to become a Super Representative candidate |
| `updateWitness`          | Update Super Representative info                 |
| `getBrokerage`           | Get SR reward brokerage ratio                    |
| `updateBrokerage`        | Update SR reward brokerage ratio                 |
| `voteWitnessAccount`     | Vote for Super Representatives                   |
| `getReward`              | Get unclaimed voting rewards                     |
| `withdrawBalance`        | Withdraw SR rewards                              |
| `getNextMaintenanceTime` | Get next TRON voting maintenance time            |

#### SR Listing (1)

| Tool Name                    | Description           |
| ---------------------------- | --------------------- |
| `getPaginatedNowWitnessList` | Get paginated SR list |

#### Governance Proposals (5)

| Tool Name         | Description                     |
| ----------------- | ------------------------------- |
| `listProposals`   | List all TRON network proposals |
| `getProposalById` | Get a specific proposal by ID   |
| `proposalCreate`  | Create a new network proposal   |
| `proposalApprove` | Approve a network proposal      |
| `proposalDelete`  | Delete a network proposal       |

### 6.3 WalletSolidity Read-Only Tools (25 tools)

Read data from the confirmed (irreversible) Solidity node, ensuring data finality. All tool names are prefixed with `solidity`.

#### Account (1)

| Tool Name            | Description                             |
| -------------------- | --------------------------------------- |
| `solidityGetAccount` | Query account info from solidified node |

#### Transaction Queries (4)

| Tool Name                               | Description                                |
| --------------------------------------- | ------------------------------------------ |
| `solidityGetTransactionById`            | Get confirmed transaction by ID            |
| `solidityGetTransactionInfoById`        | Get confirmed transaction fee info by ID   |
| `solidityGetTransactionInfoByBlockNum`  | Get confirmed transaction info in a block  |
| `solidityGetTransactionCountByBlockNum` | Get transaction count in a confirmed block |

#### Block Queries (1)

| Tool Name          | Description                           |
| ------------------ | ------------------------------------- |
| `solidityGetBlock` | Get confirmed block header/full block |

#### Resource Delegation Queries (7)

| Tool Name                                    | Description                                           |
| -------------------------------------------- | ----------------------------------------------------- |
| `solidityGetDelegatedResource`               | Query delegation info from solidified node            |
| `solidityGetDelegatedResourceAccountIndex`   | Query delegation index from solidified node           |
| `solidityGetDelegatedResourceV2`             | Query Stake 2.0 delegation from solidified node       |
| `solidityGetDelegatedResourceAccountIndexV2` | Query Stake 2.0 delegation index from solidified node |
| `solidityGetCanDelegatedMaxSize`             | Get max delegatable amount from solidified node       |
| `solidityGetCanWithdrawUnfreezeAmount`       | Get withdrawable amount from solidified node          |
| `solidityGetAvailableUnfreezeCount`          | Get unstaking slots from solidified node              |

#### Node & Chain Info (2)

| Tool Name             | Description                               |
| --------------------- | ----------------------------------------- |
| `solidityGetNodeInfo` | Get TRON solidified node information      |
| `solidityGetBurnTrx`  | Get total burned TRX from solidified node |

#### Smart Contracts (2)

| Tool Name                         | Description                                |
| --------------------------------- | ------------------------------------------ |
| `solidityTriggerConstantContract` | Simulate contract call on solidified state |
| `solidityEstimateEnergy`          | Estimate energy on solidified state        |

#### TRC-10 Asset Queries (5)

| Tool Name                            | Description                                      |
| ------------------------------------ | ------------------------------------------------ |
| `solidityGetAssetIssueById`          | Get TRC-10 asset by ID from solidified node      |
| `solidityGetAssetIssueByName`        | Get TRC-10 asset by name from solidified node    |
| `solidityGetAssetIssueList`          | Get all TRC-10 assets from solidified node       |
| `solidityGetAssetIssueListByName`    | Get TRC-10 assets by name from solidified node   |
| `solidityGetPaginatedAssetIssueList` | Get paginated TRC-10 assets from solidified node |

#### Super Representative Queries (3)

| Tool Name                            | Description                                |
| ------------------------------------ | ------------------------------------------ |
| `solidityGetReward`                  | Get unclaimed rewards from solidified node |
| `solidityGetBrokerage`               | Get SR brokerage from solidified node      |
| `solidityGetPaginatedNowWitnessList` | Get paginated SR list from solidified node |

### 6.4 JSON-RPC Tools (33 tools)

Ethereum-compatible JSON-RPC API methods for developers transitioning from the Ethereum ecosystem.

#### Accounts & Balances (1)

| Tool Name       | Description                       |
| --------------- | --------------------------------- |
| `ethGetBalance` | Returns balance of a TRON account |

#### Block Operations (7)

| Tool Name                             | Description                                |
| ------------------------------------- | ------------------------------------------ |
| `ethBlockNumber`                      | Returns the most recent TRON block number  |
| `ethGetBlockByHash`                   | Get TRON block by hash                     |
| `ethGetBlockByNumber`                 | Get TRON block by number                   |
| `ethGetBlockReceipts`                 | Get all receipts for a TRON block          |
| `ethGetBlockTransactionCountByHash`   | Get transaction count in a block by hash   |
| `ethGetBlockTransactionCountByNumber` | Get transaction count in a block by number |
| `ethGetWork`                          | Returns current TRON block hash            |

#### Transaction Operations (6)

| Tool Name                                | Description                                                    |
| ---------------------------------------- | -------------------------------------------------------------- |
| `ethGetTransactionByHash`                | Get TRON transaction by hash                                   |
| `ethGetTransactionByBlockHashAndIndex`   | Get transaction by block hash and index                        |
| `ethGetTransactionByBlockNumberAndIndex` | Get transaction by block number and index                      |
| `ethGetTransactionReceipt`               | Get TRON transaction receipt                                   |
| `ethCall`                                | Execute a read-only message call on TRON                       |
| `buildTransaction`                       | Build a TRON transaction (TRX transfer, TRC-20, contract call) |

#### Contracts & Storage (4)

| Tool Name         | Description                                        |
| ----------------- | -------------------------------------------------- |
| `ethGetCode`      | Get contract bytecode at a TRON address            |
| `ethGetStorageAt` | Get storage value at a TRON contract address       |
| `ethEstimateGas`  | Estimate energy consumption for a TRON transaction |
| `ethGasPrice`     | Returns current energy price in sun                |

#### Filters & Logs (6)

| Tool Name             | Description                               |
| --------------------- | ----------------------------------------- |
| `ethNewFilter`        | Create a TRON log filter                  |
| `ethNewBlockFilter`   | Create a TRON new block filter            |
| `ethGetFilterChanges` | Poll for TRON filter changes              |
| `ethGetFilterLogs`    | Get logs matching a TRON filter           |
| `ethGetLogs`          | Get logs matching filter criteria on TRON |
| `ethUninstallFilter`  | Uninstall a TRON filter                   |

#### Chain & Network Info (9)

| Tool Name            | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `ethChainId`         | Returns the TRON chain ID                            |
| `ethCoinbase`        | Returns the Super Representative address of the node |
| `ethProtocolVersion` | Returns TRON block version                           |
| `ethSyncing`         | Returns TRON sync status                             |
| `netListening`       | Check if TRON client is listening                    |
| `netPeerCount`       | Get number of peers connected to TRON                |
| `netVersion`         | Returns TRON genesis block hash                      |
| `web3ClientVersion`  | Returns TRON node client version                     |
| `web3Sha3`           | Compute Keccak-256 hash on TRON                      |

## 7. Integrating with AI Clients

### Direct Connection Mode (Clients Supporting Streamable HTTP)

Add the following configuration to your MCP client configuration file:

```json
{
  "mcpServers": {
    "trongrid-mcp": {
      "url": "https://mcp.trongrid.io/mcp"
    }
  }
}

```

### Bridging via mcp-remote (Claude Code, etc.)

For clients that do not directly support Streamable HTTP (like Claude Code), you can use `mcp-remote` as a bridge:

```json
{
  "mcpServers": {
    "mcp-server-trongrid": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.trongrid.io/mcp"]
    }
  }
}

```

## 8. FAQ

**Q: Tool call returns `405 Method Not Allowed`?**

A: The session may have expired or become invalid. Please re-run the `initialize` handshake process.

**Q: Receiving TronGrid API rate limit errors?**

A: pass your API Key via the `TRON-PRO-API-KEY` request header.

**Q: curl request returns no data?**

A: Ensure the request header includes `Accept: application/json, text/event-stream`, which is mandatory for the Streamable HTTP protocol.
