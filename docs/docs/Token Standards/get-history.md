---
title: Get Transaction history
excerpt: Trc20 Transaction information by account address
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
# TRC20 Transaction History

**Get historical transaction records of a certain address for a certain TRC20**

```javascript
curl --request GET \
  --url 'https://api.trongrid.io/v1/accounts/TJmmqjb1DK9TTZbQXzRQ2AuA94z4gKAPFh/transactions/trc20?limit=100&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'

参数说明：
version: latest version: v1
address: owner address in base58 or hex。
only_confirmed:  true | false. If false, it returns both confirmed and unconfirmed transactions. If no param is specified, it returns both confirmed and unconfirmed transactions. Cannot be used at the same time with only_unconfirmed param.
only_unconfirmed: true|false, true | false. If false, it returns both confirmed and unconfirmed transactions. If no param is specified, it returns both confirmed and unconfirmed transactions. Cannot be used at the same time with only_confirmed param.
limit:number of transactions per page, default 20, max 200
fingerprint：fingerprint of the last transaction returned by the previous page; when using it, the other parameters and filters should remain the same
contract_address：contract address in base58 or hex

// Example
// Get the transaction about TRC20 USDT on the address TJmmqjb1DK9TTZbQXzRQ2AuA94z4gKAPFh
curl --request GET \
  --url ' https://api.trongrid.io/v1/accounts/TJmmqjb1DK9TTZbQXzRQ2AuA94z4gKAPFh/transactions/trc20?limit=20&contract_address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'
```
