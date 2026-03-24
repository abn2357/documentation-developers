---
title: TRON-CLI
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
# Introduction

TRON-CLI is a command line tool which allows developers to quickly set up and manage TRON Nodes and service. 

# Dependencies

* Python 3.6+
* JDK 1.8
* MongoDB (for event server)
* MacOS or Linux

# Installation

In the destination directory, optionally set up the python virtual environment and activate the environment. Then perform the pip install for troncli.    

```shell
python3 -m venv venv    // Optional step

. ./venv/bin/activate   // Optional step

pip install troncli
```

> 📘 Why Python Virtual Environments?
>
> TRON-CLI, like many Python programs, contains essential dependency files. In the absence of a Python Virtual Environment, a `pip install` command by default downloads the required package into your local machine's **lib/python/site-packages** directory. If another Python program checks for a different version of the same package dependency, that program may end up using the wrong package since there exists no indication of version number. With a Python Virtual Environment, all the required dependencies are neatly packaged into a `venv` directory that conveniently resides on the same level as your working directory. This eliminates any potential confusion stemming from package name overlap, as well as making the package easier to locate.

A successful `pip install` within the virtual environment produces the following output: 

<Image title="pipinstalltroncli.png" alt={969} src="https://files.readme.io/55e4638-pipinstalltroncli.png">
  Successful pip install output
</Image>

# TRON-CLI Interactive Mode

```shell
tron-cli i
```

Quickly set up what you want by answering a few questions:

![alt text](https://tronprotocol.github.io/tron-cli/doc/imode.gif)

# TRON-CLI Quickstart

For those wanting to start up a local private network, you can run the command `tron-cli quick`. This command sets up the `tron_nodes` directory and sub-folders, moves the .jar files into the folders, sets up the configuration files on default ports, runs the node, and outputs the status details.

```shell
tron-cli quick
```

By default, it will set up a private test-net full node. 

* You can also type `--nettype main` to set up a Full Node that syncs to the Mainnet. 
* Type `--reset True` to reset all. 

![alt text](https://tronprotocol.github.io/tron-cli/doc/quick.gif)

# TRON-CLI Mainnet

The following procedures allow for advanced users to customize their setup and connect to the Mainnet. The process consists of initialization, settings configuration, and running the node.  

## Initialization

Run the 'tron-cli init' command to set up the directories, download the .jar files, and move the .jar files into the directories: 

```shell
tron-cli init
```

This command creates a directory called `tron_nodes` in the working directory and then creates the four folders `fullnode`, `soliditynode`, `eventnode`, and `gridapi`. The command then downloads `full.jar` and `solidity.jar`, and places these executable files within their respective folders.  

<Image title="troncli_init.png" alt={979} src="https://files.readme.io/01333b6-troncli_init.png">
  Successful TRON-CLI init output
</Image>

## Configuration

TRON-CLI allows users to easily configure HTTP and gRPC IP ports for Full and Solidity nodes. The default settings are:

**Full Node HTTP**: 8500\
**Solidity Node HTTP**: 8600\
**Event-Node HTTP**: 8400\
**Full Node RPC**: 58500\
**Solidity Node RPC**: 58600\
**Event-Node RPC**: 58400

To customize a setting, simply execute the `tron-cli config --nettype` command. For example, to set Full Node HTTP port to 8090, run `tron-cli config --fullhttpport 8090`:

<Image title="fullhttpport_change.png" alt={1241} src="https://files.readme.io/f54f510-fullhttpport_change.png">
  Full Node HTTP port set to 8090
</Image>

## Run Node

To launch a full node only, execute `tron-cli run`:

<Image title="troncli_run.png" alt={429} src="https://files.readme.io/2d3b18c-troncli_run.png">
  Running the full node
</Image>

You can then check the overall node status with `tron-cli status`: 

<Image title="troncli_status.png" alt={856} src="https://files.readme.io/2ebbc66-troncli_status.png">
  Checking TRON-CLI overall node status
</Image>

To run a solidity node, run the command `tron-cli run --nodetype sol`. For event node, run the command `tron-cli run --nodetype event`: 

<Image title="troncli_sol.png" alt={449} src="https://files.readme.io/3c1de6a-troncli_sol.png">
  Running TRON-CLI Solidity Node
</Image>

## Check Logs

Once both a Full Node and Solidity Node are running, you can view the synchronization logs. The Full Node log is located under `tron_nodes/fullnode/logs/tron.log`, while Solidity Node log is located under `tron_nodes/soliditynode/logs/tron.log`. The logs are updated dynamically, with the Solidity Node 1 block behind the Full Node due to syncing. 

<Image title="tronlogs.png" alt={1283} src="https://files.readme.io/061cd9c-tronlogs.png">
  Full Node (left) and Solidity Node (right) logs.
</Image>

## Stop Node

Stop a node easily by running the following command:

```shell
tron-cli stop --node NODENUMBER
```

![583](https://files.readme.io/ded57c4-stopnode.png "stopnode.png")

# Common Use Cases

**Note:** It is highly suggested to first take a look at `tron-cli i`, as Interactive Mode should cover most use cases.  

## 1. Private Net Nodes Setup

*Setup Full Node*

```shell
tron-cli quick
```

*Add Solidity Node*

```shell
tron-cli run --nodetype sol
```

## 2. Mainnet Nodes Setup

*Init*

```shell
tron-cli init
```

*Config to Mainnet*

```shell
tron-cli config --nettype main
```

*Run Full Node*

```shell
tron-cli run
```

## 3. Advanced Config to Start Nodes

*Initialize*

```shell
tron-cli init --version latest --reset True
```

*Detail Configuration (Specify parameter to overwrite default)*

```shell
tron-cli config --nettype private --fullhttpport 8500 --solhttpport 8600 --eventhttpport 8400 --fullrpcport 58500 --solrpcport 58600 --eventrpcport 58400 --enablememdb True --dbsyncmode async --saveintertx False --savehistorytx False --gridport 18891 --dbname Null --dbusername Null --dbpassword Null
```

*Run Full/Sol*

```shell
tron-cli run --nodetype full
```

## 4. Private Full Node + Event Node + Tron-Grid

*Install MongoDB and create User and Database. Then initialize.*

```shell
tron-cli init
```

*Config (Specify parameter to overwrite default)* **dbname, dbusername, and dbpassword are required to set**

```shell
tron-cli config --nettype private --fullhttpport 8500 --solhttpport 8600 --eventhttpport 8400 --fullrpcport 58500 --solrpcport 58600 --eventrpcport 58400 --enablememdb True --dbsyncmode async --saveintertx False --savehistorytx False --gridport 18891 --dbname events --dbusername tron --dbpassword 12345678
```

*Run Full Node, Event Node, and Tron-Grid*

```shell
tron-cli run
tron-cli run --nodetype event
tron-cli run --nodetype grid
```

## 5. Mainnet Event Node + Tron-Grid

*Install MongoDB and create User and Database. Then initialize*

```shell
tron-cli init
```

*Config (Specify parameter to overwrite default)* **dbname, dbusername, and dbpassword are required to set**

```shell
tron-cli config --nettype main --fullhttpport 8500 --solhttpport 8600 --eventhttpport 8400 --fullrpcport 58500 --solrpcport 58600 --eventrpcport 58400 --enablememdb True --dbsyncmode async --saveintertx False --savehistorytx False --gridport 18891 --dbname events --dbusername tron --dbpassword 12345678
```

*Run Event Node*

```shell
tron-cli run --nodetype event
```

*Run Tron-Grid*

```shell
tron-cli run --nodetype grid
```

# Commands Overview

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Command
      </th>

      <th>
        Functions
      </th>

      <th>
        Usage Example 1
      </th>

      <th>
        Usage Example 2
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        tron-cli init --version --reset
      </td>

      <td>
        Initiate directories and fetch the code.
      </td>

      <td>
        tron-cli init
      </td>

      <td>
        tron-cli init --version 3.2.2 --reset True
      </td>
    </tr>

    <tr>
      <td>
        tron-cli config --nettype ---nettype --fullhttpport --solhttpport --eventhttpport --fullrpcport --solrpcport --eventrpcport --enablememdb --dbsyncmode --saveintertx --savehistorytx --gridport --dbname --dbusername --dbpassword
      </td>

      <td>
        Create and customize configuration files.
      </td>

      <td>
        tron-cli config
      </td>

      <td>
        tron-cli config --nettype private --fullhttpport 8500 --solhttpport 8600 --eventhttpport 8400 --fullrpcport 58500 --solrpcport 58600 --eventrpcport 58400 --enablememdb True --dbsyncmode async --saveintertx False --savehistorytx False --gridport 18891 --dbname events --dbusername tron --dbpassword 12345678
      </td>
    </tr>

    <tr>
      <td>
        tron-cli run --nodetype
      </td>

      <td>
        Run nodes.
      </td>

      <td>
        tron-cli run
      </td>

      <td>
        tron-cli run --nodetype full
      </td>
    </tr>

    <tr>
      <td>
        tron-cli stop --node
      </td>

      <td>
        Stop nodes.
      </td>

      <td>
        tron-cli stop
      </td>

      <td>
        tron-cli stop --node 7777
      </td>
    </tr>

    <tr>
      <td>
        tron-cli status --node
      </td>

      <td>
        Monitor nodes status.
      </td>

      <td>
        tron-cli status
      </td>

      <td>
        tron-cli status --node 777
      </td>
    </tr>

    <tr>
      <td>
        tron-cli quick --reset
      </td>

      <td>
        Quick Start.
      </td>

      <td>
        tron-cli quick
      </td>

      <td>
        tron-cli quick -- reset True
      </td>
    </tr>

    <tr>
      <td>
        tron-cli version
      </td>

      <td>
        Check installed troncli version.
      </td>

      <td>
        tron-cli version
      </td>

      <td>
        tron-cli version
      </td>
    </tr>

    <tr>
      <td>
        tron-cli -h, --help
      </td>

      <td>
        Check out the help manual.
      </td>

      <td>
        tron-cli -h
      </td>

      <td>
        tron-cli --help
      </td>
    </tr>
  </tbody>
</Table>

# Installation FAQs

1. How to fix "fail to build a wheel for psutil" error?

a. Please check if clang is installed correctly, or install it using Homebrew:

```
brew install --with-toolchain llvm
```

b. Please check if you are using Python 3.x 

2. How to test in a virtual environment?

a. Create Virtual Environment

```
python3 -m venv venv
```

b. Activate VENV

```
. ./venv/bin/activate
```

c. Install TRON-CLI in VENV

```
pip install troncli
```

d. Deactivate the VENV when done testing or using

```
deactivate
```

# GitHub Link

<a href="https://tronprotocol.github.io/tron-cli/" target="_blank">https\://tronprotocol.github.io/tron-cli/</a>
