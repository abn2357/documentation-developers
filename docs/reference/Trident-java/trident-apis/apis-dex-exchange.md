---
title: DEX Exchange
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# listExchanges

List all exchange pairs.

### Usage

```
listExchanges()
```

### Parameter

None.

### Return

Object -ExchangeList object.

### Example

```
wrapper.listExchanges();
```

Execution result:

```
exchanges {
    exchange_id: 1
    creator_address: "AW\304\362\371&\260A\267\247\006\202\377\336\367$\236\031\220\206Y"
    create_time: 1586852889000
    first_token_id: "1000032"
    first_token_balance: 6682
    second_token_id: "_"
    second_token_balance: 6583
  }
  ...
```

# getExchangeById

Query exchange pair based on id.

### Usage

```
getExchangeById(id)
```

### Parameter

| Parameter | Description         | Type   |
| :-------- | :------------------ | :----- |
| id        | Transaction pair id | String |

### Return

Object -Exchange object. An IllegalException is thrown when it fails to get exchange pair.\
\###Example

```
wrapper.getExchangeById("1");
```

Execution result:

```
exchange_id: 1
  creator_address: "AW\304\362\371&\260A\267\247\006\202\377\336\367$\236\031\220\206Y"
  create_time: 1586852889000
  first_token_id: "1000032"
  first_token_balance: 6682
  second_token_id: "_"
  second_token_balance: 6583
```
