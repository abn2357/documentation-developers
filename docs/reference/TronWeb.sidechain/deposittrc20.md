---
title: depositTrc20
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
Deposit TRC20 token from mainchain to sidechain.

* `num` &lt;Integer&gt; Required. Amount of TRC20 to deposit.

* `depositFee` &lt;Integer&gt; Required. Deposit fee. Units in SUN. Default `0`.

* `feeLimit` &lt;Integer&gt; Required. Cost limit.

* `contractAddress` &lt;String&gt; Required. TRC20 Contract Address in mainchain.

* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.

* `privateKey` &lt;String&gt; Optional, default the privateKey passed when creating the tronWeb instance. You can also pass a new privateKey used to sign.

* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const num = 100;
const depositFee = 0;
const feeLimit = 100000000;
const contractAddress = 'TQq3EYEiaYr95r6ePRQwycukCEAE4qWkE7';
const txID = tronWeb.sidechain.depositTrc20(num, depositFee, feeLimit, contractAddress);
```