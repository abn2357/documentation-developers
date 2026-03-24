---
title: Protocol Interfaces
excerpt: Implementation Rules
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# TRC-1155 Standard

## Required Items

The TRC-1155 contract must implement the following TRC-1155 and TRC-165 interfaces:

```solidity
  interface ITRC1155 {
    // Events
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);
    event TransferSingle(address indexed _operator, address indexed _from, address indexed _to, uint256 _id, uint256 _value);
    event TransferBatch(address indexed _operator, address indexed _from, address indexed _to, uint256[] _ids, uint256[] _values);
    event URI(string _value, uint256 indexed _id);
    // Required Functions
    function setApprovalForAll(address _operator, bool _approved) external;
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);
    function balanceOf(address _owner, uint256 _id) external view returns (uint256);
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids) external view returns (uint256[] memory);
    function safeTransferFrom(address _from, address _to, uint256 _id, uint256 _value, bytes calldata _data) external;
    function safeBatchTransferFrom(address _from, address _to, uint256[] calldata _ids, uint256[] calldata _values, bytes calldata _data) external;
}
  interface ITRC165 {
    function supportsInterface(bytes4 interfaceID) external view returns (bool);
}
```

1. setApprovalForAll(address \_operator, bool \_approved)\
   The caller authorizes all tokens in this TRC-1155 contract to \_operator or cancels the authorization.

   * Parameters:
     * \_operator: the address to be authorized or deauthorized
     * \_approved: Authorize (true) / Deauthorize (false)
   * Event: ApprovalForAll

   ```
   contract TRC1155 is ITRC1155, ITRC165
   {

       // id => (owner => balance)
       mapping (uint256 => mapping(address => uint256)) internal balances;

       // owner => (operator => approved)
       mapping (address => mapping(address => bool)) internal operatorApproval;

       function setApprovalForAll(address _operator, bool _approved) external {
           operatorApproval[msg.sender][_operator] = _approved;
           emit ApprovalForAll(msg.sender, _operator, _approved);
       }
       
       ......
   }
   ```

2. isApprovedForAll(address \_owner, address \_operator)\
   Query whether \_operator has the authorization from \_owner.

```
    function isApprovedForAll(address _owner, address _operator) external view returns (bool) {
        return operatorApproval[_owner][_operator];
    }
```

3. balanceOf(address \_owner, uint256 \_id)\
   Query the number of tokens (\_id) owned by an address (\_owner).

```
    function balanceOf(address _owner, uint256 _id) external view returns (uint256) {
        return balances[_id][_owner];
    }
```

4. balanceOfBatch(address\[] calldata \_owners, uint256\[] calldata \_ids)\
   Get the balance of multiple tokens under multiple accounts.

```
    function balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids) external view returns (uint256[] memory) {

        require(_owners.length == _ids.length);

        uint256[] memory balances_ = new uint256[](_owners.length);

        for (uint256 i = 0; i < _owners.length; ++i) {
            balances_[i] = balances[_ids[i]][_owners[i]];
        }

        return balances_;
    }
```

5. safeTransferFrom(address \_from, address \_to, uint256 \_id, uint256 \_value, bytes calldata \_data)\
    Transfer the `_value` amount of `_id` from the `_from` address to the `_to` address (with safety call).
   * Parameters
     * \_from: the source address
     * \_to: the target address
     * \_id: the token ID
     * \_value: the transfer amount
     * \_data: additional data with no specified format, MUST be sent unaltered in a call to `onERC1155Received` on `_to`
   * Event: TransferSingle

```
    bytes4 constant public TRC1155_ACCEPTED = 0xf23a6e61; // Return value from `onERC1155Received` call if a contract accepts receipt (i.e `bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)"))`).
    
    function safeTransferFrom(address _from, address _to, uint256 _id, uint256 _value, bytes calldata _data) external {

        require(_to != address(0x0), "_to must be non-zero.");
        require(_from == msg.sender || operatorApproval[_from][msg.sender] == true, "Need operator approval for 3rd party transfers.");

        // SafeMath will throw with insufficient funds _from
        // or if _id is not valid (balance will be 0)
        balances[_id][_from] = balances[_id][_from].sub(_value);
        balances[_id][_to]   = _value.add(balances[_id][_to]);

        // MUST emit event
        emit TransferSingle(msg.sender, _from, _to, _id, _value);

        // Now that the balance is updated and the event was emitted,
        // call onTRC1155Received if the destination is a contract.
        if (_to.isContract()) {
             _doSafeTransferAcceptanceCheck(msg.sender, _from, _to, _id, _value, _data);
        }
    }
    
    function _doSafeTransferAcceptanceCheck(address _operator, address _from, address _to, uint256 _id, uint256 _value, bytes memory _data) internal {

        require(TRC1155TokenReceiver(_to).onERC1155Received(_operator, _from, _id, _value, _data) == TRC1155_ACCEPTED, "contract returned an unknown value from onERC1155Received");
    }
```

6. safeBatchTransferFrom(address \_from, address \_to, uint256\[] calldata \_ids, uint256\[] calldata \_values, bytes calldata \_data)\
   Transfer the `_values` amount(s) of `_ids` from the `_from` address to the `_to` address (with safety call).
   * Parameters
     * \_ids: IDs of each token type (order and length must match the \_values array)
     * \_values: the transfer amounts of different token types (order and length must match the \_ids array)
   * Event: TransferBatch

```
    bytes4 constant internal TRC1155_BATCH_ACCEPTED = 0xbc197c81; // bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"))

    function safeBatchTransferFrom(address _from, address _to, uint256[] calldata _ids, uint256[] calldata _values, bytes calldata _data) external {

        // MUST Throw on errors
        require(_to != address(0x0), "destination address must be non-zero.");
        require(_ids.length == _values.length, "_ids and _values array length must match.");
        require(_from == msg.sender || operatorApproval[_from][msg.sender] == true, "Need operator approval for 3rd party transfers.");

        for (uint256 i = 0; i < _ids.length; ++i) {
            uint256 id = _ids[i];
            uint256 value = _values[i];

            // SafeMath will throw with insufficient funds _from
            // or if _id is not valid (balance will be 0)
            balances[id][_from] = balances[id][_from].sub(value);
            balances[id][_to]   = value.add(balances[id][_to]);
        }

        // Note: instead of the below batch versions of event and acceptance check you MAY have emitted a TransferSingle
        // event and a subsequent call to _doSafeTransferAcceptanceCheck in the above loop for each balance change instead.
        // Or emitted a TransferSingle event for each in the loop and then the single _doSafeBatchTransferAcceptanceCheck below.
        // However it is implemented the balance changes and events MUST match when a check (i.e. calling an external contract) is done.

        // MUST emit event
        emit TransferBatch(msg.sender, _from, _to, _ids, _values);

        // Now that the balances are updated and the events are emitted,
        // call onTRC1155BatchReceived if the destination is a contract.
        if (_to.isContract()) {
            _doSafeBatchTransferAcceptanceCheck(msg.sender, _from, _to, _ids, _values, _data);
        }
    }
    
    function _doSafeBatchTransferAcceptanceCheck(address _operator, address _from, address _to, uint256[] memory _ids, uint256[] memory _values, bytes memory _data) internal {

        require(TRC1155TokenReceiver(_to).onERC1155BatchReceived(_operator, _from, _ids, _values, _data) == TRC1155_BATCH_ACCEPTED, "contract returned an unknown value from onERC1155BatchReceived");
    }
```

7. event URI(string \_value, uint256 indexed \_id)\
   Emit when the URI is updated for a token ID.\
   \_value: the URI that points to a JSON file that conforms to the "TRC-1155 Metadata URI JSON Schema".

8. supportsInterface(bytes4 interfaceID)\
   It is an interface under the [TRC-165](https://github.com/tronprotocol/tips/blob/master/tip-165.md) standard to query whether a contract supports a contract interface (interfaceID). The parameter is the identifier of the interface to be queried. If the queried contract interface is supported, true is returned. Otherwise, false is returned. For a TRC-1155 contract, the TRC-1155 interface and the TRC-165 interface must be supported. So the code is as follows:

```
/////////////////////////////////////////// TRC165 //////////////////////////////////////////////

    /*
        bytes4(keccak256('supportsInterface(bytes4)')) == 0x01ffc9a7;
    */
    bytes4 constant private INTERFACE_SIGNATURE_TRC165 = 0x01ffc9a7;

    /*
        bytes4(keccak256("safeTransferFrom(address,address,uint256,uint256,bytes)")) ^
        bytes4(keccak256("safeBatchTransferFrom(address,address,uint256[],uint256[],bytes)")) ^
        bytes4(keccak256("balanceOf(address,uint256)")) ^
        bytes4(keccak256("balanceOfBatch(address[],uint256[])")) ^
        bytes4(keccak256("setApprovalForAll(address,bool)")) ^
        bytes4(keccak256("isApprovedForAll(address,address)"));
    */
    bytes4 constant private INTERFACE_SIGNATURE_TRC1155 = 0xd9b67a26;

    function supportsInterface(bytes4 _interfaceId) public view returns (bool) 
    {
         if (_interfaceId == INTERFACE_SIGNATURE_TRC165 ||
             _interfaceId == INTERFACE_SIGNATURE_TRC1155) {
            return true;
         }
         return false;
    }
```

## Optional Items

### TRC-1155 Token Receiver

If a contract wants to receive tokens of type TRC-1155, the contract must implement the following interface:

```solidity
interface TRC1155TokenReceiver {

function onERC1155Received(address _operator, address _from, uint256 _id, uint256 _value, bytes calldata _data) external returns(bytes4);
function onERC1155BatchReceived(address _operator, address _from, uint256[] calldata _ids, uint256[] calldata _values, bytes calldata _data) external returns(bytes4);
}
```

* onERC1155Received(address \_operator, address \_from, uint256 \_id, uint256 \_value, bytes calldata \_data) external returns(bytes4)
  * \_operator: the address that invokes safeTransferFrom
  * return: `0xf23a6e61`, which is the result of `bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)"))`

* onERC1155BatchReceived(address \_operator, address \_from, uint256\[] calldata \_ids, uint256\[] calldata \_values, bytes calldata \_data) external returns(bytes4)
  * \_operator: the address that invokes safeBatchTransferFrom
  * return: `0xbc197c81`, which is the result of `bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"))`

* supportsInterface(bytes4 interfaceID) external view returns (bool)

    Contracts that implement the TRC1155TokenReceiver interface should also implement this TRC-165 interface:

```
function supportsInterface(bytes4 interfaceID) external view returns (bool) {
    return  interfaceID == 0x01ffc9a7 ||    // TRC-165 interface support (i.e. `bytes4(keccak256('supportsInterface(bytes4)'))`).
            interfaceID == 0x4e2312e0;      // TRC-1155 `TRC1155TokenReceiver` interface support (i.e. `bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)")) ^ bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"))`).
}
```

The implementation may differ from the above but:

* It MUST return the constant value true if 0x01ffc9a7 is passed through the interfaceID argument. This signifies TRC-165 support.
* It MUST return the constant value true if 0x4e2312e0 is passed through the interfaceID argument. This signifies TRC-1155 TRC1155TokenReceiver support.

### Metadata Extension Interface

The TRC1155Metadata\_URI extension is optional for TRC-1155 smart contracts.

```javascript
interface TRC1155Metadata_URI {
     function uri(uint256 _id) external view returns (string memory);
}
```

1. uri(uint256 \_id)\
   Query the URI of a token. The URI points to a JSON file that conforms to the `TRC-1155 Metadata URI JSON file` specification.

`TRC-1155 Metadata URI JSON Schema`:

```json
{
    "title": "Token Metadata",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Identifies the asset to which this token represents",
        },
        "decimals": {
            "type": "integer",
            "description": "The number of decimal places that the token amount should display - e.g. 18, means to divide the token amount by 1000000000000000000 to get its user representation."
        },
        "description": {
            "type": "string",
            "description": "Describes the asset to which this token represents"
        },
        "image": {
            "type": "string",
            "description": "A URI pointing to a resource with mime type image/* representing the asset to which this token represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
        },
        "properties": {
            "type": "object",
            "description": "Arbitrary properties. Values may be strings, numbers, object or arrays.",
        },
        "localization": {
            "type": "object",
            "required": ["uri", "default", "locales"],
            "properties": {
                "uri": {
                    "type": "string",
                    "description": "The URI pattern to fetch localized data from. This URI should contain the substring `{locale}` which will be replaced with the appropriate locale value before sending the request."
                },
                "default": {
                    "type": "string",
                    "description": "The locale of the default data within the base JSON"
                },
                "locales": {
                    "type": "array",
                    "description": "The list of locales for which data is available. These locales should conform to those defined in the Unicode Common Locale Data Repository (http://cldr.unicode.org/)."
                }
            }
        }
    }
}
```

### Other Optional Interfaces

```javascript
interface ITRC1155MixFungible  {
    function isFungible(uint256 _id) public pure returns(bool)
    function isNonFungible(uint256 _id) public pure returns(bool)
    function getNonFungibleIndex(uint256 _id) public pure returns(uint256)
    function mintFungible(uint256 _id, address[] calldata _to, uint256[] calldata _quantities) external;
    function mintNonFungible(uint256 _type, address[] calldata _to) external;
}
```

**1. isFungible(uint256\_id)**\
Query whether the token is fungible.

**Recommended token ID encoding rules**\
In a TRC-1155 contract, there may be both fungible tokens and non-fungible tokens. In order to distinguish the types of tokens, it is recommended to use the following coding rules for token ID (256bit):

* For non-fungible tokens, a common 128-bit prefix is used, and the last 128 bits are used to distinguish different non-fungible tokens.
* For fungible tokens, the first 128 bits are used to distinguish different fungible tokens, and the last 128 bits are all 0.

Therefore, the implementation of isFungible can be:

```
contract TRC1155MixedFungible is ITRC1155 {

    // Use a split bit implementation.
    // Store the type in the upper 128 bits..
    uint256 constant TYPE_MASK = uint256(uint128(~0)) << 128;

    // the non-fungible index in the lower 128
    uint256 constant NF_INDEX_MASK = uint128(~0);

    // The top bit is a flag to tell if this is a NFI.
    uint256 constant TYPE_NF_BIT = 1 << 255;

    mapping (uint256 => address) nfOwners;

    function isFungible(uint256 _id) public pure returns(bool) {
        return _id & TYPE_NF_BIT == 0;
    }
}
```

**2.isNonFungible(uint256\_id)**\
Query whether the token is non-fungible.

```
    function isNonFungible(uint256 _id) public pure returns(bool) {
        return _id & TYPE_NF_BIT == TYPE_NF_BIT;
    }
```

**3.getNonFungibleIndex(uint256\_id)**\
Get the index of the NFT.

```
    function getNonFungibleIndex(uint256 _id) public pure returns(uint256) {
        return _id & NF_INDEX_MASK;
    }
```

**4.getNonFungibleBaseType(uint256\_id)**\
Get the base type of the NFT.

```
    function getNonFungibleBaseType(uint256 _id) public pure returns(uint256)     {
        return _id & TYPE_MASK;
    }
```

**5.mintFungible(uint256\_id, address\[] calldata \_to, uint256\[] calldata \_quantities)**\
Mint a fungible token for multiple people.

```
    function mintFungible(uint256 _id, address[] calldata _to, uint256[] calldata _quantities) external creatorOnly(_id) {

        require(isFungible(_id));

        for (uint256 i = 0; i < _to.length; ++i) {

            address to = _to[i];
            uint256 quantity = _quantities[i];

            // Grant the items to the caller
            balances[_id][to] = quantity.add(balances[_id][to]);

            // Emit the Transfer/Mint event.
            // the 0x0 source address implies a mint
            // It will also provide the circulating supply info.
            emit TransferSingle(msg.sender, address(0x0), to, _id, quantity);

            if (to.isContract()) {
                _doSafeTransferAcceptanceCheck(msg.sender, msg.sender, to, _id, quantity, '');
            }
        }
```

**6. mintNonFungible(uint256\_type, address\[] calldata \_to)**\
Mint an NFT for each specified person.

```
    function mintNonFungible(uint256 _type, address[] calldata _to) external creatorOnly(_type) {

        // creatorOnly() will only let a type pass through.
        require(isNonFungible(_type));

        // Index are 1-based.
        uint256 index = maxIndex[_type] + 1;
        maxIndex[_type] = _to.length.add(maxIndex[_type]);

        for (uint256 i = 0; i < _to.length; ++i) {
            address dst = _to[i];
            uint256 id  = _type | index + i;

            nfOwners[id] = dst;

            // You could use base-type id to store NF type balances if you wish.
            // balances[_type][dst] = quantity.add(balances[_type][dst]);

            emit TransferSingle(msg.sender, address(0x0), dst, id, 1);

            if (dst.isContract()) {
                _doSafeTransferAcceptanceCheck(msg.sender, msg.sender, dst, id, 1, '');
            }
        }
    }
```
