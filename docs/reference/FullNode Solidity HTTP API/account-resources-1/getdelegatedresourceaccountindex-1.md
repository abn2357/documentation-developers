---
title: GetDelegatedResourceAccountIndex
excerpt: >-
  Queries the resource delegation by an account during stake 1.0 phase. i.e.
  list all addresses that have delegated resources to an account. (Confirmed
  state)
api:
  file: full-node-solidity-http-api.json
  operationId: getdelegatedresourceaccountindex-1
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

| Field          | Type     | Description                                                                 |
| :------------- | :------- | :-------------------------------------------------------------------------- |
| `account`      | string   | Account address.                                                            |
| `fromAccounts` | string[] | List of account addresses that delegate resources to this account.          |
| `toAccounts`   | string[] | List of account addresses that receive resources delegated by this account. |

<br />
