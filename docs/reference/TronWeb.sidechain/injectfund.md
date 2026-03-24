---
title: Injectfund
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
Inject asset into the fundation of the sidechain.

* `num` &lt;Integer&gt; Num of injecting.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const num = 1000;
const feeLimit = 1000000;
const txID = await tronWeb.sidechain.injectFund(num, feeLimit);
```