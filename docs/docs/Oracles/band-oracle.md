---
title: Band Oracle
excerpt: Tron Band Oracle Developer Docs
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Band Protocol Integration

Developers building on Tron can now leverage Band’s decentralized oracle infrastructure. With Band’s oracle, they now have access to various cryptocurrency price data to integrate into their applications.

# The Bridge Contract

## Bridge Architecture

Anyone looking to integrate Band’s oracle data into their application can do so through Band’s bridge contract. This contract is deployed on the TRON testnet at address `TPxsemS7h9rrJPZAPDjP7rmLoA4ErYny69`. The contract source code can also be found on the BandChain repository.

The price data originates from data requests made on BandChain. The values are the median of the results retrieved by BandChain’s validators from CoinGecko, CryptoCompare, TRON, and Alpha Vantage APIs. The data request is then made by executing a price aggregator oracle script, the code of which can be examined on BandChain’s devnet.

Band’s bridge contract then retrieves and stores the results of those requests onto the contract state.

## Data Available (Testnet)

The bridge contract stores the following price pairs, the values of which are updated every 5 minutes. The specific data that is available through the bridge contract, as well as the source(s) where the data was retrieved from, are as follows:

Cryptocurrency Prices (CoinGecko, CryptoCompare, Binance, Binance US):

* BTC/USD
* ETH/USD
* TRX/USD
* BAND/USD

Commodity Prices (Alpha Vantage):

* XAU/USD
* XAG/USD

Foreign Exchange Conversion Rates (Alpha Vantage):

* EUR/USD
* CNY/USD
* JPY/USD
* GBP/USD
* KRW/USD

In addition to the actual price value, the following information is also available:

* The multiplier used to calculate the stored price value
* The timestamp of when the specific price request was resolved on BandChain

These parameters are intended to act as security parameters to help anyone using the data to verify that the data they are using is what they expect and, perhaps more importantly, actually valid.

## Bridge Contract Price Update Process

For the ease of development, the Band Foundation will be maintaining and updating the bridge contract with the latest price data. In the near future, we will be releasing guides on how developers can create similar contracts themselves to retrieve data from Band’s oracle.

# Retrieving and Using the Price Data

We will now illustrate an example of a simple price database contract that uses data from Band’s oracle. The code for the contract is shown below.

```javascript solidity
pragma solidity 0.5.9;
pragma experimental ABIEncoderV2;

import "./Obi.sol";
import {IBridge, IBridgeCache} from "./IBridgeWithCache.sol";
import {ParamsDecoder, ResultDecoder} from "./Decoders.sol";
import "openzeppelin-solidity/contracts/math/SafeMath.sol";


contract SimplePriceDB {
    using SafeMath for uint256;
    using ResultDecoder for bytes;
    using ParamsDecoder for bytes;
    
    IBridgeCache public bridge;
    IBridge.RequestPacket public req;
    
    uint256 public current_price;

    constructor(IBridgeCache bridge_) public {
        bridge = bridge_;
        
        req.clientId = "tron_testnet";
        req.oracleScriptId = 76;
        // {symbol:"BTC"}
        req.params = hex"00000003425443";
        req.askCount = 4;
        req.minCount = 3;
    }

    // Fetches the latest BTC/USD price value from the bridge contract and saves it to state.
    function setPrice() public {
        IBridge.ResponsePacket memory res = bridge.getLatestResponse(req);
        ResultDecoder.Result memory result = res.result.decodeResult();
        current_price = result.px;
    }
}
```

Let’s break down the code into sections.

## Imports

```javascript solidity
import "./Obi.sol";
import {IBridge} from "./IBridgeWithCache.sol";
import {ParamsDecoder, ResultDecoder} from "./Decoders.sol";
import "openzeppelin-solidity/contracts/math/SafeMath.sol";
```

Aside from SafeMath.sol, the contract we will be writing requires three helper files specific to Band’s oracle: **Obi.sol**, **Decoders.sol**, and **IBridgeWithCache.sol.** 

**Obi.sol**\
This contains a set of functions to help serialize and deserialize binary data when interacting with the BandChain ecosystem. The full standard specificationcan be found on their [wiki](https://github.com/bandprotocol/bandchain/wiki/Oracle-Binary-Encoding-\(OBI\)) and the code on the BandChain[ repository.](https://github.com/bandprotocol/bandchain/blob/master/bridges/evm/contracts/obi/Obi.sol) 

**Decoders.sol**\
This is what we will use to work with data related to requests made on BandChain. This will help us in extracting the various information, such as the price value, that we may need from the request response from Band’s oracle. The file is available from the oracle script’s [bridge code tab](https://guanyu-devnet.cosmoscan.io/oracle-script/76#bridge) on the devnet explorer.

**IBridgeWithCache.sol**\
The interface file for Band’s bridge contract.

## Contract

```javascript solidity
contract SimplePriceDB {
    using SafeMath for uint256;
    using ResultDecoder for bytes;
    using ParamsDecoder for bytes;
    
    IBridgeCache public bridge;
    IBridge.RequestPacket public req;
    
    uint256 public current_price;

    constructor(IBridgeCache bridge_) public {
        bridge = bridge_;
        
        req.clientId = "tron_testnet";
        req.oracleScriptId = 76;
        // {symbol:"BTC"}
        req.params = hex"00000003425443";
        req.askCount = 4;
        req.minCount = 3;
    }

    // Fetches the latest BTC/USD price value from the bridge contract and saves it to state.
    function setPrice() public {
        IBridge.ResponsePacket memory res = bridge.getLatestResponse(req);
        ResultDecoder.Result memory result = res.result.decodeResult();
        current_price = result.px;
    }
}
```

The contract itself can then be further broken down into two parts: the contract constructor and the main `getPrice` function.

### **Contract Constructor**

```javascript solidity
constructor(IBridge bridge_) public {
    bridge = bridge_;

    req.clientId = "tron_testnet";
    req.oracleScriptId = 76;
    // {symbol:"BTC"}
    req.params = hex"00000003425443";
    req.askCount = 4;
    req.minCount = 3;
}
```

The contract’s constructor takes one argument, which is the address of the bridge contract. It then sets the various fields of the `req`  (RequestPacket) variable. This `req` variable will be what we will use as the key to match and retrieve the price from the bridge contract. Specifically, in this case, we set `req` to have the following parameters:

* **clientId ("tron\_testnet")**: the unique identifier of this oracle request, as specified by the client.
* **oracleScriptId (76)**: The unique identifier number assigned to the oracle script when it was first registered on Bandchain.
* **params (hex"00000003425443")**: The data passed over to the oracle script for the script to use during its execution. In this case, it is the hex representation of the OBI-encoded request struct`{"symbol":"BTC"}`.
* **minCount (3)**: The minimum number of validators necessary for the request to proceed to the execution phase. Therefore, the `minCount` value must be less than or equal to the `askCount`.
* **askCount (4)**: The number of validators that are requested to respond to this request.

The specific params for each of the available price pairs are:

| Pair     | Params               |
| :------- | :------------------- |
| BTC/USD  | hex"00000003425443"  |
| ETH/USD  | hex"00000003455448   |
| TRX/USD  | hex"00000003545258   |
| BAND/USD | hex"0000000442414e44 |
| XAU/USD  | hex"00000003584155   |
| XAG/USD  | hex"00000003584147   |
| EUR/USD  | hex"00000003455552   |
| CNY/USD  | hex"00000003434e59   |
| JPY/USD  | hex"000000034a5059   |
| GBP/USD  | hex"00000003474250   |
| KRW/USD  | hex"000000034b5257   |

### `setPrice` Function

```javascript solidity
// Fetches the latest BTC/USD price value from the bridge contract and saves it to state.
function setPrice() public {
    IBridge.ResponsePacket memory res = bridge.getLatestResponse(req);
    ResultDecoder.Result memory result = res.result.decodeResult();
    current_price = result.px;
}
```

This is the main function that we will use to fetch the price from Band’s bridge contract and save it into our price database contract’s state. It calls the bridge contract’s `getLatestResponse` to retrieve the latest request response associated with a *BTC/USD* price request. It then uses `Decoders.sol`'s `decodeResult` method to parse that response into a struct. Finally, we save the price value from that response into the contract’s `price` variable.
