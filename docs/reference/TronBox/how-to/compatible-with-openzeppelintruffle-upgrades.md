---
title: Compatible-with-Openzeppelin-upgrades
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
**TronBox packages for deploying and managing upgradable contracts.** TronBox is compatible with the migration and testing functions in this package, so you may use TronBox to deploy proxies for your contracts.

## Installation

```js
npm install --save-dev @openzeppelin/truffle-upgrades
```

Using `@openzeppelin/truffle-upgrades` in TronBox requires TronBox V3.2.0 or later.

## Usage in migrations

### Deploying Proxies

Use the `deployProxy` function to deploy an upgradable instance of one of your contracts in your migrations. `deployProxy` supports `UUPS(Universal Upgradeable Proxy Standard)` and `transparent` proxies.

> Note: To adapt to the `deployProxy` function, please first set `deployer.trufflePlugin` to `true`.

```js
// migrations/NN_deploy_upgradeable_box.js
const { deployProxy } = require('@openzeppelin/truffle-upgrades');

const Box = artifacts.require('Box');

module.exports = async function (deployer) {
  try {
    // Setup tronbox deployer
    deployer.trufflePlugin = true;
    const instance = await deployProxy(Box, [42], { deployer });
    console.info('Deployed', instance.address);

    // Call proxy contract
    const box = await Box.deployed();
    const beforeValue = await box.value();
    console.info('Value before', beforeValue.toNumber());

    // Set new Value
    await box.setValue(beforeValue.toNumber() + 100);
    const afterValue = await box.value();
    console.info('Value after', afterValue.toNumber());
  } catch (error) {
    console.error('Transparent: deploy box error', error);
  }
};
```

`deployProxy` will automatically check that the `Box` contract is upgrade-safe, deploy an implementation contract for the `Box` contract (unless there is one already from a previous deployment), create and deploy a proxy contract, and initialize it by calling `initialize(42)`. In the case of `transparent` proxies, a ProxyAdmin contract will also be created and deployed.

### Deploying proxies in the Beacon mode

The beacon proxy mode allow multiple proxy contracts to share the same logic implementation by referencing the beacon contract. TronBox is also compatible with the beacon proxy mode, therefore can be used to deploy beacon proxy contracts.

Use `deployBeacon` to deploy the beacon management contract, which is a central contract for managing multiple contracts that implement the same interface.

Use `deployBeaconProxy` to deploy one or more beacon proxy contracts and point them to the beacon contract for upgrade and maintenance.

> Note: To adapt to the `deployBeacon` and `deployBeaconProxy` functions, please first set `deployer.trufflePlugin` to `true`.

```js
// migrations/NN_deploy_upgradeable_box.js
const { deployBeacon, deployBeaconProxy } = require('@openzeppelin/truffle-upgrades');

const Box = artifacts.require('Box');

module.exports = async function (deployer) {
  try {
    // Setup tronbox deployer
    deployer.trufflePlugin = true;
    const beacon = await deployBeacon(Box, { deployer });
    console.info('Beacon deployed', beacon.address);
    const instance = await deployBeaconProxy(beacon, Box, [42], { deployer });
    console.info('Deployed', instance.address);

    // Call proxy contract
    const box = await Box.deployed();
    const beforeValue = await box.value();
    console.info('Value before', beforeValue.toNumber());

    // Set new Value
    await box.setValue(beforeValue.toNumber() + 100);
    const afterValue = await box.value();
    console.info('Value after', afterValue.toNumber());
  } catch (error) {
    console.error('Beacon: deploy box error', error);
  }
};
```

## About upgradeProxy

TronBox is not yet compatible with using the `upgradeProxy` function to upgrade a deployed instance to a new version. If you need to upgrade an instance of a proxy contract, please refer to the following example to deploy a new `BoxV2` implementation contract, and upgrade an existing proxy to the new implementation.

### UUPS

```js
// migrations/MM_upgrade_uups_box.js
const TransparentUpgradeableProxy = artifacts.require(
  '@openzeppelin/upgrades-core/artifacts/@openzeppelin/contracts/proxy/transparent/TransparentUpgradeableProxy.sol/TransparentUpgradeableProxy.json'
);
const Box = artifacts.require('UUPSBox');
const BoxV2 = artifacts.require('UUPSBoxV2');

module.exports = async function (deployer) {
  try {
    // Deploy the new BoxV2 implementation contract
    await deployer.deploy(BoxV2);

    // Upgrade proxy contract
    const proxyContract = await TransparentUpgradeableProxy.at(Box.address);
    await proxyContract.upgradeTo(BoxV2.address);
    console.info('Upgraded', Box.address);

    // Call proxy contract
    const box = await BoxV2.at(Box.address);
    const beforeValue = await box.value();
    console.info('Value before', beforeValue.toNumber());

    // Set new Value
    await box.setValue(beforeValue.toNumber() + 100);
    const afterValue = await box.value();
    console.info('Value after', afterValue.toNumber());

    // Read new V2 Value
    const beforeValueV2 = await box.valueV2();
    console.info('ValueV2 before', beforeValueV2.toNumber());

    // Set new V2 Value
    await box.setValueV2(beforeValueV2.toNumber() + 100);
    const afterValueV2 = await box.valueV2();
    console.info('ValueV2 after', afterValueV2.toNumber());
  } catch (error) {
    console.error('UUPS: upgrade box error', error);
  }
};
```

### Transparent

```js
// migrations/MM_upgrade_transparent_box.js
const { admin } = require('@openzeppelin/truffle-upgrades');
const ProxyAdmin = artifacts.require(
  '@openzeppelin/upgrades-core/artifacts/@openzeppelin/contracts/proxy/transparent/ProxyAdmin.sol/ProxyAdmin.json'
);
const Box = artifacts.require('TransparentBox');
const BoxV2 = artifacts.require('TransparentBoxV2');

module.exports = async function (deployer) {
  try {
    // Deploy the new BoxV2 implementation contract
    await deployer.deploy(BoxV2);

    // Upgrade proxy contract by admin
    const adminIns = await admin.getInstance();
    const adminContract = await ProxyAdmin.at(adminIns.address);
    await adminContract.upgrade(Box.address, BoxV2.address);
    console.info('Upgraded', Box.address);

    // Call proxy contract
    const box = await BoxV2.at(Box.address);
    const beforeValue = await box.value();
    console.info('Value before', beforeValue.toNumber());

    // Set new Value
    await box.setValue(beforeValue.toNumber() + 100);
    const afterValue = await box.value();
    console.info('Value after', afterValue.toNumber());

    // Read new V2 Value
    const beforeValueV2 = await box.valueV2();
    console.info('ValueV2 before', beforeValueV2.toNumber());

    // Set new V2 Value
    await box.setValueV2(beforeValueV2.toNumber() + 100);
    const afterValueV2 = await box.valueV2();
    console.info('ValueV2 after', afterValueV2.toNumber());
  } catch (error) {
    console.error('Transparent: upgrade box error', error);
  }
};

```

### Beacon

When the beacon is upgraded, all of the beacon proxies that point to it will use the new contract implementation.

```js
// migrations/MM_upgrade_beacon_box.js
const UpgradeableBeacon = artifacts.require(
  '@openzeppelin/upgrades-core/artifacts/@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol/UpgradeableBeacon.json'
);
const { erc1967 } = require('@openzeppelin/truffle-upgrades');

const Box = artifacts.require('BeaconBox');
const BoxV2 = artifacts.require('BeaconBoxV2');

module.exports = async function (deployer) {
  try {
    // Deploy the new BoxV2 implementation contract
    await deployer.deploy(BoxV2);
    const beaconAddress = await erc1967.getBeaconAddress(Box.address);

    // Upgrade proxy contract
    const proxyContract = await UpgradeableBeacon.at(beaconAddress);
    await proxyContract.upgradeTo(BoxV2.address);
    console.info('Upgraded', Box.address);

    // Call proxy contract
    const box = await BoxV2.at(Box.address);
    const beforeValue = await box.value();
    console.info('Value before', beforeValue.toNumber());

    // Set new Value
    await box.setValue(beforeValue.toNumber() + 100);
    const afterValue = await box.value();
    console.info('Value after', afterValue.toNumber());

    // Read new V2 Value
    const beforeValueV2 = await box.valueV2();
    console.info('ValueV2 before', beforeValueV2.toNumber());

    // Set new V2 Value
    await box.setValueV2(beforeValueV2.toNumber() + 100);
    const afterValueV2 = await box.valueV2();
    console.info('ValueV2 after', afterValueV2.toNumber());
  } catch (error) {
    console.error('Beacon: upgrade box error', error);
  }
};

```
