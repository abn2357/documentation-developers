---
title: GetAssetIssueListByName
excerpt: Query the list of all the TRC10 tokens by a name. (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: getassetissuelistbyname
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Returns**

assetIssue - List\<AssetIssueCapsule> : The list of TRC10 token with same query name, please refer to [GetAssetIssueById](/reference/getassetissuebyid-1) for detailed fields of AssetIssueCapsule object, please note that string fields are in HexString format.
