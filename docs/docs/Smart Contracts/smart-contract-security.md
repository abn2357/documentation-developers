---
title: Security
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Smart contracts are extremely flexible, capable of both holding large quantities of tokens and running immutable logic based on previously deployed smart contract code. While this has created a vibrant and creative ecosystem of trustless, interconnected smart contracts, it is also the perfect ecosystem to attract attackers looking to profit by exploiting vulnerabilities in smart contracts and unexpected behavior in the TRON network. Smart contract code usually cannot be changed to patch security flaws, so assets that have been stolen from smart contracts are irrecoverable, and stolen assets are extremely difficult to track.

Before launching any code to Mainnet, it is important to take sufficient precaution to protect anything of value your smart contract is entrusted with. In this article, we will discuss a few specific attacks and best practices to ensure your contracts function correctly and securely.

# Smart Contract Development Process

Security starts with a proper design and development process. There are many things to keep in mind about the smart contract development process, but at least ensure the following:

* All code is stored in a version control system, such as git
* All code modifications are made via Pull Requests
* All Pull Requests have at least one reviewer
* A TRON-based contract development tool (e.g., TronBox) is used to compile, deploy, and run a suite of tests against your code with a single command.
* You have run your code through basic code analysis tools such as Mythril and Slither, ideally before each Pull Request is merged, comparing differences in output
* Solidity does not emit ANY compiler warnings
* Your code is well-documented

# Attacks & Vulnerabilities

Here are some common vulnerabilities:

## Re-entrancy

Re-entrancy is one of the largest and most significant security issue to consider when developing Smart Contracts. While the TVM cannot run multiple contracts at the same time, a contract calling a different contract pauses the calling contract's execution and memory state until the call returns, at which point execution proceeds normally. This pausing and re-starting can create a vulnerability known as "re-entrancy".

Here is a simple version of a contract that is vulnerable to re-entrancy:

```solidity=
// THIS CONTRACT HAS INTENTIONAL VULNERABILITY, DO NOT COPY
contract Victim {
    mapping (address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        (bool success, ) = msg.sender.call.value(amount)("");
        require(success);
        balances[msg.sender] = 0;
    }
}

```

To allow users to withdraw TRX they have previously stored on the contract, the `withdraw()` function will do the following in sequence:

1. Reads how much balance a user has
2. Sends the user that balance amount in TRX
3. Resets the balance to 0, so the user cannot withdraw the balance again.

If called from a regular external account (such as your own TronLink account), this functions as expected: `msg.sender.call.value()` simply sends TRX to your account. However, other smart contracts can make calls as well. If a custom, malicious contract is the one calling `withdraw()`, `msg.sender.call.value()` will not only send an amount of TRX, it will also implicitly call the contract to begin executing code. Imagine this malicious contract:

```solidity=
contract Attacker {
    uint count；
    function beginAttack() external payable {
        count = 5；
        Victim(VICTIM_ADDRESS).deposit.value(1 trx)();
        Victim(VICTIM_ADDRESS).withdraw();
    }

    function() external payable {
        if（count>0）
        {
            count -=1;
            Victim(VICTIM_ADDRESS).withdraw(); 
        }
            
    }
}

```

Calling `Attacker.beginAttack()` will start a cycle that looks something like:

```
0.) Attacker's external account calls Attacker.beginAttack() with 1 TRX
0.) Attacker.beginAttack() deposits 1 TRX into Victim contract: Victim.deposit.value(1 trx)();

  1.) Attacker calls Victim's withdraw function: Victim.withdraw()
  1.) Victim reads the caller's balance 1TRX: balances[msg.sender]
  1.) Victim sends TRX to Attacker ，which executes default function call of Attacker contract
    2.) In Attacker's default function  -> Victim.withdraw()
    2.) Victim reads balance: balances[msg.sender]
    2.) Victim sends TRX to Attacker which executes default function call of Attacker contract
      3.) In Attacker's default function -> Victim.withdraw()
      3.) Victim reads balance: balances[msg.sender]
      3.) Victim sends TRX to Attacker which executes default function call of Attacker contract
        4.) For Attacker, in order not to exceed the maximum execution time allowed by the contract, after executing several times, do not continue to execute withdraw, and return directly.
      3.) balances[msg.sender] = 0;
    2.) balances[msg.sender] = 0; 
  1.) balances[msg.sender] = 0; 

```

Calling Attacker.beginAttack with 1 TRX will re-entrancy attack Victim, withdrawing more TRX than it provided. That is, Attacker takes TRX from other users' balances.

### How to Handle Re-entrancy

By simply switching the order of the storage update and external call, we prevent the re-entrancy condition that enabled the attack. In the following example, the withdraw function first sets the stored balance information to 0, and then transfers TRX to avoid malicious code reentrancy attacks.

```solidity=
contract NoLongerAVictim {
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        (bool success, ) = msg.sender.call.value(amount)("");
        require(success);
    }
}

```

Any time you are sending TRX to an untrusted address or interacting with an unknown contract (such as calling transfer() of a user-provided token address), you open yourself up to the possibility of re-entrancy. By designing contracts that neither send TRX nor call untrusted contracts, you prevent the possibility of re-entrancy!

## More Attack Types

In addition to the above-mentioned re-entrancy attacks caused by smart contract coding, there are many other types of attacks, such as:

* TRX send rejection
* Integer overflow/underflow
