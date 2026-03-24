---
title: GetAvailableUnfreezeCount
excerpt: >-
  Returns remaining times of executing unstake operation in Stake2.0. (Confirmed
  state)
api:
  file: full-node-http-api.json
  operationId: getavailableunfreezecount-2
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Stake 2.0 supports unstaking in batches, but only allows a maximum of 32 unstake operations at the same time. That is to say, when a user initiates the first unstake operation, before the TRX of the first unstaking arrives and is ready to be withdrawn to the account, only another 31 unstake operations can be initiated. This is designed to prevent malicious attacks.

**Returns**  
`count`, int64 - Remaining times of available unstaking.