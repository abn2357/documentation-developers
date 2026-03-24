---
title: '[Collapsible json table]Get account info by address'
api:
  file: trongrid-v1-api.json
  operationId: get_v1accounts{address}-2
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
**Returns**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Structure & Fields
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `success` (Boolean)
      </td>

      <td style={{ textAlign: "left" }}>
        Whether the request was successful.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>meta</b></summary>

          <ul>
            <li><code>at</code> (Long): Response timestamp in ms.</li>
            <li><code>page\_size</code> (Integer): Items per page.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Response metadata.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>data</b> (Basic Info)</summary>

          <ul>
            <li><code>address</code> (String): Hex format address.</li>
            <li><code>balance</code> (Long): TRX balance in <code>sun</code>.</li>
            <li><code>account\_name</code> (String): Account identifier.</li>
            <li><code>create\_time</code> (Long): Creation timestamp.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Core account identifiers.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>data.account\_resource</b> (Resources)</summary>

          <ul>
            <li><code>energy\_usage</code> (Long): Current energy used.</li>
            <li><code>energy\_window\_size</code> (Long): Blocks for recovery.</li>
            <li><code>energy\_window\_optimized</code> (Boolean): Recovery optimization flag.</li>
            <li><code>latest\_consume\_time\_for\_energy</code> (Long): Last usage timestamp.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Real-time Energy stats.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>data.frozenV2\[]</b> (Stake 2.0)</summary>
          <p>Current active staking positions in the new model:</p>

          <ul>
            <li><code>amount</code> (Long): Staked TRX in <code>sun</code>.</li>
            <li><code>type</code> (String): <code>BANDWIDTH</code> or <code>ENERGY</code>.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Modern staking mechanism data.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>data.permissions</b> (Multi-Sig)</summary>
          <p><b>Owner Permission:</b> Root control.</p>
          <p><b>Active Permission\[]:</b> Array of custom permissions for transfers/calls.</p>

          <ul>
            <li><code>threshold</code> (Integer): Required weight sum.</li>
            <li><code>keys\[i].address</code> (String): Signer address.</li>
            <li><code>keys\[i].weight</code> (Integer): Signature weight.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Security and Multi-sig structure.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <details open>
          <summary><b>Legacy Data</b> (Stake 1.0)</summary>

          <ul>
            <li><code>frozen</code>: Bandwidth stakes from V1.</li>
            <li><code>account\_resource.frozen\_balance\_for\_energy</code>: Energy stakes from V1.</li>
          </ul>
        </details>
      </td>

      <td style={{ textAlign: "left" }}>
        Deprecated Stake 1.0 fields.
      </td>
    </tr>
  </tbody>
</Table>
