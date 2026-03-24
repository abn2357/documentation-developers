---
title: TronWeb.sidechain Object
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
Create a tronWeb instance with sidechain options

```js
const TronWeb = require('tronweb');
let fullNode = '';
let solidityNode = '';
let eventServer = '';
let sideOptions = {
  fullNode: '',
  solidityNode: '',
  eventServer: '',
  mainGatewayAddress: '',
  sideGatewayAddress: '',
  sideChainId: ''
}
const privateKey = '';
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,sideOptions,privateKey);
```

if you prefer to use our tronex testnet with a sidechain, you can create an TronWeb instance as follows:

```js
const fullNode = 'https://testhttpapi.tronex.io';
const solidityNode = 'https://testhttpapi.tronex.io';
const eventServer = 'https://testhttpapi.tronex.io';
const sideOptions = {
  fullNode: 'https://suntest.tronex.io',
  solidityNode: 'https://suntest.tronex.io',
  eventServer: 'https://suntest.tronex.io',
  mainGatewayAddress: 'TFLtPoEtVJBMcj6kZPrQrwEdM3W3shxsBU',
  sideGatewayAddress: 'TRDepx5KoQ8oNbFVZ5sogwUxtdYmATDRgX',
  sideChainId: '413AF23F37DA0D48234FDD43D89931E98E1144481B'
}
const tronWeb = new TronWeb(
  fullNode,
  solidityNode,
  eventServer,
  {
    fullNode: sideOptions.fullNode,
    solidityNode: sideOptions.solidityNode,
    eventServer: sideOptions.eventServer,
    mainGatewayAddress: sideOptions.mainGatewayAddress,
    sideGatewayAddress: sideOptions.sideGatewayAddress,
    sideChainId: sideOptions.sideChainId
  }
);
```
