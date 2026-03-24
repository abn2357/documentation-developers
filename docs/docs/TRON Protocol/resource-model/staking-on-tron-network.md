---
title: Staking on the TRON network
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
The TRON network has three system resources:

* [Energy](/docs/resource-model#energy)
* [Bandwidth](/docs/resource-model#bandwidth)
* [Voting Right](/docs/resource-model#voting-right)

## How to Stake to Obtain System Resources

Energy and Bandwidth resources can be obtained by account owners through staking, you can refer to [wallet/freezebalancev2](/reference/freezebalancev2-1) to learn how to complete a staking operation through the HTTP API. You can also refer to the [Stake 2.0 Solidity API](/docs/stake-20-solidity-api#freezebalancev2uint-amount-uint-resourcetype) to learn how to complete a staking operation through the contract. 

TRON allocates resources through the staking mechanism. In addition to obtaining Bandwidth or Energy resources, staking TRX can also bring you voting rights (which is TRON Power, TP for short), equal to the amount of TRX staked. Staking 1 TRX, you will get 1 TP. The Energy or Bandwidth resources obtained by staking are used to pay transaction fees, and the obtained voting rights are used to [vote](/reference/votewitnessaccount) for Super Representatives (SRs) to obtain voting rewards.

The unstaking operation will release the corresponding resources.

## How to Delegate Resources

After an account obtains Energy or Bandwidth resources through staking, the account can delegate resources to other addresses through the [delegation operation](/reference/delegateresource-1) or take delegated resources back through the [cancel delegation operation](/reference/undelegateresource-1). Please pay attention to the following situations when delegating resources:

* Only Energy and Bandwidth can be delegated to other addresses. Voting rights cannot be delegated
* Only unused resources that obtained by staking in Stake 2.0 can be delegated to other addresses
* Energy/Bandwidth can only be delegated to an activated external account address, not to a contract address

You can use the [wallet/getcandelegatedmaxsize](/reference/getcandelegatedmaxsize) interface to query the delegable resource share of a certain resource type in an account. A time`lock`and the corresponding `lock_period` can be configured when you delegate resources. If the time `lock` is enabled, after the delegating operation is completed, the resource delegation to the address can only be canceled after the locking period specified by `lock_period` is over. During the lock-up period, if the user delegates the same type of resource to the same address again, the lock-up time of the previous transaction will also be synchronized with the new value. If the time lock is not enabled, the delegation can be canceled immediately after the resource is delegated.

## How to Unstake TRX

After staking your TRX, you can unstake the fund at any time. After initiating the unstaking operation, you need to wait for 14 days before you can withdraw the unstaked TRX into your account. 14 days is [the No.70 parameter](https://tronscan.org/#/sr/committee) of the TRON network, which can be voted on through network governance proposals. You can refer to [unfreezebalancev2](/reference/unfreezebalancev2-1) to learn how to unstake your asset through the HTTP API, and then use [withdrawexpireunfreeze](/reference/withdrawexpireunfreeze) to withdraw the unstaked TRX, which has passed the 14-day pending period, into your account.

Staked TRX can be partially unstaked, but only a maximum of 32 ongoing unstaking operations are allowed at the same time. To be more specific, when a user initiates the first unstaking operation, before TRX of the first unstaking request is available to be withdrawn, the user can only initiate another 31 unstaking operations. You can query the remaining unstaking requests through the [getavailableunfreezecount](/reference/getavailableunfreezecount-1) interface.

Staked TRX of the delegated resources cannot be unstaked. In addition to losing the corresponding resources, the unstaking operation will also cause you to lose the same amount of TP resources.

When you send an unstaking operation and also have unstaked asset that has passed the pending period and is available for withdrawal at the same time, the unstaked asset will be withdrawn to your account along with the unstaking operation. You can use the `[gettransactioninfobyid](/reference/gettransactioninfobyid)` API to query the amount of unstaked TRX that has passed the pending period and been withdrawn, as indicated by the `withdraw_expire_amount` field in the transaction. 

### TRON Power Reclamation

After you unstake the TRX staked in Stake 2.0, the same amount of voting rights will be reclaimed. The system will first reclaim the idle TP in your account. If the idle TP is insufficient, it will continue to reclaim the used TP. If you have voted for multiple SRs, votes will be revoked in proportion from each SR to reclaim the corresponding voting rights. The calculation formula for revoking votes from each SR is as follows,

```
Number of votes revoked from the current super representative = Total number of votes to be revoked * (Number of votes for the current super representative / Total number of votes from this account)
```

For example, suppose User A staked 2,000 TRX and obtained 2,000 TP, of which 1,000 TP has been voted for 2 SRs, 600 votes and 400 votes respectively, and 1,000 idle TP remained in the account. At this time, User A unstakes 1,500 TRX, which means that 1,500 TP needs to be reclaimed from User A's account. In this case, the idle 1,000 TP in the User A’s account will be reclaimed first, and the remaining 500 TP will be reclaimed from the voted TP resources, which is 300 TP and 200 TP respectively from the two SRs. Here's how the votes are calculated:

* Number of votes revoked from SR 1 = 500 \* (600 / 1,000) = 300
* Number of votes revoked from SR 2 = 500 \* (400 / 1,000) = 200

At present, the TRON network uses the Stake 2.0 mechanism, but the resources and votes obtained from Stake 1.0 are still valid. TRX staked in Stake 1.0 can still be withdrawn through the [Stake 1.0 API](/reference/account-resources-unfreezebalance), but it should be noted that if the TRX staked in Stake 1.0 is unstaked, all votes of the account will be revoked.

## How to Cancel All Ongoing Unstaking Operations

Stake 2.0 allows users to cancel all unstaking operations after the user submits the operations, which will make the asset be staked again to obtain corresponding resources, without having to wait for the unstaking funds to pass the pending period before being withdrawn to the account and staked again. You can refer to [cancelallunfreezev2](/reference/cancelallunfreezev2) to learn how to cancel all unstaking operations through the HTTP API.

When you cancel unstaking operations, all unstaking funds still in the pending period will be re-staked, and the resources obtained through re-staking remain the same as before. Unstaking operations that have passed the 14-day pending period cannot be canceled, and this part of unstaked funds will be automatically withdrawn to your account along with the cancel-unstaking transaction. You can query the amount of TRX involved in the unstaking requests that have been canceled (`cancel_unfreezeV2_amount`), and the amount of unstaked TRX that has passed the pending period and been withdrawn (`withdraw_expire_amount`) in the transaction through the `gettransactioninfobyid` interface. 

## APIs

The following table shows the interfaces of the staking model and their descriptions:

| API                                                                                   | Description                                                                                              |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [freezebalancev2](/reference/freezebalancev2-1)                                       | Stake TRX                                                                                                |
| [unfreezebalancev2](/reference/unfreezebalancev2-1)                                   | Unstake TRX                                                                                              |
| [unfreezebalance](/reference/account-resources-unfreezebalance)                       | Unstake TRX staked in Stake 1.0                                                                          |
| [delegateresource](/reference/delegateresource-1)                                     | Delegate resources                                                                                       |
| [undelegateresource](/reference/undelegateresource-1)                                 | Cancel resource delegation                                                                               |
| [withdrawexpireunfreeze](/reference/withdrawexpireunfreeze)                           | Withdraw unstaked asset                                                                                  |
| [getavailableunfreezecount](/reference/getavailableunfreezecount-1)                   | Query the remaining times of submitting unstaking operations                                             |
| [getcanwithdrawunfreezeamount](/reference/getcanwithdrawunfreezeamount-1)             | Query the withdrawable balance                                                                           |
| [getcandelegatedmaxsize](/reference/getcandelegatedmaxsize)                           | Query the amount of delegable resource share of a specific resource type                                 |
| [getdelegatedresourcev2](/reference/getdelegatedresourcev2)                           | Query the amount of resources delegated by fromAddress to toAddress                                      |
| [getdelegatedresourceaccountindexv2](/reference/getdelegatedresourceaccountindexv2-1) | Query the resource delegation index of an account                                                        |
| [getaccount](/reference/account-getaccount)                                           | Query the account staking status,  resources share, unstaking status, and voting status                  |
| [getaccountresource](/reference/getaccountresource)                                   | Query the total amount of resources, the amount of resources used, and the amount of resources available |
| [cancelallunfreezev2](/reference/cancelallunfreezev2)                                 | Cancel all ongoing unstaking                                                                             |
