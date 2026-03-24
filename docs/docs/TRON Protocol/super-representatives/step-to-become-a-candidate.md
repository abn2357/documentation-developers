---
title: Step to become a Candidate
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
# Super Representative Candidate Application Process

* Open TRON Blockchain explorer:  [https://tronscan.org](https://tronscan.org)
* Click "Account". 

![](https://raw.githubusercontent.com/ybhgenius/Documentation/master/images/Blockchain-Explorer/竞选超级代表/点击账户.jpg)

* Click "APPLY TO BE A SUPER REPRESENTATIVE CANDIDATE".

![](https://raw.githubusercontent.com/ybhgenius/Documentation/master/images/Blockchain-Explorer/竞选超级代表/申请成为超级代表候选.jpg)

* Input your website address and check the information below website address.

![](https://raw.githubusercontent.com/ybhgenius/Documentation/master/images/Blockchain-Explorer/竞选超级代表/填写网站地址并勾选.jpg)

Note: 9999 TRX will be paid when users apply to be an SR candidate.

Tronscan provides a way for Super Representatives to publish their information right where the voters are, on Tronscan!

Super Representatives can use this template to build a static page which will be shown on Tronscan. The link will be placed in the voting overview page right next to the name of SR.

The Super Representatives can manage their content by editing files in the Github repository.

**This guide assumes that you already have an account with Super Representative (candidate) status.**

1. Copy/Fork the Template on Github

* Go to [https://github.com/tronscan/tronsr-template](https://github.com/tronscan/tronsr-template)
* Fork the repository\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/fork-repo.png)

After forking the repository, you will be navigated to your own `tronsr-template` version of the repository where you can make changes.

2. Fill in the Template

Editing files on Github can now modify the template.

* Click the file you want to edit\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/github-open-file.png)
* Open edit mode\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/github-edit-file.png)
* Add some information to the file\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/edit-team-intro.png)

Files are written in markdown format. An excellent intro can be found at [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/).

* Update the logo.png and banner.png\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/github-upload-files.png)\
  Then click on "choose your files" and make sure the logo or banner you want to upload is named `logo.png` or `banner.jpg` to overwrite the placeholder images.

It can e published on [https://tronscan.org](https://tronscan.org) after you filled the template.

3. Publish to Tronscan

* Go to [https://tronscan.org](https://tronscan.org)
* Login to your account. In this example, it uses the private key, but you may use any login method.\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/login-with-private-key.png)
* Open an account and make sure the "Representative" label is visible\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/open-account.png)
* Scroll to the bottom and click "Set Github Link."\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/set-github-link.png)
* Enter your Github username and then press "Link Github."\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/input-username.png)
* View your new Page!\
  ![](https://raw.githubusercontent.com/tronscan/docs/master/images/view-page.png)

## Example

This example shows where each file should be placed. The page will be updated immediately whenever a file on Github is modified.

![](https://raw.githubusercontent.com/tronscan/docs/master/images/example-page.png)

# Voting

Every account in TRON’s network can vote for the Super Representatives they support. Voting requires TRON Power (TP), 1 TP = 1 staked TRX.

Users can use Tronscan or Tronlink to stake, vote or obtain reward.

* e.g.

```
freezebalance password 10,000,000 3    // 10 TP for 10 staked TRX
votewitness password witness1 4 witness2 6    //4 votes for witness1 and 6 votes for witness2
votewitness password witness1 3 witness2 7    // 3 votes for witness1 and 7 votes for witness2
```

The final result of the above commands is three votes for witness1 and seven votes for witness2.

# stake/Unstake Balance

## Why are Tokens staked?

The balance stake mechanism is set up out of two considerations:

* To prevent malicious spam transactions from clogging the network and causing delayed transaction confirmation.
* To prevent malicious voting.

## Stake/Unstake Mechanism

Once the balance is staked, the user will receive a proportionate amount of TP and bandwidth. TP represents voting power, whereas bandwidth points are used to pay for transactions. 

Staked assets are held in your stake account and cannot be used for trading.

The fixed stake duration is three days, after which you can unstake your balance any time you like manually. Balance unstaked will be transferred back into your current account.

* The stake command is as follows: 

```
freezebalance password amount time
amount: the unit of stake balance is Sun. The minimum stake balance is 1,000,000 Sun or 1 TRX.
time: stake duration lasting from date of stake and date to unstake is three days.
```

* e.g.

    `freezebalance password 10_000_000 3`

* Unstake command:

    `unfreezebalance password`
