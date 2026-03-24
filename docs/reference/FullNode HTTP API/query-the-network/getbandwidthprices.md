---
title: GetBandwidthPrices
excerpt: Query historical bandwidth unit price.
api:
  file: full-node-http-api.json
  operationId: getbandwidthprices
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

prices - string: All historical bandwidth price information. Each price change is separated by a comma, in the format `timestamp:price`, where the timestamp is in milliseconds and the price is in sun.
