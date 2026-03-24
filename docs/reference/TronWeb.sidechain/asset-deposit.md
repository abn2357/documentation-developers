---
title: depositTrx
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
## depositTrx

Deposit TRX asset to the sidechain.

\- `callValue` &lt;Integer&gt; Required. Amount of TRX (Units in SUN) to deposit.

\- `depositFee` &lt;Integer&gt; Required. Deposit fee. Units in SUN. Default `0`.

\- `feeLimit` &lt;Integer&gt; Required. Cost limit.

\- `options` &lt;Object&gt; Optional, permission\_id for multi-signature use. Default `{}`.

\- `privateKey` &lt;String&gt; Optional, default the privateKey passed when creating the tronWeb instance. You can also pass a new privateKey used to sign.

\- `callback` &lt;Function&gt;

Returns &lt;Promise&gt; If no callback was passed it returns a Promise instance. The response data is the TXID.

Example:

```javascript
const callValue = 10000000;
const depositFee = 0;
const feeLimit = 100000000;
const txID = await tronWeb.sidechain.depositTrx(callValue, depositFee, feeLimit);
// response
// da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0
```