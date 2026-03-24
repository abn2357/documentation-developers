---
title: Protocol Interfaces
excerpt: Protocol Interfaces
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# TRC-721 Standard

A standard interface allows applications to track and transfer NFTs on TRON. TRC-20 token standard is insufficient for handling NFTs because each token under TRC-721 is unique. The standard of TRC-721 is inspiring on TRON. It plays a role as important as TRC-20.

# MUST Implemented Interfaces

Every TRC-721 compliant contract must implement the TRC-721 and TRC-165 interfaces

```javascript solidity
pragma solidity ^0.4.20;

  interface TRC721 {
    event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);
    event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);

    function balanceOf(address _owner) external view returns (uint256);
    function ownerOf(uint256 _tokenId) external view returns (address);
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable;
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) external payable;
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
    function approve(address _approved, uint256 _tokenId) external payable;
    function setApprovalForAll(address _operator, bool _approved) external;
    function getApproved(uint256 _tokenId) external view returns (address);
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);
  }
  interface TRC165 {
      function supportsInterface(bytes4 interfaceID) external view returns (bool);
  }
```

**balanceOf(address\_owner)**\
Returns the number of NFTs owned by the specified account

**ownerOf(uint256\_tokenId)**\
Returns the owner of the specified NFT

**safeTransferFrom(address\_from, address \_to, uint256 \_tokenId, bytes data)**\
Transfer the ownership of an NFT

**safeTransferFrom(address\_from, address \_to, uint256 \_tokenId)**\
Transfer the ownership of an NFT

**transferFrom(address\_from, address \_to, uint256 \_tokenId)**\
Transfer the ownership of an NFT (the caller must confirm whether the \_to address can receive the NFT, otherwise the NFT will be lost)

**approve(address\_approved, uint256 \_tokenId)**\
Grant another account the control of an NFT

**setApprovalForAll(address\_operator, bool \_approved)**\
Grant/recover the control of all NFTs by a third party (\_operator)

**getApproved(uint256\_tokenId)**\
Query the authorization of a specific NFT

**isApprovedForAll(address\_owner, address \_operator)**\
Query whether the operator is an authorized address of the owner

**supportsInterface(bytes4 interfaceID)**\
Query whether a specific interface is supported (interfaceID)

**event Approval(address indexed\_owner, address indexed \_approved, uint256 indexed \_tokenId)**\
The Approval Event will be triggered after Approval succeeds

**event Transfer(address indexed\_from, address indexed \_to, uint256 indexed \_tokenId)**\
Successful transferFrom and safeTransferFrom will trigger the Transfer Event

**event ApprovalForAll(address indexed\_owner, address indexed \_operator, bool \_approved)**\
The ApprovalForAll Event will be triggered after setApprovalForAll succeeds

A wallet/broker/auction application MUST implement the wallet interface if it opts to accept safe transfers.

```javascript solidity
interface TRC721TokenReceiver {
       function onTRC721Received(address _operator, address _from, uint256 _tokenId, bytes _data) external       returns(bytes4);
   }
```

**onTRC721Received(address\_operator, address \_from, uint256 \_tokenId, bytes \_data)**

Works with the `safeTransferFrom` method. When \_to is the contract address, you need to call this method and check the return value. If the return value is not bytes4(keccak256("onTRC721Received(address,address,uint256,bytes)")), an exception will be thrown. A smart contract that can receive NFT must implement the TRC721TokenReceiver interface.

> 📘 Note
>
> The hash of bytes4(keccak256("onTRC721Received(address,address,uint256,bytes))) is different from the Ethereum version bytes4(keccak256("onERC721Received(address,address,uint256,bytes))). For the return value of function `onTRC721Received`, please use 0x5175f878 instead of 0x150b7a02.

# Metadata Extension Interface (OPTIONAL)

The metadata extension is OPTIONAL for TRC-721 smart contracts. This allows your smart contract to be interrogated for its name and details about the assets that your NFTs represent.

```javascript solidity
interface TRC721Metadata {
     function name() external view returns (string _name);
     function symbol() external view returns (string _symbol);
     function tokenURI(uint256 _tokenId) external view returns (string);
  }
```

**name()**\
Returns the contract name

**symbol()**\
Returns the contract symbol

**tokenURI(uint256\_tokenId)**\
Returns the URI of the external file corresponding to \_tokenId. External resource files need to include names, descriptions, and pictures.

# Enumeration Extension Interface (OPTIONAL)

The enumeration extension is OPTIONAL for TRC-721 smart contracts. This allows your contract to publish its full list of NFTs and make them discoverable.

```javascript solidity
interface TRC721Enumerable  {
    function totalSupply() external view returns (uint256);
    function tokenByIndex(uint256 _index) external view returns (uint256);
    function tokenOfOwnerByIndex(address _owner, uint256 _index) external view returns (uint256);
  }
```

**totalSupply()**\
Returns the total amount of NFTs

**tokenByIndex(uint256\_index)**\
Returns the corresponding tokenId through \_index

**tokenOfOwnerByIndex(address\_owner, uint256 \_index)**\
Returns the tokenId corresponding to the index in the owner's NFT list
