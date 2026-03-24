---
title: API Key
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
# API Key

## What are API Keys

TronGrid provides core FullNode HTTP APIs and extended APIs of the TRON network. All API requests require an API Key parameter to ensure fair allocation of requested resources. Requests submitted without an API Key will be severely limited or unanswered.

> 📘 Note
>
> Currently, making requests to the Shasta or Nile testnets via TronGrid does not require an API Key.

## How to get an API Key

After logging in to [TronGrid](https://www.trongrid.io/), users can quickly create API Keys on the Dashboard or the API Key list page. Each API Key has a separate configuration page, allowing users to configure Keys to meet different operational needs.

## How to use API Keys

To use an API Key, add the `TRON-PRO-API-KEY` field to your HTTP request headers and set its value to your actual API Key.

**HTTP Examples**

```curl
curl -X POST \
  https://api.trongrid.io/wallet/createtransaction \
  -H 'Content-Type: application/json' \
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

**gRPC Examples:**

```java
import io.grpc.Metadata;
import io.grpc.stub.MetadataUtils;

// Add these new codes: create a custom header
Metadata header=new Metadata();
Metadata.Key<String> key =
    Metadata.Key.of(“TRON-PRO-API-KEY”, Metadata.ASCII_STRING_MARSHALLER);
header.put(key, “25f66928-0b70-48cd-9ac6-da6f8247c663");

// Create client stub
ServiceGrpc.ServiceBlockingStub stub = ServiceGrpc.newBlockingStub(channel);

// add this new line to attach header
stub = MetadataUtils.attachHeaders(stub, header);

public Block getNowBlock() {
    return stub.getNowBlock(EmptyMessage.newBuilder().build());
}
```
