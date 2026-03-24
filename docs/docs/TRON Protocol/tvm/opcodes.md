---
title: Opcodes
excerpt: Opcodes for the TVM
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
TVM opcodes are the same as EVM except for TRON-specific opcodes. Please get the details of each opcode from the table below.

| opcode    | Name                   | Energy                                    | Initial Stack                                                                | Resulting Stack                | Mem / Storage                                           | Notes                                                                                    |
| :-------- | :--------------------- | :---------------------------------------- | :--------------------------------------------------------------------------- | :----------------------------- | :------------------------------------------------------ | :--------------------------------------------------------------------------------------- |
| 0x00      | STOP                   | 0                                         |                                                                              |                                |                                                         | halt execution                                                                           |
| 0x01      | ADD                    | 3                                         | a, b                                                                         | a + b                          |                                                         | (u)int256 addition modulo 2\*\*256                                                       |
| 0x02      | MUL                    | 5                                         | a, b                                                                         | a \* b                         |                                                         | (u)int256 multiplication modulo 2\*\*256                                                 |
| 0x03      | SUB                    | 3                                         | a, b                                                                         | a - b                          |                                                         | (u)int256 addition modulo 2\*\*256                                                       |
| 0x04      | DIV                    | 5                                         | a, b                                                                         | a // b                         |                                                         | uint256 division                                                                         |
| 0x05      | SDIV                   | 5                                         | a, b                                                                         | a // b                         |                                                         | int256 division                                                                          |
| 0x06      | MOD                    | 5                                         | a, b                                                                         | a % b                          |                                                         | uint256 modulus                                                                          |
| 0x07      | SMOD                   | 5                                         | a, b                                                                         | a % b                          |                                                         | int256 modulus                                                                           |
| 0x08      | ADDMOD                 | 8                                         | a, b, N                                                                      | (a + b) % N                    |                                                         | (u)int256 addition modulo N                                                              |
| 0x09      | MULMOD                 | 8                                         | a, b, N                                                                      | (a \* b) % N                   |                                                         | (u)int256 multiplication modulo N                                                        |
| 0x0A      | EXP                    | [A1](#a1-exp-energy-cost)                 | a, b                                                                         | a \*\* b                       |                                                         | uint256 exponentiation modulo 2\*\*256                                                   |
| 0x0B      | SIGNEXTEND             | 5                                         | b, x                                                                         | SIGNEXTEND(x, b)               |                                                         | [sign extend](https://wikipedia.org/wiki/Sign_extension)  x from (b+1) bytes to 32 bytes |
| 0x0C-0x0F | invalid                |                                           |                                                                              |                                |                                                         |                                                                                          |
| 0x10      | LT                     | 3                                         | a, b                                                                         | a \< b                         |                                                         | uint256 less-than                                                                        |
| 0x11      | GT                     | 3                                         | a, b                                                                         | a > b                          |                                                         | uint256 greater-than                                                                     |
| 0x12      | SLT                    | 3                                         | a, b                                                                         | a \< b                         |                                                         | int256 less-than                                                                         |
| 0x13      | SGT                    | 3                                         | a, b                                                                         | a > b                          |                                                         | int256 greater-than                                                                      |
| 0x14      | EQ                     | 3                                         | a, b                                                                         | a == b                         |                                                         | (u)int256 equality                                                                       |
| 0x15      | ISZERO                 | 3                                         | a                                                                            | a == 0                         |                                                         | (u)int256 iszero                                                                         |
| 0x16      | AND                    | 3                                         | a, b                                                                         | a && b                         |                                                         | bitwise AND                                                                              |
| 0x17      | OR                     | 3                                         | a, b                                                                         | a                              |                                                         | b                                                                                        |
| 0x18      | XOR                    | 3                                         | a, b                                                                         | a ^ b                          |                                                         | bitwise XOR                                                                              |
| 0x19      | NOT                    | 3                                         | a                                                                            | \~a                            |                                                         | bitwise NOT                                                                              |
| 0x1A      | BYTE                   | 3                                         | i, x                                                                         | (x >> (248 - i \* 8)) && 0xFF  |                                                         | ith byte of (u)int256 x, from the left (i start from 0)                                  |
| 0x1B      | SHL                    | 3                                         | shift, val                                                                   | val \<\< shift                 |                                                         | shift left                                                                               |
| 0x1C      | SHR                    | 3                                         | shift, val                                                                   | val >> shift                   |                                                         | logical shift right                                                                      |
| 0x1D      | SAR                    | 3                                         | shift, val                                                                   | val >> shift                   |                                                         | arithmetic shift right                                                                   |
| 0x20      | SHA3                   | [A2](#a2-sha3-energycost)                 | ost, len                                                                     | keccak256(mem\[ost:ost+len-1]) |                                                         | keccak256                                                                                |
| 0x21-0x2F | invalid                |                                           |                                                                              |                                |                                                         |                                                                                          |
| 0x30      | ADDRESS                | 2                                         | .                                                                            | address(this)                  |                                                         | address of executing contract                                                            |
| 0x31      | BALANCE                | 20                                        | addr                                                                         | addr.balance                   |                                                         | balance, in sun                                                                          |
| 0x32      | ORIGIN                 | 2                                         | .                                                                            | tx.origin                      |                                                         | address that originated the tx                                                           |
| 0x33      | CALLER                 | 2                                         | .                                                                            | msg.sender                     |                                                         | address of msg sender                                                                    |
| 0x34      | CALLVALUE              | 2                                         | .                                                                            | msg.value                      |                                                         | msg value, in sun                                                                        |
| 0x35      | CALLDATALOAD           | 3                                         | idx                                                                          | msg.data\[idx:idx+32]          |                                                         | read word from msg data at indexidx                                                      |
| 0x36      | CALLDATASIZE           | 2                                         | .                                                                            | len(msg.data)                  |                                                         | length of msg data, in bytes                                                             |
| 0x37      | CALLDATACOPY           | [A3](#a3-copy-operations)                 | dstOst, ost, len                                                             | .                              | mem[dstOst:dstOst+len-1] \:= msg.data\[ost:ost+len-1]   | copy msg data                                                                            |
| 0x38      | CODESIZE               | 2                                         | .                                                                            | len(this.code)                 |                                                         | length of executing contract's code, in bytes                                            |
| 0x39      | CODECOPY               | [A3](#a3-copy-operations)                 | dstOst, ost, len                                                             | .                              |                                                         | mem[dstOst:dstOst+len-1] \:= this.code\[ost:ost+len-1]                                   |
| 0x3A      | GASPRICE               | 2                                         | .                                                                            | tx.gasprice                    |                                                         | gas price of tx                                                                          |
| 0x3B      | EXTCODESIZE            | 20                                        | addr                                                                         | len(addr.code)                 |                                                         | size of code at addr, in bytes                                                           |
| 0x3C      | EXTCODECOPY            | [A4](#a4-extcodecopy)                     | addr, dstOst, ost, len                                                       | .                              | mem[dstOst:dstOst+len-1] \:= addr.code\[ost:ost+len-1]  | copy code from addr                                                                      |
| 0x3D      | RETURNDATASIZE         | 2                                         | .                                                                            | size                           |                                                         | size of returned data from last external call, in bytes                                  |
| 0x3E      | RETURNDATACOPY         | [A3](#a3-copy-operations)                 | dstOst, ost, len                                                             | .                              | mem[dstOst:dstOst+len-1] \:= returndata\[ost:ost+len-1] | copy returned data from last external call                                               |
| 0x3F      | EXTCODEHASH            | 400                                       | addr                                                                         | hash                           |                                                         | hash = addr.exists ? keccak256(addr.code) : 0                                            |
| 0x40      | BLOCKHASH              | 20                                        | blockNum                                                                     | blockHash(blockNum)            |                                                         |                                                                                          |
| 0x41      | COINBASE               | 2                                         | .                                                                            | block.coinbase                 |                                                         | address of proposer of current block                                                     |
| 0x42      | TIMESTAMP              | 2                                         | .                                                                            | block.timestamp                |                                                         | timestamp of current block                                                               |
| 0x43      | NUMBER                 | 2                                         | .                                                                            | block.number                   |                                                         | number of current block                                                                  |
| 0x44      | DIFFICULTY             | 2                                         | .                                                                            | 0                              |                                                         | block’s difficulty,                                                                      |
| 0x45      | GASLIMIT               | 2                                         | .                                                                            | block.gaslimit                 |                                                         | gas limit of current block                                                               |
| 0x46      | CHAINID                | 2                                         | .                                                                            | chain\_id                      |                                                         | push current chain id onto stack                                                         |
| 0x47      | SELFBALANCE            | 5                                         | .                                                                            | address(this).balance          |                                                         | balance of executing contract, in sun                                                    |
| 0x48      | BASEFEE                | 2                                         | .                                                                            | block.basefee                  |                                                         | base fee of current block                                                                |
| 0x50      | POP                    | 2                                         | .                                                                            | .                              |                                                         | remove item from top of stack and discard it                                             |
| 0x51      | MLOAD                  | [A5](#a5-mload-mstore)                    | ost                                                                          | mem\[ost:ost+32]               |                                                         | read word from memory at offsetost                                                       |
| 0x52      | MSTORE                 | [A5](#a5-mload-mstore)                    | ost, val                                                                     | .                              | mem\[ost:ost+32] \:= val                                | write a word to memory                                                                   |
| 0x53      | MSTORE8                | [A6](#a6-mstore8)                         | ost, val                                                                     | .                              | mem\[ost] \:= val && 0xFF                               | write a single byte to memory                                                            |
| 0x54      | SLOAD                  | 50                                        | key                                                                          | storage\[key]                  |                                                         | read word from storage                                                                   |
| 0x55      | SSTORE                 | [A7](#a7-sstore)                          | key, val                                                                     | .                              | storage\[key] \:= val                                   | write word to storage                                                                    |
| 0x56      | JUMP                   | 8                                         | dst                                                                          | .                              |                                                         | \$pc := dstmark thatpcis only assigned ifdstis a valid jumpdest                          |
| 0x57      | JUMPI                  | 10                                        | dst, condition                                                               | .                              |                                                         | \$pc := condition ? dst : \$pc + 1                                                       |
| 0x58      | PC                     | 2                                         | .                                                                            | \$pc                           |                                                         | program counter                                                                          |
| 0x59      | MSIZE                  | 2                                         | .                                                                            | len(mem)                       |                                                         | size of memory in current execution context, in bytes                                    |
| 0x5A      | GAS                    | 2                                         | .                                                                            | gasRemaining                   |                                                         | the amount of available gas                                                              |
| 0x5B      | JUMPDEST               | 1                                         |                                                                              |                                |                                                         | \$pc := \$pc + 1                                                                         |
| 0x5F      | PUSH0                  | 2                                         | .                                                                            | uint8                          |                                                         | push the constant value 0 onto stack                                                     |
| 0x60      | PUSH1                  | 3                                         | .                                                                            | uint8                          |                                                         | push 1-byte value onto stack                                                             |
| 0x61      | PUSH2                  | 3                                         | .                                                                            | uint16                         |                                                         | push 2-byte value onto stack                                                             |
| 0x62      | PUSH3                  | 3                                         | .                                                                            | uint24                         |                                                         | push 3-byte value onto stack                                                             |
| 0x63      | PUSH4                  | 3                                         | .                                                                            | uint32                         |                                                         | push 4-byte value onto stack                                                             |
| 0x64      | PUSH5                  | 3                                         | .                                                                            | uint40                         |                                                         | push 5-byte value onto stack                                                             |
| 0x65      | PUSH6                  | 3                                         | .                                                                            | uint48                         |                                                         | push 6-byte value onto stack                                                             |
| 0x66      | PUSH7                  | 3                                         | .                                                                            | uint56                         |                                                         | push 7-byte value onto stack                                                             |
| 0x67      | PUSH8                  | 3                                         | .                                                                            | uint64                         |                                                         | push 8-byte value onto stack                                                             |
| 0x68      | PUSH9                  | 3                                         | .                                                                            | uint72                         |                                                         | push 9-byte value onto stack                                                             |
| 0x69      | PUSH10                 | 3                                         | .                                                                            | uint80                         |                                                         | push 10-byte value onto stack                                                            |
| 0x6A      | PUSH11                 | 3                                         | .                                                                            | uint88                         |                                                         | push 11-byte value onto stack                                                            |
| 0x6B      | PUSH12                 | 3                                         | .                                                                            | uint96                         |                                                         | push 12-byte value onto stack                                                            |
| 0x6C      | PUSH13                 | 3                                         | .                                                                            | uint104                        |                                                         | push 13-byte value onto stack                                                            |
| 0x6D      | PUSH14                 | 3                                         | .                                                                            | uint112                        |                                                         | push 14-byte value onto stack                                                            |
| 0x6E      | PUSH15                 | 3                                         | .                                                                            | uint120                        |                                                         | push 15-byte value onto stack                                                            |
| 0x6F      | PUSH16                 | 3                                         | .                                                                            | uint128                        |                                                         | push 16-byte value onto stack                                                            |
| 0x70      | PUSH17                 | 3                                         | .                                                                            | uint136                        |                                                         | push 17-byte value onto stack                                                            |
| 0x71      | PUSH18                 | 3                                         | .                                                                            | uint144                        |                                                         | push 18-byte value onto stack                                                            |
| 0x72      | PUSH19                 | 3                                         | .                                                                            | uint152                        |                                                         | push 19-byte value onto stack                                                            |
| 0x73      | PUSH20                 | 3                                         | .                                                                            | uint160                        |                                                         | push 20-byte value onto stack                                                            |
| 0x74      | PUSH21                 | 3                                         | .                                                                            | uint168                        |                                                         | push 21-byte value onto stack                                                            |
| 0x75      | PUSH22                 | 3                                         | .                                                                            | uint176                        |                                                         | push 22-byte value onto stack                                                            |
| 0x76      | PUSH23                 | 3                                         | .                                                                            | uint184                        |                                                         | push 23-byte value onto stack                                                            |
| 0x77      | PUSH24                 | 3                                         | .                                                                            | uint192                        |                                                         | push 24-byte value onto stack                                                            |
| 0x78      | PUSH25                 | 3                                         | .                                                                            | uint200                        |                                                         | push 25-byte value onto stack                                                            |
| 0x79      | PUSH26                 | 3                                         | .                                                                            | uint208                        |                                                         | push 26-byte value onto stack                                                            |
| 0x7A      | PUSH27                 | 3                                         | .                                                                            | uint216                        |                                                         | push 27-byte value onto stack                                                            |
| 0x7B      | PUSH28                 | 3                                         | .                                                                            | uint224                        |                                                         | push 28-byte value onto stack                                                            |
| 0x7C      | PUSH29                 | 3                                         | .                                                                            | uint232                        |                                                         | push 29-byte value onto stack                                                            |
| 0x7D      | PUSH30                 | 3                                         | .                                                                            | uint240                        |                                                         | push 30-byte value onto stack                                                            |
| 0x7E      | PUSH31                 | 3                                         | .                                                                            | uint248                        |                                                         | push 31-byte value onto stack                                                            |
| 0x7F      | PUSH32                 | 3                                         | .                                                                            | uint256                        |                                                         | push 32-byte value onto stack                                                            |
| 0x80      | DUP1                   | 3                                         | a                                                                            | a, a                           |                                                         | clone 1st value on stack                                                                 |
| 0x81      | DUP2                   | 3                                         | \_, a                                                                        | a, \_, a                       |                                                         | clone 2nd value on stack                                                                 |
| 0x82      | DUP3                   | 3                                         | \_, \_, a                                                                    | a, \_, \_, a                   |                                                         | clone 3rd value on stack                                                                 |
| 0x83      | DUP4                   | 3                                         | \_, \_, \_, a                                                                | a, \_, \_, \_, a               |                                                         | clone 4th value on stack                                                                 |
| 0x84      | DUP5                   | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 5th value on stack                                                                 |
| 0x85      | DUP6                   | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 6th value on stack                                                                 |
| 0x86      | DUP7                   | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 7th value on stack                                                                 |
| 0x87      | DUP8                   | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 8th value on stack                                                                 |
| 0x88      | DUP9                   | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 9th value on stack                                                                 |
| 0x89      | DUP10                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 10th value on stack                                                                |
| 0x8A      | DUP11                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 11th value on stack                                                                |
| 0x8B      | DUP12                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 12th value on stack                                                                |
| 0x8C      | DUP13                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 13th value on stack                                                                |
| 0x8D      | DUP14                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 14th value on stack                                                                |
| 0x8E      | DUP15                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 15th value on stack                                                                |
| 0x8F      | DUP16                  | 3                                         | ..., a                                                                       | a, ..., a                      |                                                         | clone 16th value on stack                                                                |
| 0x90      | SWAP1                  | 3                                         | a, b                                                                         | b, a                           |                                                         | swap the 1st item from the stack with the top                                            |
| 0x91      | SWAP2                  | 3                                         | a, \_, b                                                                     | b, \_, a                       |                                                         | swap the 2nd item from the stack with the top                                            |
| 0x92      | SWAP3                  | 3                                         | a, \_, \_, b                                                                 | b, \_, \_, a                   |                                                         | swap the 3rd item from the stack with the top                                            |
| 0x93      | SWAP4                  | 3                                         | a, \_, \_, \_, b                                                             | b, \_, \_, \_, a               |                                                         | swap the 4th item from the stack with the top                                            |
| 0x94      | SWAP5                  | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 5th item from the stack with the top                                            |
| 0x95      | SWAP6                  | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 6th item from the stack with the top                                            |
| 0x96      | SWAP7                  | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 7th item from the stack with the top                                            |
| 0x97      | SWAP8                  | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 8th item from the stack with the top                                            |
| 0x98      | SWAP9                  | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 9th item from the stack with the top                                            |
| 0x99      | SWAP10                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 10th item from the stack with the top                                           |
| 0x9A      | SWAP11                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 11th item from the stack with the top                                           |
| 0x9B      | SWAP12                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 12th item from the stack with the top                                           |
| 0x9C      | SWAP13                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 13th item from the stack with the top                                           |
| 0x9D      | SWAP14                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 14th item from the stack with the top                                           |
| 0x9E      | SWAP15                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 15th item from the stack with the top                                           |
| 0x9F      | SWAP16                 | 3                                         | a, ..., b                                                                    | b, ..., a                      |                                                         | swap the 16th item from the stack with the top                                           |
| 0xA0      | LOG0                   | [A8](#a8-log0，-log1--log4)                | ost, len                                                                     | .                              |                                                         | LOG0(memory\[ost:ost+len-1])                                                             |
| 0xA1      | LOG1                   | [A8](#a8-log0，-log1--log4)                | ost, len, topic0                                                             | .                              |                                                         | LOG1(memory\[ost:ost+len-1], topic0)                                                     |
| 0xA2      | LOG2                   | [A8](#a8-log0，-log1--log4)                | ost, len, topic0, topic1                                                     | .                              |                                                         | LOG2(memory\[ost:ost+len-1], topic0, topic1)                                             |
| 0xA3      | LOG3                   | [A8](#a8-log0，-log1--log4)                | ost, len, topic0, topic1, topic2                                             | .                              |                                                         | LOG3(memory\[ost:ost+len-1], topic0, topic1, topic2)                                     |
| 0xA4      | LOG4                   | [A8](#a8-log0，-log1--log4)                | ost, len, topic0, topic1, topic2, topic3                                     | .                              |                                                         | LOG4(memory\[ost:ost+len-1], topic0, topic1, topic2, topic3)                             |
| 0xD0      | CALLTOKEN              | [A9](#a9-calltoken-call)                  | callEnergy, addr,val, tokenId, argOst, argLen, retOst, retLen                | success                        | mem[retOst:retOst+retLen-1] \:= returndata              | call the addr with val and argument.                                                     |
| 0xD1      | TOKENBALANCE           | 20                                        | tokenId,address                                                              | balance                        |                                                         | balance of address on tokenId trc10 token                                                |
| 0xD2      | CALLTOKENVALUE         | 2                                         | .                                                                            | value                          |                                                         | call token value                                                                         |
| 0xD3      | CALLTOKENID            | 2                                         |                                                                              | tokenId                        |                                                         | token id                                                                                 |
| 0xD4      | ISCONTRACT             | 20                                        | address                                                                      | isContract                     |                                                         | If the address is contract                                                               |
| 0xD5      | FREEZE                 | A10                                       | resouceType, frozenBalance, receiverAddress                                  | success                        |                                                         | Freeze frozenBalance resource of resourceType to receiverAddress                         |
| 0xD6      | UNFREEZE               | 20000                                     | resourceType, targetAddress                                                  | success                        |                                                         | Unfreeze all resource of resourceType on targetAddress                                   |
| 0xD7      | FREEZEEXPIRETIME       | 50                                        | resourceType, targetAddress                                                  | expireTime                     |                                                         | expireTime of resourceType on targetAddress                                              |
| 0xD8      | VOTEWITNESS            | [A11](#a11-votewitness)                   | amountArrayLength, amountArrayOffset, witnessArrayLength, witnessArrayOffset | success                        |                                                         | vote amount in amountArray for corresponding witness in witnessArray.                    |
| 0xD9      | WITHDRAWREWARD         | 20000                                     | .                                                                            | withdrawReward                 |                                                         | withdrawReward                                                                           |
| 0xDA      | FREEZEBALANCEV2        | 10000                                     | resourceType, frozenBalance                                                  | success                        |                                                         | freeze balance v2                                                                        |
| 0xDB      | UNFREEZEBALANCEV2      | 10000                                     | resouceType, unfreezeBalance                                                 | success                        |                                                         | unfreeze balance v2                                                                      |
| 0xDC      | CANCELALLUNFREEZEV2    | 10000                                     | .                                                                            | success                        |                                                         | cancel all unfreeze V2 balance                                                           |
| 0xDD      | WITHDRAWEXPIREUNFREEZE | 10000                                     | .                                                                            | success                        |                                                         | Withdraw expired unfreeze balance                                                        |
| 0xDE      | DELEGATERESOURCE       | 10000                                     | resouceType, delegateBalance, receiverAddress                                | success                        |                                                         | Delegate resource                                                                        |
| 0xDF      | UNDELEGATERESOURCE     | 10000                                     | resourceType, unDelegateBalance, receiverAddress                             | success                        |                                                         | Undelegate resource                                                                      |
| 0xF0      | CREATE                 | [A12](#a12-create)                        | val, ost, len                                                                | .                              |                                                         | create contract                                                                          |
| 0xF1      | CALL                   | [A9](#a9-calltoken-call)                  | callEnergy, addr, val, argOst, argLen, retOst, retLen                        | success                        | mem[retOst:retOst+retLen-1] \:= returndata              | call codeAddress with value and argument.                                                |
| 0xF2      | CALLCODE               | [A13](#a13-callcode)                      | gas, addr, val, argOst, argLen, retOst, retLen                               | success                        | mem[retOst:retOst+retLen-1] = returndata                | same as DELEGATECALL, but does not propagate original msg.sender and msg.value           |
| 0xF3      | RETURN                 | [A14](#a14-return-revert)                 | ost, len                                                                     | .                              |                                                         | halt execution and return mem\[ost:ost+len-1]                                            |
| 0xF4      | DELEGATECALL           | [A15](#a15-delegatecall-staticcallenergy) | callEnergy, addr, argOst, argLen, retOst, retLen                             | success                        | mem[retOst:retOst+retLen-1] \:= returndata              | delegate call                                                                            |
| 0xF5      | CREATE2                | [A16](#a16-create2)                       | val, ost, len, salt                                                          | addr                           |                                                         | addr = keccak256(0x41 ++ address(this) ++ salt ++ keccak256(mem\[ost:ost+len-1]))\[12:]  |
| 0xFA      | STATICCALL             | [A15](#a15-delegatecall-staticcallenergy) | gas, addr, argOst, argLen, retOst, retLen                                    | success                        | mem[retOst:retOst+retLen-1] \:= returndata              |                                                                                          |
| 0xFD      | REVERT                 | [A14](#a14-return-revert)                 | ost, len                                                                     | .                              |                                                         | revert(mem\[ost:ost+len-1])                                                              |
| 0xFF      | SUICIDE                | [A17](#a17-suicide)                       | addr                                                                         | .                              |                                                         | halt execution and register account for later deletion                                   |

<br />

<br />

### APPENDIX FOR ENERGY COST

#### A01: memNeed(offset, size)

Calculate the memory needed.

* offset :  The start position in memory.
* Size : data length need to handle begin at offset
* Return : offset + size

#### A02: calcMemEnergy(oldMemorySIze, memorySize, copySize)

calculate the memory energy cost.

* oldMemorySize : old memory size.
* memorySize : new memory size after the operation.
* copySize : if the operation need to copy, copySize is the data size to copy.
* memWords = (memorySize + 31) / 32
* oldMemWords = oldMemorySize / 32
* energyCost =  3 \* memWords + memWords^2 / 512 - (3 \* oldMemWords + oldMemWords^2 / 512) + 3 \*((copySize + 31) / 32)

#### A03: penalty(energyCost)

If dynamic energy is allowed, return the penalty.

* DYNAMIC\_ENERGY\_FACTOR = 10000
* Factor : contract context factor
* Penalty = energyCost \* factor / DYNAMIC\_ENERGY\_FACTOR - energyCost
* return penalty > 0 ? penalty : 0

#### A04: isDeadAccount(address)

If the address is not a contract, return true. Else return false.

#### A05: sizeInWords(len)

Return len == 0 ? 0 : (len - 1) / 32 + 1

***

#### A1: EXP Energy Cost

* byte\_len\_exponent: the number of bytes in the exponent (exponent is b in the stack representation)

Calculation:

* energy\_cost = 10 + 10 \* byte\_len\_exponent

#### A2: SHA3-energyCost

* energy\_cost = 30 + [calcMemEnergy](#a02-calcmemenergyoldmemorysize-memorysize-copysize)(oldMemSize, [memNeed](#a01-memneedoffset-size)(ost, len), 0)

#### A3: \*COPY Operations

The following applies for the operations CALLDATACOPY, CODECOPY, and RETURNDATACOPY (not EXTCODECOPY).

* energy\_cost = calcMemEnergy(oldMemSize, memNeed(dstOst, len), len)

#### A4: EXTCODECOPY

* energy\_cost = 20 + calcMemEnergy(oldMemSize, memNeed(dstOst, len), len)

#### A5: MLOAD, MSTORE

* energy\_cost = calcMemEnergy(oldMemSize, memNeed(ost,32), 0)

#### A6: MSTORE8

* energy\_cost = calcMemEnergy(oldMemSize, memNeed(ost,1), 0)

#### A7: SSTORE

* oldValue: old value of storage\[key]
* energy\_cost =   (oldValue == null && val != 0) ? 20000 : (oldValue != null && value == 0) ? 5000 : 5000

#### A8: LOG0， LOG1 … LOG4

* nTopics: number of topics
* energyCost = 375 + 375 + 8 \* len + calcMemEnergy(oldMemSize, memNeed(ost,len), 0)

#### A9: CALLTOKEN, CALL

* energyCost\_1 = 40 +  (val != 0 ? 9000 : 0) +

(value != 0 && [isDeadAccount](#a04-isdeadaccountaddress)(addr) ? 25000 : 0) +

calcMemEnergy(oldMemSize, max(memNeed(orgOst, orgLen), memNeed(retOst, retLen)), 0)

* energyCost\_2 = energeCost\_1 + [penalty](#a03-penaltyenergycost)(energyCost\_1)
* energyLimitLeft = energeLimit - energyCost\_2
* energyCost = energyCost\_2 + min(callEnergy, energyLimitLeft)

#### A10: FREEZE

* energyCost = 20000 + (isDeadAccount(receiverAddress) ? 25000 : 0)

#### A11: VOTEWITNESS

* energyCost = 30000 + ALLOW *ENERGY\_ADJUSTMENT ? calcMemEnergy(oldMemSize, max(memNeed(amountArrayOffset, amountArrayLength),\
          memNeed(witnessArrayOffset, witnessArrayLength)), 0) :  calcMemEnergy(oldMemSize, max(memNeed(amountArrayOffset, amountArrayLength* 32 + 32),\
           memNeed(witnessArrayOffset, witnessArrayLength \_ 32 + 32)), 0)

#### A12: CREATE

* energyCost  = 32000 + calcMemEnergy(oldMemSIze, memNeed(ost, len), 0)

#### A13: CALLCODE

* energyCost\_1 = 40 +  (val != 0 ? 9000 : 0) +

calcMemEnergy(oldMemSize, max(memNeed(orgOst, orgLen), memNeed(retOst, retLen)), 0)

* energyCost\_2 = energeCost\_1 + [penalty](#a03-penaltyenergycost)(energyCost\_1)
* energyLimitLeft = energeLimit - energyCost\_2
* energyCost = energyCost\_2 + min(callEnergy, energyLimitLeft)

#### A14: RETURN, REVERT

* calcMemEnergy(oldMemSize, memNeed(ost, len), 0)

#### A15: DELEGATECALL, STATICCALLENERGY

* energyCost\_1 = 40 + calcMemEnergy(oldMemSize, max(memNeed(orgOst, orgLen), memNeed(retOst, retLen)), 0)
* energyCost\_2 = energeCost\_1 + [penalty](#a03-penaltyenergycost)(energyCost\_1)
* energyLimitLeft = energeLimit - energyCost\_2
* energyCost = energyCost\_2 + min(callEnergy, energyLimitLeft)

#### A16: CREATE2

* energyCost  = 32000 + calcMemEnergy(oldMemSIze, memNeed(ost, len), 0) + 6 \* [sizeInWords](#a05-sizeinwordslen)(Len)

#### A17: SUICIDE

* energyCost =   ALLOW\_ENERGY\_ADJUSTMENT ? ( isDeadAccount(addr) ? 25000 : 0 ) : 0
