---
title: TRX
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
TRX is the most important cryptocurrency on the TRON network and has a wide range of application scenarios. Rewards on the TRON network are issued in the form of TRX. Users can obtain resources and voting rights by staking TRX. TRX is also used as the primary form of collateral in the DeFi lending market, as a unit of accounting in NFT marketplaces, and so on.

The TRON network allows developers to create decentralized applications, also called DApps, which share limited TRON network resources together. Therefore, TRON needs a mechanism to prevent DApps from accidentally or maliciously occupying all network resources.

Consumption of TRON network resources is measured in Bandwidth and Energy, where Bandwidth is a unit that measures the size of transactions in bytes stored in the blockchain database, and Energy is a unit that measures the amount of computing power required by the TRON Virtual Machine (TVM) to execute a specific operation. When users make a transaction, they need to pay for the Bandwidth and Energy required to execute the transaction, and TRON supports paying for Bandwidth and Energy by burning TRX.

Therefore, even if a malicious DApp submitted an infinite loop, the transaction would eventually run out of TRX and terminate, allowing the network to return to normal.

# Minting TRX

Minting is the process in which new TRX gets created on the TRON network. The underlying TRON protocol creates the new TRX, and it is not possible for a user to create TRX.

TRX will be minted when a Super Representative (SR) produces a block on the TRON network. Currently, for each new block, the TRON protocol will generate a block production reward of 8 TRX and a voting reward of 128 TRX. Both rewards are dynamic parameters of the TRON network and can be modified through committee proposals.

# Burning TRX

TRX can get destroyed by a process called 'burning'. When TRX gets burned, it gets removed from circulation permanently.

Every transaction on TRON consumes Bandwidth or Energy. When a user's Bandwidth or Energy is insufficient, they need to burn TRX to pay for the resources required for the transaction. The burning of TRX can not only help reduce the inflation of TRX, but also prevent accidental or malicious transactions from occupying all TRON network resources.

# Denominations of TRX

Since many transactions on TRON are small, TRON has introduced a currency denomination, sun, which can be referenced for smaller amounts. The technical implementation of many applications is calculated based on sun. The conversion formula between TRX and sun is as below:

```
1 TRX = 1000000 sun
```

# Transferring TRX

Transferring TRX is a `TransferContract` type of TRON network transaction which transfers TRX from one account to another. Here are examples of transferring TRX using the HTTP API and the TronWeb SDK:

* HTTP API\
  The following section creates an unsigned TRX transfer transaction through the Fullnode HTTP interface `wallet/createtransaction`:

  ```javascript=
  curl -X POST  https://api.shasta.trongrid.io/wallet/createtransaction -d 
      '{
          "to_address": "TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 
          "owner_address": "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR", 
          "amount": 10000000,
          "visible":true
      }'
  ```

  After creating the unsigned transaction through the above interface, you need to sign and broadcast the transaction to finally complete the TRX transfer. 

* TronWeb SDK\
  The following section creates a TRX transfer transaction through TronWeb:
  ```javascript=
  const privateKey = "..."; 
  var fromAddress = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR"; //address _from
  var toAddress = "TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr"; //address _to
  var amount = 10000000; //amount，in sun
  // Create an unsigned TRX transfer transaction
  const tradeobj = await tronWeb.transactionBuilder.sendTrx(
        toAddress,
        amount,
        fromAddress
  );
  // Sign
  const signedtxn = await tronWeb.trx.sign(
        tradeobj,
        privateKey
  );
  // Broadcast
  const receipt = await tronWeb.trx.sendRawTransaction(
        signedtxn
  ).then(output => {
    console.log('- Output:', output, '\n');
    return output;
  });
  ```

# Querying TRX Balance

* HTTP API\
  You can query an account's TRX balance through the Fullnode HTTP API `wallet/getaccount`. The `balance` field of the returned value is the TRX balance, in sun:
  ```javascript=
  curl -X POST  https://api.shasta.trongrid.io/wallet/getaccount -d 
        '{"address": "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR",
          "visible": true
          }'
  ```
* TronWeb SDK\
  You can also query the TRX balance of an account through TronWeb:
  ```javascript=
  const privateKey = "..."; 
  var address = "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR"; 
  // Query the information of an account, and get the balance through the 'balance' in the return value.
  var tradeobj = await tronWeb.trx.getAccount(
        address,
  ).then(output => {console.log('- Output:', output, '\n');});
  ```
