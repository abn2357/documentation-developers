---
title: GetAccountBalance
excerpt: >-
  Query the historical balance of an account at a specific block. (Note: This
  API requires the node to enable the historical balance query feature. When
  using official nodes, the interface is currently available only on the
  following nodes: 13.228.119.63, 18.139.193.235, 18.141.79.38, and
  18.139.248.26.)
api:
  file: full-node-http-api.json
  operationId: getaccountbalance
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

| Field                   | Type   | Description                        |
| :---------------------- | :----- | :--------------------------------- |
| balance                 | int64  | Account's TRX balance. (Unit: sun) |
| block_identifier.hash   | string | Block hash.                        |
| block_identifier.number | int64  | Block number.                      |