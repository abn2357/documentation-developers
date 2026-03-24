---
title: GetCanDelegatedMaxSize
excerpt: >-
  In Stake2.0, query the amount of delegatable resources share of the specified
  resource type for an address, unit is sun.
api:
  file: full-node-http-api.json
  operationId: getcandelegatedmaxsize
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
max_size - int64 : Maximum amount of delegatable resource shares. (Unit: sun)

* When querying the delegatable energy share of an account, if the available energy share in the account is 0, this API returns \{}
* When querying the delegatable bandwidth share of an account, if the bandwidth obtained by staking in the account is not enough to pay for the bandwidth consumed by a resource delegation transaction itself, this API also returns \{}

Note: If the delegating transaction has a memo, it would consume more bandwidth, therefore the actual delegatable share would be less than the return of this API.