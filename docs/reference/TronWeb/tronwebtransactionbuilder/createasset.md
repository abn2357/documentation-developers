---
title: createAsset
excerpt: >-
  Create an unsigned transaction that issue trc10  token，equivalent to
  createToken
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Usage**

```javascript
const trc_options = {
             name : "test",//Token name, default string
             abbreviation : "tt",//Token name abbreviation, default string
             description : "fortest",//Token description, default string
             url : "www.baidu.com",//Token official website url, default string
             totalSupply : 100000,//Token total supply
             trxRatio : 1, // Define the price by the ratio of trx_num/num
             tokenRatio : 1, // Define the price by the ratio of trx_num/num
             saleStart : 1581047830000,//ICO start time
             saleEnd : 1681047110000,//ICO end time
             freeBandwidth : 0, // The creator's "donated" bandwidth for use by token holders
             freeBandwidthLimit : 0, // Out of `totalFreeBandwidth`, the amount each token holder get
             frozenAmount : 0, //Token staked supply
             frozenDuration : 0,
             // for now there is no default for the following values
             precision : 6,//Precision of issued tokens
             permission_id : 1//Optional, for multi-signature use
         }
tronWeb.transactionBuilder.createAsset(trc_options, issuerAddress);
```

**Parameter**\
object(trc\_options),string(issuerAddress,format:hexstring or base58)

**Return**\
object

**Example**

```javascript
const trc_10_options = {
              name : "test",
              abbreviation : "tt",
              description : "fortest",
              url : "www.baidu.com",
              totalSupply : 100000,
              trxRatio : 1, 
              tokenRatio : 1, 
              saleStart : 1581064352000,
              saleEnd : 1681047110000,
              freeBandwidth : 0, 
              freeBandwidthLimit : 0, 
              frozenAmount : 0,
              frozenDuration : 0,
              precision : 6
          }
undefined
> tronWeb.transactionBuilder.createAsset(trc_10_options,"41BF97A54F4B829C4E9253B26024B1829E1A3B1120").then(result=>console.log(result))
Promise { <pending> }
> {
  visible: false,
  txID: 'abfb7d021a36194b631f395fcfde625c053ea54348551ae83cb2b068f597e835',
  raw_data: {
    contract: [ [Object] ],
    ref_block_bytes: 'ccdd',
    ref_block_hash: 'dcfd491f536c5c4a',
    expiration: 1581064395000,
    timestamp: 1581064336498
  },
  raw_data_hex: '0a02ccdd2208dcfd491f536c5c4a40f8b1a0f6812e5a8b0108061286010a2f747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e41737365744973737565436f6e747261637412530a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201204746573741a02747420a08d063001380640014880e29df6812e50f082ddb1f630a20107666f7274657374aa010d7777772e62616964752e636f6d70f2e89cf6812e'
}
```
