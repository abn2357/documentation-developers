---
title: retryMapping
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
Retry mapping.

* `nonce` &lt;Integer&gt; Nonce value of asset mapping.
* `retryMappingFee` &lt;Integer&gt; Fee of retry mapping operation.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default &#123;&#125;.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

```javascript
const nonce = 1000;
const retryMappingFee = 1000000;
const feeLimit = 1000000;
const txID = await tronWeb.sidechain.retryMapping(nonce, retryDepositFee, feeLimit);
```