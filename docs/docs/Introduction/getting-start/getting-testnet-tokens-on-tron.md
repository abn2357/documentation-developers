---
title: Getting Testnet Tokens on TRON
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
This guide details the process for getting testnet tokens (TRX and TRC-20 tokens) on the TRON Shasta and Nile testnets. These free tokens allow developers to test and validate their smart contracts and decentralized applications (DApps) at no cost.

# Methods for Getting Testnet Tokens

## Getting Testnet Tokens Through a Faucet Website

This is the most direct and common way to get testnet tokens. Follow these steps:

1. **Prepare Your Wallet Address**: In your TRON wallet (such as TronLink), switch to the Shasta or Nile testnet and copy your wallet address. To create a new wallet:
   * Refer to the official [TronLink guide](https://support.tronlink.org/hc/en-us/articles/5012004270361-How-to-Create-an-Account-in-TronLink-Extension) for step-by-step instructions, 
   * Watch the [video tutorial](https://trondao.org/videos/how-to-create-a-tronlink-wallet/) for a visual walkthrough, or 
   * See the [developer documentation](https://developers.tron.network/docs/account#external-account-creation) to understand the underlying technical principles.
2. **Navigate to an Official Faucet Website**: In your browser, go to the latest official faucet website for your target testnet:
   * Nile testnet: [https://nileex.io/join/getJoinPage](https://nileex.io/join/getJoinPage)
   * Shasta testnet: [https://shasta.tronex.io/join/getJoinPage](https://shasta.tronex.io/join/getJoinPage)
3. **Request Testnet Tokens**: Once you find the token you wish to request on the page, paste your wallet address into the input field, complete the reCAPTCHA verification, and then click "Obtain" to submit your request.

   ![](https://files.readme.io/43bad567189958af96629746f1ac26628bc94bf370fd7324b97aa604118cbf9a-image.png)
4. **Confirm Your Request Status**: The faucet will provide immediate feedback of your request outcome via a pop-up message. There are three primary responses:
   * **Request Succeeded -*"Successful acquisition of test tokens."***\
     When a request is successful, the faucet will automatically process the transaction. Please allow a brief period for the transaction to be confirmed on the blockchain. You will see the tokens reflected in your wallet balance once the transaction is confirmed.
   * **Repeated Request -*"You have acquired test tokens today and cannot be retrieved repeatedly!"***\
     This message appears if you have already requested the same token for the same wallet or IP address within the 24-hour cooldown period. In this case, please try again after the cooldown period has ended.
   * **Invalid Address Format -*"Failed to get test tokens, please enter the address in the correct format!"***\
     This message appears if you enter a wallet address that is invalid or incorrectly formatted. Please double-check and retry with the correct TRON wallet address.

### Important Notes

* **Usage Limits**: To prevent resource abuse, each unique wallet and IP address is limited to one faucet request every 24 hours. Note that the requestable amount per request varies by token; please refer to the faucet page for specific details.
* **Link Verification**: Faucet URLs are subject to change. For security, always use links from trusted sources, such as official documentation or developer communities. Never use links from unverified sources.

## Getting Testnet Tokens via Official Community Bot

Alternatively, developers can request testnet tokens from the official TronFAQBot on Telegram or Discord. Follow this process:

1. **Join a Developer Community**: Use the links below to join an official developer group where the TronFAQBot is active:
   * Telegram:
     * TRON Official Developer Group: [https://t.me/TronOfficialDevelopersGroupEn](https://t.me/TronOfficialDevelopersGroupEn)
     * TRON Core Devs Community: [https://t.me/troncoredevscommunity](https://t.me/troncoredevscommunity)
   * Discord: [https://discord.com/invite/hqKvyAM](https://discord.com/invite/hqKvyAM)
2. **Review Bot Commands**: In the group chat, type in the `!help` command to display a list of all available functions and their syntax:

   ```
   TronFAQBot Help:

   The following commands start with "!" (without quotes), for example: !help

       !help shows this.

       !ping shows the latency.
       !check ADDR checks if the given ADDR is a valid TRON Address.
       !balance shows the balances of the faucet.
       !balance ADDR shows the balances of the given ADDR (TRX, USDT, USDC, USDD).

       !nile ADDR sends 5000 nile TRX to ADDR (max 5000 in 24 hours).
       !nile_usdt ADDR sends 5000 USDT (Smart Contract on Nile Test Net) to ADDR (max 5000 in 24 hours).
       !nile_usdd ADDR sends 5000 USDD (Smart Contract on Nile Test Net) to ADDR (max 5000 in 24 hours).
       !nile_usdc ADDR sends 5000 USDC (Smart Contract on Nile Test Net) to ADDR (max 5000 in 24 hours).

       !shasta ADDR sends 5000 shasta TRX to ADDR (max 5000 in 24 hours).
       !shasta_usdt ADDR sends 5000 USDT (Smart Contract on Shasta Test Net) to ADDR (max 5000 in 24 hours).
       !shasta_usdd ADDR sends 5000 USDD (Smart Contract on Shasta Test Net) to ADDR (max 5000 in 24 hours).
       !shasta_usdc ADDR sends 5000 USDC (Smart Contract on Shasta Test Net) to ADDR (max 5000 in 24 hours).
   ```
3. **Request Testnet Tokens**: Send a command using the format `!<command> <your_wallet_address>` in the group. For example:

   ```
   # Request 5000 TRX on Nile Testnet for address TA5w..yfps
   !nile TA5w..yfps

   # Request 5000 USDT on Shasta Testnet for address TA5w..yfps
   !shasta_usdt TA5w..yfps
   ```

   Upon receiving the command, TronFAQBot will typically reply with a confirmation message, such as `<username> will receive 5000 TRX (Shasta) soon. Thank you!` You can then verify the transaction by checking your wallet balance.

# Security Best Practices

Regardless of how you get or use testnet tokens, please follow these principles:

* **Isolate Your Wallet**: We strongly recommend using a dedicated, newly-created wallet exclusively for testing. To eliminate the risk of asset compromise, never import a Mainnet private key or mnemonic phrases into a test environment.
* **Secure Your Private Keys**: Safeguard test wallet private keys with the same diligence as Mainnet keys. Adhere to standard key management security protocols to prevent accidental exposure.
* **Use Tokens for Testing Only**: Testnet tokens have no financial value and are strictly for development and testing purposes. We recommend avoiding any form of trading activity involving testnet tokens.
* **Verify Transactions On-Chain**: Use the corresponding TRONSCAN testnet explorer to verify transaction details, confirm balances, and debug smart contracts:
  * Nile Explorer: [nile.tronscan.org]()
  * Shasta Explorer: [shasta.tronscan.org]()

# Frequently Asked Questions (FAQ)

## What should I do if I need more testnet tokens than the faucets' daily limit?

When the standard faucet allowance (such as 5,000 tokens per 24 hours) is inadequate, consider these options:

* **Ask an Admin**：Politely post a public message to an admin in the official developer community (Telegram or Discord). To expedite your request, please include the following details:
  * **Project Description**: A brief summary of what you are building or testing.
  * **Reason for Request**: The reason you need a larger number of tokens (such as for automated stress tests or large-scale user simulations).
  * **Required Amount**: The specific number of tokens you need (such as 100,000 Shasta TRX).
  * **Receiving Address**: Your testnet wallet address.
* **Ask the Community**: As another option, you can politely ask other developers in the community if they can send you a small amount.
* **Use Multiple Wallets**: A good method for acquiring a moderate amount of tokens is to generate several testnet addresses, request tokens for each, and then consolidate the funds.
* **Deploy a Private Testnet**: For projects that require long-term, high-volume, and fully controllable testing resources, the most robust solution is to deploy a local, private testnet.
