---
title: GetChainParameters
excerpt: >-
  Retrieve all parameters that can be configured by the blockchain committee
  along with their values.
api:
  file: full-node-http-api.json
  operationId: wallet-getchainparameters
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

chainParameter - ChainParameters[]: List of dynamic chain parameter objects. Each dynamic parameter contains the following fields:

| Field | Type   | Description      |
| :---- | :----- | :--------------- |
| key   | string | Parameter name.  |
| value | int64  | Parameter value. |

The following table introduces the meaning of each dynamic parameter:

| ID | Parameter Name                          | Description                                                                                                                                  | Current Value         |
| :- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
| 0  | getMaintenanceTimeInterval              | The maintenance time interval.                                                                                                               | 6 Hour                |
| 1  | getAccountUpgradeCost                   | The fee required for an account to become a Super Representative (SR).                                                                       | 9999 TRX              |
| 2  | getCreateAccountFee                     | The fee burned to pay for Bandwidth when the account creator does not have sufficient staked Bandwidth for the account creation transaction. | 0.1 TRX               |
| 3  | getTransactionFee                       | Bandwidth unit price.                                                                                                                        | 0.001 TRX             |
| 4  | getAssetIssueFee                        | The fee for issuing a TRC-10 token.                                                                                                          | 1024 TRX              |
| 5  | getWitnessPayPerBlock                   | SR block generation reward.                                                                                                                  | 8 TRX                 |
| 6  | getWitnessStandbyAllowance              | The rewards distributed among the top 27 SRs and the following 100 partners; currently deprecated.                                           | 115200 TRX            |
| 7  | getCreateNewAccountFeeInSystemContract  | The fee for activating a new account via the system contract.                                                                                | 1 TRX                 |
| 9  | getAllowCreationOfContracts             | Activate the Virtual Machine.                                                                                                                | 1                     |
| 10 | getRemoveThePowerOfTheGr                | Propose to remove the GR Genesis votes.                                                                                                      | 1                     |
| 11 | getEnergyFee                            | Energy unit price.                                                                                                                           | 0.0001 TRX            |
| 12 | getExchangeCreateFee                    | The cost of trading pair creation.                                                                                                           | 1024 TRX              |
| 13 | getMaxCpuTimeOfOneTx                    | The maximum execution time of one transaction.                                                                                               | 80 ms                 |
| 14 | getAllowUpdateAccountName               | Propose to allow duplicate account names.                                                                                                    | 0                     |
| 15 | getAllowSameTokenName                   | Propose to allow duplicate TRC-10 token names.                                                                                               | 1                     |
| 16 | getAllowDelegateResource                | Propose to allow resource delegation.                                                                                                        | 1                     |
| 17 | getTotalEnergyLimit                     | Currently deprecated.                                                                                                                        | 180000000000          |
| 18 | getAllowTvmTransferTrc10                | Propose to allow the TRC-10 token transfer in smart contracts                                                                                | 1                     |
| 19 | getTotalEnergyCurrentLimit              | Propose to modify the total Energy limit                                                                                                     | 180000000000 ENERGY   |
| 20 | getAllowMultiSign                       | Proposes to enable the multi-signature feature.                                                                                              | 1                     |
| 21 | getAllowAdaptiveEnergy                  | Propose to allow adaptive adjustment for total Energy.                                                                                       | 0                     |
| 22 | getUpdateAccountPermissionFee           | The fee for updating account permission.                                                                                                     | 100 TRX               |
| 23 | getMultiSignFee                         | The fee for multi-signature.                                                                                                                 | 1 TRX                 |
| 24 | getAllowProtoFilterNum                  | Propose to enable protocol optimization.                                                                                                     | 0                     |
| 26 | getAllowTvmConstantinople               | Propose to support Constantinople Upgrade for TVM.                                                                                           | 1                     |
| 29 | getAdaptiveResourceLimitMultiplier      | Propose to modify the adaptive Energy limit.                                                                                                 | 1000                  |
| 30 | getChangeDelegation                     | Propose to support the decentralized vote dividend.                                                                                          | 1                     |
| 31 | getWitness127PayPerBlock                | Propose to modify the block voting rewards given to the top 27 SRs and the following 100 partners.                                           | 128 TRX               |
| 32 | getAllowTvmSolidity059                  | Propose to allow TVM to support Solidity 0.5.9.                                                                                              | 1                     |
| 33 | getAdaptiveResourceLimitTargetRatio     | Propose to modify the adaptive Energy limit target.                                                                                          | 10                    |
| 35 | getForbidTransferToContract             | Proposes to prohibit the transfer of TRX and TRC10 tokens to smart contracts via `TransferContract` or `TransferAssetContract`.              | 0                     |
| 39 | getAllowShieldedTRC20Transaction        | Proposes to enable the verification of zero-knowledge proofs (ZKP) within the TVM (Shielded TRC20).                                          | 1                     |
| 40 | getAllowPBFT                            | Propose to enable PBFT consensus.                                                                                                            | 0                     |
| 41 | getAllowTvmIstanbul                     | Propose to enable TVM Istanbul instruction.                                                                                                  | 1                     |
| 44 | getAllowMarketTransaction               | Propose to allow enabling DEX.                                                                                                               | 0                     |
| 45 | getMarketSellFee                        | Propose to modify fees for creating orders on DEX.                                                                                           | 0                     |
| 46 | getMarketCancelFee                      | Propose to modify fees for cancelling orders on DEX.                                                                                         | 0                     |
| 47 | getMaxFeeLimit                          | Proposes to modify the upper fee limit for a single smart contract transaction.                                                              | 15000 TRX             |
| 48 | getAllowTransactionFeePool              | Proposal to open reward pool for transaction fee.                                                                                            | 0                     |
| 49 | getAllowOptimizeBlackHole               | Proposal to optimize black hole accounts.                                                                                                    | 1                     |
| 51 | getAllowNewResourceModel                | Propose to enable the new resource model.                                                                                                    | 0                     |
| 52 | getAllowTvmFreeze                       | Propose to enable the function to stake/unstake balance in contracts during stake1.0 period.                                                 | 0                     |
| 53 | getAllowAccountAssetOptimization        | Propose to enable the optimization of account assets.                                                                                        | 0                     |
| 59 | getAllowTvmVote                         | Propose to enable TVM contract voting.                                                                                                       | 1                     |
| 60 | getAllowTvmCompatibleEvm                | Propose to initiate EVM-compatible mode for TVM.                                                                                             | 0                     |
| 61 | getFreeNetLimit                         | Propose to modify the upper limit of free Bandwidth for each account.                                                                        | 600 Bandwidth         |
| 62 | getTotalNetLimit                        | Proposes to modify the upper limit of total Bandwidth available from stake.                                                                  | 43200000000 Bandwidth |
| 63 | getAllowTvmLondon                       | Propose to support London Upgrade for TVM.                                                                                                   | 1                     |
| 65 | getAllowHigherLimitForMaxCpuTimeOfOneTx | Propose to allow raising the maximum of MaxCpuTimeOfOneTx net parameters to 400.                                                             | 1                     |
| 66 | getAllowAssetOptimization               | Propose to enable account asset optimization.                                                                                                | 1                     |
| 67 | getAllowNewReward                       | Propose to enable an optimized reward computing algorithm.                                                                                   | 1                     |
| 68 | getMemoFee                              | The memo fee.                                                                                                                                | 1 TRX                 |
| 69 | getAllowDelegateOptimization            | Propose to enable the delegate storage optimization.                                                                                         | 1                     |
| 70 | getUnfreezeDelayDays                    | Proposes to set the unstaking lock-up days (delay period) for the Stake 2.0 mechanism.                                                       | 14                    |
| 71 | getAllowOptimizedReturnValueOfChainId   | Propose to allow optimizing the return value of the chainid command.                                                                         | 1                     |
| 72 | getAllowDynamicEnergy                   | Propose to allow enabling the dynamic energy model.                                                                                          | 1                     |
| 73 | getDynamicEnergyThreshold               | Propose to modify the threshold of the dynamic energy model.                                                                                 | 5000000000            |
| 74 | getDynamicEnergyIncreaseFactor          | Propose to modify the increase factor (in basis points) of the dynamic energy model.                                                         | 2000                  |
| 75 | getDynamicEnergyMaxFactor               | Propose to modify the maximum increase factor (in basis points) of the dynamic energy model.                                                 | 34000                 |
| 76 | getAllowTvmShangHai                     | Propose to allow TVM to support Shanghai upgrade.                                                                                            | 1                     |
| 77 | getAllowCancelAllUnfreezeV2             | Propose to allow cancellation of all unstaking requests..                                                                                    | 1                     |
| 78 | getMaxDelegateLockPeriod                | Propose to allow optimization of delegating resource lock and set the maximum lock period (number of blocks).                                | 864000                |
| 79 | getAllowOldRewardOpt                    | Propose to allow the optimization of the reward withdrawal algorithm for Phase 1.                                                            | 1                     |
| 81 | getAllowEnergyAdjustment                | Propose to allow the adjustment on Energy consumption of TVM instructions.                                                                   | 1                     |
| 82 | getMaxCreateAccountTxSize               | Propose to allow setting an upper limit (in bytes) for the size of account creation transactions.                                            | 1000                  |
| 87 | getAllowStrictMath                      | Propose to migrate operation from java.lang.Math to java.lang.StrictMath for cross-platform computational consistency.                       | 1                     |
| 88 | getConsensusLogicOptimization           | Enable verification of transaction limitations at the consensus layer.                                                                       | 1                     |
| 89 | getAllowTvmBlob                         | Allow introducing `BLOBHASH` and `BLOBBASEFEE` transaction instructions as stubs.                                                            | 1                     |
| 92 | getProposalExpireTime                   | The expiration time of proposal.                                                                                                             | 259200000             |
| 94 | getAllowTvmSelfdestructRestriction      | Enable `SELFDESTRUCT` instruction restriction (compatible with EIP-6780).                                                                    | 0                     |

<br />
