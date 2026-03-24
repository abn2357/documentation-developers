---
title: FAQ
fullscreen: false
hidden: false
metadata:
  title: ''
  description: ''
---
# Most common problem in

<a href="#toc_1">Full Node in Private Networks</a>\ <a href="#toc_2">Super Node in Private Networks</a>\ <a href="#toc_3">Operation in Public Networks</a>\ <a href="#toc_4">Error Occurrences for Super Nodes</a>\ <a href="#toc_5">Block Generation by Super Nodes</a>\ <a href="#toc_6">Super Representatives Election</a>

<p id="toc_1">
# Full Node in Private Networks
</p>
<p>
**Do I need to delete other addresses when replacing genesis.block.witnesses under config.conf with the address string given upon registration on https://tronscan.org ?**

There is no need to delete. However, those address will be part of your network too, and useless if you don’ t have their private key. Att: Zion, Sun, and Blackhole Accounts cannot be deleted from the genesis block config file. However, you can change their addresses.

</p>
<p>
</p>
<p>
</p>
<p>
**After replacing the seed.node.ip.list with the IP-address of my own public network and entering the command “java -jar java-tron.jar”, how can I test if the deployment has been successful? Are there any testing interfaces or commands such as the “redis” command (which sends a ping to a server and gets a pong back from the server) for a successful deployment?**

There is no default interface with java-tron. There are several ways to check if you have a successful deployment, as once your server is running you can send gRPC commands. First thing you will need to check is if the gRPC port is open:

`netstat -tulnp| grep 50051`

If the port is open, you can test your node using tronscan.org. Make sure your port and IP is open on internet. If you are using a private IP only, you will need to use other gRPC software.

</p>
<p>
https://raw.githubusercontent.com/tronprotocol/Documentation/master/images/FAQ/查询节点.png
</p>
<p>
You can also check if your node is running using the following terminal command:

`tail -f logs/tron.log |grep "MyheadBlockNumber"`

</p>
<p>
</p>
<p>
</p>
<p>
**The Full Node is not syncing. What could be the issue & solution?**

One reason could be that the configuration file is incorrect. Try using this [configuration file](https://github.com/tronprotocol/TronDeployment/blob/master/main_net_config.conf). Another reason could be that the Full Node and Solidity Node are deployed on the same machine, but the Solidity Node's ports did not change, causing conflict with the Full Node port. Try modifying the listen port and RPC port of the solidity node's configuration file. 

</p>
<p>
</p>
<p>
</p>
<p>
**During Full Node sync, how to prevent it from being stuck on a certain block?**

First ensure the internet connection has no disruption. If the network was disrupted, please reboot the node after network resumption. For Full Nodes earlier than 2.0.8, please delete the output-directory first. For 2.0.7 version of the solidity node, please delete the library first.   

If internet connection is not the issue, the issue may have been caused by an unexpected program shutdown. The correct way to stop the node is using command `kill -15 pid`. **DO NOT USE** `kill -9`. Suggestion: reboot the node. (You need to delete the output-directory first then reboot the node if using 2.0.7 and earlier versions.) 

</p>
<p>
</p>
<p>
</p>
<p>
**Does java-tron.jar need to be deployed?**

Java-tron.jar and FullNode.jar are the same, only one of them needs to be deployed.

</p>
<p>
</p>
<p>
</p>
<p>
**How to deal with a Node Startup Exception?**

The exception may be due to using the development branch's code, which is not compatible with the main-net. Please download the latest release version of the code. 

</p>
<p>
</p>
<p>
</p>
<p id="toc_2">

# Super Node in Private Networks

</p>
<p>
**On a private network-environment, what relation exists between a Super Node and a FullNode? Is it preferred to deploy a Super Node over a FullNode?**

On a private deployment, you will need at least one Super Node, no minimum requirements for FullNode.

</p>
<p>
</p>
<p>
</p>
<p>
**As user voting determines Super Node selection in private networks, do I need to submit any application materials to the TRON foundation to be approved as a Super Node?**

You don’ t need to submit material to TRON Foundation.

</p>
<p>
</p>
<p>
</p>
<p>
**Why is data in private environments continuously synchronized and why is the journal still continuously updated to all other nodes? What is the difference between a private and a public environment then?**

If this is related to the IP list-> A: On config.conf you need to update the seed.ip, if you use the same of the public network, and your computer is connected to the internet, it will attempt to connect to those nodes and the IP list will be saved in the DB, even if the connection fails. If this is related to the Block and transactions -> A: On a private environment, you need to change p2p version and parent hash. If you use the same of mainnet or testnet, and your computer is connected to the internet. Your node will synchronize with public network.

</p>
<p>
</p>
<p>
</p>
<p id="toc_3">
# Operation in Public Networks

**Which amount of memory is currently supported by the java software?**

This will depend on your system environment: If you use 32-bit references, your heap is limited to 32 GB. If you are using 64-bit references, the size will be limited by your OS

Is a good practice to limit JVM heap size to fit inside one NUMA region (Around 1 TB on the bigger machines). If its JVM spans NUMA regions, GC will take much longer.

</p>
<p>
</p>
<p>
</p>
<p>
**What performance does a processor need to have in order to run the node software?**

At least 2 core CPUs are required to run a full node, at the minimum performance. If you are running on a private environment, with fewer transactions, then you will be fine with 4 CPU cores. So, the amount of network requests determines the CPU performance required to run the nodes. You will need to monitor your machine to decide the best requirements. In the PUBLIC NETWORK, TRON recommends to run a machine with at least 64 CPU cores for a Super Representative to become an approved applicant.

</p>
<p>
</p>
<p>
</p>
<p>
**What ports should be opened to be externally accessible? A: 18888 and 50051 are the two default ports.**
</p>
<p>
</p>
<p>
</p>
<p>
**What amount of data traffic can I expect? Will the data to be spread out to many hosts or will it be enough to just provide several nodes myself?** 

The network traffic will depend on the number of transactions. For a fast reference you could use the number of 200Bytes per transactions. Current network specification is 2000TPS (Transactions per seconds).

</p>
<p>
</p>
<p>
</p>
<p>
**Upon successful token issuance, how do I change the status from “not started yet” to “participate”?**

It is not possible to change the start date after you issue a token. You will need to wait for the time and date you have specified during creation. One can only change URL and Description after a token is created.

</p>
<p>
</p>
<p>
</p>
<p id="toc_4">
# Error Occurrences for Super Nodes
</p>
<p>
</p>
<p>
</p>
<p>
**How can I interpret the following error message?
17:02:42.699 INFO [o.t.c.s.WitnessService] Try Produce Block
17:02:42.699 INFO [o.t.c.s.WitnessService] Not sync**

This message means your node is not in sync with the network. To start produce blocks, you need to be in sync. Check your clock height with the command:

`tail -f logs/tron.log |grep "MyheadBlockNumber"`

</p>
<p>
</p>
<p>
</p>
<p id="toc_5">
# Block Generation by Super Nodes

**Do Super Nodes produce blocks in rotation? What is the speed of block production? If there is no heartbeat message for 24 hours, will the node be removed from the list of Super Nodes?**

Yes, Super Nodes produce blocks in rotation. Within current testing environment, one block is produced every 3 seconds.

</p>
<p>
</p>
<p>
</p>
<p>
**If a Super Node cannot connect to the TRON network, how long will it take to be able to connect to the network again?**

An SR’s recovery depends only on it’s connection speeds and it has nothing to do with the TRON network.

</p>
<p>
</p>
<p>
</p>
<p>
**What’s the formula of the miss rate of Super Nodes’ block production?**

“The number of blocks which supposedly should have been produced but aren’t” will be taken into account. The number will keep accumulating and not be cleared.

</p>
<p>
</p>
<p>
</p>
<p>
**Are the test version or the source code of Super Node server accessible now?**

Yes, they are open-source and can be found at [https://github.com/tronprotocol/java-tron](https://github.com/tronprotocol/java-tron).

</p>
<p>
</p>
<p>
</p>
<p>
**How do I know if my test Super Node is running?**

Run the following command:

`tail -f logs/tron.log |grep "Try Produce Block"`

Based on this command: `java -jar java-tron.jar -p yourself private key –witness -c yourself config.conf` (Example: /data/java-tron/config.conf) 

</p>
<p>
</p>
<p>
</p>
<p>
**How do I know I am running a Super Node?**

Run the following command:

`tail -f logs/tron.log |grep "Try Produce Block"`

</p>
<p>
</p>
<p>
</p>
<p>
**What are some command-line commands that can generate an address to be sent to TRON? Is web wallet the only way?**

You can use Wallet CLI: [https://github.com/tronprotocol/wallet-cli](https://github.com/tronprotocol/wallet-cli)

</p>
<p>
</p>
<p>
</p>
<p>
**If we want to test block production and other functions of the Super Node, do we need your votes to first become elected?**

We will vote for you during your test trial.

</p>
<p>
</p>
<p>
</p>
<p>
**How do we know if our own node has produced any blocks?**

You can have this information using “[https://tronscan.org/#/address/YOURADDRESS”](https://tronscan.org/#/address/YOURADDRESS”)

</p>
<p>
</p>
<p>
</p>
<p>
**Will block production speed be 1 block / 5 seconds initially when the main-net launches? What is the expected timeline for this speed to reach 1 block / 3 seconds?**

As soon as the main-net launches, the block production speed will be 1 block / 3 seconds. This will be updated to 1 block / 1 second in the future.

</p>
<p>
</p>
<p>
</p>
<p>
**Is it within TRON’s plan to reduce the reward of TRX for block production by half? If yes, when?**

The TRON Foundation is currently not planning to halve the TRX reward per block in the future.

</p>
<p>
</p>
<p>
</p>
<p>
**If any of the 27 nodes malfunctions, will it be detected automatically and disqualified from elections? Will it remain as a Super Representative if such thing occur? If it won’t, how and when it can regain the status?**

An event of incompetency & missed block rates will be kept permanently and will be public. We expect voters to make a rational judgement by not voting for that particular SR in future voting cycles.

</p>
<p id="toc_6">
# Super Representatives Election
</p>
<p>
</p>
<p>
</p>
<p>
**Why I can’t see any votes for my node at https://tronscan.org/#/network even though I’ve just submitted 2 million votes for it in the current voting round?**

Results are updated every 6 hours, which will be announce only after this round of voting.

</p>
<p>
</p>
<p>
</p>
<p>
**The amount of votes one holds is equivalent to the amount of his/her holding of TRX, so one vote can be made for one TRX, right? And the vote can be made to more than one Super Representative candidate?**

Every TRX equals one vote can only be casted for one candidate. However, if you have more than one TP( or frozen TRX), you can spread the votes among all the candidates you want to.

</p>
<p>
</p>
<p>
</p>
<p>
**Since TRX is required to obtain the right to vote, do we need to deposit a certain amount of TRX into Tronscan wallet?**

Yes, you need to have TRX in order to be able to freeze them. But no, since your balance is held on the blockchain and not on Tronscan you can use any other wallet or means to freeze your TRX.

</p>
<p>
</p>
<p>
</p>
<p>
**Is there a threshold for the daily election of 27 Super Representatives? Or is it encouraged to compete freely?**

Free competition. Solicit the votes if you want them. Due to the existence of the GR system, an SR needs at least 100 million votes to replace a GR. There is no reward for GRs’ work.

</p>
<p>
</p>
<p>
</p>
<p>
**Will TRX rewards be distributed evenly among these 27 Super Representatives or based on their hashrate?**

As they produce blocks in rotation, the distribution of reward is irrelevant to hashrate.

</p>
<p>
</p>
<p>
</p>
<p>
**If large mining operations run for the election, is hashrate exceeding 50% a possibility?**

No.

</p>
<p>
</p>
<p>
</p>
<p>
**What does the community support plan in the guidelines refer to?**

It can be understood as the budget and attention to community development.

</p>
<p>
</p>
<p>
</p>
<p>
**Does voting consume TRX?**

Voting does not consume your TRX.

</p>
<p>
</p>
<p>
</p>
<p>
**Does the status of Super Representatives only last for 24 hours?**

No. The status of Super Representatives lasts for 6 hours. But if the results of the next election remains the same, the status will be maintained for another 6 hours.

</p>
<p>
</p>
<p>
</p>
<p>
**Information on my node is not included in either of the two configuration nodes, namely build/resources/main/config.conf and build/resources/main/config.conf in the wallet. Is it still possible to discover my node and proceed to block production?**

Set your own private key in the configuration file. With a successful vote a block will be produced.

</p>
<p>
</p>
<p>
</p>
<p>
**How should I configurate my node after I’ve generated my private key?**

Find localwitness within the configuration file and set your private key for the voting account.\
Others

</p>
<p>
</p>
<p>
</p>
<p>
**Where can I find the file for RPC interface?**

[https://github.com/tronprotocol/documentation/tree/master/TRX](https://github.com/tronprotocol/documentation/tree/master/TRX)

</p>
<p>
</p>
<p>
</p>
<p>
**How do I specify the data storage directory when I activate my node?**

Currently we can’t specify data storage directory yet. This function will be made possible in the upcoming version.

</p>
<p>
</p>
<p>
</p>
<p>
**Can nodes serve as wallets?**

There is a RPC interface for wallet on nodes, but no command can call the wallet directly. Wallets on full nodes can be used through the wallet-cli(commandline wallet) on another repo.

</p>
<p>
</p>
<p>
</p>
<p>
**I don’t need to calculate my own address with the private key generated according to the file, do I?**

You don’t have to worry about private key generation once you’ve successfully registered for an account. All you need to do is log in with you pin-code to access your address.

**Is there a specific file to the calling of API like Bitcoin and Ethereum do?**

Yes. It can be found [here](doc:tron-wallet-rpc-api). 

**Can Solidity Node and Full Node be employed on the same machine? Since we can’t specify data directory, will there be consequences to the two nodes’ sharing data?**

You actually can specify data directory, config file parameter: db.directory = “database”, and index.directory = “index”. But you can also run FullNode.jar and SolidityNode.jar in different directories, and totally separate the data and log files. Remember to change the ports on config.conf, as two applications can’t run on the same port.

**Without Txid, how can we tell the users to inquire the transaction after our transfer?**

You can use transaction hash as TXID.

</p>
<p>
</p>
<p>
</p>
<p>
**Do SolidityNodes synchronize blocks in accordance with FullNodes?**

Yes.

</p>
<p>
</p>
<p>
</p>
<p>
**Is gateway for the connection to Solidity Nodes?**

Solidity Nodes are set up for the storage of irrevocable blocks, a few blocks behind Full Nodes, so they are more suitable for the confirmation of transfer. You can connect to both Solidity Node and Full Node through gateway.

</p>
<p>
</p>
<p>
</p>
<p>
**Listaccounts is a list of all addresses in the network?**

For now, yes. But that may change, as it requires further discussion if the address base becomes enormous.

</p>
<p>
</p>
<p>
</p>
<p>
**How many decimal places are there for the balance?**

Six.

</p>
<p>
</p>
<p>
</p>
<p>
**Is the machines of the nodes in Beijing? Is the wall an issue?**

Only 39.106.220.120 is in Beijing. The rest are in the US, Europe and Hong Kong.

</p>
<p>
</p>
<p>
</p>
<p>
**Can token holders hold trx on tron.network for main-net conversion. If not what other wallets may be capable, or if only exchanges.**

No wallets are capable. Only exchanges.

</p>
<p>
</p>
<p>
</p>
<p>
**In regards to TRON wallets, how many wallets are currently created.**

We already have wallet-cli, a web wallet and an iOS, android and chrome wallet.

</p>
<p>
</p>
<p>
</p>
<p>
**Is 25Gbps a requirement or is 10Gbps satisfactory, or what is the threshold that is acceptable?**

There is no hard requirement for the network TRON Power(TP). The specification we gave is just an advice.

</p>
<p>
</p>
<p>
</p>
<p>
**The people outside of the top 27 but in the top 100, are they ranked in order, 28-100 or is there an algorithm to just select who would be next if someone is voted out?**

For testnet we now just simply pick top 27 nodes with most votes. For mainnet and future testnet we may chose a different algorithm to add some randomness to part of the SR election.

</p>
<p>
</p>
<p>
</p>
**Is a well formed technical plan all we need, or must we have the hardware before applying?**

The technical plan has two parts:1 before June 26 the first election & 2 after June 26 the first election. The second part just need the plan. For the first part you can only have the plan for now but only after you have hardware we can test your node and tell everyone “yes, they do have a test node.”Applying to be a SR has no direct connection to qualifying a SR.