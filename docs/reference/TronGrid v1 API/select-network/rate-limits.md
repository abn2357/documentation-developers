---
title: Rate Limits
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
> At present, the total number of requests per Account per day is 100,000 (the total number of requests will be adjusted according to related needs later).

In order to ensure the reasonable allocation of requested resources, it is recommended that all requests to the Trongrid service have the parameter API Key. Trongrid has the following rate limits for all users:

1. If the user uses the API Key, and the usage does not exceed the total amount per day, the access frequency per second is limited to 15qps. If this limit is exceeded, the access will be denied and a 429 error will be returned.
2. If the user uses the API Key and the usage exceeds the total amount per day, the access frequency per second will be limited to a very low value, such as 5qps. If this limit is exceeded, access will be denied and a 429 error will be returned.
3. If the user does not use the API Key, trongrid will dynamically limit the access rate. Once the access frequency exceeds the rate limit, trongrid will take a penalty mechanism for blocking access within 30 seconds and return a 403 error. After 30 seconds, the blocking will be released.

## How to tell whether I’m rate-limited?

If you are subject to rate limiting, your request will return with an HTTP status code “4xx” or "5xx" and include an error message that you can adjust according.

```text v1 interface
{
     "Success": false,
     "Error": "The key exceeds the frequency limit(15), and the query server is suspended for 30s",
     "StatusCode": 429
}
```

```text Full Node interface
{
     "Error": "The key exceeds the frequency limit(15), and the query server is suspended for 30s"
}
```

## What should I do if I’m rate-limited?

If you continue to be rate-limited, try these work-arounds:

* Make sure you have the API Key in the URL. Requests without API Key will be subject to strict rate limiting or even complete rejection.
* Limit the number of requests when launching the Dapp.
* Don't use polling for Trongrid very often, the TRON network produces a block around every 3s, and thus it usually doesn’t make sense to request new data at a faster speed.
