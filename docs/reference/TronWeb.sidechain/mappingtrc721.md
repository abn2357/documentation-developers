---
title: mappingTrc721
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
Mapping TRC721 token to side-chain.

* `trxHash` &lt;String&gt; The hash value of the transaction for the main-chain deployment TRC721 contract.
* `mappingFee` &lt;Integer&gt; Mapping Fee.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const trxHash = '548442d9080605a60adf1d30cc126a2b9c6308cbe9ec224f8c67a6c2590fa299';
const mappingFee = 10000;
const feeLimit = 10000000;
const txID = await tronWeb.sidechain.mappingTrc721(trxHash, mappingFee, feeLimit);
```