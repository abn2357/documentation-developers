---
title: Event Plugin Deployment (MongoDB)
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
This document explains how to subscribe to on-chain events using the MongoDB event subscription plugin. It covers node configuration, plugin compilation, deployment, as well as the deployment and usage of the event query service.

# Suggested Configuration

* CPU/ RAM: 16Core / 32G
* SSD: 2.5T+
* System: Linux, MacOS

# Plugin Logic

* TRON event subscribe plugin is used to get event information from nodes and store it in MongoDB
* MongoDB is used to save event information
* TRON Event Query Service is used to provide the encapsulated HTTP interfaces to get event information from MongoDB.

# Deploy Tron Event Subscribe Plugin

```shell
#Deployment
git clone https://github.com/tronprotocol/event-plugin.git
cd eventplugin
./gradlew build
```

* Configure node configuration file

  You can subscribe to on-chain events by configuring the node to use a custom event plugin. In the configuration file, you need to specify parameters such as the plugin path, server address, and the event topics to subscribe to. Below is an example configuration:

```javascript
event.subscribe = {
  version = 1  //  1 means v2.0 , 0 means v1.0
  startSyncBlockNum =0 // starting Block Height
	native = {
      useNativeQueue = false // if true, use native message queue, else use event plugin.
      bindport = 5555 // bind port
      sendqueuelength = 1000 //max length of send queue for native message queue.
    }
    path = "/deploy/fullnode/event-plugin/build/plugins/plugin-mongodb-1.0.0.zip" // absolute path of plugin
    server = "127.0.0.1:27017" // target server address to receive event triggers
    dbconfig = "eventlog|tron|123456" // dbname|username|password
    topics = [
        {
          triggerName = "block" // block trigger, the value can't be modified
          enable = true
          topic = "block" // plugin topic, the value could be modified
        },
        {
          triggerName = "transaction"
          enable = true
          topic = "transaction"
        },
        {
          triggerName = "contractevent"
          enable = true
          topic = "contractevent"
        },
        {
          triggerName = "contractlog"
          enable = true
          topic = "contractlog"
        }
    ]

    filter = {
       fromblock = "" // the value could be "", "earliest" or a specified block number as the beginning of the queried range
       toblock = "" // the value could be "", "latest" or a specified block number as end of the queried range
       contractAddress = [
           "" // contract address you want to subscribe to, if it's set to "", you will receive contract logs/events with any contract address.
       ]

       contractTopic = [
           "" // contract topic you want to subscribe to, if it's set to "", you will receive contract logs/events with any contract topic.
       ]
    }
}
```

> 📘 Field parsing
>
> * version: Specifies the version of the event service framework. Set to 1 to use V2.0, set to 0 to use V1.0.  
>   If not configured, V1.0 will be used by default.
> * startSyncBlockNum: (Available in V2.0 only) Enables processing and pushing events from locally stored historical blocks to support historical data subscriptions. When startSyncBlockNum \<= 0, historical event synchronization is disabled. When startSyncBlockNum > 0, the feature is enabled, and historical events will be synchronized starting from the specified block height. Note: It is recommended to use the latest version of the event plugin when enabling this feature.
> * native.useNativeQueue: Specifies whether to use the built-in message queue (ZeroMQ) to subscribe to events. true means using the built-in message queue, and false means subscribing to events through the plugin.
> * path: The absolute path of "plugin-kafka-1.0.0.zip" or "plugin-mongodb-1.0.0.zip"
> * server: The Kafka server address or mongodb server address
> * dbconfig: This is MongoDB configuration. Assign it to `""` for Kafka plugin (please refer to the example)
> * topics: Each event type maps to one Kafka topic, we support four event types subscribing, block, transaction, contract log and contract event.
> * triggerName: The trigger type. The value can't be modified.
> * enable: The plugin can receive nothing if the value is false.
> * topic: The Kafka topic or MongoDB collection to receive events. Make sure it has been created and the Kafka process is running

# Deploy MongoDB

```shell
#1、Download and install MongoDB

cd /home/java-tron
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-4.0.4.tgz
tar zxvf mongodb-linux-x86_64-4.0.4.tgz
mv mongodb-linux-x86_64-4.0.4 mongodb

#2、Set environmentvariable

export MONGOPATH=/home/java-tron/mongodb/
export PATH=$PATH:$MONGOPATH/bin

#3、Create mongodb configuration file

mkdir -p /home/java-tron/mongodb/{log,data}
cd /home/java-tron/mongodb/log/ && touch mongodb.log && cd
vim mgdb.conf
```

Write the created data and log folder to the configuration file (absolute path)  
Configuration file example:

```text
dbpath=/home/java-tron/mongodb/data
logpath=/home/java-tron/mongodb/log/mongodb.log
port=27017
logappend=true
fork=true
bind_ip=0.0.0.0
auth=true
wiredTigerCacheSizeGB=2
```

> 📘 Notes:
>
> * `bind_ip` must be configured to 0.0.0.0, otherwise remote connection will be refused.
> * `wiredTigerCacheSizeGB`, must be configured to prevent OOM

```shell
#4、Launch MongoDB
mongod --config ./mgdb.conf &

#5、Create admin account：
mongo
use admin
db.createUser({user:"root",pwd:"admin",roles:[{role:"root",db:"admin"}]})

#6、Create eventlog and its owner account
db.auth("root", "admin")
use eventlog
db.createUser({user:"tron",pwd:"123456",roles:[{role:"dbOwner",db:"eventlog"}]})
```

# Deploy Tron Event Query Service

<Callout icon="❗️" theme="error">
  Note:

  The deployment of the Tron Event Query Service depends on a Java environment. On Linux Ubuntu systems (e.g., Ubuntu 16.04.4 LTS), ensure the machine is using <a href="https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04" target="_blank">Oracle JDK 8</a> rather than OpenJDK 8.
</Callout>

```shell
#1、Download
git clone https://github.com/tronprotocol/tron-eventquery.git cd troneventquery

#2、Install
wget https://mirrors.cnnic.cn/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz --no-check-certificate
tar zxvf apache-maven-3.5.4-bin.tar.gz
export M2_HOME=$HOME/maven/apache-maven-3.5.4
export PATH=$PATH:$M2_HOME/bin
mvn --version
mvn package
```

After the command is successfully executed, the jar package is generated under the troneventquery/target, and the configuration file is generated. The path is troneventquery/config.conf. The configured content is:

```text
mongo.host=IP
mongo.port=27017
mongo.dbname=eventlog
mongo.username=tron
mongo.password=123456
mongo.connectionsPerHost=8
mongo.threadsAllowedToBlockForConnectionMultiplier=4
```

```shell
#3、Start Tron Event Query Service
sh troneventquery/deploy.sh
sh troneventquery/insertIndex.sh
```

> 📘 Note:
>
> * The default port is 8080. If you want to change it, modify the script troneventquery/deploy.sh:  
>   nohup java -jar -Dserver.port=8081 target/troneventquery-1.0.0-SNAPSHOT.jar 2>&1 &

# Load plugin in java-tron and Verification

```shell
#1, Start Fullnode
Java -jar FullNode.jar -c config.conf --es
#Note: Start mongodb before starting the whole node.
#Fullnode installation reference: https://github.com/tronprotocol/java-tron/blob/develop/build.md

#2, Verify Plugin Loading
Tail -f logs/tron.log |grep -i eventplugin
# appears below the word is successful
#o.t.c.l.EventPluginLoader 'your plugin path/plugin-kafka-1.0.0.zip' loaded

#3, Verify whether the data is stored in mongodb
Mongo 47.90.245.68:27017
Use eventlog
Db.auth("tron", "123456")
Show collections
Db.block.find()
#A successful return of the data indicates that the data can be obtained from the node and stored in the mongod by event subscription. Otherwise,check the fullnode log to troubleshoot it.
```

# Use Event Query Service

* Main HTTP Service

```text
#Function: get transaction list
subpath: $baseUrl/transactions
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
block: start block number, default is 0
Example: http://127.0.0.1:8080/transactions?limit=1&sort=-timeStamp&start=2&block=0

#Function: get transaction by hash
subpath: $baseUrl/transactions/{hash}
parameters   
hash: transaction id
Example: http://127.0.0.1:8080/transactions/9a4f096700672d7420889cd76570ea47bfe9ef815bb2137b0d4c71b3d23309e9


#Function: get transfers list
subpath: $baseUrl/transfers	
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
from: from address, default is ""
to: to address, default is ""
token: tokenName, default is ""
Example: http://127.0.0.1:8080/transfers?token=trx&limit=1&sort=timeStamp&start=2&block=0&from=TJ7yJNWS8RmvpXcAyXBhvFDfGpV9ZYc3vt&to=TAEcoD8J7P5QjWT32r31gat8L7Sga2qUy8

#Function: get transfers by transactionId
subpath: $baseUrl/transfers/{hash}
parameters   
hash: transfer hash
Example: http://127.0.0.1:8080/transfers/70d655a17e04d6b6b7ee5d53e7f37655974f4e71b0edd6bcb311915a151a4700

#Function: get events list
subpath: $baseUrl/events
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
since: start time of event occurrence, timeStamp >= since will be shown
start: start page, default is 1
block: block number, block number >= block will be shown
Example: http://127.0.0.1:8080/events?limit=1&sort=timeStamp&since=0&block=0&start=0

#Function: get events by transactionId
subpath: $baseUrl/events/transaction/{transactionId}
parameters   
transactionId
Example: http://127.0.0.1:8080/events/transaction/cd402e64cad7e69c086649401f6427f5852239f41f51a100abfc7beaa8aa0f9c

#Function: get events by contract address
subpath: $baseUrl/events/{contractAddress}
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
since: start time of event occurrence, timeStamp >= since will be shown
block: block number, block number >= block will be shown
contractAddress: contract address
start: start page, default is 1
Example: http://127.0.0.1:8080/events/TMYcx6eoRXnePKT1jVn25ZNeMNJ6828HWk?limit=1&sort=-timeStamp&since=0&block=0&start=4

#Function: get events by contract address and event name
subpath: $baseUrl/events/contract/{contractAddress}/{eventName}
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
since: start time of event occurrence, timeStamp >= since will be shown
contract`Address`: contract address
start: start page, default is 1
eventName: event name
Example: http://127.0.0.1:8080/events/contract/TMYcx6eoRXnePKT1jVn25ZNeMNJ6828HWk/Bet?limit=1&sort=timeStamp&since=1&start=0

#Function: get events by contract address, event name and block number
subpath: $baseUrl/events/contract/{contractAddress}/{eventName}/{blockNumber}
parameters   
contractAddress: contract address
blockNumber: block number, block number >= block will be shown
eventName: event name
Example: http://127.0.0.1:8080/events/contract/TMYcx6eoRXnePKT1jVn25ZNeMNJ6828HWk/Bet/4835773

#Function: get events by timeStamp
subpath: $baseUrl/events/timestamp
parameters   
since: start time of event occurrence, timeStamp >= since will be shown
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
contract: contract address
Example: http://127.0.0.1:8080/events/timestamp?since=1544483426749&limit=1&start=1&sort=timeStamp

#Function: get confirm events list
subpath: $baseUrl/events/confirmed
parameters   
since: start time of event occurrence, timeStamp >= since will be shown
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
Example: http://127.0.0.1:8080/events/confirmed?since=1544483426749&limit=1&start=1&sort=timeStamp

#Function: get block by block hash
subpath: $baseUrl/blocks/{hash}
parameters   
hash: block hash
Example: http://127.0.0.1:8080/blocks/000000000049c11f15d4e91e988bc950fa9f194d2cb2e04cda76675dbb349009

#Function: get block list
subpath: $baseUrl/blocks
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
block: block number, block number >= block will be shown 
Example: http://127.0.0.1:8080/blocks?limit=1&sort=timeStamp&start=0&block=0

#Function: get latest block number
subpath: $baseUrl/blocks/latestSolidifiedBlockNumber
parameters   
none
Example: http://127.0.0.1:8080/blocks/latestSolidifiedBlockNumber

#Function: get contract log list
subpath: $baseUrl/contractlogs
parameters   
limit: each page size, default is 25
sort: sort Field, default is sort by timeStamp descending order
start: start page, default is 1
block: block number, block number >= block will be shown 
Example: http://127.0.0.1:8080/contractlogs

#Function: get contract log list based on transactionId
subpath: $baseUrl/contractlogs/transaction/{transactionId}
parameters   
transactionId
Example: http://127.0.0.1:8080/contractlogs/transaction/{transactionId}

#Function: post abi string and get contract log list based on transactionId(release on 3.6)
subpath: $baseUrl/contract/transaction/{transactionId}
parameters   
transactionId
body:
abi: user self upload abi
Example: http://127.0.0.1:8080/contract/transaction/{transactionId}

#Function: get contract log list based on contractAddress
subpath: $baseUrl/contractlogs/contract/{contractAddress}
parameters   
contractAddress
Example: http://127.0.0.1:8080/contractlogs/contract/{contractAddress}

#Function: post abi string and get contract log list based on contractAddress(release on 3.6)
subpath: $baseUrl/contract/contractAddress/{contractAddress}
parameters   
contractAddress
abi: user self upload abi
Example: http://127.0.0.1:8080/contract/contractAddress/{contractAddress}

#Function: get contract log list based on uniqueId
subpath: $baseUrl/contractlogs/uniqueId/{uniqueId}
parameters   
uniqueId
Example: http://127.0.0.1:8080/contractlogs/uniqueId/{uniqueId}

#Function: post abi string and get contract log list based on uniqueId(release on 3.6)
subpath: $baseUrl/contract/uniqueId/{uniqueId}
parameters   
uniqueId
abi: user self upload abi
Example: http://127.0.0.1:8080/contract/uniqueId/{uniqueId}
```
