---
title: Stake 2.0 Solidity APIs
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
With Stake 2.0 integrated into the TVM, users can perform staking/unstaking, delegating/undelegating, voting, and claiming voting rewards operations in the smart contract. The following content introduces Solidity APIs related to Stake 2.0.

## freezebalancev2(uint amount, uint resourceType)

**Description:** Stake TRX to obtain TRON Power (TP, i.e. voting rights) and Bandwidth or Energy. If the operation fails, the revert exception will be thrown.

**Params:**

* amount — the amount of TRX to be staked (unit: sun)
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** N/A

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event BalanceFreezedV2(uint, uint);

    // stake 1 TRX to obtain energy
    function example() external {
        freezebalancev2(1000000, 1);
        emit BalanceFreezedV2(1000000, 1);
    }
}
```

## unfreezeBalanceV2(uint amount, uint resourceType)

**Description:** Unstake TRX in Stake 2.0. The corresponding Bandwidth and Energy will be released and TPs will also be deducted at the same time (i.e., the corresponding votes will be recycled). After performing this operation, you need to wait for N days before calling withdrawexpireunfreeze to withdraw the funds.

**Params:**

* amount — the amount of TRX to be unstaked (unit: sun)
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** N/A

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event BalanceFreezedV2(uint, uint);

    // unstake 1 TRX staked for energy
    function example() external {
        unfreezebalancev2(1000000, 1);
        emit BalanceUnfreezedV2(1000000, 1);
    }
}
```

## cancelAllUnfreezeV2()

**Description:** Cancel all pending unstaking requests. Before calling selfdestruct(address) to destroy the contract, you need to cancel all pending unstaking requests. Otherwise, the contract cannot be destroyed.

**Params:**  N/A

**Returns:** N/A

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event AllUnFreezeV2Canceled();

   // cancel all pending unstaking requests and destroy the contract
   function killme(address payable target) external {
         cancelallunfreezev2();
         emit AllUnFreezeV2Canceled();
    
         selfdestruct(target);
   }

}
```

## withdrawExpireUnfreeze() returns(uint amount)

**Description:** Withdraw unfrozen TRX. You can call this API to withdraw your unstaked fund after executing the `unfreezeBalanceV2` transaction and waiting for N days. N is the #70 [network parameter](https://tronscan.org/#/sr/parameter) and currently set to 14 for the Mainnet.

**Params:** N/A

**Returns:** the amount of TRX withdrawn successfully (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event ExpireUnfreezeWithdrew(uint);

    // withdraw unfrozen TRX
    function example() external{
        amount = withdrawexpireunfreeze();
        emit ExpireUnfreezeWithdrew(amount);
    }

}
```

## \<address payable>.delegateResource(uint amount, uint resourceType)

**Description:** Delegate Bandwidth or Energy to the address.

**Params:**

* amount — the amount of staked TRX corresponding to the resources to be delegated (unit: sun)
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** N/A

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event ExpireUnfreezeWithdrew(uint);

    // the contract delegates 1 TRX bandwidth resource share to receiver
    function example(address payable receiver) external {
        receiver.delegateResource(1000000, 0);
        emit ResourceDelegated(1000000, 0, receiver);
    }

}
```

## \<address payable>.unDelegateResource(amount, resourceType)

**Description:** Cancel the resource delegation to the address.

**Params:**

* amount — the amount of staked TRX corresponding to the resources to be undelegated (unit: sun)
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** N/A

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    event ResourceUnDelegated(uint, uint, address);

    // the contract undelegates 1 TRX bandwidth resource share from the receiver
    function example(address payable receiver) external {
        receiver.unDelegateResource(1000000, 0);
        emit ResourceDelegated(1000000, 0, receiver);
    }
}
```

## Chain Properties

* chain.totalNetLimit: total Bandwidth provision in the network (current value: 43,200,000,000)
* chain.totalNetWeight: total TRX staked for Bandwidth in the network (unit: TRX)
* chain.totalEnergyCurrentLimit: total Energy provision in the network (current value: 180,000,000,000)
* chain.totalEnergyWeight: total TRX staked for Energy in the network (unit: TRX)
* chain.unfreezeDelayDays: the unstaking pending period (unit: DAY, current value: 14 days)

**Example:**

```
pragma solidity ^0.8.17;

contract C {

    function getChainParameters() view public returns(uint, uint, uint, uint, uint)       

    {
        return (chain.totalNetLimit, chain.totalNetWeight,
                chain.totalEnergyCurrentLimit, chain.totalEnergyWeight,
                chain.unfreezeDelayDays);
    }
}
```

## \<address>.availableUnfreezeV2Size() returns(uint)

**Description:** Query the address' remaining times of executing the unstaking operation.

**Params:**N/A

**Returns:** remaining times of executing the unstaking operation

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function getvailableUnfreezeV2Size(address target) view public returns(uint) {
        return target.availableUnfreezeV2Size();
    }
}
```

## \<address>.unfreezableBalanceV2() returns(uint amount)

**Description:** Query the unfreezable TRX balance corresponding to a specified resourceType under the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"  
  **Returns:** the unfreezable TRX balance (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    
    function getvailableUnfreezeV2Size(address target) view public returns(uint amount) {
        return target.unfreezableBalanceV2(1);
    }
}
```

## \<address>.expireUnfreezeBalanceV2(uint timestamp) returns(uint amount)

**Description:** Query the withdrawable balance of the address at the specified timestamp.

**Params:**

* timestamp — the cut-off timestamp (unit: second)

**Returns:** the withdrawable TRX balance (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    
    function getExpireUnfreezeBalanceV2(address target) view public returns(uint amount) {
        return target.expireUnfreezeBalanceV2(block.timestamp);
    }
}
```

## \<address>.delegatableResource(uint resourceType) returns(uint amount)

**Description:** Query the delegatable resource share of the specified resourceType under the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** the delegatable resource share (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    //query the amount of delegatable resources share of energy for target address
    function getDelegatableResource(address target) view public returns(uint) {
        return target.delegatableResource(1);
    }
}
```

## \<address>.resourceV2(address from, uint resourceType) returns(uint amount)

**Description:** Query the resource share of a specific resourceType delegated by a "from" address to the address.

**Params:**

* from — the resource owner address
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** the resource share (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    //query the amount of resources share of energy delegated by a to b
    function getResourceV2(address b, address a) view public returns(uint) {
        return b.resourceV2(a, 1);
    }
}
```

## \<address>.checkUnDelegateResource(uint amount, uint resourceTyp) returns(uint available, uint used, uint restoreTime)

**Description:** Query the resource shares of a specific resourceType that has been used and those available for recycling if delegation to the address is canceled.

**Params:**

* amount — the resource share (unit: sun)
* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** "available" indicates the amount of the available resource share, with sun as the unit. "used" indicates the amount of the used resource share, with sun as the unit. "restoreTime" indicates the restore time point for the used resources, with second as the unit.

**Example:**

```
pragma solidity ^0.8.17;

contract C {

    function checkUnDelegateResource(address target) view public returns(uint, uint, uint) {
        (uint available, uint used, uint restoreTime) = target.checkUnDelegateResource(1000000, 1);
        return (available, used, restoreTime);
    }
}
```

## \<address>.getResourceUsage(uint resourceTyp) returns(uint used, uint restoreTime)

**Description:** Query the resource usage of a specific resourceType by the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** "used" indicates the amount of the used resource share, with sun as the unit. "restoreTime" indicates the restore time point for the used resources, with second as the unit.

**Example:**

```
pragma solidity ^0.8.17;

contract C {

    function getResourceUsage(address target) view public returns(uint, uint) {
        (uint used, uint restoreTime) = target.resourceUsage(1);
        return (used, restoreTime);
    }

}
```

## \<address>.totalResource(uint resourceTyp) returns(uint amount)

**Description:** Query the total available resource share of a specific resourceType under the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** the amount of the available resource share (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    //query the available resource share of energy for the target address
    function getTotalResource(address target) view public returns(uint) {
        return target.totalResource(1);
    }

}
```

## \<address>.totalDelegatedResource(uint resourceTyp) returns(uint amount)

**Description:** Query the resource share of a specific resourceType delegated by the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** the amount of the delegated resource share (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    //query the delegated resource share of energy for the target address
    function getTotalDelegatedResource(address from) view public returns(uint) {
        return from.totalDelegatedResource(1);
    }
}
```

## \<address>.totalAcquiredResource(uint resourceType) returns(uint amount)

**Description:** Query the resource share of a specific resourceType delegated to the address.

**Params:**

* resourceType — the resource type, with 0 for "BANDWIDTH" and 1 for "ENERGY"

**Returns:** the amount of the acquired resource share (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    //query the acquired resource share of energy for the target address
    function getTotalAcquiredResource(address target) view public returns(uint) {
        return target.totalAcquiredResource(1);
    }
}
```

## vote(address[]  srList, uint[]  tpList)

**Description:** Vote for Super Representatives (SRs) in the `srList` array and every SR will get corresponding TPs as listed in the `tpList` array.

**Params:**

* `srList` — the SR list
* `tpList` — the number of votes for SRs in srList

**Returns:** N/A

The following situations can cause the `revert` exception:

* Lengths of the`srList` array and the `tpList` array are different.
* The array length is greater than MAX_VOTE_NUMBER (30).
* There are non-SR addresses in the `srList` array.
* There are negative values in the 'tpList' array.
* Total TPs required are greater than the current TP balance of the contract.

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function voteWitness(address[] calldata srList, uint[] calldata tpList) external {
        vote(srList, tpList);
    }
}
```

## withdrawReward() returns(uint)

**Description:** Claim all voting rewards to the contract balance.

**Params:**N/A

**Returns:** the rewards claimed successfully (unit: sun)

The following situations can cause the `revert` exception:

* The contract address is in the SR list of the genesis block.
* Sum of the contract balance and rewards overflow the value allowed for "long" (8 bytes).

**Example:**c

```
pragma solidity ^0.8.17;

contract C {
    function withdrawReward() external returns(uint) {
        return withdrawreward();
    }
}
```

## rewardBalance() returns(uint)

**Description:** Query claimable rewards of the contract account.

**Params:**N/A

**Returns:** the claimable rewards of the contract account (unit: sun)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function queryRewardBalance() external view returns(uint) {
        return rewardBalance();
    }
}
```

## isSrCandidate(address sr) returns(bool)

**Description:** Query whether the address is an SR candidate address.

**Params:**

* `sr` - the target address

**Returns:** If the address is an SR candidate address, `true` is returned. Otherwise,  `false` is returned.

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function isWitness(address sr) external view returns(bool) {
        return isSrCandidate(sr);
    }
}
```

## voteCount(address from, address to)  returns(uint)

**Description:** Query votes of the `from` account voting for the `to` account.

**Params:**

* `from` - the voting address
* `to` - the SR address

**Returns:** the corresponding votes (unit: TP, 1 TRX = 1 TP)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function queryVoteCount(address from, address to) external view returns(uint) {
        return voteCount(from, to);
    }
}
```

## usedVoteCount(address owner)  returns(uint)

**Description:** Query votes used by the address.

**Params:**

* `owner` - the target address

**Returns:** the votes used by the `owner` account (unit: TP, 1 TRX = 1 TP)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function queryUsedVoteCount(address owner) external view returns(uint) {
        return usedVoteCount(owner);
    }
}
```

## ReceivedVoteCount(address owner)  returns(uint)

**Description:** Query votes received by the address.

**Params:**

* `owner` - the target address

**Returns:** the votes received by the `owner` account (unit: TP, 1 TRX = 1 TP)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function queryReceivedVoteCount(address owner) external view returns(uint) {
        return receivedVoteCount(owner);
    }
}
```

## TotalVoteCount(address owner)  returns(uint)

**Description:** Query total votes owned by the address (also called TPs owned by the contract).

**Params:**

* `owner` - the target address

**Returns:** total votes owned by the `owner` account (unit: TP, 1 TRX = 1 TP)

**Example:**

```
pragma solidity ^0.8.17;

contract C {
    function queryTotalVoteCount(address owner) external view returns(uint) {
        return totalVoteCount(owner);
    }
}
```
