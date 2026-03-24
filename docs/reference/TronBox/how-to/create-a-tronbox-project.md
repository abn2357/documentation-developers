---
title: Create a TronBox Project
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
Most of the TronBox commands are run under the directories of TronBox projects.  So the first step is to create a TronBox project.  You can create a bare project, but for those getting started, you can use `TronBox Boxes`, which offers example applications and project templates.  We'll use the     `MetaCoin box`, which creates a token that can be transferred between accounts.

1. Create a directory for MetaCoin:

```
mkdir MetaCoin

cd MetaCoin
```

2. Download ("unbox") the MetaCoin project:

```
tronbox unbox metacoin
```

```
You can create a bare project without smart contracts using `tronbox init`.
```

Once this operation is completed, you will have a project directory structure with the following items:

* `contracts/`: [Directory for Solidity contracts](https://developers.tron.network/reference/interact-with-a-contract) 
* `migrations/`:  [Directory for scriptable deployment files](https://developers.tron.network/reference/contract-deploymentmigrations)
* `test/`: Directory for test files for testing your applications and contracts. For more information, refer to [How to test contracts?](https://developers.tron.network/reference/test-your-contracts)
* `tronbox.js`: [TronBox configuration file](https://developers.tron.network/reference/tronbox-configuration)
