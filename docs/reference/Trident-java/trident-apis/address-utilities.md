---
title: Address Utilities
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# generateAddress

Generate a private key offline.

### Usage

```
generateAddress()
```

### Parameter

None

### Return

Random private key.

### Example

```
wrapper.generateAddress()
```

Execution result：

```
0701b12b547d65abea69ee7d165fb04e52251d221d44acb6bbd92c8a47eeba81
```

# parseAddress

Address conversion tool that converts the legal address entered by the user into ByteString format.

### Usage

```
parseAddress(String address)
```

### Parameter

| Parameter | Description                                                | Type   |
| :-------- | :--------------------------------------------------------- | :----- |
| address   | address account or contract address in any allowed formats | String |

### Return

The address in ByteString format.

### Example

```
wrapper.parseAddress("4122ED62967ED0D2186B2FC639D7972D172A95C855")
```

Execution result：

```
<ByteString@2d9caaeb size=21 contents="A\"\355b\226~\320\322\030k/\3069\327\227-\027*\225\310U">
```
