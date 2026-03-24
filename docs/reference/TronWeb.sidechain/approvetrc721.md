---
title: approveTrc721
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
Approve TRC721 token. Before depositTrc20 and depositTrc721, you should call the approve function.

* `id` &lt;Integer&gt; Id of TRC721.
* `contractAddress` &lt;String&gt; Main-chain TRC721 Contract Address.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const id = 100;
const feeLimit = 10000000;
const contractAddress = 'TESb314YKXtqLuuEPybYzMLPbe4uCJy1Th';
const txID = await tronWeb.sidechain.approveTrc721(id, feeLimit, contractAddress);
```