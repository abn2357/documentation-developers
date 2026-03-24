---
title: GetDelegatedResourceAccountIndexV2
excerpt: >-
  In Stake2.0, query the resource delegation index of an account. Two lists will
  return, one is the list of addresses the account has delegated its
  resources(toAddress), and the other is the list of addresses that have
  delegated resources to the account(fromAddress).
api:
  file: full-node-http-api.json
  operationId: getdelegatedresourceaccountindexv2-1
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
| fromAccounts | string[] | A list of account addresses that delegate resources to this account.        |
| toAccounts   | string[] | List of account addresses that receive resources delegated by this account. |