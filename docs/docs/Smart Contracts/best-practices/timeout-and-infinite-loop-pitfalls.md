---
title: Timeout and Infinite Loop Pitfalls
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
If a complex Solidity contract deploys on the TRON network, there is a probability the execution times out, causing the user to consume all energy from the account up to the fee limit. The maximum amount of CPU time allowed per transaction is 80 ms (adjustable network parameter #14 [here](https://tronscan.org/#/sr/committee)), resulting in a maximum of 50,000 Energy consumed before timing out (1 Energy = 1 Microsecond). Note that this number is actually \~250,000 Energy due to *maxTimeRatio = 5.0* set on SR nodes relaxing the upper timeout for different machine configurations. **OUT\_OF\_ENERGY** failures may incur higher than 250,000 Energy due to penalties.

To avoid timeout executions, try to break large contracts into smaller chunks, and reference each other as needed. To avoid infinite loops, watch for common pitfalls and recursive calling.
