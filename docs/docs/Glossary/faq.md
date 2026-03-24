---
title: FAQ
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
# 1. Why do I need to submit the `fee_limit` field when sending a transaction to call a smart contract？

**Answer**  
Prevent the contract call transaction from consuming too much Energy.

**Explanation**  
The `fee_limit`indicates the value of the total Energy that a contract caller can tolerate at most for this transaction. The base unit is sun, and the maximum value can be set to 1.5e10. If the user does not set `fee_limit`, the default value is 0. For example, if the `fee_limit` is set to 1000 sun in the transaction, it means that the contract caller will endure the transaction and consume up to 1000/100 Energy (the current unit price of Energy is 100 sun).

If the amount of Energy consumed by the transaction execution exceeds the `fee_limit`*Energy unit price, contract execution will be stopped and an `OUT_OF_ENERGY` error will be triggered.

In some contract functions, there will be complex loops. If the user calls it by mistake without knowing it, it may cause the user to consume too much Energy, so the user can set this `fee_limit`field as an upper limit.

There are some situations that cause all `fee_limit` to be deducted:

* If encountering an llegal instruction during contract execution
* Contract call timeout, trigger `OUT_OF_TIME` error
* If the array index you are accessing is too large or negative (for example,  `x[i]` where `i >= x.length` or `i < 0`).
* If you access a fixed length of `bytesN` the index is too large or negative.
* If you use zero as a divisor for division or modulo operations (for example, 5 / 0 or 23 % 0 ).
* If you shift the negative digit.
* If you convert a value that is too large or a negative value to an `enum` type.
* If you call an uninitialized internal function type variable.
* If you call the argument of the assert (expression), and the final result is false.
* If a `JVMStackOverFlowException` occurs.
* If an `OutofMem` exception occurs, that is, memory exceeds 3M.
* During contract operation, an overflow occurs, such as addition.
* After Dynamic Energy Model is applied, the fee for calling a certain contract may vary during different maintenance cycles.

***

# 2. Why would I trigger the`OUT_OF_TIME` error when calling the contract function?

**Answer**  
The contract function is too complex or the performance of the SR node fluctuates.

**Explanation**  
At present, TRON has a global setting: the execution time of calling smart contract transactions cannot exceed 80ms. This 80ms parameter can be modified by SR voting. If the contract code is very complex and the execution time exceeds 80ms, it will trigger an `OUT_OF_TIME` error and deduct all `fee_limit` fees.

If the same contract function sometimes triggers the `OUT_OF_TIME` error, sometimes it does not trigger the `OUT_OF_TIME` error, indicating that the complexity of the contract code is at a critical value. Because the machine performance of different SRs is different, it will cause intermittent triggering.

In addition, it should be noted that due to the fluctuation of SR machine performance, there will be a small probability that the contract function call with very low complexity will also trigger the `OUT_OF_TIME` error. It is recommended that users set the appropriate `fee_limit` according to the contract complexity, to prevent excessive losses caused by the excessive setting of `fee_limit`.

***

# 3. Common token destruction addresses

Following a common industry practice, addresses like “0”, “1", “2”, and “dead” function as generic null addresses or burn addresses. They are often associated with token burn (reducing total supply) and mint/genesis events.

These addresses are not owned by any known user, and any assets transferred to them become permanently inaccessible and irrecoverable.

|            | Hex Format                                   | Base58Check Format                   |
| :--------- | :------------------------------------------- | :----------------------------------- |
| **"0"**    | `410000000000000000000000000000000000000000` | `T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb` |
| **"1"**    | `410000000000000000000000000000000000000001` | `T9yD14Nj9j7xAB4dbGeiX9h8unkKLxmGkn` |
| **"2"**    | `410000000000000000000000000000000000000002` | `T9yD14Nj9j7xAB4dbGeiX9h8unkKT76qbH` |
| **"dead"** | `41000000000000000000000000000000000000dead` | `T9yD14Nj9j7xAB4dbGeiX9h8upfCg3PBbY` |

***

# 4. How to troubleshoot when calling the contract and return the `revert` error?

**Answer**

1. First, according to txid, query the `contractResult` field in the result returned through the `wallet/gettransactioninfobyid` interface. If the field is not empty, you can see the abi code value of the message, convert the code value into a string, and find the reason for the error.  
   For example, `txid:e5e013e81cb50a4c495a11c8130ad165a4e98d89b9e3fb5b79e6111bf23b31ed`  
   Returns the following contractResult data:
   ```
    "contractResult": [
   "08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001e536166654d6174683a207375627472616374696f6e206f766572666c6f770000"  
    ]
   ```
   Converting `1e536166654d6174683a207375627472616374696f6e206f766572666c6f77` into a string is: `SafeMath: subtraction overflow`, this transaction is failed due to the transfer address overflowing during the subtraction operation when transferring. The specific failure may be caused by insufficient balance. You need to check the address balance and transfer amount. Other errors can be checked according to the specific reason of the error.
2. If the `contractResult` field is empty, it may be caused by the failure of the `require` assertion without a message in the contract. For details, please refer to the [documentation](https://developers.tron.network/docs/vm-exception-handling#require-style-exception) and view the contract source code for analysis.

***

# 5. How to calculate the Bandwidth and Energy consumed when calling/deploying a contract?

**Answer**

The amount of Bandwidth a transaction consumes is equal to the number of bytes occupied by the on-chain transaction. This includes the following three components:

* The `raw_data` of the transaction
* The transaction signature(s)
* The transaction result

The total Bandwidth consumed by the transaction is the combined number of bytes occupied by these three parts after protobuf serialization encoding.

You can estimate the Bandwidth required for a transaction before broadcasting it. Below are examples of how to do this using Trident and TronWeb.

1. **Estimate Bandwidth with Trident**

   Trident provides a Bandwidth estimation API: [estimateBandwidth](/reference/apis-transactions#estimatebandwidth), which takes a signed transaction as its parameter. The interface is implemented as follows:

   ```
   public long estimateBandwidth(Transaction txn) 
   {
       long byteSize = txn.toBuilder().clearRet().build().getSerializedSize() + 64;
       return byteSize;
   }
   ```

   In this implementation, `64` represents the fixed number of bytes occupied by the transaction result.

2. **Estimate Bandwidth with TronWeb**  
   The following function estimates the Bandwidth for a signed transaction.

   ```
   function estimateBandwidth(signedTxn)
   {
       var DATA_HEX_PROTOBUF_EXTRA = 3;
       var MAX_RESULT_SIZE_IN_TX = 64;
       var A_SIGNATURE = 67;

       var len = signedTxn.raw_data_hex.length /2 + DATA_HEX_PROTOBUF_EXTRA + MAX_RESULT_SIZE_IN_TX  ;
       var signatureListSize = signedTxn.signature.length
       console.log(signatureListSize)
       for(let i=0;i<signatureListSize;i++)
       {
           len += A_SIGNATURE;
       }
       return len;
   }
   ```

In addition to Bandwidth, a contract invocation or deployment transaction also consumes Energy. Energy is deducted based on the instructions executed by the contract. Different instructions are deducted differently. The more complex the contract, the more Energy will be consumed. The Energy consumed by the current contract can be estimated by testing on the testnet or viewing the previous historical calls of the contract through tronscan, or invoking API. For how to use API to estimate the Energy consumption of a contract invocation transaction or a contract deployment transaction, please refer to [here](/docs/set-feelimit#how-to-estimate-energy-consumption).

***

# 6. After the transaction broadcast is successful, why can't it be queried on the chain?

**Answer**  
The transaction broadcast is successful but not on the chain because the transaction is not broadcast to the SR node because of the node's network or other unknown reasons. In this case, because the transaction has a validity period, it is best to add a delay judgment, and add it after the transaction validity period. If a little extra time is not on the chain, it can be judged that the transaction has exceeded the validity period, and the transaction can be initiated again, or the transaction can be rebroadcast within the validity period.

***

# 7. How to solve `OUT_OF_ENERGY` error?

**Answer**

1. A contract call will fail if the initiating address has insufficient TRX to cover the required Energy or Bandwidth costs. To ensure successful transactions, please maintain adequate TRX balance in the calling address at all times. For resource consumption estimates, please refer to [Calculating Bandwidth and Energy Usage](https://developers.tron.network/docs/faq#5-how-to-calculate-the-bandwidth-and-energy-consumed-when-callingdeploying-a-contract).
2. If a transaction fails despite sufficient TRX balance, the issue may be caused by an inadequate `feeLimit` setting. The `feeLimit` parameter determines the maximum TRX amount that can be used to cover resource deficits. To resolve this, please increase your `feeLimit` value to ensure successful transaction processing.
3. Getting more Energy (Low Energy Solutions)  
   If you frequently experience low Energy levels, you can acquire more through these reliable methods:  
   Stake TRX for Energy & Voting Rights: Stake directly through [Tronscan explorer](https://tronscan.org) or [TronLink Wallet](https://www.tronlink.org). This method is simple, secure, and allows you to participate in TRON governance with voting rights. For detailed guidance, refer to [Staking on the TRON network](https://developers.tron.network/docs/staking-on-tron-network).  
   Rent Energy via JustLend DAO [Energy Rental Market](https://app.justlend.org/energyRental?lang=en-US\&pre=EnergyRent\&from=portal): An instant Energy access without asset freezing. This method provides fast, flexible access to Energy with transparent pricing and adjustable rental terms. For more information, refer to [Energy Rental Documentation]().

***

# 8. How to solve the problem of slow node block synchronization or stop synchronization?

**Answer**

1. Improve machine configuration, recommend 16core 32GRAM 1T hard drive (ssd)  
   In the result of the following command, the maximum value of both cpu cores and siblings needs to be greater than or equal to 16.
   ```
   $cat /proc/cpuinfo | grep -e "cpu cores"  -e "siblings" | sort | uniq  
   cpu cores   : 8  
   siblings    : 16
   ```
2. Increase the time tolerance of verification transactions  
   Increase the value of the maxTimeRatio configuration item in the node configuration file to 20.0 or higher.
   ```
   vm = {  
     supportConstant = false  
     minTimeRatio = 0.0  
     maxTimeRatio = 20.0  
     saveInternalTx = false  
   }
   ```
3. Modify `java-tron` startup parameters to increase parallel garbage collection parameters：`XX:+UseConcMarkSweepGC` and `-Xmx`  
   For example:
   ```
   java -Xmx24g -XX:+UseConcMarkSweepGC -jar FullNode.jar -c .....
   ```
   Where:
   * `-XX:+UseConcMarkSweepGC` should be placed before the `-jar` parameter, not at the end
   * `-Xmx` can be set to 80% of physical memory

***

# 9. How to solve SERVER_BUSY error?

**Answer**  
If the number of unprocessed transactions of the node exceeds 2000, a server busy error will be returned. According to the machine situation, you can increase the `PendingSize` by modifying the `node.maxTransactionPendingSize` in the node configuration file. For example, set `node.maxTransactionPendingSize = 5000`.

***

# 10. How to solve the error of TronGrid 503 Service Temporarily Unavailable?

**Answer**  
In order to ensure a reasonable allocation of requested resources, TronGrid currently has IP [frequency limits](https://cn.developers.tron.network/reference/rate-limits) for all requests. TronGrid will return a 4xx or 5xx error code when the access frequency limit is exceeded. The solution is:

1. Make sure you use the API Key in the URL. Requests without an API Key will be severely rate limited or even rejected outright.
2. You can appropriately reduce the request frequency, for example, limit the number of requests when the Dapp starts; Don't use polling for TronGrid very often, the TRON network produces a block around every 3s, and thus it usually doesn’t make sense to request new data at a faster speed.

***

# 11. How to solve no `Constant_result` in the transaction when user triggers the `pure` or `view` methods of the contract.

**Answer**  
This issue is currently only seen when users downgrade the java-tron version from GreatVoyage-v4.2.2 (Lucretius) or other higher versions to GreatVoyage-v4.2.1 (Origen) (or GreatVoyage-v4.2.0 (Plato)). If users encounter this problem, they need to use a repair tool to repair the database. After the repair is complete, users can use GreatVoyage-v4.2.2.1 (Epictetus) or later versions to start the node normally. Please refer to the detailed operation steps from [DBReqair.jar User Guide](https://developers.tron.network/docs/greatvoyage-422lucretius#dbreqairjar-user-guide).

***

# 12. Broadcast Response Code

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Error Code
      </th>

      <th>
        Cause
      </th>

      <th>
        Solution
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `SIGERROR`
      </td>

      <td>
        Signature error
      </td>

      <td>
        1. Check whether the private key used for the sign belongs to the address which sends the transaction.
        2. Check the format of the input private key.
      </td>
    </tr>

    <tr>
      <td>
        `BANDWITH_ERROR`
      </td>

      <td>
        There is not enough Bandwidth/Energy or TRX to burn to send a transaction.
      </td>

      <td>
        Deposit TRX in the account, or use another account to delegate resources to this account.
      </td>
    </tr>

    <tr>
      <td>
        `DUP_TRANSACTION_ERROR`
      </td>

      <td>
        Having broadcast a transaction with the same transaction hash with a former transaction.
      </td>

      <td>
        1. Rebuild a transaction.
        2. Change a node to broadcast.
      </td>
    </tr>

    <tr>
      <td>
        `TAPOS_ERROR`
      </td>

      <td>
        The transaction and its reference block are not in the same chain.
      </td>

      <td>
        1. Change the field value of `trx.reference.block` to `solid` for transactions created by local nodes.
        2. Try to refer to the newest solidified block for transactions that are constructed locally.
      </td>
    </tr>

    <tr>
      <td>
        `TOO_BIG_TRANSACTION_ERROR`
      </td>

      <td>
        The transaction is too big, which may be caused by a too long memo.
      </td>

      <td>
        Reduce the size of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        `TRANSACTION_EXPIRATION_ERROR`
      </td>

      <td>
        The transaction is expired.  
        The default transaction expiration time is 60 seconds. If the time period between transaction creation and broadcast is over 60 seconds, the transaction will be regarded as expired.
      </td>

      <td>
        Broadcast the transaction before its expiration time.

        1. If transaction is created through your node API, you can change the transaction expiration time In your local node configuration file, `trx.expiration.timeInMilliseconds = 60000`.
        2. If transaction is created through public node API, the transaction expiration time can not be changed, the default value is 60 seconds.
        3. If the transaction is constructed locally, please set a larger expiration time.
      </td>
    </tr>

    <tr>
      <td>
        `SERVER_BUSY`
      </td>

      <td>
        The whole network is busy.
      </td>

      <td>
        Wait. Stagger the busy time of the network before.
      </td>
    </tr>

    <tr>
      <td>
        `NOT_ENOUGH_EFFECTIVE_CONNECTION`
      </td>

      <td>
        The reason is the node has not synchronized to the newest block.
      </td>

      <td>
        Check the current block height on Tronscan, compare the height with the result of `/wallet/getnowblock` of the local node.
      </td>
    </tr>

    <tr>
      <td>
        `OTHER_ERROR`
      </td>

      <td>
        Unknown error.
      </td>

      <td>
        The detailed error information can only be obtained through the node log.
      </td>
    </tr>

    <tr>
      <td>
        `NO_CONNECTION`
      </td>

      <td>
        The node has no available connection
      </td>

      <td>
        Configure seed node, then restart the node.
      </td>
    </tr>

    <tr>
      <td>
        `CONTRACT_EXE_ERROR`
      </td>

      <td>
        Generally, contract execution fails due to runtime exceptions or illegal protobuf exceptions.
      </td>

      <td>
        Detailed error information can be obtained through node logs.
      </td>
    </tr>

    <tr>
      <td>
        `BLOCK_UNSOLIDIFIED`
      </td>

      <td>
        The number of unsolidified blocks on the node is too many and exceeds the threshold set by `node.maxUnsolidifiedBlocks`.
      </td>

      <td>
        Wait for the node status to return to normal before broadcasting the transaction. If it is a self-built node, you can also turn off the unsolidified block number check function by configuring `node.unsolidifiedBlockCheck`, or set a smaller threshold through `node.maxUnsolidifiedBlocks`.
      </td>
    </tr>

    <tr>
      <td>
        `CONTRACT_VALIDATE_ERROR`
      </td>

      <td>
        Transaction (system contract) verification failed
      </td>

      <td>
        Any parameter error may cause this error, need to parse the error message to view the details with [hex-to-string-converter](https://codebeautify.org/hex-string-converter) . Common error messages are shown in the table below.
      </td>
    </tr>
  </tbody>
</Table>

**`CONTRACT_VALIDATE_ERROR`Common Error Messages Description**

|                                           |                                                                                                |
| :---------------------------------------- | :--------------------------------------------------------------------------------------------- |
| account does not exist                    | The account that initiated the transaction is not activated                                    |
| Validate *** error, no OwnerAccount       | The owner address is incorrect                                                                 |
| No contract or not a valid smart contract | The contract address is incorrect                                                              |
| this node does not support constant       | The `vm.supportconstant` of the node is not set to `true`. This is common in self-built nodes. |

***

# 13. How to speed up the node startup process？

**Answer**

For nodes using LevelDB, the **LevelDB Startup Optimization Tool** can speed up node startup by optimizing the manifest file size and LevelDB initialization to reducing memory usage. See the [User Guide](https://tronprotocol.github.io/documentation-en/using_javatron/toolkit/#leveldb-startup-optimization-tool) for detailed instructions.

***

# 14. How to use TronWeb to invoke contract whose ABI is not on the chain?

**Answer**  
Please refer to the document: [How to use TronWeb to invoke contract whose ABI is not on the chain](https://tronweb.network/docu/docs/API%20List/contract/tronweb.contract).

***

# 15. How to judge the funds transferring in and out of an address by scanning the block?

**Answer**  
For exchange or wallet, it is usually necessary to obtain historical transaction information of an account, or to monitor the real-time transfer of funds from an account address. The exchange or wallet can build a full node, and then obtain the transaction records of the account address by parsing historical blocks, for more details please refer to [here](https://developers.tron.network/docs/exchangewallet-integrate-with-the-tron-network#parse-blocks-to-get-transaction-records).

***

# 16. Why do two transfer transactions of the same TRC-20 token consume different Energy?

**Answer:** This is mainly caused by two factors: the storage state of the recipient account and the dynamic energy model.

1. Storage State Difference (`SSTORE` Instruction Cost)

In the TVM, the `SSTORE` instruction is used to save word to storage. Its energy consumption depends on the state of a storage slot:

* Original value is 0 and new value is greater than 0: Executing `SSTORE` consumes **20,000** Energy.
* Original value is not 0: Executing `SSTORE` consumes **5,000** Energy.

TRC20 token transfers typically involve the execution of the `SSTORE` instruction (to change account balance). Therefore, the energy consumption of a TRC20 transfer transaction will vary based on the actual storage state of the recipient.

2. Impact of the Dynamic Energy Model

For popular TRC20 token contracts, due to the influence of the **[Dynamic Energy Model](/docs/resource-model#/dynamic-energy-model)**, the energy consumption may vary even for the same operation executed at different times.

3. Examples

Taking the popular **USDT** contract as an example, its energy consumption is affected by the dynamic energy model. Currently, the energy consumption for a USDT transfer transaction usually falls within the following magnitude:

* Transfer to an address with USDT balance > 0: approximately 64,000 Energy, [Example transaction](https://tronscan.io/#/transaction/60a254a511a6ecf9b3e180770c22fdc864fb1f221976822fa1332d26b6402d16).
* Transfer to an address with USDT balance = 0: approximately 130,000 Energy, [Example transaction](https://tronscan.io/#/transaction/c1f8ec2e4a7c3260206832517d6217894229c6230b06e1dd98c9af615c608882).

  Note: Actual energy consumption is variable. These values are for reference only and represent the magnitude of the energy consumption. The consumption value fluctuates with changes in the USDT contract's `energy_factor`, and any consumption near this magnitude is considered reasonable, depending on the network's real-time status at that time.

In contrast, for TRC20 contracts that have not triggered the dynamic energy mechanism,  their energy consumption is relatively fixed and is not affected by the dynamic energy model. Taking [BTT](https://tronscan.io/#/contract/TAFjULxiVgT4qWk6UZwjqwZXTSaGaqnVp4/code) as an example, the estimated energy consumption for a transfer is:

* Transfer to an address with BTT balance > 0: Approximately 13,253 energy. [Example transaction](https://tronscan.io/#/transaction/32e11d0b9b9e0db33c29fe5bc2b9a2c82e5b027954e3a1320cb02ed30fae8a65).
* Transfer to an address with BTT balance = 0: Approximately 28,253 energy. [Example transaction](https://tronscan.io/#/transaction/c6b06b116c264305860b12d471ae7a8716cc8839f3738546632dbe1377695a7b).

***

# 17. Why does it prompt ‘Permission denied’ when using multi-signature for Stake 2.0 staking?

**Answer**

For accounts activated before the mainnet [Stake 2.0](https://coredevs.medium.com/committee-proposal-84-a3e0894bebd8) took effect, when using multi-signatures to initiate Stake 2.0 related transactions, it may prompt ‘Permission denied’.

The reason is that the multi-sign permission operations of the accounts activated before Stake 2.0 took effect does not contain permission for Stake 2.0. You need to update the multi-signature settings of your account,  add one or more Stake 2.0 related permissions to your current account according to your needs in the multi-signature permission operations, below is the TronLink wallet permission update page,

<Image align="center" border={false} width="50% " src="https://files.readme.io/60568ad-image.png" />

***

# 18. How to parse `raw_data_hex` data in transaction?

**Answer**

The structure of a transaction `raw_data` is as below, and the result of serializing `raw_data` is hex string `raw_data_hex`.

```
{
  .......
  "raw_data": 
  {
        "contract": 
        [
            {
                "parameter": {
                    "value": {
                        "data": "a9059cbb00000000000000000000000074178942c355dc4b88f3a43499a18e4990ed6cf7000000000000000000000000000000000000000000000000000000012a05f200",
                        "owner_address": "41b3dcf27c251da9363f1a4888257c16676cf54edf",
                        "contract_address": "41eca9bc828a3005b9a3b909f2cc5c2a54794de05f"
                    },
                    "type_url": "type.googleapis.com/protocol.TriggerSmartContract"
                },
                "type": "TriggerSmartContract"
            }
        ],
        "ref_block_bytes": "1b98",
        "ref_block_hash": "4e1c1e7428d1d7a4",
        "expiration": 1719223548000,
        "fee_limit": 30000000,
        "timestamp": 1719223489371
    },
    "raw_data_hex": "0a021b9822084e1c1e7428d1d7a440e0f0d5cd84325aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541b3dcf27c251da9363f1a4888257c16676cf54edf121541eca9bc828a3005b9a3b909f2cc5c2a54794de05f2244a9059cbb00000000000000000000000074178942c355dc4b88f3a43499a18e4990ed6cf7000000000000000000000000000000000000000000000000000000012a05f20070dba6d2cd843290018087a70e"
}
```

Below is an example code using Trident SDK to parse the `raw_data_hex` in transaction:

```
import com.google.protobuf.Any;
import com.google.protobuf.InvalidProtocolBufferException;
import org.tron.trident.abi.TypeDecoder;
import org.tron.trident.abi.datatypes.Address;
import org.tron.trident.abi.datatypes.generated.Uint256;
import org.tron.trident.core.utils.ByteArray;
import org.tron.trident.crypto.Hash;
import org.tron.trident.proto.Chain.Transaction;
import org.tron.trident.proto.Contract;
import org.tron.trident.proto.Contract.TriggerSmartContract;
import java.math.BigInteger;

public class Demo {
    public void parseRawDataHex() throws InvalidProtocolBufferException {
        ApiWrapper client = ApiWrapper.ofNile("3333333333333333333333333333333333333333333333333333333333333333");

        String rawDataHexString = "0a021b9822084e1c1e7428d1d7a440e0f0d5cd84325aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a1541b3dcf27c251da9363f1a4888257c16676cf54edf121541eca9bc828a3005b9a3b909f2cc5c2a54794de05f2244a9059cbb00000000000000000000000074178942c355dc4b88f3a43499a18e4990ed6cf7000000000000000000000000000000000000000000000000000000012a05f20070dba6d2cd843290018087a70e";

        Transaction.raw rawData = Transaction.raw.parseFrom(ByteArray.fromHexString(rawDataHexString));
        System.out.println("ref_block_bytes:" +  ApiWrapper.toHex(rawData.getRefBlockBytes()) +
                "\n ref_block_hash:" + ApiWrapper.toHex(rawData.getRefBlockHash()) +
                "\n expiration:" + rawData.getExpiration() +
                "\n timestamp:" + rawData.getTimestamp() +
                "\n fee_limit:" + rawData.getFeeLimit() +
                "\n contract.type:" + rawData.getContract(0).getType() );
        Transaction.Contract contract = rawData.getContract(0);
        Any contractParameter = contract.getParameter();
        switch (contract.getType()) {
            case TriggerSmartContract:
                TriggerSmartContract triggerSmartContract = contractParameter.unpack(TriggerSmartContract.class);
                System.out.println("\n contract_address:" +  ApiWrapper.toHex(triggerSmartContract.getContractAddress()) +
                        "\n owner_address:" +  ApiWrapper.toHex(triggerSmartContract.getOwnerAddress()) +
                        "\n data:" +  ApiWrapper.toHex(triggerSmartContract.getData() ));

                // decode the data filed in contract parameter
                dataDecodingTutorial(ApiWrapper.toHex(triggerSmartContract.getData()));
                break;
            case TransferContract:
                Contract.TransferContract transferContract = contractParameter.unpack(Contract.TransferContract.class);
                break;
            default:
                break;
        }
    }

    public void dataDecodingTutorial(String DATA) {
        // DATA: a9059cbb00000000000000000000000074178942c355dc4b88f3a43499a18e4990ed6cf7000000000000000000000000000000000000000000000000000000012a05f200
        String rawSignature = DATA.substring(0,8);

        String functionSignatureExample = "transfer(address,uint256)"; //function signature
        String functionSelectorExample = Hash.sha3String(functionSignatureExample).substring(2,10); // function selector
        if(rawSignature.equals(functionSelectorExample))
        {
            Address rawRecipient = TypeDecoder.decodeAddress(DATA.substring(8,72)); //recipient address
            String recipient = rawRecipient.toString();
            Uint256 rawAmount = TypeDecoder.decodeNumeric(DATA.substring(72,136), Uint256.class); //amount
            BigInteger amount = rawAmount.getValue();

            System.out.println("Called function: " + functionSignatureExample);
            System.out.println("Transfer " + amount + " to " + recipient);
        }
    }
}
```

***

# 19. How to set reference block information for a transaction?

**Answer**

Please pay attention, the valid reference block of a transaction is the latest 65536 blocks, and generally, the latest solidified block is used as the reference block. Below is a demo code for setting reference block information.

```
public void setReference(long blockNum, byte[] blockHash) {
    byte[] refBlockNum = ByteArray.fromLong(blockNum);
    Transaction.raw rawData = this.transaction.getRawData().toBuilder()
        .setRefBlockHash(ByteString.copyFrom(ByteArray.subArray(blockHash, 8, 16)))
        .setRefBlockBytes(ByteString.copyFrom(ByteArray.subArray(refBlockNum, 6, 8)))
        .build();
    setRawData(rawData);
  }
```

***

# 20. Is there a way to temporarily bypass the transaction execution time limit for testing or debugging purposes?

**Answer**

At present, the maximum execution time for a smart contract transaction is 80 milliseconds, If this limit is exceeded, the transaction will throw an `OUT_OF_TIME` exception. However, in certain testing scenarios — such as query operations that involve heavy computation — it may be necessary to temporarily bypass the execution time limit. This can be achieved by starting the node with the `--debug` parameter. Then the node will skip the 80ms timeout check when processing transactions, meaning there will be no execution time restriction. You can then use the `/wallet/triggerconstantcontract` API to query contract data for testing or debugging purposes.

Please note that when the transaction execution time limit is bypassed, if a received block contains a transaction whose expected result is `OUT_OF_TIME`, the local execution of that transaction will produce a different result (since the TVM no longer performs the timeout check). This causes a discrepancy between the local execution result and the  recorded result in the block, which may lead to a `different resultCode` error and cause the node to stop synchronization.

Therefore, we strongly recommend that you do not perform such tests on mainnet nodes, as this could lead to unpredictable behavior. If you need to test complex contracts or long-running transactions, we suggest using a private chain environment.

***

# 21. How to stop a node at a specific block height?

To facilitate data backup or query operations, the node supports automatic shutdown when certain conditions are met. Developers can configure any one of the following conditions in the node's configuration file to control the node's shutdown behavior. Once the specified condition is met, the node will stop syncing blocks and exit automatically.

```
node {
  shutdown {
    # Stop at a specific time (based on Quartz expression)
    BlockTime  = "54 59 08 * * ?"

    # Stop at a specific block height
    BlockHeight = 33350800

    # Stop after syncing a specified number of blocks since startup
    BlockCount = 12
  }
}
```

Note: Only one of the above three options can be set at a time. If multiple options are set simultaneously, the node will fail to start and throw an error.

After the node stops and exits based on the specified condition, developers can proceed with data backup or restart the node to perform data queries.

If only query functionality is needed, the node can be started in query mode by adding the `--p2p-disable true` parameter to the startup command. In this mode, the node does not start the network module,  nor does it participate in peer discovery or block synchronization. However, it continues to provide API services, allowing developers to query the current system state. Example startup command:

```
java -jar FullNode.jar -c config.conf --p2p-disable true
```

***

# 22. How to improve a node’s network stability and resource usage Control?

To enhance the network stability of a node and maintain better control over its resource usage—especially in scenarios involving abnormal traffic or limited direct memory—developers can configure according to the following two aspects:

1. Limit the Maximum Allocated Direct Memory for the JVM  
   You can set the `MaxDirectMemorySize` JVM parameter to limit the amount of direct (off-heap) memory that a node can use. This helps prevent excessive memory usage and ensures more predictable resource allocation. A common best practice is to set this value to one-quarter of the machine’s physical memory. For example, if the node runs on a server with 16GB of physical memory, you can configure the JVM to allow up to 4GB of direct memory. The node startup command would be:
   ```
   java -XX:MaxDirectMemorySize=4g -jar FullNode.jar -c config.conf
   ```
2. **Limit Inbound and Outbound TCP Traffic**  
   To maintain better control over network usage and prevent unexpected resource consumption during periods of unusual traffic, developers can use the system's `iptables` command along with the `hashlimit` module to manage both outbound and inbound TCP traffic. The following are example configurations to throttle TCP traffic. You may adjust these parameters based on your Bandwidth capacity and specific business needs:  
   **Example 1: Limit Outbound TCP Rate**  
   This rule restricts outbound traffic to each destination IP to a maximum of 15 MB per second, with a burst limit of 30 MB:

   ```
   iptables -A OUTPUT -p tcp -m hashlimit \
     --hashlimit-name out_limit \
     --hashlimit-mode dstip \
     --hashlimit-above 15mb/sec \
     --hashlimit-burst 30mb \
     -j DROP
   ```

   **Example 2: Limit Inbound TCP Rate**  
   This rule limits the number of incoming TCP packets from each source IP to port 18888 to a maximum of 300 packets per second, with a burst limit of 600 packets:

   ```
   iptables -A INPUT -p tcp --dport 18888 -m hashlimit \
     --hashlimit-name in_limit \
     --hashlimit-mode srcip,dstport \
     --hashlimit-above 300/sec \
     --hashlimit-burst 600 \
     -j DROP

   ```

   Explanation of `hashlimit` Parameters:

   * `--hashlimit-name`: A label for the rule to make it identifiable
   * `--hashlimit-mode`: Defines the scope for rate limiting (e.g., `srcip`, `dstip`, `srcip`, `dstport`)
   * `--hashlimit-above`: The threshold rate limit
   * `--hashlimit-burst`: The maximum burst allowed above the limit
   * `-j`: Specifies the action when the threshold is exceeded (commonly `DROP` to discard packets)

***

# 23. How to resolve the issue where the node stops syncing and the log shows `different resultCode`?

During the block synchronization process, if the log contains the message `different resultCode`, it indicates that the local node produced a result different from the expected outcome recorded in the block when executing a specific transaction. This inconsistency prevents the node from continuing to sync blocks. Common causes and corresponding solutions are as follows:

1. Expected result: `SUCCESS`; actual result: `OUT_OF_TIME`
   ```
   05:32:54.591 ERROR [sync-handle-block] [DB](Manager.java:1337) different resultCode txId: ae53f8a6394d7adcc2337e0e71724f520818161cbb1f6f5d556f873b08e17c99, expect: SUCCESS, actual: OUT_OF_TIME
   ```
   **Cause**: This typically indicates that the local node took too long to execute the transaction and exceeded the allowed time limit, which is typically due to insufficient machine performance.  
   **Solution**: To ensure stable operation on the Mainnet, we strongly recommend using a machine with at least 16 CPU cores, with 8 cores being the absolute minimum requirement. You can also increase the time tolerance for transaction validation by adjusting the `maxTimeRatio` parameter in the configuration file (for example, set `maxTimeRatio = 50`). After making the adjustment, restart the node to apply the changes.
2. Expected result: `OUT_OF_ENERGY`; actual result: `SUCCESS`
   ```
   11:29:18.294 ERROR [pool-48-thread-1] [DB](Manager.java:1306) different resultCode txId: fbe7109a993b52243dc4de4087967cebc74be739d725dc27e96eb757496bd359, expect: OUT_OF_ENERGY, actual: SUCCESS
   ```
   **Cause**: Data inconsistencies exist among the local node’s databases, causing transactions that should have failed to be mistakenly marked as successful. Such database corruption may result from events like unexpected node shutdowns, hardware failures, or other issues.  
   **Solution**: It is recommended to download the [latest database snapshot](/docs/main-net-database-snapshots) and restart the node to ensure consistency across all database states.
3. Expected result:`OUT_OF_TIME`; actual result:`SUCCESS`
   ```
   06:22:13.575 ERROR [sync-handle-block] [DB](Manager.java:1323) different resultCode txId: 4ccf1feb7da348cef4190bc5d84d09d3c37160bfbdd21a0b5fd0b1d5005ead09, expect: OUT_OF_TIME, actual: SUCCESS
   ```
   **Cause**: Check if the node was started with the `--debug` parameter. When the node runs with the `--debug` parameter, it skips the default 80ms execution time limit check. This may cause transactions that should fail due to timeout to be successfully executed locally, resulting in inconsistencies with the results recorded in the block and ultimately triggering sync interruptions.  
   **Solution**: Remove the `--debug` parameter from the startup command and restart the node, then the node will resume normal synchronization.
