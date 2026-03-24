---
title: User/Developer Energy Pay Ratio
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
# User Energy Pay Ratio

It is highly recommended to set an appropriate user energy pay ratio before deploying a contract to the Mainnet. The user energy pay ratio is defined as the energy cost ratio of smart contract execution the user pays vs. what the developer pays. For example, if the user energy pay ratio is set at 60, then the user pays 60% of the execution energy, and the developer (contract owner) pays the remaining 40%. This parameter accepts an integer between 0 and 100, inclusively. A high user energy pay ratio is recommended in case users attack the contract and drain the owner's account. 

This value can be set in both Tron-Box and Tron-Web:

### Tron-Box

For Tron-Box smart contract deployment, all global settings are in the **tronbox.js** file. Within this file, there is a parameter called *consume\_user\_resource\_percent*, which refers to the user energy pay ratio.

```javascript
module.exports = {
  networks: {
    development: {
      from: 'TPL66VK2gCXNCD7EJg9pgJRfqcRazjhUZY',
      privateKey: 'da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0',
      consume_user_resource_percent: 30,  // Set user energy pay ratio
      feeLimit: 1e9,
      originEnergyLimit: 1e7,
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: "*" // Match any network id
    },
  }
};
```

### Tron-Web

The *tronweb.contract.new* API call takes in a parameter called *userFeePercentage*. This parameter refers to the user energy pay ratio.

```javascript
let abi = 'abi';
let code = 'bytecode';
async function deploy_contract() {
  let contract_instance = await tronWeb.contract().new({
    abi: JSON.parse(abi),
    bytecode: code,
    feeLimit: 1e9,
    callValue: 0,
    userFeePercentage: 30,
    originEnergyLimit: 1e7,
    parameters: [param1, param2, param3, ...]
  })
  console.log(contract_instance.address);
}
deploy_contract();
```

# Updating User Energy Pay Ratio

After a contract deploys, it's user energy pay ratio can be adjusted through the [updateSetting](ref:updatesetting) endpoint. Make sure to sign & broadcast this call to take effect.
