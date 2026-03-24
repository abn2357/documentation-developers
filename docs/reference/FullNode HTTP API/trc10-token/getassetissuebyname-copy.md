---
title: GetAssetIssueByName
excerpt: Query a token by name, returns token info.
api:
  file: full-node-http-api.json
  operationId: getassetissuebyname-copy
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
> 📘 Duplicated TRC10 Token Names
>
> TRC10 allows for duplicate token names. Thus TRC10 tokens are identifiable by a unique Token ID.

**Returns**

AssetIssueCapsule : Token found with the provided name, please refer to [GetAssetIssueByAccount](/reference/getassetissuebyaccount) for detailed fields, please note that string fields are in HexString format.

If the token name is duplicate, it will return:

“Error”: “class org.tron.core.exception.NonUniqueObjectException : To get more than one asset, please use getAssetIssueById syntax”