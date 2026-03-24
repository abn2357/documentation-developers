---
title: TRC-721 Contract Interaction
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
### 1. Query Token Name

Call the name() function of the TRC-721 contract to get the token name.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_name() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let trc721name = await contract.name().call();
        console.log('name: ', trc721name);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_name()
```

Return result:

```
name:  TRC721TEST  
```

### 2. Query Token Symbol

Call the symbol() function of the TRC-721 contract to get the token symbol.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_symbol() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let trc721symbol = await contract.symbol().call();
        console.log('symbol: ', trc721symbol);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_symbol()
```

Return result:

```
symbol:  TEST
```

### 3. Query Token Balance

Call the balanceOf() function of the TRC-721 contract to get the balance of a specific token in the specified account.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_balanceOf() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address
    var address = "TA1g2WQiXbU5GnYBTJ5Cp22dvSjT3ug9uK";

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let result = await contract.balanceOf(address).call();
        console.log('balance: ', tronWeb.toDecimal(result));
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_balanceOf()
```

Return result:

```
balance:  1
```

### 4. NFT Transfer

Call the tranferFrom() function of the TRC-721 contract for NFT transfers.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_transferFrom() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modify or change values on the blockchain.
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
        await contract.transferFrom(
            "TA1g2WQiXbU5GnYBTJ5Cp22dvSjT3ug9uK", //address _from
            "TM8vRhebJD7zeoBLWAnr9SrYrhWNrHjBgC", //address _to
            666 //uint256 tokenId
        ).send({
            feeLimit: 100000000
        }).then(output => {console.log('- transferFrom hash:', output, '\n');});
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_transferFrom()
```

Return result:

```
- transferFrom hash: 9f4d10713cb0406adb7c729013b941d35597afeeba56faf2a1bc7647fc0a92bd

Note: The above result is the transfer transaction hash, you can check the transaction details via Nile tronscan browse
```

### 5. Grant Control of an NFT to Another Address

Call the approve() function of the TRC-721 contract to authorize the control of an NFT to another address.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_approve() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modify or change values on the blockchain.
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
        await contract.approve(
            "TA1g2WQiXbU5GnYBTJ5Cp22dvSjT3ug9uK", //address _spender
            666 //uint256 tokenId
        ).send({
            feeLimit: 100000000
        }).then(output => {console.log('- approve hash:', output, '\n');});
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_approve()
```

Return result:

```
- approve hash: d7cb1451ed962667f3e24323655dadd8c650ee80d171ea5e44ea97b97eaa3118 

Note: The above result is the authorized transaction hash, you can check the transaction details through Nile tronscan browser
```

### 6. Query All NFT Info of a TRC-721 Contract under an Address

(1) Call the function of balanceOf(address \_owner) to query the number of NFT holdings of a specific address.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_balanceOf() {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address
    var address = "TM8vRhebJD7zeoBLWAnr9SrYrhWNrHjBgC";

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let result = await contract.balanceOf(address).call();
        console.log('result: ', tronWeb.toDecimal(result));
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_balanceOf()
```

Return result:

```
result:  2
Note: The returned result indicates that the above query address holds a quantity of 2.
```

(2) Call the function of tokenOfOwnerByIndex(address \_owner, uint256 \_index) to traverse all token\_ids.

The number of NFTs held by the above address is 2, so the index of the query is 0 and 1 respectively.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_tokenOfOwnerByIndex(index) {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let token_id = await contract.tokenOfOwnerByIndex(
            "TM8vRhebJD7zeoBLWAnr9SrYrhWNrHjBgC", // address owner
            index //uint256 index
            ).call();
        console.log('token_id: ', tronWeb.toDecimal(token_id));
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_tokenOfOwnerByIndex(0)
trc721_tokenOfOwnerByIndex(1)
```

Return result:

```
token_id:  666
token_id:  555
```

(3) Call the function of tokenURI(uint256 \_tokenId) to query details of each NFT.

```javascript
const TronWeb = require('tronweb')

const HttpProvider = TronWeb.providers.HttpProvider;
const fullNode = new HttpProvider("https://nile.trongrid.io");
const solidityNode = new HttpProvider("https://nile.trongrid.io");
const eventServer = new HttpProvider("https://nile.trongrid.io");
const privateKey = "your private key";
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);

async function trc721_tokenURI(tokenid) {
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address

    try {
        let contract = await tronWeb.contract().at(trc721ContractAddress);
        //Use call to execute a pure or view smart contract method.
        // These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
        let tokenURI = await contract.tokenOfOwnerByIndex(
            tokenid //uint256 tokenid
            ).call();
        console.log(tokenid + ' tokenURI:', tokenURI);
    } catch(error) {
        console.error("trigger smart contract error",error)
    }
}
trc721_tokenURI(666)
trc721_tokenURI(555)
```

Return result:

```
666 tokenURI:  https://gateway.btfs.io/btfs/QmWq4cp588QD8tzrSxvPs2bGikDdKyA35BT3iysBcP1jFD
555 tokenURI: https://gateway.btfs.io/btfs/QmWq4cp588QD8tzrSxvPs2bGikDdKyA35BT3iysBcP1jFD
```
