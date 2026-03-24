---
title: '[full txn obj layout]TriggerSmartContract'
excerpt: >-
  Returns a `TransactionExtention` object, which encapsulates the unsigned
  transaction data.
api:
  file: full-node-http-api.json
  operationId: post_wallettriggersmartcontract-1-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
**Note:**  
Reference examples for encoding and decoding [ABI](https://solidity.readthedocs.io/en/latest/abi-spec.html#examples) parameters: [Parameter and return value encoding and decoding](https://developers.tron.network/docs/parameter-and-return-value-encoding-and-decoding)

**Returns**

**Return Object:** Unsigned Transaction (JSON)

* **General:** See [Transaction Core](/docs/...) for base fields.
* **Specific :** The table below lists the parameters for **TriggerSmartContract** found in:
  `raw_data.contract[0].parameter.value`




<Table align={["left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: 'left' }}>Transaction Structure & Instructions</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: 'left' }}>
        <code>txID</code> (String): The unique hash of the transaction, calculated from the <code>raw_data</code>.
      </td>
    </tr>


    <tr>
      <td style={{ textAlign: 'left' }}>
        <code>signature[]</code> (Array): The sender's cryptographic signature for authentication.
      </td>
    </tr>

    
  </tbody>
</Table>










<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Structure & Fields
      </th>

      <th>
        Description Summary
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <code>txID</code> (String)
      </td>

      <td>
        The unique hash of the transaction, calculated from the <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <details open style={{ padding: "12px 16px" }}>
          <summary style={{ cursor: "pointer", listStyle: "none" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span><b>raw\_data</b> (Object)</span>
              <span style={{ fontSize: "0.9em", color: "#666" }}>Metadata & TAPOS execution constraints</span>
            </div>
          </summary>

          <div style={{ marginTop: "12px", paddingLeft: "20px", borderLeft: "2px solid #eee" }}>
            <ul style={{ listStyleType: "none", padding: "0", margin: "0", lineHeight: "1.8" }}>
              <li><code>ref\_block\_bytes</code> (String): The height of the transaction reference block (6th to 8th bytes).</li>
              <li><code>ref\_block\_hash</code> (String): The hash of the transaction reference block (8th to 16th bytes).</li>
              <li><code>expiration</code> (Long): Transaction expiration time; beyond this, it won't be packed (max 24h).</li>
              <li><code>data</code> (String): The transaction memo/note (optional).</li>
              <li><code>timestamp</code> (Long): Transaction creation time.</li>
              <li><code>fee\_limit</code> (Long): Maximum Energy cost allowed for smart contract execution.</li>
            </ul>
          </div>
        </details>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <details open style={{ padding: "12px 16px" }}>
          <summary style={{ cursor: "pointer", listStyle: "none" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span><b>raw\_data.contract\[]</b> (Array)</span>
              <span style={{ fontSize: "0.9em", color: "#666" }}>Main instruction & payload details</span>
            </div>
          </summary>

          <div style={{ marginTop: "12px", paddingLeft: "20px", borderLeft: "2px solid #eee" }}>
            <p style={{ fontSize: "0.9em", color: "#444" }}>The main content of the transaction. Only one element is used at present.</p>

            <ul style={{ listStyleType: "none", padding: "0", margin: "10px 0", lineHeight: "1.8" }}>
              <li><code>type</code> (String): Transaction type (e.g., <code>TriggerSmartContract</code>).</li>

              <li>
                <details>
                  <summary style={{ cursor: "pointer", color: "#0066cc" }}><code>parameter.value</code> (Object) - Specific for <i>TriggerSmartContract</i></summary>

                  <ul style={{ listStyleType: "none", paddingLeft: "20px", marginTop: "8px", fontSize: "0.9em", color: "#555" }}>
                    <li><code>owner\_address</code> (String): Transaction initiator address.</li>
                    <li><code>contract\_address</code> (String): Target smart contract address.</li>
                    <li><code>call\_value</code> (int64): Amount of TRX transferred into the contract (Unit: <code>sun</code>).</li>
                    <li><code>data</code> (String): Function call data, containing the function selector and encoded parameters (Hex string).</li>
                    <li><code>call\_token\_value</code> (int64): Amount of TRC-10 token transferred into the contract.</li>
                    <li><code>token\_id</code> (int64): TRC-10 token ID transferred into the contract.</li>
                  </ul>
                </details>
              </li>
            </ul>
          </div>
        </details>
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <code>signature[]</code> (Array)
      </td>

      <td>
        The sender's cryptographic signature for authentication.
      </td>
    </tr>

    <tr>
      <td>
        <details style={{ padding: "12px 16px" }}>
          <summary style={{ cursor: "pointer", listStyle: "none" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span><b>internal\_transactions\[]</b> (Array)</span>
              <span style={{ fontSize: "0.9em", color: "#666" }}>Triggered actions within the TVM</span>
            </div>
          </summary>

          <div style={{ marginTop: "12px", paddingLeft: "20px", borderLeft: "2px solid #eee" }}>
            <ul style={{ listStyleType: "none", padding: "0", lineHeight: "1.8", fontSize: "0.9em" }}>
              <li><code>caller\_address</code> (String): The contract address triggering the call.</li>
              <li><code>transferTo\_address</code> (String): Recipient address (external account or contract).</li>
              <li><code>callValueInfo</code> (Array): List containing the amount of TRX/TRC10 tokens.</li>
              <li><code>note</code> (String): Instruction type (e.g., call, create).</li>
              <li><code>rejected</code> (Boolean): Whether the internal transaction failed.</li>
            </ul>
          </div>
        </details>
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Structure & Fields (Type)
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <code>txID</code> (String)
      </td>

      <td>
        The unique hash of the transaction, calculated from <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data</b> (Object)</summary>

          <ul style={{ marginTop: "10px", fontSize: "0.95em" }}>
            <li><code>ref\_block\_bytes</code> (String)</li>
            <li><code>ref\_block\_hash</code> (String)</li>
            <li><code>expiration</code> (Long)</li>
            <li><code>data</code> (String)</li>
            <li><code>timestamp</code> (Long)</li>
            <li><code>fee\_limit</code> (Long)</li>
          </ul>
        </details>
      </td>

      <td>
        <p>Transaction metadata and execution constraints:</p>

        <ul style={{ fontSize: "0.9em" }}>
          <li>The height of the transaction reference block (6th to 8th bytes).</li>
          <li>The hash of the transaction reference block (8th to 16th bytes).</li>
          <li>Transaction expiration timestamp (max 24h).</li>
          <li>The transaction memo/note.</li>
          <li>Transaction creation time.</li>
          <li>Maximum Energy allowed for execution (in <code>sun</code>).</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data.contract\[]</b> (Array)</summary>

          <ul style={{ marginTop: "10px", fontSize: "0.95em" }}>
            <li><code>type</code> (String)</li>

            <li>
              <details open>
                <summary><code>parameter.value</code> (Object)</summary>

                <ul style={{ fontSize: "0.9em", color: "#444", marginTop: "5px" }}>
                  <li><code>owner\_address</code> (String)</li>
                  <li><code>contract\_address</code> (String)</li>
                  <li><code>call\_value</code> (int64)</li>
                  <li><code>data</code> (String)</li>
                  <li><code>call\_token\_value</code> (int64)</li>
                  <li><code>token\_id</code> (int64)</li>
                </ul>
              </details>
            </li>
          </ul>
        </details>
      </td>

      <td>
        <p>The main instruction of the transaction. Currently supports exactly one element.</p>
        <p><b>TriggerSmartContract Parameters:</b></p>

        <ul style={{ fontSize: "0.9em" }}>
          <li>Initiator's account address.</li>
          <li>The target contract address.</li>
          <li>TRX amount sent to the contract (in <code>sun</code>).</li>
          <li>Data for function call (Hex format).</li>
          <li>Amount of TRC-10 tokens transferred.</li>
          <li>The unique ID of the TRC-10 token.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        <code>signature[]</code> (Array)
      </td>

      <td>
        The sender's cryptographic signature for authentication.
      </td>
    </tr>

    <tr>
      <td>
        <details>
          <summary><b>internal\_transactions\[]</b> (Array)</summary>

          <ul style={{ marginTop: "10px", fontSize: "0.9em" }}>
            <li><code>caller\_address</code> (String)</li>
            <li><code>transferTo\_address</code> (String)</li>
            <li><code>callValueInfo</code> (Array)</li>
            <li><code>note</code> (String)</li>
            <li><code>rejected</code> (Boolean)</li>
          </ul>
        </details>
      </td>

      <td>
        <p>Actions triggered within the TVM during execution:</p>

        <ul style={{ fontSize: "0.85em" }}>
          <li>Address that triggered the internal call.</li>
          <li>The recipient of the internal transfer.</li>
          <li>Amount of TRX or TRC-10 tokens involved.</li>
          <li>Instruction type (e.g., call, create).</li>
          <li>Indicates if the internal call failed.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</Table>

<br />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Structure & Fields
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <code>txID</code>
      </td>

      <td>
        String
      </td>

      <td>
        The unique hash of the transaction calculated from <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data</b></summary>

          <ul style={{ marginTop: "10px" }}>
            <li><code>ref\_block\_bytes</code></li>
            <li><code>ref\_block\_hash</code></li>
            <li><code>expiration</code></li>
            <li><code>data</code></li>
            <li><code>timestamp</code></li>
            <li><code>fee\_limit</code></li>
          </ul>
        </details>
      </td>

      <td>
        <br /><ul style={{ marginTop: "24px", listStyleType: "none", paddingLeft: "0" }}>
          <li>String</li>
          <li>String</li>
          <li>Long</li>
          <li>String</li>
          <li>Long</li>
          <li>Long</li>
        </ul>
      </td>

      <td>
        <p>Transaction metadata and constraints:</p>

        <ul style={{ fontSize: "0.9em" }}>
          <li>The height of the transaction reference block (6th to 8th bytes).</li>
          <li>The hash of the transaction reference block (8th to 16th bytes).</li>
          <li>Expiration timestamp (max 24h).</li>
          <li>The transaction memo.</li>
          <li>Transaction creation time.</li>
          <li>Maximum Energy cost for smart contract execution (in <code>sun</code>).</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data.contract\[]</b></summary>

          <ul style={{ marginTop: "10px" }}>
            <li><code>type</code></li>

            <li>
              <details>
                <summary><code>parameter.value</code></summary>

                <ul style={{ fontSize: "0.9em", color: "#444" }}>
                  <li><code>owner\_address</code></li>
                  <li><code>contract\_address</code></li>
                  <li><code>call\_value</code></li>
                  <li><code>data</code></li>
                  <li><code>call\_token\_value</code></li>
                  <li><code>token\_id</code></li>
                </ul>
              </details>
            </li>
          </ul>
        </details>
      </td>

      <td>
        <br /><ul style={{ marginTop: "24px", listStyleType: "none", paddingLeft: "0" }}>
          <li>String</li>
          <li style={{ marginTop: "24px" }}>Object</li>

          <ul style={{ listStyleType: "none", paddingLeft: "0", fontSize: "0.9em" }}>
            <li>String</li>
            <li>String</li>
            <li>int64</li>
            <li>String</li>
            <li>int64</li>
            <li>int64</li>
          </ul>
        </ul>
      </td>

      <td>
        <p>The main content of the transaction. Only one element is used at present.</p>
        <p><b>Specific for TriggerSmartContract:</b></p>

        <ul style={{ fontSize: "0.9em" }}>
          <li>Transaction initiator address.</li>
          <li>Target smart contract address.</li>
          <li>TRX amount transferred into the contract (Unit: <code>sun</code>).</li>
          <li>Function call data (Hex string).</li>
          <li>Amount of TRC-10 token transferred.</li>
          <li>TRC-10 token ID.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        <code>signature[]</code>
      </td>

      <td>
        Array
      </td>

      <td>
        The sender's signature proving authenticity and origin.
      </td>
    </tr>

    <tr>
      <td>
        <details>
          <summary><b>internal\_transactions\[]</b></summary>

          <ul style={{ marginTop: "10px" }}>
            <li><code>caller\_address</code></li>
            <li><code>transferTo\_address</code></li>
            <li><code>callValueInfo</code></li>
            <li><code>note</code></li>
            <li><code>rejected</code></li>
          </ul>
        </details>
      </td>

      <td>
        <br /><ul style={{ marginTop: "24px", listStyleType: "none", paddingLeft: "0", fontSize: "0.9em" }}>
          <li>String</li>
          <li>String</li>
          <li>Array</li>
          <li>String</li>
          <li>Boolean</li>
        </ul>
      </td>

      <td>
        <p>Transactions triggered in the TVM:</p>

        <ul style={{ fontSize: "0.85em" }}>
          <li>The contract address triggering the call.</li>
          <li>The recipient address.</li>
          <li>Amount of TRX/TRC10 tokens.</li>
          <li>Instruction type (Hex format).</li>
          <li>Execution failure status.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</Table>

<br />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Structure & Fields
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <code>txID</code> (String)
      </td>

      <td>
        The unique hash of the transaction, calculated from the <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <details>
          <summary><b>raw\_data</b> (Metadata)</summary>

          <ul style={{ marginTop: "10px" }}>
            <li><code>ref\_block\_bytes</code>: The height of the transaction reference block (6th to 8th bytes).</li>
            <li><code>ref\_block\_hash</code>: The hash of the transaction reference block (8th to 16th bytes).</li>
            <li><code>expiration</code>: Transaction expiration time, beyond which it will no longer be packed (max 24h).</li>
            <li><code>data</code>: The transaction memo (optional).</li>
            <li><code>timestamp</code>: Transaction creation time; however, the actual on-chain time is the block timestamp.</li>
            <li><code>fee\_limit</code>: Maximum Energy cost allowed for smart contract execution.</li>
          </ul>
        </details>
      </td>

      <td>
        Contains block references and execution constraints. Uses the <b>TAPOS</b> mechanism to prevent replays on forks.
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data.contract\[]</b> (Instruction)</summary>

          <p style={{ margin: "8px 0", fontSize: "0.95em" }}>
            The main content of the transaction. It is a list, but only one element is used at present.
          </p>

          <ul style={{ borderLeft: "2px solid #eee", paddingLeft: "15px" }}>
            <li><code>type</code>: Transaction type, such as <code>TransferContract</code> or <code>TriggerSmartContract</code>.</li>

            <li>
              <details open>
                <summary><code>parameter.value</code> (Specific for <i>TriggerSmartContract</i>)</summary>

                <ul style={{ fontSize: "0.9em", color: "#444", marginTop: "5px" }}>
                  <li><code>owner\_address</code> (String): Transaction initiator address.</li>
                  <li><code>contract\_address</code> (String): Target smart contract address.</li>
                  <li><code>call\_value</code> (Long): Amount of TRX transferred into the contract (Unit: <code>sun</code>).</li>
                  <li><code>data</code> (String): Function call data, containing the function selector and encoded parameters (Format: hex string).</li>
                  <li><code>call\_token\_value</code> (Long): Amount of TRC-10 token transferred into the contract.</li>
                  <li><code>token\_id</code> (Long): TRC-10 token ID transferred into the contract.</li>
                </ul>
              </details>
            </li>
          </ul>
        </details>
      </td>

      <td>
        Defines the specific action (e.g., transfer, contract call) and its required parameters.
      </td>
    </tr>

    <tr>
      <td>
        <code>signature[]</code> (Array)
      </td>

      <td>
        The sender's cryptographic signature, proving the transaction's authenticity and origin.
      </td>
    </tr>

    <tr>
      <td>
        <details>
          <summary><b>internal\_transactions\[]</b></summary>

          <ul style={{ marginTop: "10px", fontSize: "0.9em" }}>
            <li><code>caller\_address</code>: The contract address triggering the call.</li>
            <li><code>transferTo\_address</code>: Recipient address (external or contract).</li>
            <li><code>callValueInfo</code>: Amount of TRX/TRC10 tokens transferred.</li>
            <li><code>note</code>: Instruction type (e.g., <code>call</code>, <code>create</code>).</li>
            <li><code>rejected</code>: Whether the internal transaction execution failed.</li>
          </ul>
        </details>
      </td>

      <td>
        Transactions triggered in the TVM. Requires <code>saveInternalTx = true</code> in node configuration to be saved.
      </td>
    </tr>
  </tbody>
</Table>

<br />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Structure & Fields
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        <code>txID</code> (String)
      </td>

      <td>
        The unique hash of the transaction, calculated from <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <code>visible</code> (Boolean)
      </td>

      <td>
        Whether the addresses in the transaction are displayed in Base58 (true) or Hex (false).
      </td>
    </tr>

    <tr>
      <td>
        <details open>
          <summary><b>raw\_data</b></summary>

          <ul>
            <li>
              <details>
                <summary><code>contract\[]</code> (Array)</summary>

                <ul>
                  <li><code>type</code>: Transaction type (e.g., <code>TransferContract</code>, <code>FreezeBalanceV2Contract</code>).</li>

                  <li>
                    <details>
                      <summary><code>parameter</code> (Object)</summary>

                      <ul>
                        <li><code>value</code>: Specific parameters like <code>amount</code>, <code>owner\_address</code>, or <code>frozen\_balance</code>.</li>
                        <li><code>type\_url</code>: Protobuf type identifier.</li>
                      </ul>
                    </details>
                  </li>
                </ul>
              </details>
            </li>

            <li><code>ref\_block\_bytes</code>: 2 bytes height of the reference block. Used in <b>TAPOS</b> to prevent replays.</li>
            <li><code>ref\_block\_hash</code>: 8 bytes hash of the reference block.</li>
            <li><code>expiration</code>: Expiration timestamp (max 24h). Automatically set to +60s by java-tron APIs.</li>
            <li><code>data</code>: Transaction memo. Consumes 1 TRX extra fee if present.</li>
            <li><code>timestamp</code>: Creation time. Note: The block timestamp is the actual on-chain time.</li>
            <li><code>fee\_limit</code>: Max Energy cost (in <code>sun</code>) for smart contracts. 100 sun per Energy unit.</li>
          </ul>
        </details>
      </td>

      <td>
        The core data of the transaction. Only one element in the <code>contract</code> list is currently supported.
      </td>
    </tr>

    <tr>
      <td>
        <code>raw_data_hex</code> (String)
      </td>

      <td>
        The Protobuf serialized hex string of <code>raw_data</code>.
      </td>
    </tr>

    <tr>
      <td>
        <code>signature</code> (Array)
      </td>

      <td>
        List of cryptographic signatures (ECDSA). Proves the transaction originated from the sender.
      </td>
    </tr>

    <tr>
      <td>
        <details>
          <summary><b>internal\_transactions\[]</b> (Optional)</summary>

          <ul>
            <li><code>hash</code>: Internal transaction hash.</li>
            <li><code>caller\_address</code>: The contract address triggering the call.</li>
            <li><code>transferTo\_address</code>: Receiver address.</li>
            <li><code>callValueInfo</code>: Amount of TRX/TRC10 transferred.</li>
            <li><code>note</code>: Instruction type (e.g., <code>call</code>, <code>freezeBalanceV2</code>).</li>
            <li><code>rejected</code>: Whether the internal execution failed.</li>
          </ul>
        </details>
      </td>

      <td>
        Only returned via <code>/walletsolidity/*</code> and requires <code>saveInternalTx = true</code> in node config.
      </td>
    </tr>
  </tbody>
</Table>

<br />

<br />

<br />

<br />

<br />

| Field            | Type   | Description                                                                                                                                     |
| :--------------- | :----- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| owner_address    | string | Transaction initiator address.                                                                                                                  |
| contract_address | string | Contract address.                                                                                                                               |
| call_value       | int64  | Amount of TRX transferred into the contract in this call. (Unit: sun)                                                                           |
| data             | string | Function call data, containing the function selector and encoded parameters, specifying which function to execute and how. (Format: hex string) |
| call_token_value | int64  | Amount of TRC-10 token transferred into the contract.                                                                                           |
| token_id         | int64  | TRC-10 token id transferred into the contract.                                                                                                  |

### Returns

Returns an **Unsigned Transaction (JSON)**. For general field definitions, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter.

<details open>
  <summary><strong>Specific Parameters: TriggerSmartContract</strong> (<code>raw\_data.contract\[0].parameter.value</code>)</summary>

  | Field              | Type   | Description                                                                                       |
  | :----------------- | :----- | :------------------------------------------------------------------------------------------------ |
  | `owner_address`    | string | Transaction initiator address.                                                                    |
  | `contract_address` | string | Contract address.                                                                                 |
  | `call_value`       | int64  | Amount of TRX transferred into the contract in this call. (Unit: sun)                             |
  | `data`             | string | Function call data, containing the function selector and encoded parameters. (Format: hex string) |
  | `call_token_value` | int64  | Amount of TRC-10 token transferred into the contract.                                             |
  | `token_id`         | int64  | TRC-10 token id transferred into the contract.                                                    |
</details>

<br />
