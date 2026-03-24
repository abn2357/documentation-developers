---
title: Networks
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
Since TRON is a protocol, there can be multiple independent "networks" conforming to this protocol without interacting with each other.

These networks are different TRON environments you can access for development, testing, or production use cases. Your TRON account will work across the different networks but your account balance and transaction history won't carry over from the main TRON network. For testing purposes, it's useful to know which networks are available and how to get testnet TRX so you can play around with it.

## Public Networks

Public networks are accessible to anyone in the world with an internet connection. Anyone can read or create transactions on a public blockchain and validate the transactions being executed.

### Mainnet

Mainnet is the primary public TRON production blockchain, where actual-value transactions occur on the distributed ledger. When people and exchanges discuss TRX prices, they're talking about Mainnet TRX.

* Browser：[https://tronscan.org](https://tronscan.org)
* TronGrid API：[https://api.trongrid.io](https://api.trongrid.io)
* TronGrid JSON-RPC API: [https://api.trongrid.io/jsonrpc](https://api.trongrid.io/jsonrpc)
* TronGrid gRPC Fullnode API: grpc.trongrid.io:50051
* TronGrid gRPC Solidity API: grpc.trongrid.io:50052
* Database backup：[Data backup](https://developers.tron.network/docs/main-net-database-snapshots)

#### Mainnet Infrastructure Providers

In addition to TronGrid's RPC services, you can also use other infrastructure providers' RPC services:

* [Ankr](https://www.ankr.com/rpc/tron/)
* [GetBlock](https://getblock.io/nodes/trx/)
* [QuickNode](https://www.quicknode.com/chains/tron?utm_source=tron-docs)
* [NOWNodes](https://nownodes.io/nodes/tron-trx)
* [Chainstack](https://chainstack.com/build-better-with-tron/)
* [Tatum](https://tatum.io/chains/tron)
* [TronQL](https://tronql.com/)
* [Alchemy](https://www.alchemy.com/docs/reference/tron-api-quickstart) 

#### Public Nodes

Public nodes are stable online mainnet nodes, which can be used as seed nodes in the TRON network for node discovery:

* 3.225.171.164
* 18.133.82.227
* 15.207.144.3
* 15.222.19.181
* 18.209.42.127
* 3.218.137.187
* 34.237.210.82
* 13.228.119.63
* 18.139.193.235
* 18.141.79.38
* 18.139.248.26
* 52.8.46.215
* 3.12.212.122
* 52.24.128.7
* 3.39.38.55
* 3.79.71.167
* 108.128.110.16
* 35.180.81.133
* 13.210.151.5

Ports of public nodes：

* HTTP port: 8090
* HTTP Solidity port: 8091
* gRPC port: 50051
* gRPC Solidity port: 50061
* P2P network port: 18888

### Testnets

In addition to Mainnet, there are also public testnets. These are networks used by protocol developers or smart contract developers to test both protocol upgrades as well as potential smart contracts before deployment to Mainnet.

It’s generally important to test any contract code you write on a testnet before deploying to Mainnet. TRX on testnets has no real value; therefore, there are no markets for testnet TRX. Anyone can get testnet TRX from faucets.

#### Shasta Testnet

Parameters of the Shasta testnet are consistent with the Mainnet. Currently, the Shasta test network does not support adding new nodes run by anyone.

* Website: [https://www.trongrid.io/shasta](https://www.trongrid.io/shasta)
* Faucet: [https://shasta.tronex.io](https://shasta.tronex.io)
* Browser: [https://shasta.tronscan.org](https://shasta.tronscan.org)
* HTTP API: [https://api.shasta.trongrid.io](https://api.shasta.trongrid.io)
* gRPC Fullnode API: grpc.shasta.trongrid.io:50051
* gRPC Solidity API: grpc.shasta.trongrid.io:50052
* JSON-RPC API: [https://api.shasta.trongrid.io/jsonrpc](https://api.shasta.trongrid.io/jsonrpc)

#### Nile Testnet

The Nile testnet is used to test new features of TRON, and the code version is generally ahead of the Mainnet.

* Website：[http://nileex.io](http://nileex.io)
* Faucet: [http://nileex.io/join/getJoinPage](http://nileex.io/join/getJoinPage)
* Browser: [https://nile.tronscan.org](https://nile.tronscan.org)
* Status: [http://nileex.io/status/getStatusPage](http://nileex.io/status/getStatusPage)
* HTTP API: [https://api.nileex.io/](https://api.nileex.io/)
* TronGrid HTTP API: [https://nile.trongrid.io/](https://nile.trongrid.io/)
* gRPC API: grpc.nile.trongrid.io:50051
* gRPC Fullnode API: grpc.nile.trongrid.io:50051
* gRPC Solidity API: grpc.nile.trongrid.io:50061
* Database backup：[http://47.90.243.177](http://47.90.243.177)

##### Nile Testnet Infrastructure Providers

In addition to TronGrid's RPC services, you can also use other infrastructure providers' RPC services:

* [Chainstack](https://chainstack.com/build-better-with-tron/)

## Private Networks

For a network, if its nodes are not connected to a public network (mainnet or testnet), then it is a private network. For more information about private networks, please refer to the [How to build a private chain](https://developers.tron.network/docs/tron-private-chain).

Before deploying your TRON DApp to Mainnet, you can develop and test it on a private network. Similar to deploying a web development environment locally, you can also deploy a private chain locally to test the DAPP. Compared with the public test network , the local private network will provide a faster speed for interaction.

For more information about related DAPP development tools, please refer to [DAPP development tools](https://developers.tron.network/docs/dapp-development-tools).
