---
title: Mainnet Database Snapshots
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
TRON officially offers database snapshots regularly for quick node deployment. A data snapshot is a compressed file of the database backup of a TRON network node at a certain time. Developers can download and use the data snapshot to speed up the node synchronization process.

# Step 1 - Choose a Data Snapshot

## Fullnode data snapshot

The following table shows the download address of Fullnode data snapshots. Please select a suitable data snapshot according to the location and node database type, and whether you need to query historical internal transactions.

| Fullnode Data Source                      | Download Site                                  | Description                                                                                                     |
| ----------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Official data source (Asia: Singapore)    | [http://34.143.247.77](http://34.143.247.77)   | LevelDB, excludes internal transactions (About 2,259G by May 5, 2025)                                           |
| Official data source (America)            | [http://34.86.86.229](http://34.86.86.229)     | LevelDB, excludes internal transactions (About 2,261G by May 6, 2025)                                           |
| Official data source (America)            | [http://35.197.17.205](http://35.197.17.205)   | RocksDB, excludes internal transactions (About 2,233G by May 6, 2025)                                           |
| Official data source (Singapore)          | [http://35.247.128.170](http://35.247.128.170) | LevelDB, includes internal transactions (About 2,447G by May 6, 2025)                                           |
| Official data source with account balance | [http://34.48.6.163](http://34.48.6.163)       | LevelDB, excludes internal transactions but includes address history TRX balance (Around 2,837G by May 6, 2025) |

**Note**：The data of LevelDB and RocksDB are not allowed to be mixed. The database can be specified in the config file of the FullNode, by settting `db.engine` to `LEVELDB` or `ROCKSDB`.

## Lite Fullnode data snapshot

The TRON Public Chain has supported the type of the Lite Fullnode since the version of the GreatVoyage-v4.1.0 release. All the data required by the Lite Fullnode for running is the entire status data and a little essential block data, therefore, it is much more lightweight (smaller database and faster startup) than the normal Fullnode. TRON officially offers database snapshots of the Lite Fullnode.

| Lite Fullnode Data Source        | Download Site                                  | Description |
| -------------------------------- | ---------------------------------------------- | ----------- |
| Official data source (Singapore) | [http://34.143.247.77/](http://34.143.247.77/) | LevelDB     |

**Tips**: You can split the data from the whole data, or prune Lite Fullnode data regularly with the help of the "Lite Fullnode Data Pruning Tool" of [Toolkit](/docs/node-maintenance-tool-toolkit).

# Step 2 - Download and Extract the Snapshot Data

The TRON network snapshot data size exceeds 2TB. To save disk space, we recommend using the streaming method, which downloads and extracts the data simultaneously. The operational commands are as follows:

**Method 1: Streamed Download and Extract (Recommended, Saves Space)**

Create a script file named `download_snapshot.sh` and add the following content:

```bash
#!/bin/bash
wget -q -O - SNAPSHOT_URL/FullNode_output-directory.tgz | tar -zxvf -
```

Run the script:

```Text Bash
bash download_snapshot.sh
```

Note: This method avoids storing the complete compressed file and extracts the data on-the-fly, **significantly reducing disk space requirements**.

**Method 2: Full Download before Extraction (Requires Sufficient Storage Space)**

```bash
# 1. Download the complete snapshot file
wget SNAPSHOT_URL/FullNode_output-directory.tgz

# 2. Extract the file
tar -zxvf FullNode_output-directory.tgz
```

Note: During extraction, both the compressed archive and the extracted files must be stored simultaneously. We recommend using two 3TB disks (3TB+ for the archive & 3TB+ for the extracted data. You can release the archive disk after extraction to reduce costs.).

# Step 3 - Use the Data Snapshot

The steps for using data snapshots are as follows:

1. Download the corresponding compressed backup database based on your needs.
2. Decompress the compressed file of the backup database to the `output-directory` directory or to the corresponding directory according to your needs.
3. Start the node. The node reads the output-directory directory by default. If you need to specify another directory, add the `-d directory` parameter when starting the node.
