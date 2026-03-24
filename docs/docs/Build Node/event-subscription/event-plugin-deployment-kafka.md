---
title: Event Plugin Deployment (Kafka)
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
This document explains how to subscribe to on-chain events using the Kafka event subscription plugin. It covers plugin compilation, Kafka deployment, and practical examples of event subscription.

# Recommended Configuration

* CPU/ RAM: 16Core / 32G
* SSD: 2.5T+
* System: Linux / MacOS

# 1. Compile Kafka Event Plugin

```java
git clone https://github.com/tronprotocol/event-plugin.git
cd event-plugin
./gradlew build
```

You can find `plugin-kafka-1.0.0.zip` in the `event-plugin/build/plugins/` directory after compilation.

# 2. Deploy Kafka

## Install Kafka

_Linux:_

```java
cd /usr/local
wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
$ tar -xzf kafka_2.13-2.8.0.tgz
```

## Start Kafka

_Linux:_

```java
cd /usr/local/kafka_2.13-2.8.0
// start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties &
// start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties &
```

# 3. Event Subscription

## 3.1 Event Subscripion Configuration

Add items of `event.plugin` to the configuration file of your FullNode to support event subscription with Kafka.

### 3.1.1 Plugin Configurations

```shell
event.subscribe = {
version = 1  //  1 means v2.0 , 0 means v1.0
startSyncBlockNum =0 // starting Block Height
  native = {
    useNativeQueue = false// if true, use native message queue, else use event plugin.
    bindport = 5555 // bind port
    sendqueuelength = 1000 //max length of send queue
  }

  path = "" // absolute path of plugin
  server = "" // target server address to receive event triggers
  dbconfig = "" // dbname|username|password
  contractParse = true,
  …………
  …………

}
```

* `version`: Specifies the version of the event service framework. Set the value to `1 ` to use V2.0, or set it to `0` to use V1.0. If not configured, V1.0 will be used by default.
* `startSyncBlockNum` (Available in V2.0 only): Enables processing and pushing events from locally stored historical blocks to support historical data subscriptions. 
  * When `startSyncBlockNum \<= 0`, historical event synchronization is disabled. 
  * When `startSyncBlockNum > 0`, the feature is enabled, and historical events will be synchronized starting from the specified block height. 
  > Note: It is recommended to use the latest version of the event plugin when enabling this feature.
* `native`: contains configurations for TRON's built-in message queue. Please always keep 'useNativeQueue' as 'false' to subscribe events with Kafka.
* `path`: the local path for `plugin-kafka-1.0.0.zip`. Please ensure the path is correct.
* `server`: the Kafka's server address in the format of `IP:port`, with default port set to `9092`. Please use the correct port number and ensure that the Kafka service is accessible.
* `dbconfig`: specifically usd for MongoDB and can be ignored here.

### 3.1.2 Event Subscription Configuration Items

TRON Event Subscription supports seven types of events. They are: `block`, `transaction`, `contractevent`, `contractlog`, `solidity`, `solidityevent` and `soliditylog`.

Subscription of too many topics will cause performance degradation. Please subscribe 1-2 types of events according to your needs.

Take the block event subscription as an example:

```shell
topics = [
    {
      triggerName = "block" // block trigger, the value can't be modified
      enable = true
      topic = "block" // plugin topic, the value could be modified
    }
]
```

* `triggerName`: Built-in field. This can't be changed.
* `enable`: Set the value as `true` to subscribe the event of `block`
* `topic`: This field corresponds to the pre-created topic in Kafka. The topic name can either be default or customized.

The item `filter` works as the filter for subscribed events. For accurate subscription, according to your needs, you can customize the block range(`fromblock` ~ `toblock`), contract address(`contractAddress`) and specific contract topic(`contractTopic`) .

```shell
filter = {
    fromblock = "" // the value could be "", "earliest" or a specified block number as the beginning of the queried range
    toblock = "" // the value could be "", "latest" or a specified block number as end of the queried range
    contractAddress = [
      "" // contract address you want to subscribe, if it's set to "", you will receive contract logs/events with any contract address.
    ]

    contractTopic = [
      "" // contract topic you want to subscribe, if it's set to "", you will receive contract logs/events with any contract topic.
    ]
}
```

## 3.2 Create Subscription Topics in Kafka

The name of the Kafka subscription topic should be consistent with the configuration item in 3.1.2. E.g., to subscribe event `block`, please set `topic` as `block` in `block trigger` and create topic `block` in Kafka to receive `block` events.

_Linux:_

```java
bin/kafka-topics.sh --create --topic block --bootstrap-server localhost:9092
```

## 3.3 Start an Event Subscription Node

After completing the above configuration, please start your FullNode with `--es` to turn on the event subscription.

```java
java -jar FullNode.jar -c config.conf --es
```

Check `tron.log` to see whether the Kafka Event Plugin has been successfully loaded.

```java
grep -i eventplugin logs/tron.log
```

The loading is successful when this reminder displayed:

```shell
[o.t.c.l.EventPluginLoader] 'your plugin path/plugin-kafka-1.0.0.zip' loaded
```

## 3.4 Event Subscription Queries

Execute the `kafka-console-consumer.sh` script to get messages of topic `block` in Kafka.

_Linux:_

```java
bin/kafka-console-consumer.sh --topic block --from-beginning --bootstrap-server localhost:9092
```

You have successfully subscribed to the events when the following appears:

```shell
{
	"timeStamp": 1539973125000,
	"triggerName": "blockTrigger",
	"blockNumber": 3341315,
	"blockHash": "000000000032fc03440362c3d42eb05e79e8a1aef77fe31c7879d23a750f2a31",
	"transactionSize": 16,
	"latestSolidifiedBlockNumber": 3341297,
	"transactionList": ["8757f846e541b51b5692a2370327f4b8031125f4557f8ad4b1037d4452616d39", "f6adab7814b34e5e756170f93a31a0c3393c5d99eff11e30271916375adc7467", ..., "89bcbcd063a48ef4a5678a033acf5edbb6b17419a3c91eb0479a3c8598774b43"]
}
…………
```
