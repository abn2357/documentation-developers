---
title: GetApprovedList
excerpt: >-
  Query the account address list which signed the transaction based on the
  transaction content and signature information, which can be used for
  transaction verification.
api:
  file: full-node-http-api.json
  operationId: http-getapprovedlist
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

| Field         | Type                 | Description                                                             |
| :------------ | :------------------- | :---------------------------------------------------------------------- |
| result        | Result               | The parsing result. Returns an error code and message if parsing fails. |
| approved_list | string[]             | List of account addresses that have signed the transaction.             |
| transaction   | TransactionExtention | Transaction information.                                                |