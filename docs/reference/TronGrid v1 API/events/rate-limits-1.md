---
title: Rate Limits
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Currently, Trongrid rate limiting will be triggered in the following two situations:

1. When a user’s usage exceeds the total amount allowed per day, only a very low frequency such as 1/s will be allowed, and access beyond this limit will be denied.
2. When a user’s usage is below the total amount allowed per day, the frequency will be limited to 30/s. Access beyond this limit will be denied and there will be a penalty mechanism of not responding to service within 30s.
