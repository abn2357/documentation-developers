---
title: Verifying a Contract
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
Contract verification on TRONSCAN is the process of comparing the contract's source code with its bytecode deployed on the TRON blockchain and making it publicly accessible. Upon successful verification, the source code will be displayed on the "Contract" tab of the contract's detailed page, allowing users to review and interact with it.

## 1. Purpose and Significance of Contract Verification

Contract verification is not only a crucial means of safeguarding user rights but also a key step in promoting the healthy development of the TRON ecosystem. Verified contracts offer the following significant advantages:

* **Enhance Transparency**: Users can directly view the contract's source code, understanding its internal logic and functionality, which greatly increases user trust in the project and the contract.
* **Facilitate Auditing and Security Checks**: Publicly available source code allows community members or professional third-party institutions to audit the contract, promptly identify and fix potential security vulnerabilities or risks, and ensure asset security.
* **Support Interactive Operations**: TRONSCAN provides an intuitive visual interface for contract calls. Users and developers can directly call public methods of the contract on the page for testing, verification, and interaction, without the need to write additional code.
* **Demonstrate Project Professionalism**: Contract verification is an important indicator of a project's development professionalism and compliance. The successful verification of a contract signifies that the project team has followed good development practices.
* **Improve Ecosystem Compatibility**: Some third-party platforms (such as wallets, data analysis services, DApp browsers, etc.) only support verified contracts. Therefore, contract verification is a prerequisite for your project to integrate with these services and expand its ecosystem influence.

## 2. Contract Verification Guide

You can verify deployed contracts using the online verification tool provided by TRONSCAN. Please visit [TRONSCAN Contract Verification Tool](https://tronscan.org/#/contracts/verify) to start the verification process.

### 2.1 Fill in Basic Contract Information

On the verification page, you need to accurately fill in the basic information of your contract. **It is crucial to note that the following information must be exactly consistent with those used during contract deployment; otherwise, verification will fail.**

* **Contract Address**: The address generated after deploying the contract.
* **Main Contract**: The name of your main contract (i.e., the name after the `contract` keyword). 
* **Solidity Compiler Version**: The Solidity compiler version used during deployment.
* **License**: The type of open-source license used. If there are no special requirements, `None` can usually be selected.
* **Optimization**: Whether compiler optimization was enabled during contract deployment. Please select based on your actual choice during deployment.
* **Runs**: If optimization was enabled, please enter the number of optimization runs set during deployment.

![](https://files.readme.io/2922de80c777c66adecff322f78f8400bb0bec3b70bee2ba7fa37adc400b3e65-image.png)

<br />

After filling in the information, click "Upload Contract File(s)" to continue the verification process.

### 2.2 Submit Contract Source Code

1. Click the "Upload Contract File(s)" button, select your contract source code files, and then upload them. **Please ensure that the uploaded code is exactly consistent with the version deployed on the chain, including all dependent files.**
2. Check "I am not a robot" box to complete the CAPTCHA check.
3. Click the "Verify and Publish" button.

![](https://files.readme.io/1ed080fadc94d6bac9ff70a10691617e566fffd5779ac705f65a2eee7e5a4cc4-image.png)

<br />

TRONSCAN will automatically compare your submitted source code with the bytecode deployed on the chain. If verification is successful, the system will display a message saying "Contract Verified". Afterwards, you can go to the contract page to view information of the publicly available contract source code.

![](https://files.readme.io/46f9d55cbb85109adb7f0b7fdd723a3037e5df2d704f9f71c4e889c9484030fb-image.png)

<br />

## 3. Common Issues and Solutions

During the contract verification process, you may encounter the following common issues. Solutions for each type of issue are listed below.

#### 1. How to verify contract files with subdirectory structures?

Note: TRONSCAN currently does not support direct verification of contract files with subdirectory structures. If your contract file structure includes subdirectories (e.g., `contracts/`, `libs/`, etc.), you need to "flatten" the contract before verification, which means merging all dependencies into a single `.sol` file. For specific instructions, please refer to the [TRONSCAN Official Guide](https://support.tronscan.org/hc/en-us/articles/19500651417241-How-to-verify-contracts-with-subdirectory-structures).

#### 2. Unable to perform reCAPTCHA verification

Before clicking "Verify and Publish" to submit contract verification information, TRONSCAN will send you a Google reCAPTCHA component for human identity verification (as shown in the figure below). If this component fails to load normally, it may be the unavailability of Google services due to network reasons. You can check your network connection and try again.

![](https://files.readme.io/ce214a2e5c1487bad21fee0953b5fb2cfe7a65af460f26b35a6a04e5224d3955-image.png)

<br />

#### 3. Verification failed with message: "T.... verification failed. Contract has not been deployed on the network"

This error indicates that the contract address you submitted could not be found on the currently selected network (Mainnet/Nile Testnet/Shasta testnet). Please check:

* Is the contract address correct?
* Is the selected network in the upper right corner of the TRONSCAN page correct (Mainnet/Nile Testnet/Shasta Testnet)?

#### 4. Verification failed with message: "T.... verification failed. Please confirm the correct parameters and try again"

This is the most common error, typically caused by one of the following reasons:

* **Reason One: Mismatched verification parameters**\
  Please ensure that the following parameters are **exactly consistent** with those used when deploying the contract:\
      *Solidity compiler version (note: the distinction between TRON and Ethereum compilers)\&#xA;*   License type\
      *Whether optimization was enabled\&#xA;*   Number of optimization runs

* **Reason Two: Source code mismatch**

  * The uploaded contract source code is different from the code actually deployed (e.g., edited after deployment, missing files)
  * Dependencies were not included
  * The contracts were not flattened before submission

  Solutions:

  * Ensure the uploaded source code is exactly the same as the one used for deployment
  * Include all dependencies
  * Complete [contract flattening](https://support.tronscan.org/hc/en-us/articles/19500651417241-How-to-verify-contracts-with-subdirectory-structures)