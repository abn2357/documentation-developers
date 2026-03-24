---
title: GetPaginatedNowWitnessList
excerpt: >-
  This API retrieves the real-time vote counts of all Super Representatives
  (SRs) in the current epoch, sorted in descending order, and returns a
  paginated list within the specified range. 
api:
  file: full-node-http-api.json
  operationId: get_walletgetpaginatednowwitnesslist
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
<br />

**Returns**

`witnesses` - `List<WitnessCapsule>` : A list of Super Representatives (SRs). For field details of each SR, please refer to [ListWitnesses](/reference/listwitnesses). Note: If the request parameters are invalid, the API returns `{}` (an empty object).
