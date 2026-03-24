---
title: GetPaginatedAssetIssueList
excerpt: >-
  Query the list of all the tokens by pagination.Returns a list of Tokens that
  succeed the Token located at offset.
api:
  file: full-node-http-api.json
  operationId: getpaginatedassetissuelist
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

assetIssue - List\<AssetIssueCapsule> : The list of paginated TRC10 token, please refer to [GetAssetIssueByAccount](/reference/getassetissuebyaccount) for detailed fields of AssetIssueCapsule object, please note that string fields are in HexString format.