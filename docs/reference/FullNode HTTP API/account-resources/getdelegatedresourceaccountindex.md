---
title: GetDelegatedResourceAccountIndex
excerpt: >-
  Query the resource delegation by an account during stake1.0 phase. i.e. list
  all addresses that have delegated resources to an account.
api:
  file: full-node-http-api.json
  operationId: getdelegatedresourceaccountindex
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

| Field        | Type     | Description                                                                 |
| :----------- | :------- | :-------------------------------------------------------------------------- |
| account      | string   | Account address.                                                            |
| fromAccounts | string[] | List of account addresses that delegate resources to this account.          |
| toAccounts   | string[] | List of account addresses that receive resources delegated by this account. |