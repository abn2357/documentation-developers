---
title: How to judge the recharge and withdraw funds by scanning the block?
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
1. Get block information from the solidified block according to the block number: /walletsolidity/getblockbynum

2. Get transactions from the block.

3. Iterate through transactions to get raw\_data.contract.

4. Iterate over raw\_data.contract , raw\_data.contract.type

   4.1 TRX entry: raw\_data.contract.type == transferContract 

   ```
   Check if the acceptance address and amount meet the posting criteria: /walletsolidity/gettransactioninfobyid
   ```

   4.2 TRC10 posting: raw\_data.contract.type == TransferAssetContract 

   ```
   Check if the token id, acceptance address and amount meet the entry criteria: /walletsolidity/gettransactioninfobyid
   ```

   4.3 TRC20 posting, TRX/TRC10 posting in the contract: raw\_data.contract.type == TriggerSmartContract 

   ```
   1.Check whether the transaction is successful: 
    /walletsolidity/gettransactioninfobyid query to receive.result == SUCCESS

   2.Check if it contains the transfer(address _to,uint256 _value) event: 
    /walletsolidity/gettransactioninfobyid

   3.If the transfer event is included, the event is parsed to get the contract address, transfer address, and amount in the event to determine whether the credit conditions

   4.Event parsing rules: 
    Refer to documentation: https://cn.developers.tron.network/docs/vm-event#event-%E8%A7%A3%E7%A0%81%E7%A4%BA%E4%BE%8B

   5.whether to include internal transactions, if included, then traverse the internal transactions

      a. If internal_transactions.callValueInfo ! = null & internal_transactions.callValueInfo[i].tokenId == null means it is a TRX transfer that is performed in the contract.
    Reference example transaction: https://api.nileex.io/wallet/gettransactioninfobyid?value=f66cad4376d4f611135c0a8cff4c0927fa36d4310d3c9aab20e80ddcfc8b7728
      internal_transactions.caller is the transfer address
      internal_transactions.transferTo_address is the recipient address
      internal_transactions.callValueInfo[i].callValue is the amount of the transfer

      b. If internal_transactions.callValueInfo ! = null & internal_transactions.callValueInfo[0].tokenId ! = null means that a TRC10 transfer was made in the contract.
     Reference example transaction: https://api.nileex.io/wallet/gettransactioninfobyid?value=f66cad4376d4f611135c0a8cff4c0927fa36d4310d3c9aab20e80ddcfc8b7728
       internal_transactions.caller is the remittance address
       internal_transactions.callValueInfo[i].callValue is the transfer amount
       internal_transactions.callValueInfo[i].tokenId is the TRC10 token ID
       internal_transactions.transferTo_address is the recipient address
   ```
