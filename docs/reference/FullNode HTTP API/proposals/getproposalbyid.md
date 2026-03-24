---
title: GetProposalById
excerpt: Queries proposal based on ID and returns proposal details
api:
  file: full-node-http-api.json
  operationId: getproposalbyid
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

| Field            | Type               | Description                                                                          |
| :--------------- | :----------------- | :----------------------------------------------------------------------------------- |
| proposal_id      | int64              | Unique ID for the chain proposal.                                                    |
| proposer_address | string             | Address of the proposal's creator.                                                   |
| parameters       | map\<int64, int64> | Values of chain parameters as specified in the proposal, keyed by parameter ID.      |
| parameters.key   | string             | Parameter ID.                                                                        |
| parameters.value | int64              | Parameter value.                                                                     |
| expiration_time  | int64              | Expiration time of the proposal. (Unit: millisecond)                                 |
| create_time      | int64              | The timestamp for when the account was created. (Unit: millisecond)                  |
| approvals        | string array       | List of approver addresses.                                                          |
| state            | enum               | State of the proposal. (Enum: `PENDING`, `DISAPPROVED`, `APPROVED`, `CANCELED`)state |