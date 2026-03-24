---
title: Tokenomics
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
TRON, as a next-generation blockchain operating system, is reshaping the decentralized internet infrastructure. Its native cryptocurrency, TRX, not only serves as the circulating medium for the ecosystem, powering transactions and smart contracts, but also acts as the core credential for community self-governance, empowering holders with the right to participate in network governance.

***

## TRX Supply and Distribution

According to [CMC](https://coinmarketcap.com/currencies/tron/#token_unlocks) and [Binance Research](https://www.binance.com/en-AE/research/projects/tron#3-Economics-and-supply), the initial supply distribution of TRON is as follows:

* The distribution to private sale and early investors accounts for 25.7% (25.7 billion TRX).
* The distribution to public sale accounts for approximately 40% (40 billion TRX).
* The proportion retained by TRON DAO accounts for 34.3% (34.3 billion TRX) for ecosystem development.

**Circulation Adjustment**: TRON employs a dual-track circulation adjustment mechanism. On the incremental side, new TRX is distributed to Super Representatives (SRs) and voters through block rewards (including block production rewards and voting rewards), incentivizing participation in the network consensus. Concurrently, on the decremental side, a transaction fee burning mechanism continuously reduces the circulating supply, creating deflationary pressure. Therefore, under the combined effect of block rewards and the burning mechanism, the TRX supply is elastic and dynamic.

***

## Functionalities of TRX

**Transactions and Fees**: TRX serves as the fundamental fuel for the network, used to pay transaction fees for smart contract execution, transfers, and other operations.\
**Staking and Network Security**: TRX is the underlying asset for DPoS staking.\
**DeFi Infrastructure**: TRX acts as the underlying collateral for staking and generating stablecoins (e.g., USDD), serves as the core collateral for lending protocols (JustLend DAO), and is the liquidity benchmark for decentralized exchanges (SunSwap).\
**Governance**: By staking TRX, users obtain TRON Power (TP) and system resources (Bandwidth or Energy). Holding TP grants governance rights, allowing users to vote for SRs and jointly participate in the governance of the TRON network ecosystem.

***

## Consensus Mechanism and Incentives

TRON adopts the Delegated Proof of Stake (DPoS) consensus mechanism, where 27 Super Representatives (SRs) are elected through community voting to be responsible for block production and transaction validation. This mechanism ensures high performance with over 2,000 TPS while balancing decentralized governance and network security.

### Core Operational Logic

1. **Democratized Super Representative (SR) Election**
   * TRX holders stake and vote to elect 27 Super Representatives (SRs).
   * Nodes with the most votes produce blocks in rounds, ensuring fair participation.
2. **Efficient Consensus**
   * SRs produce blocks in a rotational manner, significantly increasing the transaction speed.
   * Compared to PoW, DPoS is more energy-efficient and scalable.

### Staking (Freezing TRX)

Users participate in the DPoS mechanism by "staking" their TRX. Through staking TRX, users can obtain TP and system resources (Bandwidth or Energy).

* **TRON Power (TP)**: This represents voting power. One staked TRX equals one TRON Power. Users can then use their TP to vote for their preferred SRs.
* **Bandwidth and Energy**: Staking TRX also provides users with bandwidth and energy. These resources are crucial for conducting transactions on the TRON network, as they effectively offset transaction fees that may otherwise cause TRX burning.

Users can unstake their TRX at any time. However, from the moment unstaking is initiated, these TRX enter a specific waiting period (currently 14 days; this parameter can be modified through proposals), during which they cannot be traded or transferred. After this period, users can "unfreeze" their TRX to restore liquidity.

### Incentives and Security

**Incentivizing Participation**: TRX holders can earn rewards by staking and voting for SRs, which helps incentivize their participation in securing the network, enhances decentralization, and creates a positive feedback loop.\
**SR Accountability Mechanism**: SRs are accountable to their voters. Malicious behaviors can lead to vote loss, deprivation of the SR eligibility, and forfeiture of block rewards, ensuring fairness in network operation.\
**Resource Allocation**: The bandwidth and energy model encourages users to stake TRX to obtain resources, aligning their economic interests with the network's health and stability, thereby fostering a beneficial promotion mechanism.\
**Transaction Cost Management**: While users with resources can transact for free, a burning fee is charged for users without resources. This ensures a cost for spam transactions, preventing network abuse and effectively maintaining network order and efficiency.

***

## Resource Model (Bandwidth and Energy)

TRON innovatively adopts a "resource-burning" dual-track system. Staking TRX grants free transactions, while insufficient resources trigger intelligent TRX burning for fee payment, balancing user experience and thedeflationary economy.

### Core Resource System

#### Bandwidth

All transactions on the TRON network require bandwidth, including transfers, account creation, and smart contract execution. Users have a certain amount of free bandwidth (currently 600 units) and can also obtain bandwidth by staking TRX.

#### Energy

Energy is a resource necessary for executing smart contracts (e.g., TRC-20 token transfers, DApp interactions). Users can obtain energy by staking TRX.

### "Burning" Mechanism:

When users initiate transactions on the TRON network, if bandwidth or energy is insufficient, the system will automatically burn the corresponding amount of TRX to cover resource costs. This ensures transaction execution even with insufficient resources, allowing the network to remain highly efficient.

SiBesides, this burning mechanism also creates deflationary pressure on the TRX supply. WAlthough staking can help users avoid these fees, high network usage or insufficient staked TRX may lead to significant TRX burning, thereby adjusting the total circulating supply in the market.

***

## Dynamic Balance of Inflationary and Deflationary Mechanisms

TRON's economic model represents a balance between TRX issuance and burning mechanisms, aiming to maintain the currency value relatively stable and ensure healthy development of the ecosystem.

* **Inflationary Drivers**:\
    **Block rewards** are the primary source of inflation. Block rewards are divided into two parts: block production rewards and voting rewards. Block production rewards are distributed to SRs and their voters based on the number of blocks produced. Voting rewards are distributed to those who vote for SRs and SR partners. Each SR can independently set their **block reward distribution ratio** (0%-100%), which indicates the percentage of block rewards the SR retains, with 0 meaning all block rewards are distributed to voters. This mechanism aims to encourage staking participation, thereby ensuring the robustness of network consensus.\
    The TRON block reward ratio is controlled by **on-chain parameters**, which can be adjusted by committee proposals (e.g., on June 13, 2025, the block reward was adjusted to [136 TRX](https://tronscan.org/#/proposal/102)), requiring approval through SR voting. Current settings: 8 TRX as block production rewards, and 128 TRX as voting rewards.

* **Deflationary Drivers**:\
    **TRON Intelligent Burning System**: When resources are insufficient, TRX is automatically burned to cover fees. TRON continuously optimizes its network resource economic model through committee proposals, such as historical Proposal #11, which adjusted energy prices, and TIP-491, which adjusted the transaction fee burning mechanism, to influence resource consumption and TRX burning conditions, thus maintaining ecosystem health.\
    **Special Transaction Consumption**: Certain special transactions directly consume TRX, and these consumptions cannot be offset by bandwidth or energy.

![](https://files.readme.io/1322d6dedf601f380f112454d46cdfc6e3f0bcb9b66203387cb36a05f13f8b0d-image.png)

<br />

Based on the chart and [data provided by TRONSCAN](https://tronscan.org/#/data/charts/trx/supply), the total supply of TRX, after an initial increase (until approximately mid-2022) reaching a peak of around 102 billion, has shown a significant and sustained deflationary trend. Recent daily data further confirms this: in most cases, the amount of TRX burned by transactions and resource consumption in the network consistently exceeds the amount of newly generated TRX, leading to a net decrease of millions of TRX each day. This powerfully drives the significant decline in TRX's total supply from its peak to the present, reflecting the strong impact of the deflationary mechanism in TRON's economic model.

***

## Ecosystem

The TRON ecosystem is continuously expanding, encompassing a wide range of decentralized applications (DApps) that collectively promote the healthy development of the ecosystem and bring richer application scenarios for TRX by driving network activities and increasing utility.

**Decentralized Finance (DeFi) Protocols**: Various DeFi protocols have emerged on the TRON network, providing users with decentralized lending (e.g., JustLend DAO), trading, and liquidity mining services (e.g., SUN.io).

**Stablecoin Ecosystem**: TRON, as a major issuance network for mainstream stablecoins, has seen a significant increase in its network activities and the user base, which substantially enhance TRON's international influence and practical application value.

* **USDT (Tether)**: The TRC-20 version of USDT issued on TRON has a massive circulation. The widespread use of USDT on TRON drives a large volume of transactions, bringing significant transaction volume and fee revenue to the network, while also providing users with efficient, low-cost stablecoin transaction and transfer channels.
* **TUSD (TrueUSD)**: The introduction of TUSD on TRON not only provides users with more diverse, transparent, and audit-backed stablecoin options but also enhances the overall credibility and attractiveness of the TRON stablecoin ecosystem through its compliance and real-time on-chain verification mechanisms, further promoting the flow of funds and application innovation for institutions and individual users on the TRON network.
* **USDD (Decentralized USD)**: USDD is a fully decentralized stablecoin designed to maintain a stable value through a robust collateral support system and advanced pegging mechanisms. USDD plays a crucial role in the TRON ecosystem; it not only enriches the diversity of decentralized financial products but also brings a deeper spirit of decentralization and innovative vitality to the TRON network through its censorship-resistant nature and community-driven governance model, while providing users with autonomous choices for value storage and transactions on-chain.

The widespread adoption of these DApps and stablecoins increases on-chain transaction volume and smart contract interactions on the TRON network, thereby enhancing the utility of TRX and promoting the burning of TRX through resource consumption and special transactions. These, in turn, ensure the stable operation of the TRON economic model and collectively drive the sustainable growth of the entire ecosystem.

***

## Conclusion

TRON's economic model and network security framework together form a coordinated ecosystem, with the core objective of incentivizing active user participation, ensuring network resilience, and striving for long-term ecosystem prosperity. Although development still faces numerous challenges, TRON is diligently addressing these issues through continuous evolution and adaptive adjustments to its economic model, aiming to further strengthen its leading position in the blockchain world.
