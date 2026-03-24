---
title: Issuing a TRC-721 Token
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
# 1 Create a TRON Account

Install the Chrome extension of [TronLink](https://www.tronlink.org/) to prepare for your issuance. You may create a new account in the extension via the following three ways:

* create a new account directly

* restore from a mnemonic phrase, private key, or Keystore

* pair a hardware wallet

350 TRX is required in your account as the minimum.

# 2 Modify Code of Your TRC-721 Contract

You may modify the TRC721Token.sol file to customize the name and symbol of your token. Remember to save the changes.

TRC-721 contract template: [template](https://developers.tron.network/docs/trc-721-contract-example)

![](https://files.readme.io/91382cc-441615884766_.pic.jpg "441615884766_.pic.jpg")

# 3 Deploy a TRC-721 Smart Contract

Deploy with TRONSCAN: [Contract Compiler](https://tronscan.io/#/contracts/contract-compiler)

## 3.1 Connect Wallet

![](https://files.readme.io/e0d7ad3-451615885008_.pic.jpg "451615885008_.pic.jpg")

## 3.2 Upload Contract Code

![](https://files.readme.io/97e3263-461615885065_.pic.jpg "461615885065_.pic.jpg")

![](https://files.readme.io/62b74e8-471615885081_.pic.jpg "471615885081_.pic.jpg")

## 3.3 Compile the Contract

![](https://files.readme.io/e61fca5-481615885109_.pic_hd.jpg "481615885109_.pic_hd.jpg")

Please choose the compiler version between 0.5.5 and 0.5.14.

![](https://files.readme.io/e8a29e1-491615885127_.pic.jpg "491615885127_.pic.jpg")

Click "Compile" to compile the code. If the following content is returned, the compilation is successful.

![](https://files.readme.io/fe42cc9-501615885142_.pic.jpg "501615885142_.pic.jpg")

## 3.4 Deploy the Contract

![](https://files.readme.io/82b1060-511615885169_.pic_hd.jpg "511615885169_.pic_hd.jpg")

Remember to choose TRC721Token, for it is the main contract.

![](https://files.readme.io/502d573-521615885187_.pic_hd.jpg "521615885187_.pic_hd.jpg")

Click "Deploy" to deploy the contract and sign in the TronLink popup.

![](https://files.readme.io/1451dd0-531615885206_.pic_hd.jpg "531615885206_.pic_hd.jpg")

# 4 Mint an NFT Token

Log in to TRONSCAN with your wallet, and use the contract address to open the deployed TRC-721 contract. In this section, the TZ4NjvdqyCbWmZxXEEAb3bXhfT8f6YGxJd contract on the Nile testnet is used as an example:

* Choose "Contract > Write Contract".

![](https://files.readme.io/68befe3-731616989680_.pic_hd.jpg "731616989680_.pic_hd.jpg")

* Find the mintWithTokenURI method, and fill in the to_address, tokenId, and the tokenURI corresponding to coral.json.

![](https://files.readme.io/91e5b67-741616989852_.pic.jpg "741616989852_.pic.jpg")

> 📘 Metadata URI
>
> For the generation of metadata URI, please refer to [Uploading NFT Metadata to BTFS Network](https://developers.tron.network/docs/uploading-nft-metadata-to-btfs-network) .

* Click 'send', and accept the signature. A 'true' will be displayed if the token is minted successfully.

![](https://files.readme.io/8f385c2-711616987914_.pic.jpg "711616987914_.pic.jpg")

![](https://files.readme.io/6007a35-751616990209_.pic.jpg "751616990209_.pic.jpg")

Deployment successful. Contract address obtained. Please record the contract address.

![936](https://files.readme.io/c1abc32-391615882917_.pic_hd.jpg "391615882917_.pic_hd.jpg")

# 5 Record the TRC-721 Token

Record with TRONSCAN: [Record tool](https://tronscan.org/#/tokens/create/Type)

* Select the token type.

![](https://files.readme.io/6c81294-1.png "1.png")

Select TRC721 and click "Confirm".

* Enter the TRC-721 token information.  
  Enter the basic information, contract address, and social media information of the token. Fields with asterisks (*) are required information.  
  Please note that the recording process must be logged in with the deployer address.

![](https://files.readme.io/120ef5c-2.png "2.png")

Confirm all information required for the TRC-721 token and click "Submit".

![](https://files.readme.io/cda6330-3.png "3.png")

You will see a popup from TronLink asking for your signature. Click "Accept" to sign the message.

![](https://files.readme.io/612fbab-4.png "4.png")

* When the following content is displayed, the token is recorded.

![](https://files.readme.io/a12342d-5.png "5.png")

# 6 Follow & Transfer the TRC-721 Token in TronLink App

* Click the add assets button.

![](https://files.readme.io/d488fb3-1.png "1.png")

* Click the search button.

![](https://files.readme.io/b6ded3a-2.png "2.png")

* Input the TRC-721 contract address and click the add button.

![](https://files.readme.io/2105f04-3.png "3.png")

This indicates the token has been added.

![](https://files.readme.io/d7c0a14-4.png "4.png")

* Click the TRC-721 token. Wendy is used in this example.

![](https://files.readme.io/d0dc74f-5.png "5.png")

* Select Wendy 721 in the collectible list.

![](https://files.readme.io/3dbcbf4-6.png "6.png")

* Click "Send" to transfer the TRC-721 token.

![](https://files.readme.io/8098de2-7.png "7.png")

* Input the address for receiving and enter your wallet password.

![](https://files.readme.io/879ebd7-8.png "8.png")

* The token has been successfully transferred.

![](https://files.readme.io/92f55bb-9.png "9.png")
