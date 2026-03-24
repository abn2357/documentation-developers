---
title: Deploying A Node
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
Supported Operating Systems: `Linux`,`MacOS`

Supported Architectures and Corresponding JDK Versions

* x86_64 Architecture: `Oracle JDK 8`
* ARM64 Architecture: `Oracle JDK 17`

# Recommended Configurations

* CPU：16 cores
* RAM：32G
* SSD：2.5T+
* Bandwidth：100M

If you are a Super Representative (SR) to build a FullNode for block production, the recommended configuration is:

* CPU：32 cores
* RAM: 64 GB

# Deployment Guide

Regardless of the type of node, the deployment process is the same. Please refer to the following steps:

## 1. Obtain Fullnode.jar

You can obtain `FullNode.jar` through compiling source code or downloading [the released jar](https://github.com/tronprotocol/java-tron/releases) directly.

### Compile the source code

1. Obtain Java-Tron source code
   ```shell
       $ git clone https://github.com/tronprotocol/java-tron.git
       $ git checkout -t origin/master
   ```
2. Compile
   ```shell
       $ cd java-tron
       $ ./gradlew clean build -x test
   ```
   You will find the `FullNode.jar` file under the `./java-tron/build/libs/` folder if the build is successful.

## 2. Start The Node

For Mainnet FullNodes, please use the default configuration file [config.conf](https://github.com/tronprotocol/java-tron/blob/master/framework/src/main/resources/config.conf). For Nile testnet node configurations, please refer to the [Nile official website](https://nileex.io/). For private chain node configurations, follow the instructions in the [Tron Private Chain](https://developers.tron.network/docs/tron-private-chain) section.

* Start a FullNode for Mainnet：  
  A FullNode has full historical data, and is the entry point into the TRON network. It provides HTTP APIs and gRPC APIs for external queries. You can interact with the TRON network through a FullNode: transfer assets, deploy contracts, interact with contracts, and so on. The Mainnet FullNode startup command is as follows, and the configuration file of the FullNode is specified by the `-c` parameter:

  ```shell
  java -Xmx24g -XX:+UseConcMarkSweepGC -jar FullNode.jar -c config.conf
  ```

  * `-XX:+UseConcMarkSweepGC`: Specifies parallel garbage collection. This must be placed before the -jar parameter, not at the end.
  * `-Xmx`  : The maximum value of the JVM heap, which can be set to 80% of the physical memory.
* Startup a FullNode that produces blocks for Mainnet  
  Adding the `--witness` parameter to the startup command, the FullNode will run as a node which produces blocks. In addition to supporting all the features of FullNodes, the block-producing fullnode also supports block production and transaction packaging. Please make sure you have an SR account and get the votes of others. If the votes rank in the top 27, you need to start a full node that produces blocks to participate in block production.

  Fill in the private key of the SR address into the `localwitness` list in the `config.conf`. Below is an example. But if you don't want to use this way of specifying the private key in plain text, you can use the keystore + password method. Please refer to the [Others](#Others) section. Note that if you delegate the block production permission to another account, please refer to [here](https://developers.tron.network/docs/advanced-configuration-for-super-representative).

```
localwitness = [
  	650950B1...295BD812 // Private Key, hex, 64 characters total
]
```

Then run the following command to start the node:

```
java -Xmx24g -XX:+UseConcMarkSweepGC -jar FullNode.jar --witness -c config.conf
```

**Note**: For Mainnet and Nile testnet, since the amount of data to be synchronized is large after the new node is started, it will take a long time to synchronize the data. You can use [Data Snapshots](https://developers.tron.network/docs/main-net-database-snapshots) to speed up node synchronization. First, download the latest data snapshot and extract it to the `output-directory` directory of the tron project, and then start the node, so that the node will synchronize on the basis of the data snapshot.

For a running Fullnode, you can use the command `kill -15 process id` to shut it down.

# Others

## How to use `keystore + password` to specify the private key of an SR account?

1. You should not use the nohup command because interaction is required when starting the node. It is recommended to use session keeping tools such as screen, tmux, etc.
2. Comment the `localwitness` item in `config.conf` and uncomment the `localwitnesskeystore` item. Fill in the path of the Keystore file. Note that the Keystore file needs to be placed in the current directory where the startup command is executed or its subdirectory. If the current directory is `A` and the directory of the Keystore file is `A/B/localwitnesskeystore.json`, then it needs to be configured as:
   ```
   localwitnesskeystore = [
   		"B/localwitnesskeystore.json"
   ]
   ```
   **Note**: For `keystore + password` generation, you can use the register wallet command of the [wallet-cli](https://github.com/tronprotocol/wallet-cli.git).
3. Start the FullNode that produces blocks
   ```
   java -Xmx24g -XX:+UseConcMarkSweepGC -jar FullNode.jar --witness -c config.conf
   ```
4. Enter the password correctly to finish the node startup.

## How to optimize Memory Allocation with tcmalloc?

Memory allocation of java-tron can be optimized with tcmalloc. The method is as follows:

First install tcmalloc, then add the following two lines to the startup script. The path of tcmalloc is slightly different for different Linux distributions.

```
#!/bin/bash
  
export LD_PRELOAD="/usr/lib/libtcmalloc.so.4"
export TCMALLOC_RELEASE_RATE=10
  
# original start command
java -jar .....
```

Instructions for each Linux distributions are as below:

* Ubuntu 20.04 LTS / Ubuntu 18.04 LTS / Debian stable:

  ```
  sudo apt install libgoogle-perftools4
  ```

  In the startup script add the following content:

  ```
  export LD_PRELOAD="/usr/lib/x86_64-linux-gnu/libtcmalloc.so.4"
  export TCMALLOC_RELEASE_RATE=10
  ```

* Ubuntu 16.04 LTS  
  Same install command as above. In the startup script add the following content:

  ```
  export LD_PRELOAD="/usr/lib/libtcmalloc.so.4"
  export TCMALLOC_RELEASE_RATE=10
  ```

* CentOS 7  
  ```
  sudo yum install gperftools-libs
  ```
  In the startup script add the following content:
  ```
  export LD_PRELOAD="/usr/lib64/libtcmalloc.so.4"
  export TCMALLOC_RELEASE_RATE=10
  ```

## How to configure a node to be read-only mode?

Java-tron supports providing data query services without starting the network module. You can refer to the following steps to configure the node with the read-only mode:

1. Disable network module

Add the parameter `--p2p-disable true` to the node startup command as follows:

```
java -jar FullNode.jar -c config.conf --p2p-disable true 
```

Or set the following configuration item in the node configuration file:

```
node.p2p.enable = false
```

2. Disable P2P communication

Disable the node discovery service, and then empty the trusted node list.

```
node.discovery.enable = false
node.active = []
node.passive = []
```

Note: Although simply setting `node.p2p.enable = false` is enough to prevent a node from syncing blocks while still allowing data queries, it is still recommended to apply all above settings simultaneously for a complete read-only mode.

<br />

## How to configure a node that supports account historical balance queries？

Follow the steps below to configure a node for querying historical account balances:

1. Enable Account Historical Balance Query

   Modify [the node configuration file](https://github.com/tronprotocol/java-tron/blob/master/framework/src/main/resources/config.conf) and enable historical balance queries:
   ```
   storage {
     balance.history.lookup = true
   }
   ```
2. (Optional) Download a database snapshot
   * If the node starts synchronizing from the genesis block (block 0), or you download and use a [database snapshot](https://developers.tron.network/docs/main-net-database-snapshots#fullnode-data-snapshot) that contains historical balance data, the node will be able to query the account balances of all synchronized blocks, including historical blocks prior to the snapshot, thus supporting full account historical balance queries.
   * Otherwise, after the node starts, it can only query the account balances of new blocks synchronized after startup, and the balances of previously synchronized blocks will not be available.
   Please choose whether to use a database snapshot based on your needs.
3. Start the node

   Once the configuration is complete, start the node. After synchronization finishes, you can use the [wallet/getaccountbalance](https://developers.tron.network/reference/getaccountbalance) API to query the historical TRX balance of any account.
