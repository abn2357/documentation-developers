---
title: GetBurnTRX
excerpt: >-
  Queries the amount of TRX burned from on-chain transaction fees since [No. 54
  Committee Proposal](https://tronscan.org/#/proposal/54) took effect.
api:
  file: full-node-http-api.json
  operationId: getburntrx-1
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Before [No. 54 Committee Proposal](https://tronscan.org/#/proposal/54), on-chain transaction fees were burned via transfers to the black hole address `TLsV52sRDL79HXGGm9yzwKibb6BeruhUzy`,  Since the proposal took effect, burned TRX is logged directly in the node database rather than sent to that address. Use this API to query burn totals for the post-proposal period.

To estimate the TRX destroyed before the proposal took effect: `Balance of Black Hole Address - Initial Balance of Black Hole Address Balance`. Note: The initial Balance of the blackhole address balance can be obtained in the [node configuration file](https://github.com/tronprotocol/tron-deployment/blob/master/main_net_config.conf).

**Returns**

`burnTrxAmount`, int64 - Amount of TRX burned. (Unit: sun)
