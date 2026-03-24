---
title: withdrawTrc20
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
Withdraw TRC20 token from side-chain to main-chain.

* `num` &lt;Integer&gt; Num of TRC20.
* `withdrawFee` &lt;Integer&gt; Withdraw Fee.
* `contractAddress` &lt;Integer&gt; Side-chain TRC20 Contract Address after mapping.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const num = 10000;
const withdrawFee = 10000;
const feeLimit = 1000000;
const contractAddress = 'TWzXQmDoASGodMss7uPD6vUgLHnkQFX7ok';
const txID = await tronWeb.sidechain.withdrawTrc20(num, withdrawFee, feeLimit, contractAddress);
```