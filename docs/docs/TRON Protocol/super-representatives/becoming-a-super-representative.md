---
title: Becoming a Super Representative
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
Any account can apply to become a Super Representative (SR) candidate and then participate in the SR election. This article will introduce how to become an SR and participate in block production.

## 1\. Create an account

To participate in the SR election, you need to have an account on the TRON network first. If you have already had a TRON account, please skip to Step 2 directly.

It is recommended to create an account offline, for example, you can use various SDKs, wallet-cli, or other tools. In this article, we will use the [wallet-cli command line wallet](https://github.com/tronprotocol/wallet-cli) to create account addresses and send transactions.

**Create an account**\
Enter the "RegisterWallet" command in wallet-cli, and then enter the password as prompted.

```
wallet> RegisterWallet 
Please input password.
password: 
Please input password again.
password: 
Register a wallet successful, keystore file name is UTC--2024-04-18T07-24-17.307000000Z--TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb.json
wallet> 
```

The account is then created successfully, and the private key will be saved in the form of a Keystore file in the `Wallet` subfolder of the wallet-cli running directory. The name of the Keystore file created in this example is: `UTC--2024-04-18T07-24 -17.307000000Z--TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb.json`, of which the front part is the account creation time and the back part is the account address in the Base58 format: `TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb`.

**Login wallet-cli**\
Enter the "login" command in wallet-cli, and follow the prompts to enter the password you entered when creating the account.

```
wallet> login
Please input your password.
password: 
Login successful !!!
wallet> 
```

After logging in, you can operate this account and send transactions through wallet-cli easily. 

You can view the account private key through the "BackupWallet" command, and you need to enter the password during the process. **Remember to back up your private key to protect account security.**

```
wallet> BackupWallet
Please input your password.
password: 
BackupWallet successful !!
8759279f...8f68a5ef // Private Key, Hex, 64 total chars
```

## 2\. Deposit TRX

To apply to become an SR candidate, you need to pay an application fee of 9,999 TRX. Since all transactions consume Bandwidth resources, when the Bandwidth in your account is insufficient, TRX needs to be burned to pay for the Bandwidth. Therefore, in order to ensure the transaction of applying to become an SR candidate as well as other transactions such as updating the account name that may be performed later can all be successfully executed, it is recommended to deposit 10,100 TRX into the account. You can withdraw your TRX from an exchange, or transfer TRX from other wallets to this account.

## 3\. Apply to become an SR candidate

In wallet-cli, send a transaction to apply to become an SR candidate through the `CreateWitness` command. This command requires a parameter indicating the SR's website URL. In this example, it is `www.your-website.com`. Replace it with your own URL in actual scenarios.

```
wallet> CreateWitness www.your-website.com
{
	"raw_data":{
		"contract":[
			{
				"parameter":{
					"value":{
						"owner_address":"TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb",
						"url":"www.your-website.com"
					},
					"type_url":"type.googleapis.com/protocol.WitnessCreateContract"
				},
				"type":"WitnessCreateContract"
			}
		],
		"ref_block_bytes":"d140",
		"ref_block_hash":"fe6d51f5debe3a0d",
		"expiration":1713428409000,
		"timestamp":1713428351865
	},
	"raw_data_hex":"0a02d1402208fe6d51f5debe3a0d40a8d5aa82ef315a67080512630a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5769746e657373437265617465436f6e7472616374122d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612147777772e796f75722d7765622d7369742e636f6d70f996a782ef31"
}
before sign transaction hex string is 0a85010a02d1402208fe6d51f5debe3a0d40a8d5aa82ef315a67080512630a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5769746e657373437265617465436f6e7472616374122d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612147777772e796f75722d7765622d7369742e636f6d70f996a782ef31
Please confirm and input your permission id, if input y or Y means default 0, other non-numeric characters will cancel transaction.

```

Check and confirm the transaction, input `y` and press "Enter", and then input the password according to the prompts and wait for the transaction to be completed. If the transaction is successful, you will see the words `CreateWitness successful!!`.

```
y
Please choose your key for sign.
Please input your password.
password: 
after sign transaction hex string is 0a85010a02d1402208fe6d51f5debe3a0d40cfc7cd8cef315a67080512630a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5769746e657373437265617465436f6e7472616374122d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612147777772e796f75722d7765622d7369742e636f6d70f996a782ef311241ec56e62858ccf98ff5138002d6d4f1a3eee0c66948704956e2ef8572a8bde78e1ecc72cfa2541ace61076e4a4d4ac1c560cc5d180a28575231414a0a3ea876a701
txid is e58cbd7f8ef280c3e53c36c43e9ae5ad852af6735e439b37f65f9e0744625789
CreateWitness successful !!
wallet> 
```

After the above transaction is executed, wait for about one minute before querying whether the account is an SR candidate. The command for wallet-cli to query account information is `getaccount`, and the parameter is the target SR's account address:

```
wallet> getaccount TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb
{
    "address": "TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb",
    ......
    "is_witness": true,
    ......
}
```

If the value of `is_witness` is `true`, it means that the account is an SR candidate. If there is no `is_witness` field in the returned result, it means that the transaction for applying to become an SR candidate was not executed successfully and was not on chain.

Note: The SR URL can be changed. You can modify the URL through the `UpdateWitness` command of wallet-cli.

## 4\. (Optional) Update the brokerage ratio

The default value of the brokerage ratio is 20, that is, after becoming an SR candidate, the SR candidate retains 20% of the total income by default and rewards 80% of the total income to his voters. The brokerage ratio is modifiable.

Assume that you want to modify the brokerage ratio to 100, that is, the whole income is owned by the SR. Enter the command `updateBrokerage` in wallet-cli, and enter two parameters at the same time: the SR's account address and the brokerage ratio:

```
wallet> updateBrokerage TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb 100
{
	"raw_data":{
		"contract":[
			{
				"parameter":{
					"value":{
						"brokerage":100,
						"owner_address":"410ffe4eb0f39afcc431fdb22d77d2263161ea2106"
					},
					"type_url":"type.googleapis.com/protocol.UpdateBrokerageContract"
				},
				"type":"UpdateBrokerageContract"
			}
		],
		"ref_block_bytes":"d850",
		"ref_block_hash":"63c8641e2cf43e43",
		"expiration":1713434061000,
		"timestamp":1713434002484
	},
	"raw_data_hex":"0a02d850220863c8641e2cf43e4340c8d18385ef315a55083112510a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746542726f6b6572616765436f6e747261637412190a15410ffe4eb0f39afcc431fdb22d77d2263161ea2106106470b4888085ef31"
}
before sign transaction hex string is 0a730a02d850220863c8641e2cf43e4340c8d18385ef315a55083112510a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746542726f6b6572616765436f6e747261637412190a15410ffe4eb0f39afcc431fdb22d77d2263161ea2106106470b4888085ef31
Please confirm and input your permission id, if input y or Y means default 0, other non-numeric characters will cancel transaction.
```

Check and confirm the transaction, input `y` and press "Enter", and then input the password according to the prompts and wait for the transaction to be completed. If the transaction is successful, you will see the words `UpdateBrokerage successful !!!`.

```
y
Please choose your key for sign.
Please input your password.
password: 
after sign transaction hex string is 0a730a02d850220863c8641e2cf43e43409bb8a68fef315a55083112510a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746542726f6b6572616765436f6e747261637412190a15410ffe4eb0f39afcc431fdb22d77d2263161ea2106106470b4888085ef3112417b6e186b3ceb00af97d38267ff5b2379dd981eeb7d972745c81a588e6e37b6111dd005f4434943ad255cbf600e0d37a06a2e48996b490c68fd888974a7d90e3b01
txid is 2020feb596fdbda28b3ba3243978aedf39f8aaafe2e2c8917eb1fd8370a74d1b
UpdateBrokerage successful !!!
```

## 5\. (Optional) Set the SR account name

Any account can set its account name, but only once. In order to facilitate community publicity and promotion, it is recommended that SRs set their account names. **Remember: each account name can only be set once**.

If you want to set the account name, enter the command `UpdateAccount` in wallet-cli with the parameter: account name. The account name in this example is "SR-Name":

```
wallet> UpdateAccount SR-Name
{
	"raw_data":{
		"contract":[
			{
				"parameter":{
					"value":{
						"account_name":"SR-Name",
						"owner_address":"TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb"
					},
					"type_url":"type.googleapis.com/protocol.AccountUpdateContract"
				},
				"type":"AccountUpdateContract"
			}
		],
		"ref_block_bytes":"da37",
		"ref_block_hash":"71fd967d003f6932",
		"expiration":1713435582000,
		"timestamp":1713435522526
	},
	"raw_data_hex":"0a02da37220871fd967d003f693240b0bce085ef315a5a080a12560a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e4163636f756e74557064617465436f6e747261637412200a0753522d4e616d651215410ffe4eb0f39afcc431fdb22d77d2263161ea210670deebdc85ef31"
}
before sign transaction hex string is 0a780a02da37220871fd967d003f693240b0bce085ef315a5a080a12560a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e4163636f756e74557064617465436f6e747261637412200a0753522d4e616d651215410ffe4eb0f39afcc431fdb22d77d2263161ea210670deebdc85ef31
Please confirm and input your permission id, if input y or Y means default 0, other non-numeric characters will cancel transaction.
```

Check and confirm the transaction, input `y` and press "Enter", and then input the password according to the prompts and wait for the transaction to be completed. If the transaction is successful, you will see the words `Update Account successful !!!!`.

```
y
Please choose your key for sign.
Please input your password.
password: 
after sign transaction hex string is 0a780a02da37220871fd967d003f693240bb9b8390ef315a5a080a12560a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e4163636f756e74557064617465436f6e747261637412200a0753522d4e616d651215410ffe4eb0f39afcc431fdb22d77d2263161ea210670deebdc85ef3112419fd9833e248e6c814b92179e38de7a0ecaa4cdd221acfdbe4a729c8142d8858a45ceb8dc3cda954188384b68b1a7c603cbfb94ce23982c5812aa563a7a26ee4b00
txid is 57b6c8b53c0a7c61b43030a4cba724e826b9b3b8d1ace60612e13c6861203659
Update Account successful !!!!
```

After setting the account name, you can query it through the walllet-cli `getaccount` command.

## 6\. Run an SR node

An SR needs to run a TRON node to participate in block production, and will receive corresponding rewards.

The process of node construction is as follows:

1. [Download the latest data snapshot](https://developers.tron.network/docs/main-net-database-snapshots)
2. Deploy a node - [Node Deployment Guide](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode)

After starting the node, how to check whether the node synchronization is completed? You can query the latest block height of the local node through the interface [/wallet/getnowblock](/reference/wallet-getnowblock) or [wallet/getnodeinfo](reference/wallet-getnodeinfo), and compare it with the result displayed on TRONSCAN. If the results are consistent, it means that the local node block synchronization has been completed and the status is normal. Activities including transaction verification and broadcast, as well as block processing and production can be conducted. Please note that only when the number of votes received by the SR candidate account ranks among the top 27, that is, after the candidate becomes an SR, the node will produce blocks.

## 7\. (Optional) Participate in proposal creating and voting

The upgrade and governance of the TRON network need to be completed through proposals. A proposal can modify one or more on-chain parameters. Each SR, SR partner, and SR candidate has the right to initiate proposals to modify TRON network parameters, but only SRs have the right to vote on proposals.

**Initiate a proposal**

Enter the command "CreateProposal" in wallet-cli, along with the dynamic parameter number and its value. In this example, the value of parameter No. 70 is modified to 15.

```
wallet> CreateProposal 70 15
{
	"raw_data":{
		"contract":[
			{
				"parameter":{
					"value":{
						"owner_address":"TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb",
						"parameters":[
							{
								"value":15,
								"key":70
							}
						]
					},
					"type_url":"type.googleapis.com/protocol.ProposalCreateContract"
				},
				"type":"ProposalCreateContract"
			}
		],
		"ref_block_bytes":"2d3e",
		"ref_block_hash":"a672a46dfaa0c5dc",
		"expiration":1713502020000,
		"timestamp":1713501961789
	},
	"raw_data_hex":"0a022d3e2208a672a46dfaa0c5dc40a0c3b7a5ef315a58081012540a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c437265617465436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612040846100f70bdfcb3a5ef31"
}
before sign transaction hex string is 0a760a022d3e2208a672a46dfaa0c5dc40a0c3b7a5ef315a58081012540a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c437265617465436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612040846100f70bdfcb3a5ef31
Please confirm and input your permission id, if input y or Y means default 0, other non-numeric characters will cancel transaction.
```

Check and confirm the transaction, input `y` and press "Enter", and then input the password according to the prompts and wait for the transaction to be completed. If the transaction is successful, you will see the words `CreateProposal successful !!`.

```
y
Please choose your key for sign.
Please input your password.
password: 
after sign transaction hex string is 0a760a022d3e2208a672a46dfaa0c5dc40b1acdaafef315a58081012540a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c437265617465436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210612040846100f70bdfcb3a5ef311241b13d61162cb44bd1a8cc7e2129a93cb7650a39bd679a48d3a7052abef9d9d29736158be610214e242c8059e205bfe50c572c4d8fc1ae37177ddf373f09cf87bf01
txid is 854da5d9d2577894a061a2b3aee46075532d40ac2f047a699887c00bf2d6cbf1
CreateProposal successful !!
```

**SRs vote for proposals**\
Enter the command "ApproveProposal" in wallet-cli, along with the proposal ID and `true`. You can use the "ListProposals" command to view the ID of the proposal just created. In this example, the ID of the proposal just created is 19602.

```
wallet> ApproveProposal 19602 true
{
	"raw_data":{
		"contract":[
			{
				"parameter":{
					"value":{
						"proposal_id":19602,
						"is_add_approval":true,
						"owner_address":"TBRmnXKMEVfQ8XeQA2NroC9cGi77TvPbNb"
					},
					"type_url":"type.googleapis.com/protocol.ProposalApproveContract"
				},
				"type":"ProposalApproveContract"
			}
		],
		"ref_block_bytes":"2e24",
		"ref_block_hash":"158e49f435409805",
		"expiration":1713502734000,
		"timestamp":1713502675384
	},
	"raw_data_hex":"0a022e242208158e49f43540980540b08de3a5ef315a59081112550a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c417070726f7665436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210610929901180170b8c3dfa5ef31"
}
before sign transaction hex string is 0a770a022e242208158e49f43540980540b08de3a5ef315a59081112550a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c417070726f7665436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210610929901180170b8c3dfa5ef31
Please confirm and input your permission id, if input y or Y means default 0, other non-numeric characters will cancel transaction.
```

Check and confirm the transaction, input `y` and press "Enter", and then input the password according to the prompts and wait for the transaction to be completed. If the transaction is successful, you will see the words `ApproveProposal successful !!!`.

```
y
Please choose your key for sign.
Please input your password.
password: 
after sign transaction hex string is 0a770a022e242208158e49f435409805408cf385b0ef315a59081112550a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c417070726f7665436f6e7472616374121d0a15410ffe4eb0f39afcc431fdb22d77d2263161ea210610929901180170b8c3dfa5ef3112416653d14145ea0a861cdbb41d38fb5e46023cfa5dde9ce523e87c75ceb86e4dbe6e93b4fe2bb2c32f40812dbea40a551fe490fefd7aeb73d4ec55cbe7a71c924c00
txid is 3c3262aaee16e58bacc9f345a0422e08972a446c5859807e11d9b32f19f02afc
ApproveProposal successful !!!
```
