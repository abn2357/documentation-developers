---
title: ListWitnesses
excerpt: List all Super Representatives
api:
  file: full-node-http-api.json
  operationId: listwitnesses
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

| Field          | Type   | Description                                              |
| :------------- | :----- | :------------------------------------------------------- |
| address        | string | Super Representative (SR) address.                       |
| voteCount      | int64  | Total number of votes received.                          |
| url            | string | URL of the Super Representative's (SR) official website. |
| totalProduced  | int64  | Total number of blocks produced by the SR.               |
| totalMissed    | int64  | Total number of blocks missed by the SR.                 |
| latestBlockNum | int64  | Latest block number (height).                            |
| latestSlotNum  | int64  | Latest slot number.                                      |
| isJobs         | bool   | Whether the SR is eligible to produce blocks.            |
