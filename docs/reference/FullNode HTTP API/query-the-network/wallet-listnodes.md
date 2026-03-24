---
title: ListNodes
excerpt: Query the list of peers connected to the current node.
api:
  file: full-node-http-api.json
  operationId: wallet-listnodes
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

nodes - Node list, each node information includes the following fields:

| Field        | Type   | Description                   |
| :----------- | :----- | :---------------------------- |
| address.host | string | IP of the node. (Format: Hex) |
| address.port | int    | Port number of the node.      |

<br />
