---
title: Flattening your contracts
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
TronBox comes with a built-in flatten task that lets you combine the source code of multiple Solidity files.

```Text Text
  Note:This function requires TronBox V3.3.0 or later.
```

## Flattening specific files

If you want to flatten the specific file, you can use the `flatten` task. The `flatten` task can receive a path to the file you want to flatten:

```shell
tronbox flatten contracts/Box.sol
```

In this case, the result will contain the source code of `Box.sol` and all its transitive dependencies (the files that it imports, and the files that those files import, and so on).

You can also use multiple files:

```shell
tronbox flatten contracts/Box.sol contracts/Foo.sol
```

However, if `Foo.sol` is a dependency of `Box.sol`, then the result will be the same as in the previous example.

As mentioned in the previous section, you can redirect the output to some file:

```shell
tronbox flatten contracts/Box.sol > Flattened.sol
```
