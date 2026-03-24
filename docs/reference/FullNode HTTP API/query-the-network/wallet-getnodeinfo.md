---
title: GetNodeInfo
excerpt: Query the current node information.
api:
  file: full-node-http-api.json
  operationId: wallet-getnodeinfo
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Returns**

| Field               | Type                 | Description                                                                                                                                                              |
| :------------------ | :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| beginSyncNum        | int64                | Starting block number for synchronization.                                                                                                                               |
| block               | string               | Latest block information, including height and ID.                                                                                                                       |
| solidityBlock       | string               | Latest solidified block information, including height and ID.                                                                                                            |
| currentConnectCount | int32                | Current number of node connections.                                                                                                                                      |
| activeConnectCount  | int32                | Number of active node connections.                                                                                                                                       |
| passiveConnectCount | int32                | Number of passive node connections.                                                                                                                                      |
| totalFlow           | int64                | Total TCP flow.                                                                                                                                                          |
| peerInfoList        | PeerInfo[]           | Peer node information. See [protobuf](https://github.com/tronprotocol/java-tron/blob/develop/protocol/src/main/protos/core/Tron.proto) for details.                      |
| configNodeInfo      | ConfigNodeInfo       | Node configuration information, please refer to [protobuf](https://github.com/tronprotocol/java-tron/blob/develop/protocol/src/main/protos/core/Tron.proto) for details. |
| machineInfo         | MachineInfo          | Information about the machine running the node.                                                                                                                          |
| cheatWitnessInfoMap | map\<string, string> | Information about Super Representatives (SRs) suspected of cheating.                                                                                                     |
