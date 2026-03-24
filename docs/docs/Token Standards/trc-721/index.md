---
title: TRC-721
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
# 1 TRC-721 Protocol Standard

TRC-721 is a set of standard interfaces, for issuing non-fungible tokens (NFT) on the TRON network. TRC-721 is fully compatible with ERC-721.

## 1.1 TRC-721 Smart Contract Interface Implementation

Every TRC-721 compliant contract must implement the TRC-721 and TRC-165 interfaces. Other extension interfaces can be implemented according to specific business requirements.

### 1.1.1 TRC-721 & TRC-165 Interfaces

```javascript Solidity
pragma solidity ^0.4.20;

  interface TRC721 {
    // Returns the number of NFTs owned by the given account
    function balanceOf(address _owner) external view returns (uint256);

    //Returns the owner of the given NFT
    function ownerOf(uint256 _tokenId) external view returns (address);

    //Transfer ownership of NFT
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable;

    //Transfer ownership of NFT
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) external payable;

    //Transfer ownership of NFT
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;

    //Grants address ‘_approved’ the authorization of the NFT ‘_tokenId’
    function approve(address _approved, uint256 _tokenId) external payable;

    //Grant/recover all NFTs’ authorization of the ‘_operator’
    function setApprovalForAll(address _operator, bool _approved) external;

    //Query the authorized address of NFT
    function getApproved(uint256 _tokenId) external view returns (address);

    //Query whether the ‘_operator’ is the authorized address of the ‘_owner’
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);

    //The successful ‘transferFrom’ and ‘safeTransferFrom’ will trigger the ‘Transfer’ Event
    event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);

    //The successful ‘Approval’ will trigger the ‘Approval’ event
    event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);

    //The successful ‘setApprovalForAll’ will trigger the ‘ApprovalForAll’ event
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);

  }

  interface TRC165 {
      //Query whether the interface ‘interfaceID’  is supported
      function supportsInterface(bytes4 interfaceID) external view returns (bool);
  }
```

A wallet/broker/auction application MUST implement the `wallet` interface if it opts to accept safe transfers.

```javascript Solidity
interface TRC721TokenReceiver {
     //This method will be triggered when the ‘_to’ is the contract address during the ‘safeTransferFrom’ execution, and the return value must be checked, If the return value is not bytes4(keccak256("onTRC721Received(address,address,uint256,bytes)")) throws an exception. The smart contract which can receive NFT must implement the TRC721TokenReceiver interface.
       function onTRC721Received(address _operator, address _from, uint256 _tokenId, bytes _data) external                returns(bytes4);
   }
```

> 🚧 Note
>
> The hash of `bytes4(keccak256("onTRC721Received(address,address,uint256,bytes)))` is different from the Ethereum version `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)))`. Please use `0x5175f878` instead of `0x150b7a02`.

### 1.1.2 Metadata Extension Interface (OPTIONAL)

The metadata extension is OPTIONAL for TRC-721 smart contracts. This allows your smart contract to be interrogated for its name and details about the assets that your NFTs represent.

```javascript Solidity
interface TRC721Metadata {
     //Return the token name
     function name() external view returns (string _name);

      //Return the token symbol
     function symbol() external view returns (string _symbol);

       //Returns the URI of the external file corresponding to ‘_tokenId’. External resource files need to include names, descriptions and pictures. 
     function tokenURI(uint256 _tokenId) external view returns (string);
  }
```

URI is a URI link describing the \_tokenId asset, pointing to a JSON file that conforms to the TRC-721 metadata description structure. When tokens are minted, each token needs to be assigned a unique URI:

```json
{
	"title": "Asset Metadata",
	"type": "object",
	"properties": {
		"name": {
			"type": "string",
			"description": "Identifies the asset to which this NFT represents"
		},
		"description": {
			"type": "string",
			"description": "Describes the asset to which this NFT represents"
		},
		"image": {
			"type": "string",
			"description": "A URI pointing to a resource with mime type image/* representing the asset to which this NFT represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
		}
	}
}
```

### 1.1.3 Enumeration Extension Interface (OPTIONAL)

The enumeration extension is OPTIONAL for TRC-721 smart contracts. This allows your contract to publish its full list of NFTs and make them discoverable.

```javascript Solidity
interface TRC721Enumerable  {
    //Return the total supply of NFT
    function totalSupply() external view returns (uint256);

    //Return the corresponding ‘tokenId’ through ‘_index’
    function tokenByIndex(uint256 _index) external view returns (uint256);

     //Return the ‘tokenId’ corresponding to the index in the NFT list owned by the ‘_owner'
    function tokenOfOwnerByIndex(address _owner, uint256 _index) external view returns (uint256);
  }
```
