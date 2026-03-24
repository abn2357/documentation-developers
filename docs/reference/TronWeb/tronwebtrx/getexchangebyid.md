---
title: getExchangeByID
excerpt: Query Exchange by id
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
tronWeb.trx.getExchangeByID(exchange id);
```

**Parameter**\
Number

**Return**\
Object

**Example**

```json
> tronWeb.trx.getExchangeByID(1).then(result=>console.log(result))
Promise { <pending> }
> {
  exchange_id: 1,
  creator_address: '410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70',
  create_time: 1575754887000,
  first_token_id: '31303030303033',
  first_token_balance: 999902,
  second_token_id: '5f',
  second_token_balance: 200020000000
}
```
