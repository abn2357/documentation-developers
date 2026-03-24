---
title: Background
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
TronGrid provides standard TRON [FullNode HTTP APIs](https://developers.tron.network/reference/full-node-api-overview) alongside its proprietary, user-friendly [extension API](https://developers.tron.network/reference/get-account-info-by-address). The latest release of this proprietary API is v1.

The TronGrid API platform is engineered for high performance and reliability, featuring low latency, high consistency, high availability, and partition fault tolerance. TronGrid supports Mainnet, Shasta Testnet, and Nile Testnet environments; therefore, developers should select the network that aligns with their specific requirements prior to use.

<Callout icon="💡" theme="default">
  ### Developer Note: Client-Side Security

  While TRON APIs primarily reduce XSS risk by setting the Content-Type of HTTP APIs to `application/json`, developers should be aware that certain endpoints may lack full input validation.

  To ensure maximum user data security, we recommend that data retrieved from the APIs be HTML encoded before rendering it in your User Interface (UI), especially for parameters where `visible = true` is the default.

  **Encoding Method**: Use standard functions like `encodeURIComponent()` or `escape()` to convert special characters into HTML entities. This process helps ensure the browser interprets the data safely, preventing the execution of malicious code.

  **Action**: Please ensure XSS protection is implemented for all data retrieved from these APIs. For detailed guidance, consult the [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
</Callout>

## Select a Network

| NETWORK        | URL                                                              |
| :------------- | :--------------------------------------------------------------- |
| Mainnet        | [https://api.trongrid.io](https://api.trongrid.io)               |
| Shasta Testnet | [https://api.shasta.trongrid.io](https://api.shasta.trongrid.io) |
| Nile Testnet   | [https://nile.trongrid.io](https://nile.trongrid.io)             |

## API Key Requirement

All API requests require an **API Key** parameter to ensure fair allocation of requested resources. Requests submitted without an API Key will be severely limited or unanswered. See [API Key](https://developers.tron.network/reference/select-network) for full details.
