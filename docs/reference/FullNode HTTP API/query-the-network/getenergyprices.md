---
title: GetEnergyPrices
excerpt: Query historical energy unit price.
api:
  file: full-node-http-api.json
  operationId: getenergyprices
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

prices - string: All historical energy price information. Each price change is separated by a comma, in the format `timestamp:price`, where the timestamp is in milliseconds and the price is in sun.
