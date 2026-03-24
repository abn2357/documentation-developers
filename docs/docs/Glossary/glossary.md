---
title: Glossary
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
### **Application Programming Interface (API)**

API is mainly used for client application development, and supports developers to design their own Decentralized Applications (DApps).

### **Address (Public Key)**

The public key and the private key are a key pair obtained via a hash algorithm. 

The public key is the public part while the private key is the non-public part. 

The public key is usually used to encrypt the session secret, and the corresponding private key is used to perform digital signature verification and data decryption.

### **Application Layer**

Developers can use interfaces to easily implement rich DApps and personalized wallets. TRON protocol completely follows the Google Protobuf to implement, therefore naturally supports multi-language extensions.

### **Bandwidth** Points

Excessive insignificant transactions cause network congestion, which happens in other public blockchain projects like Ethereum everyday, and it delays transaction confirmation. To avoid the network congestion, TRON network allows each account to initiate a limited number of transactions for free with Bandwidth Points.

Bandwidth Points allows you to perform transactions on the TRON without paying any gas fees. Every account is distributed with 600 Bandwidth Points every 24 hours. Higher transaction frequency requires more Bandwidth Points, which can be obtained by staking TRX.

A transaction is transmitted and stored in the form of a byte array in the network. The Bandwidth Points consumed by a transaction is proportional to the size of the byte array in this transaction. For example if the byte array length of a transaction is 100, then the transaction needs to consume 100 Bandwidth Points.

### **Block**

Blocks are used to store your transaction information. A complete block includes block size, block header, transaction counter, and transactions. When a transaction is broadcasted to the network, the nodes pick up the transaction. Either miners (PoW) or Super Representatives (DPoS) would perform the hashing of the transaction. Once the correct hash is calculated, which fits the block header format, the block will be added after the previous block. 

### **Block Rewards**

The Super Representative's (SR) block rewards are stored in a sub-account, and the Super Representative can redeem their rewards at Tronscan.

### **Content Delivery Network**

Content Delivery Network (CDN) is designed to avoid the bottlenecks and links on the Internet which may affect the speed and stability of a data transmission. Content transmission can be faster and more stable with CDN.

### **Cold Wallet**

Cold wallet installs on "cold" devices (any network-isolated devices, e.g. computers, mobile phones, etc.). An offline cold wallet isolates the wallet private key from the internet, ensuring its security.

### **Consensus Mechanism**

The consensus mechanism is to complete the verification and confirmation of the transaction in a short period of time through the voting among nodes; for a transaction, if several nodes with irrelevant interests can reach a consensus, then the entire network could reach the consensus.

### **Maintenance Period**

The TRON network adopts the DPOS consensus algorithm and periodically elects 27 super representatives responsible for block production based on voting. The network will count votes at the beginning of every cycle to determine the super representatives and the order to produce blocks within this cycle. This period of counting votes is called the maintenance period, which is fixed at 6s. In addition to counting votes, the maintenance period also performs operations such as reward statistics and confirmation of proposals taking effect. The start time of the next maintenance period can be obtained through the [getnextmaintenancetime](https://developers.tron.network/reference/getnextmaintenancetime) interface.

### **Maintenance Time Interval**

The time interval between two maintenance periods is a parameter of the TRON network, currently it is 6 hours, and the first 6 seconds is the `maintenance period` time. There are 4 maintenance time intervals per day, and the first maintenance time interval starts at UTC 00:00. Maintenance time interval is also known as maintenance cycle.

![](https://files.readme.io/583f18e-maintenanceTime.png "maintenanceTime.png")

### **Core Layer**

TRON includes a stack-based virtual machine with an optimized instruction set, as well as numerous modules for smart contracts, account management, and consensus. 

### **Decentralized Applications (DApps)**

A decentralized application is an application that runs on a decentralized P2P network. Since DApps do not depend on a central entity for operation, this eliminates the risk of a single point of failure. Records and data from DApps are also stored on the blockchain. 

### Energy

Like Bandwidth Points, Energy can be obtained by staking TRX, but there are no free Energy distributed to every account. Different from Bandwidth Points which is used in transactions, energy represents how much CPU resources are consumed during an execution of a smart contract.

1 Energy equals 1 millisecond of a CPU spending in a smart contract execution. Depending on the complexity of a smart contract, the longer the execution time, the more Energy the account have to spend for. 

### **Stake Operation**

Stake a specified number of TRX to get TRON Power for voting. Stake also generates Bandwidth Point and Energy. The amount of Bandwidth Point and Energy generated by staking is related with the amount of staked TRX and the corresponding number of staking days.  Staked TRX cannot be circulated and cannot be used for transactions.

### **Google Protobuf**

ProtoBuf is a flexible and efficient language-independent structured data representation method that can be used to represent communication protocols and data storage. Compared to XML, ProtoBuF is smaller, faster and simpler. You can use the ProtoBuf compiler to generate source code for specific languages (such as C++, Java, Python, etc., ProtoBuf currently supports mainstream programming languages) for serialization and deserialization.

### **GRPC**

GRPC is a language-neutral, platform-neutral, open source remote procedure call (RPC) system. In gRPC, a client application can directly call a server-side application on a different machine as if it were a local object, making it easier to create distributed applications and services. Like many RPC systems, gRPC is based on the idea of defining a service that specifies the methods (including parameters and return types) that can be called remotely. Implement this interface on the server side and run a gRPC server to handle client calls. Having a stub on the client can be the same as the server.

### **Hot Wallet**

Hot wallet is known as a wallet connected to the internet. Hot wallet is said to be more vulnerable than cold wallet, as user's private key might be exposed due to potential technical security breaches or attacks by hackers, but it is more convenient to use than cold wallet.

### **JDK**

JDK is a software development kit for the Java language, primarily for Java applications on mobile devices and embedded devices. JDK is the core of the entire Java development, it contains the JAVA runtime environment (JVM + Java system class library) and JAVA tools.

### **KhaosDB**

The KhaosDB used by TRON stores all newly generated bifurcation chains for a certain period of time. When there is a need to switch the main chain, with the support of KhaosDB, the verification node can quickly switch the effective chain to the new main chain.

### **Level DB**

In order to meet both access speed and rapid development requirements, TRON will adopt Level DB in the early stage of development. After the Mainnet went online, TRON upgraded the database according to actual needs, making TRON a fully tailored database.

### **Private Testnet**

Test private network: Other developers configure their own network id, server ip, and test according to the tutorial deployment files provided by TRON. Only developers participating in the deployment have access.

### **RPC**

Remote Procedure Call (RPC) is a protocol one program can use to request a service from a program located in another computer on a network without having to understand the network's details. A procedure call is also sometimes known as a function call or a subroutine call.

### **Scalability**

Scalability is one of the features of the TRON network. Being scalable means that a system or network has the ability to handle an increasing amount of work, or has the potential to expand through this capability.

### **Smart Contracts**

A smart contract is a computer protocol with a purpose to digitally verify the negotiation of a contract. They not only define the rules and penalties related to an agreement in the same way that a traditional contract does, but it can also automatically enforce those obligations. If and when the pre-defined rules are met, the agreement is automatically enforced. The smart contract code facilitates, verifies, and enforces the negotiation or performance of an agreement or transaction. It is the simplest form of decentralized automation.

### **Storage Layer**

TRON's technical team designed a unique distributed storage protocol for TRON, including block storage and state storage. In the design of the storage layer, TRON introduced the idea of a graph database to more easily meet the needs of real-world diverse data storage.

### **TRC-20**

[TRC‌-20](https://developers.tron.network/docs/trc20) is a technical standard used for smart contracts on the TRON blockchain for implementing tokens with the TRON Virtual Machine (TVM). It’s fully compatible to [ERC‌-20](https://eips.ethereum.org/EIPS/eip-20). Interface is as follows:

```java
contract TRC20Interface {
    function totalSupply() public constant returns (uint);
    function balanceOf(address tokenOwner) public constant returns (uint balance);
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining);
    function transfer(address to, uint tokens) public returns (bool success);
    function approve(address spender, uint tokens) public returns (bool success);
    function transferFrom(address from, address to, uint tokens) public returns (bool success);

    event Transfer(address indexed from, address indexed to, uint tokens);
    event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
}
```

### **TRC-10**

[TRC-10](https://developers.tron.network/docs/trc10) is a technical token standard supported by the TRON blockchain natively, without involving the TRON Virtual Machine (TVM).
