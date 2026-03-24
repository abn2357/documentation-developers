---
title: Event Subscription
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
TRON offers multiple ways to help developers access on-chain event information. Developers can choose the appropriate solution based on their specific requirements:

1. [TronGrid](https://developers.tron.network/reference/get-events-by-transaction-id)  
   TronGrid encapsulates the event plugin interface and provides an open, easy-to-use HTTPS query service.

2. [TronWeb](https://tronweb.network/docu/docs/API%20List/event/)  
   The official JavaScript development library provided by TRON includes built-in methods for event querying, making it convenient to retrieve events in front-end or Node.js environments. Note: Only supported on Mainnet and testnets; Event queries on private chain networks are not supported.

3. [Built-in Message Queue Subscription](https://developers.tron.network/docs/use-java-trons-built-in-message-queue-for-event-subscription)  
   Subscribe to events using Java-Tron's built-in message queue (ZeroMQ) without requiring additional plugin deployment.

4. Local Event Plugin Subscription  
   Deploy event plugins locally to subscribe to real-time or historical on-chain events.

   * Supported plugin types: Kafka, MongoDB
   * Subscribable data types: Blocks, transactions, contracts, contract logs, etc.
   * Flexible filter configurations for precise event subscriptions
   * Can be integrated with the tron-eventquery service for online event querying

This document primarily introduces how to subscribe to events by deploying local nodes and event plugins.

# Event Service Framework

TRON provides a comprehensive event service mechanism that enables developers to receive and process on-chain events in real time through custom event plugins.

The event service fetches event information from the blockchain, wraps it, and writes it into an event buffer queue for asynchronous consumption by plugin modules. Upon receiving event data, plugins can process and store the data into databases, message queues, or other target systems according to specific business needs, enabling further use by upper-layer applications.

Currently, Java-Tron offers two versions of the event service framework: V1.0 and V2.0.  
Compared with V1.0, the core improvement in V2.0 is the support for historical event backtracking and pushing, which meets users’ needs to subscribe to historical block event data. V1.0 only supports real-time event pushing, where events are pushed to subscribers immediately when a new block is processed, and cannot retrieve events from historical blocks.

For detailed differences between the two versions and recommendations on version selection, please refer to the [Event Service Framework V2.0 Introduction](https://medium.com/tronnetwork/event-service-framework-v2-0-0622f2f07249).

If you need to migrate your existing system from V1.0 to V2.0, please refer to the [How to Migrate to the New Event Service](https://developers.tron.network/docs/event-subscription#how-to-migrate-to-the-new-event-service) section .

## Plugins

The purpose of event plugins is to implement the storage of on-chain events. Developers can customize plugins based on their actual needs, such as writing events into message queues (e.g., Kafka), databases (e.g., MongoDB), or local files.

Currently, TRON officially provides two implementations of event subscription plugins: the Kafka plugin and the MongoDB plugin. Developers can choose the appropriate plugin based on their business requirements to implement event subscription.

* For the detailed implementation of the plugins, please refer to [the event-plugin source code](https://github.com/tronprotocol/event-plugin).
* For instructions on using the plugins, please refer to [Event Plugin Deployment (MongoDB)](https://developers.tron.network/docs/event-plugin-deployment-mongodb) and [Event Plugin Deployment (Kafka)](https://developers.tron.network/docs/event-plugin-deployment-kafka).

## Event Types

TRON supports subscribing to multiple types of events. Developers can flexibly subscribe to desired event types by modifying configuration files. Currently, the following four event types are supported:

1. Transaction Event  
   The parameters passed to Subscriber:

```
blockHash: block hash
blockNumber: block number
energyUsage: energy usage
energyFee: energy fee
originEnergyUsage: origin energy usage  
energyUsageTotal: total energy usage total
```

2.Block Event  
The parameters passed to Subscriber:

```
blockHash: block hash
blockNumber: block number
transactionSize: the number of transactions in a block
latestSolidifiedBlockNumber: the latest solidified block number
transactionList: the transactions hash list
```

3.Contract Event  
The parameters passed to Subscriber:

```
transactionId: transaction id
contractAddress: contract address
callerAddress: contract caller address
blockNumber: the number of the block contract related events recorded
blockTimestamp: the block time stamp
eventSignature: event signature
topicMap: the map of topic in solidity language
data: the data information in solidity language
removed: 'true' means the log is removed
```

4.Contract Log Event  
The parameters passed to Subscriber:

```
transactionId: transaction hash contractAddress: contract address
callerAddress: contract caller address
blockNumber: the number of the block contract related events recorded
blockTimestamp: the block time stamp
contractTopics: the list of topic in solidity language
data: the data information in solidity language
removed: 'true' means the log is removed
```

Contract Event and Contract Log Even support event filter function which includes:

```
fromBlock: the start block number
toBlock: the end block number
contractAddress: contract adsresses list
contractTopics: contract topics list
```

More detailed information can be found in the [Event Subscription TIP](https://github.com/tronprotocol/TIPs/issues/12).

# How to Migrate to the New Event Service

## Key Considerations for Migration Decisions

1. Dependence on Internal Transactions  
   V2.0 currently does not support subscription to internal transaction logs. The `internalTransactionList` field in the `TransactionLogTrigger` event will be empty. If your business depends on this field, it is recommended to postpone migration and continue using  V1.0.

2. Plugin Version Compatibility  
   It is recommended to upgrade to the V2.0 version to improve consumption rate and stability. During historical event synchronization, the volume of event data can be large, and older versions of plugins may cause memory issues.

## &#x20;Migration Steps

### 1. Generating the New Event Plugin

Clone the [event-plugin project](https://github.com/tronprotocol/event-plugin) from the GitHub repository and switch to the master branch. Then, execute the build command to generate the .zip file for the new plugin. Or you can download [the latest release version](https://github.com/tronprotocol/event-plugin/releases) directly.

```
git clone git@github.com:tronprotocol/event-plugin.git
cd event-plugin
git checkout feature/new_event_service
./gradlew build
```

### 2. Enabling the V2.0 Framework via Configuration

In the FullNode configuration file, add the following configuration to enable the V2.0 framework:

```
event.subscribe.version = 1
```

### 3. Configuring Event Subscription

The V2.0 framework’s subscription configuration method remains consistent with V1.0; no additional modifications are required. Please refer to the documentation [Event Plugin Deployment (MongoDB)](https://developers.tron.network/docs/event-plugin-deployment-mongodb) and [Event Plugin Deployment (Kafka)](https://developers.tron.network/docs/event-plugin-deployment-kafka) for detailed configuration instructions.

### 4. (Optional) Synchronizing Historical Block Events

The V2.0 framework supports historical event synchronization starting from a specified block height. You can set the starting synchronization height using the following configuration:

```
event.subscribe.startSyncBlockNum = <block_height>
```

* `startSyncBlockNum <= 0` indicates that the historical event synchronization feature is turned off.
* `startSyncBlockNum > 0` indicates that this feature is turned on, and historical events will be synchronized starting from the specified block height.

> **Caution**:
>
> Always ensure that the `startSyncBlockNum` parameter is configured correctly before restarting the node. A correctly configured node will synchronize historical events from the specified block height upon startup. Incorrect configuration can lead to duplicate or missed event pushes, thus affecting the correctness of the business logic.

### 5. Starting the Node

Upon completing the aforementioned configurations, start the FullNode and the corresponding event plugin to finalize the migration to the V2.0 framework. The node startup command is as follows:

```
java -jar FullNode.jar -c config.conf --es
```
