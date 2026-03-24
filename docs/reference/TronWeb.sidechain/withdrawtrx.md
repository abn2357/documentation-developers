---
title: withdrawTrx
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
Withdraw trx from side-chain to main-chain.

* `callValue` &lt;Integer&gt; Amount of TRX (Units in SUN) to deposit.
* `withdrawFee` &lt;Integer&gt; Withdraw fee.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const callValue = 1000000000;
const withdrawFee = 10000;
const feeLimit = 10000000;
const txID = await tronWeb.sidechain.withdrawTrx(callValue, withdrawFee, feeLimit);
```