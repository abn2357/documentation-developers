---
title: approveTrc20
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
Approve TRC20 token. Before depositTrc20 and depositTrc721, you should call the approve function.

* `num` &lt;Integer&gt; Num of TRC20.
* `contractAddress` &lt;String&gt; Main-chain TRC20 Contract Address.
* `feeLimit` &lt;Integer&gt; Cost limit.
* `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.
* `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const num = 10000;
const feeLimit = 10000000;
const contractAddress = 'TESb314YKXtqLuuEPybYzMLPbe4uCJy1Th';
const txID = await tronWeb.sidechain.approveTrc20(num, feeLimit, contractAddress);
```