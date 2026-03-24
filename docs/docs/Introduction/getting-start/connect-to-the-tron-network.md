---
title: Connecting to the TRON Network
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
When developing on the TRON platform, the first step is to establish a connection to the TRON network. The TRON network provides the infrastructure your applications need to send transactions, query on-chain data, and interact with smart contracts. Understanding how to properly connect to these network nodes is a crucial first step in your TRON development journey.

***

## TRON Network HTTP Endpoints

TRON offers several networks, and these endpoints let your code communicate with TRON. The table below outlines the main TRON networks and their full node HTTP endpoints:

| Network            | Full Node HTTP Endpoint Example                    |
| :----------------- | :------------------------------------------------- |
| **Mainnet**        | `https://api.trongrid.io`                          |
| **Shasta Testnet** | `https://api.shasta.trongrid.io`                   |
| **Nile Testnet**   | `https://nile.trongrid.io`                         |
| **Local Node**     | `http://127.0.0.1:8090` or `http://localhost:8090` |

***

## Connecting to the TRON Network

#### JavaScript Code Example

This example uses the **TronWeb** SDK. TronWeb aims to provide a unified, seamless development experience, extending TRON's unique features and offering new tools for DApps integrations in browsers, Node.js, and IoT devices. For more information, please refer to the [TronWeb documentation](https://tronweb.network/docu/docs/intro/).

```javascript
const { TronWeb } = require('tronweb');

const tronWeb = new TronWeb({
  fullHost: 'https://api.trongrid.io',
    // Shasta testnet: https://api.shasta.trongrid.io
    // Nile testnet: https://nile.trongrid.io
  headers: { 'TRON-PRO-API-KEY': 'your api key' },
  privateKey: 'your private key'
});
```

***

### Java Code Example

This example uses the **Trident** SDK. Trident is a lightweight Java SDK for interacting with the TRON blockchain, providing a simple and efficient way to integrate TRON functionality into your Java applications. For more information, please refer to the [Trident documentation](https://tronprotocol.github.io/trident/).

```java
import org.tron.trident.core.ApiWrapper;

//Shasta testnet
ApiWrapper wrapperShasta = ApiWrapper.ofShasta('YOUR_PRIVATE_KEY_HERE');
//Nile testnet
ApiWrapper wrapperNile = ApiWrapper.ofNile('YOUR_PRIVATE_KEY_HERE');
//TRON mainnet
ApiWrapper wrapperMainnet = ApiWrapper.ofMainnet('YOUR_PRIVATE_KEY_HERE');

// Customised full node URL
// ApiWrapper wrapperCustom = ApiWrapper.of('YOUR_PRIVATE_KEY_HERE', 'http://your-custom-fullnode:8090');
```

***

## Public Nodes vs. Self-Built Nodes

TRON provides several **public nodes** for developers. These nodes are maintained by the TRON official team or the community, enabling developers to quickly access the TRON network. You can find more detailed information about public nodes in [Network Introduction](https://developers.tron.network/docs/networks).

For developers requiring a higher degree of control, privacy, or specific performance, you can also build your own TRON node. A self-built node gives you complete control over data synchronization and network connections. To learn how to deploy and run your own TRON node, please refer to [Nodes and Clients](https://developers.tron.network/docs/nodes-and-clients).

***

## Related Resources

* **Deploy a Full Node or Super Representative Node**: If you plan to run your own TRON node, it's important to understand how to deploy a full node or become a Super Representative. For detailed steps, refer to [Deploy the FullNode or SuperNode](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode).
* **Mainnet Database Snapshots**: To quickly synchronize data for your self-built node, you can use Mainnet database snapshots. For more information, please check [Main-Net Database Snapshots](https://developers.tron.network/docs/main-net-database-snapshots).
* **Event Subscription**: TRON introduced an event subscription mechanism in version 3.5, allowing developers to obtain on-chain events triggered via event plugins. To learn how to set up event subscriptions, refer to [Event Subscription](https://developers.tron.network/docs/event-subscription).
