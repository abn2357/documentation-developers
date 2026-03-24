---
title: TRC-10
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
TRC-10 is a native token standard supported by the TRON network. Unlike TRC-20 tokens, it does not rely on the TRON Virtual Machine (TVM) but is implemented directly at the blockchain protocol level. Any account can issue a TRC-10 token — limited to one issuance per account — with a creation fee of 1024 TRX.

## Issue

By utilizing`AssetIssueContract`, a particular type of transaction in TRON, each account is able to issue TRC-10 after paying 1,024 TRX. 

* HTTP API\
   The following section creates an unsigned transaction to issue TRC-10 through the FullNode HTTP API `wallet/createassetissue`:

  ```javascript=
  curl -X POST  https://api.shasta.trongrid.io/wallet/createassetissue -d '{
  "owner_address":"417946F66D0FC67924DA0AC9936183AB3B07C81126",
  "name":"0x6173736574497373756531353330383934333132313538",
  "abbr": "0x6162627231353330383934333132313538",
  "total_supply" :100000000,
  "trx_num":1,
  "num":1,
  "precision":1,
  "start_time" : 1581928489000,
  "end_time":1581938187000,
  "description":"007570646174654e616d6531353330363038383733343633",
  "url":"007570646174654e616d6531353330363038383733343633",
  "free_asset_net_limit":10000,
  "public_free_asset_net_limit":10000,
  "frozen_supply":{"frozen_amount":1, "frozen_days":2}
  }'
  ```

  After the transaction is created, you need to sign and broadcast this transaction in order to implement the issuing. For more details, please refer to [Transactions](https://developers.tron.network/docs/tron-protocol-transaction).

* TronWeb SDK

  ```javascript=
  const privateKey = "...";
  var createAssetAddress = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR";
  const trc_options = {
        name : "test", 
        abbreviation : "tt",  
        description : "fortest", 
        url : "www.baidu.com",
        totalSupply : 10000000,
        trxRatio : 1,
        tokenRatio : 1,
        saleStart : 1581929489000,
        saleEnd : 1581938187000,
        freeBandwidth : 0,
        freeBandwidthLimit : 0,
        frozenAmount : 0,
        frozenDuration : 0,
        precision : 6
  }
  //create an unsigned transaction for TRC-10 issuing
  tradeobj = await tronWeb.transactionBuilder.createAsset(
        trc_options,
        createAssetAddress
  ).then(output => {
    console.log('- Output:', output, '\n');
    return output;
  });
  //sign
  const signedtxn = await tronWeb.trx.sign(
        tradeobj,
        privateKey
  );
  //broadcast
  const receipt = await tronWeb.trx.sendRawTransaction(
        signedtxn
  ).then(output => {
    console.log('- Output:', output, '\n');
    return output;
  });
  ```

## Transfer

`TransferAssetContract` is introduced as a type of transaction in the TRON network to transfer tokens from one account address to another. It can be implemented through either the HTTP API or the TronWeb SDK.

* HTTP API\
   The following section starts an unsigned transaction with the Fullnode HTTP API `wallet/transferasset`:

  ```javascript=
  curl -X POST   https://127.0.0.1:8090/wallet/transferasset -d '{
    "owner_address":"41d1e7a6bc354106cb410e65ff8b181c600ff14292", 
    "to_address": "41e552f6487585c2b58bc2c9bb4492bc1f17132cd0", 
    "asset_name": "0x6173736574497373756531353330383934333132313538", 
    "amount": 100
  }'
  ```

  After the transaction is created, you need to sign and broadcast this transaction in order to implement the transfer. For more details, please refer to [Transactions](https://developers.tron.network/docs/tron-protocol-transaction).

* TronWeb SDK

  ```javascript=
  const privateKey = "..."; 
  var toAddress = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR";
  var tokenID= "1000088";
  var amount = 1000;
  var fromAddress = "TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr";
  //create an unsigned transfer
  tradeobj = await tronWeb.transactionBuilder.sendToken(
        toAddress,
        amount,
        tokenID,
        fromAddress,    
  ).then(output => {
    console.log('- Output:', output, '\n');
    return output;
  });
  //sign
  const signedtxn = await tronWeb.trx.sign(
        tradeobj,
        privateKey
  );
  //broadcast
  const receipt = await tronWeb.trx.sendRawTransaction(
        signedtxn
  ).then(output => {
    console.log('- Output:', output, '\n');
    return output;
  });
  ```

## Check Balance

* HTTP API\
    The return value of assetV2 in the Fullnode HTTP API`wallet/getaccount` shows the TRC-10 token balance in the wallet:

  ```javascript=
   curl -X POST  https://api.shasta.trongrid.io/wallet/getaccount -d 
       '{"address": "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR",
         "visible": true
       }'
  ```

* TronWeb SDK

  ```javascript=
  var address = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR"; 
  //check the balance by assetV2 value in return
  var tradeobj = await tronWeb.trx.getAccount(
        address,
  ).then(output => {console.log('- Output:', output, '\n');});
  ```

## More TRC-10 APIs

| No. | API                                                                                                | Description                                                                  |
| --- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1   | [getassetissuebyaccount](https://developers.tron.network/reference/getassetissuebyaccount)         | Query an issued TRC-10 token by account                                      |
| 2   | [getassetissuebyid](https://developers.tron.network/reference/getassetissuebyid)                   | Query an issued TRC-10 token by ID                                           |
| 3   | [getassetissuebyname](https://developers.tron.network/reference/getassetissuebyname)               | Query an issued TRC-10 token by name                                         |
| 4   | [getassetissuelistbyname](https://developers.tron.network/reference/getassetissuelistbyname)       | Query the issued TRC-10 token list by name                                   |
| 5   | [getassetissuelist](https://developers.tron.network/reference/getassetissuelist)                   | Query the issued TRC-10 token list                                           |
| 6   | [getpaginatedassetissuelist](https://developers.tron.network/reference/getpaginatedassetissuelist) | Query the paginated TRC-10 token list                                        |
| 7   | [unfreezeasset](https://developers.tron.network/reference/unfreezeasset)                           | Unfreeze a TRC-10 token that has passed the freezing duration for collateral |
| 8   | [updateasset](https://developers.tron.network/reference/wallet-updateasset)                        | Update TRC-10 token info                                                     |
| 9   | [participateassetissue](https://developers.tron.network/reference/participateassetissue)           | Participate in TRC-10 token issuing                                          |
