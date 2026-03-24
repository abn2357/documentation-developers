---
title: createAccount
excerpt: Create a unsigned transaction to active an account
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage**

```javascript
tronWeb.transactionBuilder.createAccount(address, options);
```

**Parameter**\
address: String - The account address to be activated.\
options: Json object - optional, for example, permission, \{permissionId: 'xx'}.

**Return**\
Object - Transaction created to activate an account.

**Example**

```javascript
const transaction = await tronWeb.transactionBuilder.createAccount('TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g');

const signedTransaction  = await tronWeb.trx.sign(transaction);

const result = await tronWeb.trx.sendRawTransaction(signedTransaction);
```
