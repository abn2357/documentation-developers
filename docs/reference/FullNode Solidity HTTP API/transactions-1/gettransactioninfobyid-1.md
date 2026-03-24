---
title: GetTransactionInfoById
excerpt: Queries the transaction fee, block height by transaction id. (Confirmed state)
api:
  file: full-node-http-api.json
  operationId: gettransactioninfobyid-1
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
**Returns**

A `TransactionInfo` object containing the following fields:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Field
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction ID (hash).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `fee`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Total amount of TRX burned as fee for this transaction, including for Bandwidth/Energy, account activation, memo, multi-signature, and other operations. (Unit: sun).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `blockNumber`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Block number (height).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `blockTimeStamp`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Block timestamp. (Unit: millisecond).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `contractResult`
      </td>

      <td style={{ textAlign: "left" }}>
        string[]
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction execution results.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `contract_address`
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        Contract address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `receipt`
      </td>

      <td style={{ textAlign: "left" }}>
        ResourceReceipt
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction receipt, including execution result and transaction fee details, which contains the following fields:

        * `energy_usage`: Amount of Energy consumed in the caller's account
        * `energy_fee`: Amount of TRX burned to pay for Energy.
        * `origin_energy_usage`: Amount of Energy consumed in the contract deployer's account
        * `energy_usage_total`: Total amount of Energy consumed by the transaction.
        * `net_usage`:  Amount of Bandwidth consumed.
        * `net_fee`: Amount of TRX burned to pay for Bandwidth.
        * `result`: Transaction execution result.
        * `energy_penalty_total`: Amount of extra Energy that needs to be paid for calling a few popular contracts"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `log`
      </td>

      <td style={{ textAlign: "left" }}>
        Log[]
      </td>

      <td style={{ textAlign: "left" }}>
        List of event logs triggered during the smart contract call. Each event log includes the following information:

        * `address`: Contract address. Note that, for EVM compatibility, TVM uses a hex format address without the `0x41` prefix. When parsing an address from the log, you need to prepend `41` to form the full Tron hex address, and convert it to Base58Check if needed.
        * `topics`: The topic of the event, including the event signature and all indexed parameters.
        * `data`: The parameters that are not marked as indexed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `result`
      </td>

      <td style={{ textAlign: "left" }}>
        int
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction execution result. Omitted if successful; `FAILED` if failed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `resMessage`
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        Detailed error message if the transaction failed. (Format: hex string).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `assetIssueID`
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        The ID of the issued TRC10 token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `withdraw_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of voting rewards withdrawn to the account in this transaction. (Applies only to reward withdrawal transactions, Unit: sun).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `unfreeze_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of TRX unstaked. (Applies only to unstaking transactions for Stake 1.0, Unit: sun).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `internal_transactions`
      </td>

      <td style={{ textAlign: "left" }}>
        InternalTransaction[]
      </td>

      <td style={{ textAlign: "left" }}>
        Array of internal transactions. See [here](https://developers.tron.network/docs/tron-protocol-transaction#internal-transactions) for details.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `withdraw_expire_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of unfrozen TRX withdrawn to the account in this transaction. (Applies only to unstaking, unfrozen balance withdrawal, and cancel-all-unstakes transactions. For Stake 2.0, Unit: sun).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `cancel_unfreezeV2_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        map\<string, int64>
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of TRX re-staked (canceled unstake), keyed by resource type ("BANDWIDTH" or "ENERGY"). (Unit: sun).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `exchange_received_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of tokens received.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `exchange_inject_another_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of the other token injected into the trading pair.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `exchange_withdraw_another_amount`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        The amount of the other token withdrawn from the trading pair.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `exchange_id`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        The ID of the trading pair.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `shielded_transaction_fee`
      </td>

      <td style={{ textAlign: "left" }}>
        int64
      </td>

      <td style={{ textAlign: "left" }}>
        Shielded transaction fee.
      </td>
    </tr>
  </tbody>
</Table>
