---
title: Recommended API Configuration for SR Nodes
deprecated: false
hidden: false
metadata:
  robots: index
---
This section outlines API access control best practices for Super Representative (SR) nodes to enhance stability and strengthen the protection of sensitive data.

## 1. Restrict Network Access

It is recommended that SR nodes avoid exposing API ports to the public internet unless absolutely necessary. Restricting access helps enhance node privacy and security.

* **Suggested Behavior**: Keep API ports closed to external traffic.
* **If Access is Required**: If you must access APIs (e.g., for internal monitoring), implement access control at the network gateway level (such as using a firewall or Nginx reverse proxy). Only allow connections from trusted internal IP addresses (allowlist).

## 2. Refining HTTP & gRPC API Accessibility

To improve node privacy, consider deactivating specific HTTP & gRPC API endpoints that offer unnecessary insights into network topology or internal metadata (e.g., `/wallet/listnodes`, `/wallet/getnodeinfo`).

**Configuration**: Use the `disabledApi` in the node's configuration file (config.conf or config.yaml) to directly disable specific APIs. This is the recommended method as it safely and completely blocks the specified endpoints.

```
# Disabled api list,
# Add the method names you wish to block. Case insensitive.

disabledApi = [
   "listnodes",
   "getnodeinfo"
]
```

## 3. gRPC and JSON-RPC Limitations

When configuring rate limits, please distinguish between gRPC and JSON-RPC, as their capabilities differ:

* **gRPC**: Supports granular limiting for specific individual methods. You can set specific limits for methods within the `rpc` configuration block.
* **JSON-RPC**: Currently does not support restricting specific individual interfaces; it only allows for a global QPS limit applied to the entire service. Because JSON-RPC operates over HTTP, its rate limit configuration must be targeted at the `JsonRpcServlet` component within the `http` configuration block.

```
rate.limiter = {
  # 1. gRPC Limits 
  rpc = [
    {
      # Limit a specific gRPC method
      component = "protocol.Wallet/ListWitnesses",
      strategy = "QpsRateLimiterAdapter",
      paramString = "qps=1000"
    }
  ]

  # 2. HTTP & JSON-RPC Limits
  http = [
    {
      # Global limit for all JSON-RPC calls
      component = "JsonRpcServlet",
      strategy = "QpsRateLimiterAdapter",
      paramString = "qps=1000"
    },
    {
      # Limit a specific HTTP method
      component = "GetTransactionInfoByIdServlet",
      strategy = "QpsRateLimiterAdapter",
      paramString = "qps=1000"
    }
  ]
}
```

**Note on gRPC Component Names**: The component name for gRPC methods must include the correct prefix (e.g., `protocol.Wallet/ListWitnesses`). To verify the exact component names available on your node, you can enable `reflectionService = true`  in the `rpc` block of the configuration file, then restart the node and run the following command: `grpcurl -plaintext IP:50051 list`.
