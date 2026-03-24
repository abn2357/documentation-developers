---
title: Nodes and Clients
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
TRON is a distributed network of computers running software (known as nodes) that can verify blocks and transaction data. You need an application, known as a client, on your computer to "run" a node.

## What are Nodes and Clients？

"Node" refers to a running instance of the client software. A client is an implementation of the TRON protocol that verifies all transactions in each block, keeping the network secure and the data accurate.

At present, the TRON client is implemented with the Java language, which follows the TRON protocol and realizes functions of the TRON blockchain.

## Node Types

There are different types of nodes in the TRON network.

### FullNode

A FullNode stores and synchronizes full blockchain data, verifies all blocks and states, and provides HTTP APIs and gRPC APIs for external query. Please note that Super Representatives (SRs) need to run a FullNode to generate blocks and package transactions.

### Lite FullNode

A Lite FullNode run the same code as a FullNode, but the difference is that the Lite FullNode only starts based on the state data snapshot, which only contains all account state data and historical data of the latest 65536 blocks. The state data snapshot is small, only about 3% of the FullNode data. Therefore, Lite FullNode have the advantages of occupying less disk space and faster starting up, but they do not support data query on historical blocks and transaction data by default, and provide only part of HTTP APIs and gRPC APIs compared to Fullnodes. For APIs that are not supported by Lite Fullnodes, please refer to [HTTP](https://github.com/tronprotocol/java-tron/blob/develop/framework/src/main/java/org/tron/core/services/filter/LiteFnQueryHttpFilter.java) and [gRPC](https://github.com/tronprotocol/java-tron/blob/develop/framework/src/main/java/org/tron/core/services/filter/LiteFnQueryGrpcInterceptor.java). But these APIs can be enabled by configuring `openHistoryQueryWhenLiteFN = true` in the configuration file. Since a Lite FullNode stores exactly the same data as a FullNode after startup, when this configuration item is turned on, the Lite FullNode supports data query on the block data synchronized after the node startup, but still does not support querying the historical block data.

Therefore, if developers only need to use nodes for block synchronization, and processing and broadcasting transactions, or only need to query blocks and transactions synchronized after node startup, then Lite FullNode would be a better choice.

## Why Should I Run a TRON Node?

Running a node allows you to trustlessly and privately use the TRON network while supporting the ecosystem. Your node verifies all the transactions and blocks against consensus rules by itself. This means you don’t have to rely on any other nodes in the network or fully trust them. And you can program your own custom RPC endpoints.

## Running a Node

Running your own node offers you various benefits, brings new possibilities, and helps support the TRON ecosystem. This page will guide you to run your own node and participate in validating TRON network transactions.

If you want to run your own TRON client, please refer to [How to deploy a FullNode](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode).

### Hardware Requirements

Before installing any client, please ensure your computer is well equipped. The recommended specifications are as below:

* FullNode:
  * CPU: 16 cores
  * RAM: 32G
  * Bandwidth: 100M
  * SSD: 2.5T+
* FullNode running by SR：
  * CPU: 32 cores
  * RAM: 64G
  * Bandwidth: 100M
  * SSD: 2.5T+

### Getting Client Software

You can get the client software by compiling the [source code](https://github.com/tronprotocol/java-tron) or from a [released version](https://github.com/tronprotocol/java-tron/releases).

### Starting the Client

Before starting the TRON client software, perform a last check on your environment. For example, make sure:

* There is enough disk space.
* The memory and CPU are not halted by other programs.
* The operating system is updated to the latest version.
* The system time and date are correct.

When everything is ready, please refer to [guide](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode) to run a TRON node. Current blockchain data will be available once the client is successfully synced to the latest state.

### Using the Client

Clients offer HTTP & RPC APIs that you can use to interact with the TRON network. For details, please refer to [API doc](https://developers.tron.network/reference/full-node-api-overview).

### Keeping the Node Online

Your node doesn't have to be online non-stop but you should keep it online as much as possible to keep it in sync with the network. You can shut it down for restart but keep in mind that:

* Forced shutdown can damage the database. Once the database is damaged, it needs to be resynchronized with the latest backup database.
* Your client will go out of sync with the network and will need to resynchronize when you restart it.

### Updating the Client

You need to keep your client software up-to-date. Especially before hard forks, make sure you are running the correct client version.

### Alternatives

Running your own node can be difficult and you don’t always need to run your own instance. In this case, you can use a third party API provider like the [TronGrid service](https://www.trongrid.io/). For an overview of this service, please check out [TronGrid Guide](https://developers.tron.network/docs/trongrid).
