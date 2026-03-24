---
title: GetPaginatedAssetIssueList
excerpt: >-
  Query the list of all the tokens by pagination.Returns a list of Tokens that
  succeed the Token located at offset. (confirmed state)
api:
  file: full-node-http-api.json
  operationId: getpaginatedassetissuelist-1
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: noindex
---
**Returns**

assetIssue - List\<AssetIssueCapsule> : The list of paginated TRC10 token, please refer to [GetAssetIssueById](/reference/getassetissuebyid-1) for detailed fields of AssetIssueCapsule object, please note that string fields are in HexString format.
