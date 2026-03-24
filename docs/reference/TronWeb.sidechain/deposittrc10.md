---
title: depositTrc10
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Deposit TRC10 token from mainchain to sidechain.

* `tokenId` &lt;Integer&gt; Required. Token Id of TRC10.

* `tokenValue` &lt;Integer&gt; Requires. Amount of trc10 token to deposit

* `depositFee` &lt;Integer&gt; Required. Deposit fee. Units in SUN. Default `0`.

* `feeLimit` &lt;Integer&gt; Required. Cost limit.

* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.

* `privateKey` &lt;String&gt; Optional, default the privateKey passed when creating the tronWeb instance. You can also pass a new privateKey used to sign.

* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const tokenId = 100059;
const tokenValue = 10000000;
const depositFee = 0;
const feeLimit = 100000000;
const txID = tronWeb.sidechain.depositTrc10(tokenId, tokenValue, depositFee, feeLimit);
// response
// da146374a75310b69d8d41456f7343337b88fa9d6e44758f1761cbc4f35a08b6cc84c042a9e8b62
```