---
title: withdrawTrc10
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
Withdraw TRC10 token from side-chain to main-chain.

* `tokenId` &lt;Integer&gt; Token Id of TRC10.
* `tokenValue` &lt;Integer&gt; Amount of TRC10 token (Units in SUN) to deposit.
* `withdrawFee` &lt;Integer&gt; Withdraw Fee.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const tokenId = 100059;
const tokenValue = 10000000;
const withdrawFee = 10000;
const feeLimit = 1000000;
const txID = await tronWeb.sidechain.withdrawTrx10(tokenId, tokenValue, withdrawFee, feeLimit);
```