---
title: AccountPermissionUpdate
excerpt: Update the account's permission.
api:
  file: full-node-http-api.json
  operationId: accountpermissionupdate
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
**Returns**

Transaction - JSON object: Unsigned transaction, please refer to the [Transaction](/docs/tron-protocol-transaction) chapter for the fields contained in it. Since the transaction type is `AccountPermissionUpdateContract`, the fields contained in `raw_data.contract[0].parameter.value` in the transaction are as follows:

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
        owner_address
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        Account address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        owner
      </td>

      <td style={{ textAlign: "left" }}>
        Permission
      </td>

      <td style={{ textAlign: "left" }}>
        Account's owner permission. Fields in `Permission` object contains:

        * `type` (int): Permission type.
        * `permission_name` (string): Name of the permission (e.g., ""owner"").
        * `threshold` (int64): Minimum combined weight of signatures required.
        * `parent_id` (int32): Parent permission ID (defaults to 0).
        * `operations` (string): A 32-byte hex string representing the allowed operations.
        * `keys` (Key[]): List of associated addresses and weights (max 5).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        witness
      </td>

      <td style={{ textAlign: "left" }}>
        Permission
      </td>

      <td style={{ textAlign: "left" }}>
        Witness permission details for a Super Representative (SR) account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        actives
      </td>

      <td style={{ textAlign: "left" }}>
        Permission[]
      </td>

      <td style={{ textAlign: "left" }}>
        List of active permissions for the account.
      </td>
    </tr>
  </tbody>
</Table>