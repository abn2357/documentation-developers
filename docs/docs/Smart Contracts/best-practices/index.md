---
title: Best Practices
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Introduction

This document dives into the knowledge base of security considerations for TRON developers. For any new findings, feel free to contribute by using the suggest edits button.    

# Contents

<br/>

**How to write a Smart Contract smartly to optimize energy:**\
When writing smart contracts, especially on networks like TRON, it’s crucial to consider energy optimization techniques. Energy costs money—so the less energy your contract consumes, the more cost-effective it is for you and your users. In this tutorial, we’ll cover a series of best practices and patterns to help you optimize energy usage and write more efficient Solidity code.

***

1. Use calldata Instead of memory for Function Parameters when possible\
   Concept:\
   Function parameters that are arrays or strings can be declared as memory or calldata. Declaring them as calldata is often cheaper because calldata parameters are read-only references directly to the call data, rather than allocating new memory. One limitation is that you cannot modify a calldata parameter inside the function, unlike memory parameters.\
   Why It Saves Energy:\
   calldata reduces the amount of copying and storage needed, as it references the input data directly.\
   Example: 

   ![](https://files.readme.io/429fb4f2e15d650149a0de91d2fe3ab2a0b0108b0934d1c0c932c0488b4ab3a4-image.png)

***

2. Pack Variables to Optimize Storage\
   Concept:\
   Storage in Solidity is organized in 32-byte slots. Multiple smaller variables (like uint8, bool) can be packed into a single 32-byte slot if they are declared consecutively. By carefully ordering variables, you reduce the total number of storage slots needed, directly saving energy.\
   Why It Saves Energy:\
   Each storage slot costs energy to read and write. Fewer storage slots used = lower energy costs.\
   Example:

   ![](https://files.readme.io/58e71a6973d515aa47d8ef8063824d8099fdbed4d462b5401fa086e1b1714715-image.png)

![](https://files.readme.io/1a8e1626d2b8383735259f61ef17b97c3349651e910ba22057f45c56834bdb7a-image.png)

***

3. Delete Unused Variables Rather Than Setting to Zero\
   Concept:\
   When a variable is no longer needed, use delete variableName; instead of assigning it to zero. The delete operation resets the variable to its default value—zero for numeric types—and may result in an energy refund. In contrast, just setting the variable to zero still consumes energy without offering this refund.\
   Why It Saves Energy:\
   Storage refunds are given when you clear storage. Using delete can be slightly more energy-efficient.\
   Example: 

   ![](https://files.readme.io/24c05ce6bbc7e2dc22f3bc656284f39986d183394f45ab8fcaf9b0348cc32f7c-image.png)

***

4. Don’t Shrink Variables Without Need\
   Concept:\
   If you’re not packing variables together, using smaller data types (like uint8 or uint128) does not necessarily save energy. In fact, sometimes using full uint256 is cheaper because the TVM operates on 256-bit words natively. Also, converting between smaller and larger types can add overhead.\
   Why It Saves Energy:\
   Using the default uint (which is uint256) can avoid unnecessary conversion instructions and is often simpler and cheaper unless you’re explicitly packing variables.\
   Example: 

   ![](https://files.readme.io/e5e40a2db898841ba17013f1cd2797916470c92589ac064441001d905143fa11-image.png)

***

5. Use Events Instead of On-Chain Storage When Possible\
   Concept:\
   If you want to record some information for later reference, but don’t need to read it back on-chain, using events is cheaper than using on-chain storage. Events are stored in the transaction logs which are cheaper and don’t consume permanent storage space.\
   Why It Saves Energy:\
   On-chain storage is the most expensive operation in Solidity. Events, while still costing some energy, are far cheaper than storage writes.\
   Example: 

   ![](https://files.readme.io/d0e0618f9acc71377452d2356eef4b286e547f43d6e84dfa6acebc78428238d4-image.png)

***

6. Use Libraries for Repeated Code\
   Concept:\
   If you have multiple contracts using the same math functions, put these functions in a library and link the library to the contracts. This reduces duplicate code and potentially saves energy if the function is reused many times.\
   Why It Saves Energy:\
   Libraries can help centralize code, and when deployed once, you don’t need to redeploy or replicate code multiple times.\
   Note: Whether this saves energy depends on your usage pattern. If you have many contracts calling the same code, a library can be beneficial.\
   Example: 

   ![](https://files.readme.io/635ba086aaf6c6c5d0b11a2b255166a9c1f1360db4bc178706f40cc3850a83d3-image.png)

***

7. Short-Circuiting in Boolean Operations\
   Concept:\
   In Solidity, the && and || operators will stop evaluating as soon as they know the final outcome. This is known as 'short-circuiting.\
   Why It Saves Energy:\
   By placing the condition that most likely returns false first in an &&, or the condition that likely returns true first in an ||, you minimize unnecessary function calls.\
   Example1: 

   ![](https://files.readme.io/9e56fe5359793850beade79c5899b9a06f0c60c42bae288b06f940938270d2e1-image.png)

Example2: 

![](https://files.readme.io/d182394f3e3b396130db79f04e3ea0d4c3b7d849f83b18cc9a6c0c929b0814ab-image.png)

***

8. Avoid Assignments Unless Needed\
   Concept:\
   Initializing variables or assigning values that are never used wastes energy. Only assign if you actually need the value.\
   Why It Saves Energy:\
   Each assignment costs energy. Avoiding unnecessary assignments reduces energy usage.\
   Example: 

   ![](https://files.readme.io/72ea2ff61adc51f5c46e3b05c3fb10934cb0fc307102b2ef828fa3eb904f5cbf-image.png)

***

9. Minimize Operations on Storage Variables Inside Loops\
   Concept:\
   Reading and writing storage variables is expensive. Doing it inside a loop is even more costly. Instead, load the value into a memory variable, work with it, and then write it back once.\
   Why It Saves Energy:\
   Fewer storage operations mean lower energy usage.\
   Example: 

   ![](https://files.readme.io/bf1a4a2663dda4a13ac52a36e9a24f180abc4b90c2c156523ca7389368816613-image.png)

***

10. Use Fixed-Size Rather Than Dynamic-Size Arrays Where Possible\
    Concept:\
    Fixed-size arrays are cheaper to handle than dynamic arrays, as dynamic arrays involve additional overhead for managing size and potential resizing.\
    Why It Saves Energy:\
    Less overhead for managing array length and resizing means fewer operations and hence lower energy.\
    Example: 

    ![](https://files.readme.io/0368603ddb5e1c84b028d14212d570ee292f8e7d2a9d5bb836fa4223dfd8faf3-image.png)

***

11. Prefer mapping Over Arrays If Possible\
    Concept:\
    mapping lookups are cheaper than array operations in some cases, especially if you need to store sparse data or just keyed lookups without iteration.\
    Why It Saves Energy:\
    Mappings provide constant-time lookups without maintaining indexing overhead.\
    Example: 

    ![](https://files.readme.io/6a695e321763b4dc4c6d2076843857fe063b720b672fff97637aaca4021aaafd-image.png)

***

12. Use bytes Instead of string Where Possible\
    Concept:\
    Strings are expensive because they are essentially dynamic arrays of bytes. If you don’t need human-readable text and only store binary data, use bytes. Even if you need to store ASCII text, if it’s processed as raw data, bytes may be more optimal.\
    Why It Saves Energy:\
    Working directly with bytes removes unnecessary conversion and formatting layers. This streamlined approach can lower processing requirements, which in turn reduces energy consumption over time.\
    Example: 

    ![](https://files.readme.io/62a87a8f55b817147c94a3c2ea73d504ca7c0a80311006f3866fdd793625b068-image.png)

***

13. Use external or internal Over public When Possible\
    Concept:\
    Functions marked as public can be called both internally and externally. If your function is never called internally, use external. If your function is never called externally, use internal. External functions are sometimes cheaper when called from outside the contract, as they do not require a wrapper function to be generated.\
    Why It Saves Energy:\
    External/internal function calls can save energy by allowing the TVM to read directly from calldata without copying arguments into memory.\
    Example: 

    ![](https://files.readme.io/44b5c23e7fdc0748dfc72f3e53a6248f1a155fa01132d1e5244260d971dc14a8-image.png)

***

<br/>

* <a href="https://developers.tron.network/docs/userdeveloper-energy-pay-ratio">User/Developer Energy Pay Ratio</a> describes how to prevent account draining attacks. 

* <a href="https://developers.tron.network/docs/setting-a-fee-limit-on-deployexecution">Fee Limit on Deploy/Execution</a> describes range limits and where to set limit. 

* <a href="https://developers.tron.network/docs/frozen-energy-and-fee-limit-model">Stake TRX for Energy and Out of Energy</a> describes the maximum energy limit formula and its applications. 

* <a href="https://developers.tron.network/docs/timeout-and-infinite-loop-pitfalls">Timeout and Infinite Loop Pitfalls</a> guides developers on how to best avoid these pitfalls. 

* <a href="https://developers.tron.network/docs/illegal-operations-and-penalties">Illegal Operations and Penalties</a> describes how invalid operation codes could be triggered, and best practices to avoid it. 

* <a href="https://developers.tron.network/docs/non-existent-account-transfers-and-penalties">Non-Existent Account Transfers and Penalties</a> describes how to avoid the non-existent account transfer penalty. 

* <a href="https://developers.tron.network/docs/developer-energy-cost-protection">Developer Energy Cost Protection</a> describes the Developer Origin Energy Limit parameter, its purpose, and how to set this parameter. 

* <a href="https://developers.tron.network/docs/fallback-functions">Fallback Functions</a> guides developers on the implementation of this class of functions within smart contracts.