---
title: GetBurnTRX
excerpt: >-
  Query the amount of TRX burned from on-chain transaction fees since [No. 54
  Committee Proposal ](https://tronscan.org/#/proposal/54) took effect.
api:
  file: full-node-http-api.json
  operationId: getburntrx
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Before the [No. 54 Committee Proposal](https://tronscan.org/#/proposal/54) takes effect, TRX from on-chain transaction fees was burned by transferring it to the black hole address `TLsV52sRDL79HXGGm9yzwKibb6BeruhUzy`. After the proposal took effect, the black hole address is no longer used, and burned TRX is directly recorded in the node database. Users can query the amount of TRX burned due to transaction fees since the proposal became effective by this API. 

The approximate amount of TRX that was destroyed before the proposal takes effect can be obtained through `Balance of Black Hole Address - Initial Value of Black Hole Address Balance`. Note: The initial value of the blackhole address balance can be obtained in the [node configuration file](https://github.com/tronprotocol/tron-deployment/blob/master/main_net_config.conf).

**Returns**

burnTrxAmount - int64 : Amount of TRX burned, in sun.
