---
title: Fee Limit on Deploy/Execution
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
# Fee Limit

It is highly recommended to set an appropriate fee limit before deploying a contract to Mainnet. The fee limit refers to the upper limit of the smart contract deploy/execution cost, in TRX. See [Energy](doc:energy) for energy cost models. This limit is measured in sun, which is 1TRX=1e6sun. The maximum limit is 10000 TRX, or 1e10sun. Setting it to a value larger than 1e10 will produce an error.

When deploying large contracts or running complex functions, this limit may need to be increased up to 10000 TRX. However, check out timeouts, infinite loops, illegal operations, and non-existent account transfer sections are why setting a higher limit may sometimes be bad practice.

This value can be set in both Tron-Box and Tron-Web:

### Tron-Box

For Tron-Box smart contract deployment, all global settings are in the **tronbox.js** file. Within this file, there is a parameter called *feeLimit*, which refers to the fee limit.

```javascript
module.exports = {
  networks: {
    development: {
      from: 'TPL66VK2gCXNCD7EJg9pgJRfqcRazjhUZY',
      privateKey: 'da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0',
      consume_user_resource_percent: 30,
      feeLimit: 1e10,  // Set fee limit
      originEnergyLimit: 1e7,
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: "*" // Match any network id
    },
  }
};
```

### Tron-Web

The *tronweb.contract.new* API call takes in a parameter called *feeLimit*. This parameter refers to the fee limit.

```javascript
let abi = 'abi';
let code = 'bytecode';
async function deploy_contract() {
  let contract_instance = await tronWeb.contract().new({
    abi: JSON.parse(abi),
    bytecode: code,
    feeLimit: 1e10,  // Set fee limit
    callValue: 0,
    userFeePercentage: 30,
    originEnergyLimit: 1e7,
    parameters: [param1, param2, param3, ...]
  })
  console.log(contract_instance.address);
}
deploy_contract();
```
