---
title: 'Advanced Configuration: SR Block Production Authorization'
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
Account permissions of Super Representatives (SRs) can be managed in groups through [account permission management](https://developers.tron.network/docs/multi-signature). A common use case is to authorize the block production permission to another account while retaining other control permissions. This allows for flexibility and potentially greater security.

This guide will introduce how to modify account permissions and how to configure the corresponding node when the block production permission of SR is changed.

## Modifying SR Account Permission

SRs can manage and modify their account permissions via [TRONSCAN](https://tronscan.org/#/wallet/permissions) or the [wallet/accountpermissionupdate](https://developers.tron.network/reference/accountpermissionupdate) API.

> ❗️ Note
>
> Before modifying the SR account permissions, please make sure that the corresponding block-producing node has been stopped.

## Querying SR Account Permission

Use the [wallet/getaccount](https://developers.tron.network/reference/account-getaccount) API to query SR's permission information:

```
curl --location --request POST 'https://api.nileex.io/wallet/getaccount' \
--header 'Content-Type: text/plain' \
--data-raw '{
     "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
     "visible": true
}'
```

Returns:

```
{
    "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
    ......
    "owner_permission": {
        "permission_name": "owner",
        "threshold": 1,
        "keys": [
            {
                "address": "TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ",
                "weight": 1
            }
        ]
    },
    "witness_permission": {
        "type": "Witness",
        "id": 1,
        "permission_name": "witness",
        "threshold": 1,
        "keys": [
            {
                "address": "TWDTKh7d3LzZhvBCrnWpJwGtsY2yw1NxFo",
                "weight": 1
            }
        ]
    },
    "active_permission": [
        ......
    ],
    ......
}
```

From the returned result, we can see that the SR `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ` authorizes his block production permission to the account `TWDTKh7d3LzZhvBCrnWpJwGtsY2yw1NxFo`.

## Configuring SR's Node

After the SR's witness permission was changed, configure the SR's block production node as follows:

```
// Optional.The default is empty.
// It is used when the witness account has set the witnessPermission.
// When it is not empty, the localWitnessAccountAddress represents the address of the witness account,
// and the localwitness is configured with the private key of the witnessPermissionAddress in the witness account.
// When it is empty,the localwitness is configured with the private key of the witness account.

localWitnessAccountAddress = TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ

// the private key of TWDTKh7d3LzZhvBCrnWpJwGtsY2yw1NxFo
localwitness = [ 9191d6......13f818
]

#localwitnesskeystore = [
#  "localwitnesskeystore.json"
#]
```

Where:

1. `localWitnessAccountAddress` : set the field with the SR's address: `TUZKijZ9Esy8JEkrqMpaVgtbDKKNA5p5CZ`.
2. `localwitness` : set value to the private key of the account that has been authorized the block production permission of the SR, which is the private key of `TWDTKh7d3LzZhvBCrnWpJwGtsY2yw1NxFo`.

Please note that if the witness permission of the SR is not changed, that is, the witness permission of the SR is retained by the SR, `localWitnessAccountAddress` does not need to be configured, only `localwitness` is necessary.

## Starting Node

To enable block production on a full node, include the `--witness` parameter in the startup command.

```
$ java -Xmx24g -XX:+UseConcMarkSweepGC -jar FullNode.jar --witness -c config.conf
```

Note: For more details on node deployment, please refer to [here](https://developers.tron.network/docs/deploy-the-fullnode-or-supernode).

After the node runs and syncs normally, when the node should produce a block, it will use the value of `localwitness` to sign the block data, and the signature data will be stored at the `block_header.witness_signature` field of the block. Then, this block will be verified by others. If the signed address has gained authorization of the SR's block production permission (the `block_header.raw_data.witness_address` field, which records the SR address), the block will pass the verification.
