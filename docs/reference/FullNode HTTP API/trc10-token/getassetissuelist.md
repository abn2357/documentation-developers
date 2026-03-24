---
title: GetAssetIssueList
excerpt: Query the list of all the TRC10 tokens.
api:
  file: full-node-http-api.json
  operationId: getassetissuelist
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

assetIssue - List\<AssetIssueCapsule> : The list of all TRC10 tokens, please refer to [GetAssetIssueByAccount](/reference/getassetissuebyaccount) for detailed fields of AssetIssueCapsule object, please note that string fields are in HexString format.