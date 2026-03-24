---
title: Built-in Message Queue Subscription (ZeroMQ)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
TRON provides event subscription service. Developers can not only obtain on-chain events through event plugins, but also through [Java-tron’s built-in ZeroMQ message queue](https://github.com/tronprotocol/tips/blob/master/tip-28.md). The difference is that an event plugin needs to be additionally deployed for event storage: developers can choose appropriate storage tools according to their needs, such as MongoDB, Kafka, etc., and the plugin will help complete the storage of subscribed events. java-tron's built-in ZeroMQ does not require additional deployment operations. Event subscribers can directly connect to the publisher's ip and port, set subscription topics, and receive subscribed events. However, this method does not support event storage. Therefore, when developers want to subscribe to events directly from nodes for a short period of time, then using the built-in message queue will be a more appropriate choice.

This article will introduce how to subscribe to events through Java-tron's built-in message queue in detail.

## Configure node

To use the built-in ZeroMQ of the node for event subscription, you need to set the configuration item `useNativeQueue` to `true` in the node configuration file.

```
event.subscribe = {
  native = {
    useNativeQueue = true // if true, use native message queue, else use event plugin.
    bindport = 5555 // bind port
    sendqueuelength = 1000 //max length of send queue
  }

  ......
 
  topics = [
    {
      triggerName = "block" // block trigger, the value can't be modified
      enable = true
      topic = "block" // plugin topic, the value could be modified
    },
    ......
  ]
}
```

* `native.useNativeQueue`: `true` is to use the built-in message queue, `false` is to use the event plugin
* `native.bindport`: ZeroMQ publisher binding port. In this example, it is `5555`, so the publisher address that the subscriber should connect to is `"tcp://127.0.0.1:5555"`
* `native.sendqueuelength`: The length of the send queue, that is, when the subscriber receives messages slowly, the maximum number of published messages from the publisher that the TCP buffer can hold. If it exceeded, later messages will be discarded.
* `topics`: Subscribed [event type](https://developers.tron.network/docs/event-subscription#event-type), including block type, transaction type, etc.

## Start node

The event subscription service is disabled by default and needs to be enabled by adding the command line parameter `--es`. The start command of the node that enables the event subscription service is as follows:

```
$ java -jar FullNode.jar --es
```

## Prepare event subscription script

This article takes Nodejs as an example to illustrate how to subscribe to events.

First, install the zeromq library:

```
$ npm install zeromq@5
```

Then, write the subscriber code:

```
// subscriber.js
var zmq = require("zeromq"),
var sock = zmq.socket("sub");

sock.connect("tcp://127.0.0.1:5555");
sock.subscribe("block");
console.log("Subscriber connected to port 5555");

sock.on("message", function(topic, message) {
  console.log(
    "received a message related to:",
    Buffer.from(topic).toString(),
    ", containing message:",
    Buffer.from(message).toString()
  );
});
```

This example connects the subscriber to the node event publisher and subscribes to `block` events.

## Start subscriber

Start command of Nodejs is as below:

```
$ node subscriber.js

> Subscriber connected to port 5555
```

When the node has a new block, the subscriber will receive the block event, and the output information is as follows:

```
received a message related to: blockTrigger, containing message: {"timeStamp":1678343709000,"triggerName":"blockTrigger","blockNumber":1361,"blockHash":"00000000000005519b3995cd638753a862c812d1bda11de14bbfaa5ad3383280","transactionSize":0,"latestSolidifiedBlockNumber":1361,"transactionList":[]}
received a message related to: blockTrigger, containing message: {"timeStamp":1678343712000,"triggerName":"blockTrigger","blockNumber":1362,"blockHash":"0000000000000552d53d1bdd9929e4533a983f14df8931ee9b3bf6d6c74a47b0","transactionSize":0,"latestSolidifiedBlockNumber":1362,"transactionList":[]}
```
