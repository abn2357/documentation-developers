---
title: Overview
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
FullNode HTTP API is the core API service provided by Tron nodes. Users can use HTTP API to send transactions. The general process includes the following three steps:

* Create a transaction via system contract APIs
* Sign the transaction using SDK
* Broadcast the transaction by `BroadcastTransaction`

To distinguish HEX and Base58check addresses, a `visible` parameter is introduced.

To handle multi-sign, a `Permission_id` parameter is introduced to select the underlying permission type.

**Note**: When using the HTTP API, you can choose to use GET or POST to request data. When choosing to use the POST method, currently parameters are only supported passing to the HTTP message body in JSON format.

<br />

> 📘 Note
>
> Although TRON has avoided XSS by setting the Content-Type of HTTP APIs to application/json, there are a few APIs that don't have input validation. To better protect user data security, we recommend that you correctly encode any data from APIs before they use it in any UI, especially when parameter "visible = true" by default.
>
> Here is a typical XSS protection method: Encode all data from the APIs in HTML. Use methods such as `encodeURIComponent()` or `escape()` to encode the data, which can convert special characters into their HTML entities and prevent them from being interpreted as HTML code by the browser.
>
> Please be sure to implement XSS protection for all data from the APIs to ensure the security of user data. We understand that you may need more information about XSS protection. It is recommended that you refer to the following resources: [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
