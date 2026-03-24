---
title: Issuing a TRC-20 Token
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
Deploying a smart contract on the TRON blockchain can be done in several ways, depending on the tools and platforms you choose. In this guide, we will walk you through the procedure using the **TRONSCAN Contract Deployment** tool as an example. For other tools, please refer to their official documentation for detailed instructions.

# Prerequisites

## 1. Prepare Your TronLink

Make sure you have installed the **TronLink** extension and are connected to the correct network (Mainnet or Testnet). If you haven’t installed TronLink yet, please visit [TronLink](https://chromewebstore.google.com/detail/tronlink/ibnejdfjmmkpcnlpebklmnkoeoihofec) to download the latest version.

## 2. Prepare the TRC-20 Contract Code

Before deploying a custom TRC-20 token on the TRON blockchain, make sure you have your contract code finalized. To illustrate the deployment procedure, this guide uses the [TRC-20 Contract Template](https://github.com/TRON-Developer-Hub/TRC20-Contract-Template/tree/main) as an example. The template provides a solid foundation and includes these essential files: **ITRC20.sol**, **SafeMath.sol**, **TRC20.sol**, **TRC20Detailed.sol**, and **Token.sol**.

Before deployment, adjust the following parameters in the `Token.sol` file from the template:

* **Token Name:** Change the name to your desired token name. Example: **"TestTokenName"**；
* **Token Symbol:** Modify the token symbol to represent your token's symbol (**e.g., TTN**)；
* **Decimals:** Set the number of decimal places for your token. The most common value is **18**, but you can specify the value as needed；
* **Total Supply:** Define the total supply of your token. In the constructor, the initial supply is multiplied by 10^decimals (**e.g., 10000000000**) to account for precision. Adjust this number to suit your needs.

```solidity
// 0.5.1-c8a2
// Enable optimization
pragma solidity ^0.5.0;

import "./TRC20.sol";
import "./TRC20Detailed.sol";

/**
 * @title SimpleToken
 * @dev Very simple TRC20 Token example, where all tokens are pre-assigned to the creator.
 * Note they can later distribute these tokens as they wish using `transfer` and other
 * `TRC20` functions.
 */
contract Token is TRC20, TRC20Detailed {

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor () public TRC20Detailed("TestTokenName", "TTN", 18) {
        _mint(msg.sender, 10000000000 * (10 ** uint256(decimals())));
    }
}
```

# 3. Deploy the TRC-20 Contract

Deploying a TRC20 contract on the TRON blockchain is a straightforward process when using the [TRONSCAN Contract Deployment Tool](https://tronscan.org/#/contracts/contract-compiler). Below is a step-by-step guide to help you deploy your TRC-20 contract with ease.

* Connect your wallet and make sure the account holds enough TRX.

<Image align="center" width="700px" src="https://files.readme.io/2b86bf2e14bd2e187e88f59fcf8442cad592b4a7fe9573d45d58268d7f104485-2025-08-05_12.15.55.png" />

* Upload the contract files, which include ITRC20.sol, SafeMath.sol, TRC20.sol, TRC20Detailed.sol, and Token.sol.

<Image align="center" width="700px" src="https://files.readme.io/0aea82aa99e296d2adde54c50e7b482bd3172312060671c03063f908a9e115d9-2025-08-05_12.27.44.png" />

* Compile the contract, and specify the parameters based on your actual needs. Below is an example used for compiling.
  * **Solidity Compiler Version:** Select 0.5.10;
  * **Optimization:** Set to Activated;
  * **Runs:** Use the default value 0.

<Image align="center" width="700px" src="https://files.readme.io/96e66f17d1dfdf4fc80bcfecd807bf951551342cb5b07d7cfc8b3aaa4b21c883-2025-08-05_12.29.31.png" />

<Image align="center" width="700px" src="https://files.readme.io/92a12db2ebd2b38f3faa12eaa3638a51294bfa0d9faa900773f339be1c88424e-2025-08-05_12.29.38.png" />

* Deploy the contract, and make sure to choose "Token" as the main contract.

<Image align="center" width="300px" src="https://files.readme.io/51f7152b9c0dcaa140c87b74b1230160e6dd043fba1271f67f8b8ee5b5ae53f7-2025-08-05_12.31.33.png" />

<Image align="center" width="700px" src="https://files.readme.io/b71d57e2bc94230069fb5bffafec0ac973eec39a4be469d4f9f1cb710dfb9615-2025-08-05_12.31.42.png" />

# 4. Verify the TRC-20 Contract (Optional)

* To verify your smart contract on TRONSCAN, navigate to the [Verification Tool](https://tronscan.org/#/contracts/verify) and enter the required contract details. For more details about verifying contracts, please refer to [Verifying](https://developers.tron.network/docs/contract-verification).

  * **Contract Address:** the address used during deployment;
  * **Main Contract:** usually the main contract name, e.g., "Token";
  * **Solidity Compiler Version:** Select 0.5.10;
  * **License:** Choose "None" if not applicable;
  * **Optimization and Runs:** Set "Optimization" to "Activated" and leave "Runs" as 0 by default.

  ![](https://files.readme.io/53cfd94914fc0910cdc3b57e71134016bcca0953589540266285529e68f68ad8-image.png)

  <br />
* Click the "Upload Contract File(s)" button, select your contract source code files, and then upload them. **Please ensure that the uploaded code is exactly consistent with the version deployed on the chain, including all dependent files.**
* Check the "I am not a robot" box to complete the CAPTCHA check.
* Click the "Verify and Publish" button.
* Once the contract is verified, you can view the contract details.

<Image align="center" width="700px" src="https://files.readme.io/3552905018c42bbe0d12324e2c3eeba8454fef6380a0dbd5f22209995e67a888-2025-08-05_12.39.36.png" />

<Image align="center" width="700px" src="https://files.readme.io/95a15d58e225091b9f68eab76b3959a3284af069c710280800a56fd894624b65-2025-08-05_12.39.45.png" />

* On the TRONSCAN page, you can see that the contract source code was verified successfully.

<Image align="center" width="700px" src="https://files.readme.io/a5617352f7726f094024ba4281457fdc738d7eab09300464d1f156462badaf2d-2025-08-05_12.41.14.png" />

# 5. Record the TRC-20 Token

The [Record Tool](https://tronscan.org/#/tokens/create/Type) allows token creators to record their TRC-20 token information on TRONSCAN. By using this tool, you can officially record your token’s basic information, contract information, and social media profiles.

* For the token type, choose **TRC20** and click "Confirm" to proceed.

<Image align="center" width="700px" src="https://files.readme.io/21612d390178eaf91c78b444d951284da6fd06c60594785750fb1aff262a492b-2025-08-05_12.43.47.png" />

* Fill in details of the TRC-20 token - enter the basic information, contract information, and social media profiles of your token.

**Important:** Ensure that the details you enter match exactly with the information in your deployed TRC-20   contract.

<Image align="center" width="700px" src="https://files.readme.io/4d933b443beff91cd8b9c1116dac3ff86ec2b1018287df8177c835074822f16b-2025-08-05_12.45.19.png" />

* Double-check the information you’ve entered and sign. Once the process is complete, you will see a confirmation that your token has been successfully recorded on the TRON network.

<Image align="center" width="700px" src="https://files.readme.io/a7b3b45f40173d71766957b4d03dcf00775b7a75066068e57c44f629d1014947-2025-08-05_12.45.58.png" />

* To further update the token information, please go to the wallet details page and click [Record a Token](https://tronscan.org/#/wallet/tokensCreate). Then, update the token information here.

<Image align="center" width="700px" src="https://files.readme.io/7c2adeb9971d609d4d6718606789e1f759290b79d60dc569ebc814b7810935c6-2025-08-05_12.47.01.png" />

# 6. Add the Token to TronLink

* To add your token to TronLink, click the ‘+’ button on the homepage of your TronLink wallet. Search the contract address of your TRC-20 token. The corresponding token details will automatically appear. Click the ‘+’ button on the right side to add the token to your asset list. After that, you can view the token on your wallet homepage and proceed with transfers and other operations.

<Image align="center" width="700px" src="https://files.readme.io/09721eb77dc65591074af3ac57c7f5e5061599d0ab59c3ccd8b50559404f1caf-2025-08-05_12.48.33.png" />

* To get more information about the token, you can also search the contract on TRONSCAN.

<Image align="center" width="700px" src="https://files.readme.io/7c09de046794ed1da105ce069676991bb57f2b53cd4a27399257c10a1e8c30a2-2025-08-05_12.49.20.png" />

**Note:** The TronLink extension currently allows users to add tokens to their wallet homepage on the Mainnet,  Nile testnet, and Shasta testnet. However, please note that the target token must have been recorded on TRONSCAN and leave 15 minutes for data synchronization before it can be searched and added in TronLink.
