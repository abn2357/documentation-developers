---
title: Proposals
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
# getProposalById

Query proposal based on ID.  

### Usage

```
getProposalById(id)
```

### Parameter

| Parameter | Description | Type   |
| :-------- | :---------- | :----- |
| id        | proposal id | String |

### Return

Object -Proposal object.  An IllegalException is thrown when it fails to get proposal.

### Example

```
wrapper.getProposalById("15");
```

Execution result:

```
proposal_id: 15
  proposer_address: "A\fLd \037f\243\'\031\317\232\264\346\364\256\3263\vH\275"
  parameters {
    key: 0
    value: 800000
  }
  expiration_time: 1582011000000
  create_time: 1582010070000
  approvals: "A\fLd \037f\243\'\031\317\232\264\346\364\256\3263\vH\275"
  state: DISAPPROVED
```
