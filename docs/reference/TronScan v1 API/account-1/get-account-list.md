---
title: Get account list
excerpt: Returns the list of accounts.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note
>
> The value sum of **start** and **limit** must be less than or equal to **10000**

```
https://apilist.tronscanapi.com/api/account/list?sort=-balance&limit=20&start=0
```

> Try this endpoint in your [browser](https://apilist.tronscanapi.com/api/account/list?sort=-balance\&limit=20\&start=0)

## Request

Query Parameters

| Parameter | Description                           |
| :-------- | :------------------------------------ |
| start     | Start number. Default: 0              |
| limit     | Number of items per page. Default: 10 |
| sort      | Sort field. Default: -balance         |

## Response

Sample Response

```json
{
    "account_number": 149682388,
    "last_24h_account_change": 201763,
    "total": 10000,
    "data": [
        {
            "address": "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR",
            "addressTagLogo": "",
            "balance": 18243211943261359,
            "power": 0,
            "totalTransactionCount": 2341329,
            "latestOperationTime": 1680173745000,
            "updateTime": 1680173745000
        },
        {
            "address": "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK",
            "addressTagLogo": "",
            "balance": 8997572047566078,
            "power": 0,
            "totalTransactionCount": 183,
            "latestOperationTime": 1675712808000,
            "updateTime": 1675712808000
        }
    ],
    "contractMap": {
        "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK": true,
        "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR": true
    },
    "rangeTotal": 149682388,
    "contractInfo": {
        "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK": {
            "tag1": "USDD-TRXBURN",
            "tag1Url": "https://usdd.io",
            "name": "MultiSigTRXBurn",
            "vip": false
        },
        "TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR": {
            "tag1": "WTRX Token",
            "tag1Url": "https://just.network/",
            "name": "WTRX",
            "vip": true
        }
    }
}
```
