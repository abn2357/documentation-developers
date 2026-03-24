---
title: Developer Energy Cost Protection
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
# Developer Origin Energy Limit

It is highly recommended to set an appropriate developer origin energy limit before deploying a contract to Mainnet. If a contract uses a low user energy pay ratio (developer pays most energy), but suffers from attacks/vulnerabilities as described in previous sections, the developer should set an *origin\_energy\_limit* during deployment. Regardless of the attack type, the developer will not use more than *origin\_energy\_limit* (in Energy) for each smart contract execution. This parameter prevents malicious attacks and fee penalties set by *fee\_limit*. Each execution is limited to this amount of energy maximum. By default, contracts deployed without this parameter (including legacy contracts before this feature was enabled) are set to 1e10 Energy. Setting it to a value larger than 1e10 produces an error.

This value can be set in Tron-Box and Tron-Web:

### Tron-Box

For Tron-Box smart contract deployment, all global settings are in the **tronbox.js** file. Within this file, there is a parameter called *originEnergyLimit*, which refers to the developer origin energy limit.

```javascript
module.exports = {
  networks: {
    development: {
      from: 'TPL66VK2gCXNCD7EJg9pgJRfqcRazjhUZY',
      privateKey: 'da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0',
      consume_user_resource_percent: 30,
      feeLimit: 1e9,
      originEnergyLimit: 1e7,  // Set origin energy limit
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: "*" // Match any network id
    },
  }
};
```

### Tron-Web

The *tronweb.contract.new* API call takes in a parameter called *originEnergyLimit*. This parameter refers to the developer origin energy limit.

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
    originEnergyLimit: 1e7,  // Set origin energy limit
    parameters: [param1, param2, param3, ...]
  })
  console.log(contract_instance.address);
}
deploy_contract();
```

# Updating Developer Origin Energy Limit

After a contract deploys, it's developer origin energy limit can be adjusted through the [updateEnergyLimit](ref:updateenergylimit) endpoint. Sign & broadcast the call to ensure it takes effect.
