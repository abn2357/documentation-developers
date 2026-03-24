---
title: GetCanDelegatedMaxSize
excerpt: >-
  [Stake2.0] Queries the amount of delegatable resources share of the specified
  resource type for an address, unit is sun. (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: getcandelegatedmaxsize-2
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

`max_size`, int64 - Maximum amount of delegatable resource shares. (Unit: sun)

* When querying the delegatable Energy share of an account, if the available Energy share in the account is 0, this API returns `{}`
* When querying the delegatable Bandwidth share of an account, if the Bandwidth obtained by staking in the account is not enough to pay for the Bandwidth consumed by a resource delegation transaction itself, this API also returns `{}`

> Note: 
>
> If the delegating transaction has a memo, it would consume more Bandwidth, therefore the actual delegatable share would be less than the return of this API.