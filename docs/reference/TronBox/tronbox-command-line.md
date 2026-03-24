---
title: TronBox Command Line
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section will describe every command available in the TronBox application.

## Usage

All commands are in the following form:

```
tronbox <command> [options]
```

Passing no arguments is equivalent to `tronbox help`, which will display all commands and then exit.

## Commands

### build

Deprecated.

```
tronbox build
```

### compile

Compile source files of smart contracts.

```
tronbox compile [--all] [--quiet] [--evm]
```

Only contracts that have changed since the last compilation will be compiled if there is no –all.\
Options:

* `--all`: Compile all contracts instead of only the contracts that have changed since the last compilation.
* `--quiet`: Suppress all compilation output.
* `--evm`: Use EVM related configuration (Requires TronBox V4.0.0 or later).

### Run a console

Run a console with contract abstractions and commands available.

```
tronbox console [--network <name>] [--evm]
```

An interface that interacts with contracts via the command line. In addition, many TronBox commands can be used in the console (without the `tronbox` prefix).\
Option:

* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--evm`: Use EVM related configuration (Requires TronBox V4.0.0 or later).

### deploy

An alias for `migrate`. Please see [Contract Deployment(Migrations)](ref:contract-deploymentmigrations).

### help

Display a list of all commands.

```
tronbox help
```

### init

Initialize a new (empty) TronBox project.

```
tronbox init
```

Create a new, empty TronBox project in the current working directory.

### migrate

Run migration files to deploy contracts.

```
tronbox migrate [--reset] [--f <number>] [--to <number>] [--network <name>] [--compile-all] [--evm]
```

This will run from the last completed migration unless otherwise specified. For more information, please see  [Contract Deployment(Migrations)](ref:contract-deploymentmigrations).\
Options:

* `--reset`: Run all migrations from the beginning, instead of running from the last completed migration.
* `--f <number>`: Run contracts from a specific migration. The number refers to the prefix of the migration file.
* `--to <number>`: Run contracts to a specific migration. The number refers to the prefix of the migration file.
* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--compile-all`: Compile all contracts, instead of intelligently choosing the contracts that need to be compiled.
* `--evm`: Use EVM related configuration (Requires TronBox V4.0.0 or later).

### serve

Build a directory as the root directory of the local server. Start the service and watch for changes.

```
tronbox serve
```

### test

Run JavaScript tests.

```
tronbox test [<test_file>] [--network <name>] [--evm]
```

Run all or some test files in the `test/` directory as specified. For more information, please see [Test Your Contracts](ref:test-your-contracts) .\
Options:

* `<test_file>`: The name of the test file to be run. Include the path information if the file does not exist in the current directory.
* `--network <name>`: Specify the network to use. The network name must exist in the configuration.
* `--evm`: Use EVM related configuration (Requires TronBox V4.0.0 or later).

### unbox

Download a [TronBox Box](https://github.com/tronsuper), which is a pre-built TronBox project.

```
tronbox unbox <box_name>
```

Download a TronBox Box to the current working directory.\
Option:

* `<box_name>`: The name of the TronBox Box (required).

### version

Display the version number and then exit.

```
tronbox version
```

### watch

Watch the filesystem for changes and rebuild the project automatically.

```
tronbox watch [--evm]
```

This command will initiate a watch for changes to contracts, the application, and configuration files. It will rebuild the application as necessary when there is a change.

Options:

* `--evm`: Use EVM related configuration (Requires TronBox V4.0.0 or later).

> ❗️ Note
>
> This command is not recommended. Please use external tools to watch for filesystem changes and rerun tests.

### flatten

The built-in flatten task lets you combine the source code of multiple Solidity files.

```shell
tronbox flatten <file_path>
```

Options：

* `<file_path>`: The path to the file that needs flatten (must be required) 

> 📘 Note
>
> This function requires TronBox V3.3.0 or later.
