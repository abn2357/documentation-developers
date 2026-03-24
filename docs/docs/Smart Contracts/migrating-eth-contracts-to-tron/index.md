---
title: Migrating Ethereum Smart Contracts to TRON
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
# Key Differences - Ethereum (EVM) vs TRON (TVM)

|                         | ​​Ethereum (EVM)​​                                                     | ​​TRON (TVM)​​                                                             |
| :---------------------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| ​​Virtual Machine​​     | EVM (Supports Solidity/Vyper)                                          | TVM (Supports Solidity, largely EVM-compatible with some distinctions)     |
| Transaction Fee Model​​ | Gas fees are determined by a dynamic market mechanism and paid in ETH. | Transactions consume Bandwidth and Energy (can be acquired by staking TRX) |
| ​Native Token​​         | ETH (18 decimal places)                                                | TRX (6 decimal places)                                                     |

# TVM and EVM Compatibility

The TRON Virtual Machine (TVM) is largely compatible with the Ethereum Virtual Machine (EVM), allowing most Solidity smart contracts from Ethereum to be deployed on TRON. However, the contracts must first be recompiled using the [solc](https://github.com/tronprotocol/solidity) compiler provided by TRON.

## Opcode-Level Differences

The following opcodes exhibit different behaviors between the TVM and the EVM: 

| Opcode              | TVM Behavior                                        | EVM Behavior                                  |
| :------------------ | :-------------------------------------------------- | :-------------------------------------------- |
| `DIFFICULTY (0x44)` | Returns `0`                                         | Returns the current block's difficulty.       |
| `GASLIMIT (0x45)`   | Returns `0`                                         | Returns the current block's `gaslimit`.       |
| `GASPRICE (0x3A)`   | Returns `energyPrice`, which is 100 sun on Mainnet. | Returns the current transaction's `gasPrice`. |
| `BASEFEE (0x48)`    | Returns `energyPrice`, which is 100 sun on Mainnet. | Returns the current block's `baseFee`.        |
| `CREATE2 (0xf5)`    | The address calculation uses a `0x41` prefix.       | The address calculation uses a `0xff`prefix.  |

Developers must account for these operational discrepancies when these specific opcodes are involved in the contract logic.

For the `CREATE2` opcode, when Solidity's `new` keyword is used to deploy a contract, the inclusion of a `salt` parameter instructs the compiler to generate the address via `CREATE2`. To ensure code portability, the TRON-Solidity compiler emulates the EVM's behavior in this scenario by automatically using the `0xff` prefix in its internal `CREATE2` address calculation. Consequently, high-level Solidity code that uses the `new {salt: ...}` pattern can be migrated directly to TRON without modification.

**Example**: *Note: The`ContractCreated` event is not defined in the source snippet but is included for functional illustration.*

```
// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.20;
 
contract Token1{
    uint256 public value;
 
    constructor(uint256 _value) {
        value = _value;
    }
}

contract Factory {
		/// Use CREATE2 to create a contract
		function createContract(bytes32 _salt,uint _x) external{
        Token1 _contract = new Token1{salt: _salt}(_x);
        emit ContractCreated(address(_contract));
		}
}

```

However, if you are referencing another library, such as OpenZeppelin's logic for `CREATE2` address computation, then make sure to change the address prefix from `0xff` to `0x41`.

```
function computeAddress(bytes32 salt, bytes32 bytecodeHash, address deployer) internal pure returns (address addr) {
            mstore(add(ptr, 0x40), bytecodeHash)
            mstore(add(ptr, 0x20), salt)
            mstore(ptr, deployer) // Right-aligned with 12 preceding garbage bytes
            let start := add(ptr, 0x0b) // The hashed data starts at the final garbage byte which we will set to 0x41
            mstore8(start, 0x41)  // This must be changed to 0x41
            addr := keccak256(start, 85)
        }
    }
```

## Precompiled Contract-Level Differences

The following table outlines the functional differences for precompiled contracts at specific addresses.

| Precompiled Address | TVM                                                                                                                              | EVM                                                 |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `Ripemd160 (0x03)`  | Performs a double `SHA-256` hashing.                                                                                             | Performs a single `SHA-256` hashing.                |
| `0x09`              | `[BatchValidateSign](https://github.com/tronprotocol/tips/blob/master/tip-43.md)`, used for native multi-signature verification. | `[Blake2F](https://eips.ethereum.org/EIPS/eip-152)` |

It is crucial to note the differences in these precompiled contracts. If your smart contract calls any of the addresses above, you must modify its logic to ensure the correct behavior before migrating to TRON.

## Differences in Native Token Precision

It is essential to account for the difference in decimal precision between the two native assets. The smallest unit of ETH is 1/1e18 (wei), whereas the smallest unit of TRX is 1/1e6 (sun). If a smart contract's logic involves calculations with these base units, it must be adjusted to ensure computational accuracy.

# SDK and Tooling Equivalents

## SDKs

To interact with the TRON network programmatically, developers can choose a variety of SDKs according to their programming language:

| Language   | TRON SDK                                           |
| :--------- | :------------------------------------------------- |
| JavaScript | [TronWeb](https://tronweb.network/)                |
| Java       | [Trident](https://github.com/tronprotocol/trident) |
| Python     | [TronPy](https://pypi.org/project/tronpy/)         |

## Development Tools

The TRON ecosystem also offers a suite of development tools that serve as alternatives to popular tools in the Ethereum space. 

| Tool      | TRON Equivalent                                       |
| :-------- | :---------------------------------------------------- |
| Truffle   | [TronBox](https://tronbox.io/)                        |
| Remix     | [TRON-IDE](https://www.tronide.io/)                   |
| solc      | [TRON solc](https://github.com/tronprotocol/solidity) |
| Etherscan | [TRONSCAN](https://tronscan.org/)                     |
