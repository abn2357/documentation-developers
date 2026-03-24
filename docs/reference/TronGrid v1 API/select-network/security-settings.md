---
title: Security Settings
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
> 📘 Note:
>
> The security configurations described below are currently applicable only to the HTTP interface.

TronGrid provides project-specific security settings to granularly control API Key usage. Security measures include:

* **Allowlists**: Restrict the types of requests permitted.
* **JSON Web Token (JWT)**: Enable token-based authentication.

## User-Agent AllowList

If you distribute applications with embedded API keys (e.g., Electron, iOS, or Android apps) and can configure a custom User-Agent, we recommend adding your application's User-Agent string to the allowlist. Once configured, any API request originating from a platform with a non-matching `User-Agent` will be automatically rejected.

How Matching Works: The User-Agent allowlist uses partial string matching. A request is registered as a match if the string specified in your allowlist is found anywhere within the request's full `User-Agent` header.

**Example:**

```curl
Allowlist entry:com.example.dapp

Request:

curl -X POST \
  https://api.trongrid.io/wallet/createtransaction \
  -H 'User-Agent: com.example.dapp/v1.2.7 (Linux; Android 8.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'TRON-PRO-API-KEY: 25f66928-0b70-48cd-9ac6-da6f8247c663' \
  -d '{
    "to_address": "41e9d79cc47518930bc322d9bf7cddd260a0260a8d",
    "owner_address": "41D1E7A6BC354106CB410E65FF8B181C600FF14292",
    "amount": 1000
}'

Result: Request is allowed while all other user-agent requests are rejected.
```

## Origin AllowList

To prevent unauthorized third parties from using your API Key on their websites, you can configure an Origin Allowlist to restrict API Key access to specific HTTP Origins.

For example, if you deploy your application to `mydapp.example.com`, adding this domain to your HTTP Origin allowlist ensures that any traffic **not containing** the Origin `mydapp.example.com` will be rejected.

### HTTP Origin Matching Rules

Similar to TLS certificates, HTTP Origin matching supports wildcard subdomain patterns. The left-most subdomain can be replaced with a special wildcard (*) to match any such subdomain. This wildcard matches a single subdomain level and can only appear as the left-most portion of an entry.

The URL scheme is optional and can be `http://`, `https://`, or any other scheme you wish to limit to. If a scheme is included in the allowlist entry, the Origin must have the same scheme. Furthermore, an entry specifying a particular scheme will limit requests strictly to Origins of that scheme.

**Examples:**

Suppose your API key is configured with the following allowlist entry: `https://*.example.com`

**1. Allowed Requests**
When the request's `Origin` header perfectly matches the rules (consistent protocol and the domain is a 1st-level subdomain), the request will be allowed.

```
# Example Request
curl -X POST [https://api.trongrid.io/wallet/createtransaction](https://api.trongrid.io/wallet/createtransaction) \
  -H 'TRON-PRO-API-KEY: YOUR_API_KEY' \
  -H 'Origin: [https://myapp.example.com](https://myapp.example.com)' \
  -H 'Content-Type: application/json' \
  -d '{"to_address": "...", "owner_address": "...", "amount": 1000}'
```

| Origin Header               | Result      | Reason                                               |
| --------------------------- | ----------- | ---------------------------------------------------- |
| `https://myapp.example.com` | **Allowed** | Both protocol (https) and 1st-level subdomain match. |
| `https://api.example.com`   | **Allowed** | Matches the 1st-level subdomain wildcard pattern.    |

**2. Rejected Requests**
The following requests will be blocked due to rule violations:

| Origin Header                   | Result       | Reason for Rejection                                                                     |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------- |
| `http://myapp.example.com`      | **Rejected** | **Scheme Mismatch:** Entry requires `https`.                                             |
| `https://example.com`           | **Rejected** | **Level Mismatch:** Wildcard `*` requires a subdomain; it doesn't cover the apex domain. |
| `https://sub.myapp.example.com` | **Rejected** | **Depth Mismatch:** Wildcard only matches a single subdomain level.                      |
| `https://myapp.other-env.com`   | **Rejected** | **Domain Mismatch:** Origin must end with `example.com`.                                 |

## Contract Address AllowList

If your application queries data exclusively from specific smart contracts or addresses, add these addresses to your Contract Address Allowlist. Once an address is added to the allowlist, any API request attempting to query an address not included in the list will be automatically rejected.

The following interfaces accept contract address parameters and are subject to this allowlist:

```text
/v1/contracts/contract_address/events
/(event)|(events)/contract/contract_address
/(event)|(events)/contract/[a-zA-Z0-9]+/[a-zA-Z0-9]+
/(event)|(events)/contract/[a-zA-Z0-9]+/[a-zA-Z0-9]+/[a-zA-Z0-9]+
/walletsolidity/triggerconstantcontract
/wallet/triggersmartcontract
/wallet/triggerconstantcontract
```

**Example:**

```curl
Allowlist entry: TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t

Request:
curl --request GET \
  --url https://api.trongrid.io/v1/contracts/TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t/events \
  --header 'TRON-PRO-API-KEY: 25f66928-0b70-48cd-9ac6-da6f8247c663' 
  
Result: Request is allowed. Any compatible request methods with non-allowlisted addresses alone as parameters will be rejected.
```

## Requested API AllowList

You can use your API Key to restrict requests to specific TronGrid API methods. If this allowlist is not empty, any request to a method not explicitly listed will be rejected.

**Example:**

```curl
Allowlist entry: walletsolidity_getTransactionById

Request:
curl --request GET \
  --url https://api.trongrid.io/v1/accounts/TUD4YXYdj2t1gP5th3A7t97mx1AUmrrQRt \
  --header 'TRON-PRO-API-KEY: 25f66928-0b70-48cd-9ac6-da6f8247c663' \
  
Result: Request is rejected, because the method is not walletsolidity_getTransactionById.
```

## JWT (JSON Web Tokens)

### What is JWT?

JSON Web Token (JWT) is an open standard (RFC 7519) used to securely transmit information between application environments as a JSON object. This information is represented as claims that are digitally signed, ensuring the data is verifiable and trustworthy.

In TronGrid, JWTs are used to pass authenticated user identity information between identity providers and service providers. The token can be used to authenticate requests and access resources from the server.

### How to use JWT

When the JWT switch is enabled, every API request must include valid token information for TronGrid to verify. Requests that fail verification will not receive a response.

Each account can create up to three JWTs. Creating a new JWT requires you to provide a user-generated public key (currently utilizing the RS256 algorithm). Once the public key is submitted, the system will automatically generate the corresponding Key ID and Fingerprint.

**Implementation Walkthrough**

The following steps demonstrate the integration process using example code.

**Step 1: Generate RSA Key Pair**

To use JWT in your project, you must first generate a Public/Private key pair. TronGrid currently supports the RS256 algorithm.

> **Note**: Please keep your Private Key secure. Never share it publicly.

Generate keys using OpenSSL:

```curl
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```

Configuration: Enter an recognizable name to identify the key and paste the text content from your public key file (`public.pem`). It should be a standard **PEM-encoded** file (e.g., generated by OpenSSL) looking like this:

```text
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvGek2v/H/TEzB+mnfbJ5
m7wgon0u/JjFQY3kYr6E0N4cRBQm8sy6ikNKi5x/1YxmhBqn6HvF9xD/p72eCBVe
RFh863pjWpF1C5yjOq3OEks00ayRP1ukATG8LtoUnWoPisXrh5/wVe4fHDPeNwe4
5RXOp6svO860o/ckAxt8yO/ZczqtN8cNA7unGawJ3cn8VeL+pa4a6f8DNfp32QUY
Y//HjPFvrTxcfJ4cM6E74L913P2CDuiSVVXMk0iyX/blh6M4h7dGAlcmHEHno9OW
5jrrAKobZZT1quc6qT43sTJviqc24Ndgas5jTOPhEV7bgkgQbTbtpgorHjUpqAIm
+wIDAQAB
-----END PUBLIC KEY-----
```

**Step 2: Generate token**

_**Method 1: Using Java**_

1. Add Dependencies: Import the `jjwt` package.

```java
compile 'io.jsonwebtoken:jjwt-api:0.11.2'
runtime 'io.jsonwebtoken:jjwt-impl:0.11.2'
runtime 'io.jsonwebtoken:jjwt-jackson:0.11.2'
```

2. Call `createSignedJwtRsa256` to generate token

```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Header;
import io.jsonwebtoken.Jws;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import org.spongycastle.util.encoders.Base64;
  
public class JwtTest {
  
 private static PublicKey getRSAPublicKey(String inputKey)
    throws NoSuchAlgorithmException, InvalidKeySpecException {
  String rsaPublicKey = inputKey.replace("-----BEGIN PUBLIC KEY-----", "");
  rsaPublicKey = rsaPublicKey.replace("-----END PUBLIC KEY-----", "");
  rsaPublicKey = rsaPublicKey.replace("\n", "");
 
  X509EncodedKeySpec keySpec = new X509EncodedKeySpec(Base64.decode(rsaPublicKey));
  KeyFactory kf = KeyFactory.getInstance("RSA");
  return kf.generatePublic(keySpec);
 }
 
 
public void createSignedJwtRsa256() {
  /**
   * {
   *   "alg": "RS256",
   *   "typ": "JWT",
   *   "kid": "bdbd8dabcb8d49f3ae9732c14c9940ea"
   * }
   *
   * {
   *   "exp": 1617736153,
   *   "aud": "trongrid.io",
   * }
   * */
 
  try {
    PrivateKey privateKey = getRSAPrivateKey(privateKeyStr);
 
    JwtBuilder builder = Jwts.builder()
        .setHeaderParam("alg", "RS256") 
        .setHeaderParam("typ", "JWT") 
        .setHeaderParam("kid", "XXXXXXXXXXX") // your jwt key id
        .claim("exp", 1617736153) 
        .claim("aud", "trongrid.io") 
        .signWith(privateKey, SignatureAlgorithm.RS256);
 
    String token = builder.compact();
    System.out.println(token);
 
  } catch (Exception e) {
    e.printStackTrace();
    assert false;
  }
}
  
}
```

**_Method 2: Using Online Tool (jwt.io)_**

1. Open website: [jwt.io](https://jwt.io/).
2. Select Algorithm: Select **RS256**.
3. Enter Header: Provide the `kid` (ID of JWT). You can view this ID in the API Key configuration after adding the JWT to your API Key.

```json
{  "alg": "RS256",
   "typ": "JWT",
   "kid": "XXXXXXX" // id of jwt
}
```

4. Enter Payload: The optional `exp` field represents the expiration time and can be left blank.

```json
{
   "exp": 1617736153,
   "aud": "trongrid.io" 
}
```

5. Verify Signature: In the VERIFY SIGNATURE section, enter your Public Key and Private Key into the respective fields.
6. Get Token: In the ENCODED section, you will see the generated token.

**Step 3: Use Token**

To authenticate a request, add the `Authorization` field to your HTTP request header.

* Value Format: `Bearer <token>` (**Note**: There must be a space between "Bearer" and the token string.)

**Examples:**

```curl
curl -X POST \
  https://api.trongrid.io/wallet/createtransaction \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer xxxxxx' \
  -H 'TRON-PRO-API-KEY: 25f66928-0b70-48cd-9ac6-da6f8247c663' \
  -d '{
    "to_address": "41e9d79cc47518930bc322d9bf7cddd260a0260a8d",
    "owner_address": "41D1E7A6BC354106CB410E65FF8B181C600FF14292",
    "amount": 1000
}'
```

```python
import requests

url = "https://api.trongrid.io/wallet/createtransaction"

payload = "{\n    \"to_address\": \"41e9d79cc47518930bc322d9bf7cddd260a0260a8d\",\n    \"owner_address\": \"41D1E7A6BC354106CB410E65FF8B181C600FF14292\",\n    \"amount\": 1000\n}"
headers = {
    'Authorization': "Bearer xxxxxx",
    'Content-Type': "application/json",
    'TRON-PRO-API-KEY': "25f66928-0b70-48cd-9ac6-da6f8247c663"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
```

```javascript
var request = require("request");

var options = { method: 'POST',
  url: 'https://api.trongrid.io/wallet/createtransaction',
  headers: {  
     'Authorization': 'Bearer xxxxxx',
     'TRON-PRO-API-KEY': '25f66928-0b70-48cd-9ac6-da6f8247c663',
     'Content-Type': 'application/json' 
},
  body: { 
      to_address: '41e9d79cc47518930bc322d9bf7cddd260a0260a8d',
     owner_address: '41D1E7A6BC354106CB410E65FF8B181C600FF14292',
     amount: 1000 
},
  json: true 
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

**Configuration Constraints**

Please adhere to the following rules when generating your token:

* **Fixed Header Type**: The `typ` in the header is fixed to `"JWT"`.
* **Algorithm Support**: Currently, only **RS256** is supported (ES256 support will be added in future versions). Therefore, the `alg` header field is currently fixed to `"RS256"`.
* **Audience Restriction**: The `aud` field in the payload is fixed to `"trongrid.io"`.

Example:

```json Header
//Header：
{
     "alg": "RS256",
     "typ": "JWT",
     "kid": "bdbd8dabcb8d49f3ae9732c14c9940ea" // your jwt id
}
//Body
{
   "exp": 1617736153,
   "aud": "trongrid.io"
}
```
