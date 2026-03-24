---
title: retryWithdraw
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
Retry Withdraw.

* `nonce` &lt;Integer&gt; Nonce value of asset withdraw.
* `retryWithdrawFee` &lt;Integer&gt; Fee of retry withdraw operation.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const nonce = 1000;
const retryWithdrawFee = 1000000;
const feeLimit = 1000000;
const txID = await tronWeb.sidechain.injectFund(nonce, retryDepositFee, feeLimit);
```