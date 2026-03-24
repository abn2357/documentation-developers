---
title: Consensus
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
## Overview

Blockchain is a distributed accounting system. There can be thousands of nodes in a blockchain system, each independently storing the same ledger. If new transaction data is to be written into the ledger, approvals from these nodes are needed. Achieving this goal in an untrusted distributed environment is a complicated systematic quest. The blockchain system operates normally meaning each node in the blockchain can always keep the same ledger, provided that most nodes in the system are honest and reliable. In order to ensure that honest and reliable nodes can jointly supervise the transaction data written into the ledgers, each blockchain system needs to build its consensus, which is equivalent to the constitution of the blockchain. As long as the vast majority of nodes comply with the consensus requirements, it can guarantee that the results will undoubtedly be credible, even in an untrusted distributed environment. Therefore, the consensus is an agreement that honest nodes achieve to maintain the stability of the blockchain.

Different blockchain systems will have a unique way of implementation. There are several types of consensus, and the most commonly used are Proof of Work (PoW), Proof of Stake (PoS), and Delegated Proof of Stake (DPoS). This article will mainly introduce the DPoS consensus on which TRON is based, including the essential components and mechanisms of DPoS.

## Block Producing Process

Super Representatives (SRs) of the TRON network collect the newly generated transactions in the network and verify the legitimacy of these transactions, then package the transactions into a block, record them as a new page on the ledger, and broadcast the page to the entire blockchain network. Next, other nodes will receive the new page and verify the legitimacy of the transaction data on the page and add it to their ledger. SRs keep repeating this process so all new transaction data in the blockchain system can be recorded in the ledger.

## DPoS Overview

The role of the consensus is to select SRs in the blockchain system, who are responsible for verifying and recording new transaction data, then broadcasting the new data to other nodes in the network and obtaining their approval on the new data. As a specific implementation of consensus, DPoS works in the following way:

The DPoS consensus selects some nodes as SRs in the blockchain system based on the number of votes they receive. First, when the blockchain system starts to operate, a certain number of tokens will be issued, and the tokens will be given to nodes in the blockchain system. Then, a node can apply to be a SR candidate in the blockchain system with a portion of the tokens. Any token-holding node in the blockchain system can vote for these candidates. Every t period, the votes for all the candidates will be counted. Top N candidate nodes with the most votes will become SRs for the following t period. After that t period, the votes will be counted again to elect the new SRs, and the cycle continues.

Let us see how it's realized in the context of TRON:

## Definition

* TRON: refers to the TRON network, also referred to as TRON, TRON blockchain, and TRON blockchain system in the following sections of this article.

* TRON token: refers to the equity token issued by and circulating in TRON, known as TRX.

* SR candidates: nodes eligible for becoming SRs in TRON.

* Super Representatives (SRs): nodes in TRON qualified for record-keeping. There will be 27 SRs in TRON, which are also called super nodes. Therefore, record-keeper, SR, and supernode will be used interchangeably in the following sections of this article.

* Record-keeping: the process of verifying transactions and recording them in a ledger. Since the ledger records are carried by blocks in TRON, the record-keeping process is also called block generation. Therefore, record-keeping and block generation will be used interchangeably in the following sections of this article.

* Record-keeping order: the block generation order, which is the descending order of the 27 SRs based on the number of votes they receive.

* Slot: In TRON, every 3 seconds is regarded as one slot. Under normal circumstances, each SR will produce a block within the corresponding slot time. Therefore, the average block interval of TRON is approximately three seconds. If an SR fails to produce a block for some reasons, the corresponding slot will be vacant and the next SR will produce a block in the following slot. During the maintenance period, block production will skip two slots.

* Epoch: TRON sets an Epoch to be 6 hours. The last two block time of an Epoch is the maintenance period, during which the block generation order for the next Epoch will be decided.

* Maintenance Period: TRON sets the period to be two block time, which is 6 seconds. This period is used to count the votes of candidates, elect a new SR list based on their votes, and process expired proposals. There are 4 Epochs in 24 hours, and naturally, 4 maintenance periods. SRs pause to produce blocks during the maintenance period. The block generation order for the next epoch will be decided in the maintenance period.

![](https://files.readme.io/2c7fd14-61624595420_.pic.jpg "61624595420_.pic.jpg")

## Election Mechanism

1. Votes

In TRON, 1 TRX equals 1 vote.

2. Voting process

In TRON, voting for candidates is a special transaction. Nodes can vote for candidates by creating a voting transaction.

3. Vote counting

During each maintenance period, the votes for candidates will be counted. The top 27 candidates with the most votes will be the SRs for the next Epoch.

## Block Generation Mechanism

During each Epoch, the 27 SRs will take turns to generate blocks according to the record-keeping order. Each SR can only generate blocks when it is their turn. When it is the turn of an SR to produce a block, the SR will take out  transactions in the transaction mempool one by one for execution, and pack the successfully executed transactions into the block. So the order of transactions in the block is consistent with that in the transaction mempool, and the transactions in the transaction mempool are enqueued in the order in which the node receives them, therefore, there is no MEV or front-running attack on TRON.

After packaging transactions into a block, the SR will sign the block with his private key and the signature will be recorded in the `witness_signature`field of the block. Except for the transactions, the SR will add some extra information into the block: the parent block hash, the address of the SR, the block height, and the time that the block is generated, into the block. 

Through storing the hash of the previous block, blocks are logically connected. Eventually, they form a chain. A typical blockchain structure is shown in the following picture:

![](https://files.readme.io/8a88caa-31624594014_.pic.jpg "31624594014_.pic.jpg")

In ideal circumstances, the record-keeping process in a DPoS consensus-based blockchain system proceeds according to the record-keeping order calculated in advance. SRs generate blocks in turn (see Figure a). However, the blockchain network is still a distributed and untrusted complex system in the following three ways:

* In a poor network environment, blocks generated by some SRs may be received by other SRs at an invalid time (see Figure b1 and b2).

* The normal operation of a certain SR cannot always be guaranteed (see Figure c).

* Some malicious SRs will generate fork blocks in order to fork the chain (see Figure d).

![](https://files.readme.io/a595076-71624595529_.pic.jpg "71624595529_.pic.jpg")

![](https://files.readme.io/de89f88-81624595552_.pic.jpg "81624595552_.pic.jpg")

As mentioned above, the basis for a blockchain system to operate normally is that most of the nodes in the system are honest and reliable. Furthermore, the primary guarantee for the security of a blockchain system is the ledger's security, meaning that illegal data should not be written into the ledger, and ledger copies saved on each node should be consistent. Based on the DPoS consensus, the record-keeping process is carried out by SRs. Therefore, the safety of TRON depends on the reliability of the majority of SRs. TRON has put confirmed blocks in the system, which are irreversible. At the same time, to resist the malicious behaviors of a small number of SR nodes, TRON recognizes the longest chain as the main chain based on "the longest chain principle".

**The confirmed block principle**

Newly produced blocks are unconfirmed. Only those blocks that are "approved" by more than 70% (i.e. 27 \* 70% = 19, rounded up) of the 27 SRs are considered irreversible blocks, commonly referred to as solidified blocks. The entire blockchain network has confirmed the transactions contained in the solidified blocks. The way to "approve" the unconfirmed state block is that SRs produce subsequent blocks after it. The point to be emphasized here is that the SRs producing these 18 blocks must be different from each other as well as the SR producing the 103rd block.

**The longest chain principle**

When a fork occurs, an honest SR would always choose to produce blocks on the longest chain.

## Incentive Model

TRON sets up an incentive model to encourage node participation and network expansion to ensure the safe and efficient operation of the blockchain system. SRs who complete block production tasks will be rewarded with TRX. The model also specifies that for every confirmed block produced by a SR, the SR will receive 32 TRX. In addition, the first 127th SRs (including SR candidates) with the most votes will receive proportional rewards during the maintenance period of each Epoch.

## Proposal-based Parameter Adjustment

A notable characteristic of DPoS is that any parameter adjustment can be proposed on the chain, and SRs will start a vote to decide whether the proposal can be approved. The advantage of this method is that it does not require hard fork upgrades to add new features. For more information about TRON network parameters, please refer to [here](/docs/super-representatives#tron-network-parameters) or  [TRONSCAN](https://tronscan.org/#/sr/committee).

## Appendix: References

* [Delegated Proof of Stake (DPoS) – Total Beginners Guide](https://www.coinbureau.com/education/delegated-proof-stake-dpos/)
* [Consensus Algorithms: Proof of Stake & Cryptoeconomics](https://www.nichanank.com/blog/2018/6/4/consensus-algorithms-pos-dpos)
* [Role of Delegates](http://docs.bitshares.org/en/master/technology/dpos.html#role-of-delegates)
* [What is Delegated Proof of Stake?](https://hackernoon.com/what-is-delegated-proof-of-stake-897a2f0558f9)
