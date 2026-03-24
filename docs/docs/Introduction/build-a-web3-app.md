---
title: Build a Web3 App
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
This chapter covers the entire process of developing a DApp from scratch, from contract writing, to deployment, and finally to launching. By learning how to build a decentralized library, you can easily grasp the process of deploying your own decentralized applications on the TRON network.

# **Preparations**

## Install

### Nodej v10+

```shell
# node -v
v10.24.1
```

### TronLink

Install [TronLink’s Chrome extension](https://www.tronlink.org/).

# **What Are We Doing**

We are building a decentralized library that contains the following functions: 

* Book Borrowing
* Book Browsing
* Book Adding

Download the complete project code from [here](https://github.com/TRON-Developer-Hub/decentralized-library), and run npm install to install dependencies.

# **Data Structure**

Typically, borrowers may want to know the title, content, availability, and price of a book. On this basis, we design a structure in the contract called Book, which comprises the following properties:

```javascript solidity
struct Book {
       string name;
       string description;
       bool valid;      // false if been borrowed
       uint256 price;   // TRX per day
       address owner;   // owner of the book
}
```

We hope that the library will be able to have an easy way to find every book. To do this, we build a `bookId` attribute and a mapping relationship between `bookId` and `Book`, named `books`.

```javascript solidity
uint256 public bookId;

mapping (uint256 => Book) public books;
```

Additionally, we must keep track of each book's rental information, including the borrower and the start and end dates of borrowing.

As with Book, construct a structure called `Tracking` to keep track of the data mentioned above. This structure possesses the following fields:

```javascript solidity
struct Tracking {
       uint256 bookId;
       uint256 startTime; // start time, in timestamp
       uint256 endTime; // end time, in timestamp
       address borrower; // borrower's address
}
```

Similarly, a mapping relationship must be established to manage each rental record:

```javascript solidity
uint256 public trackingId;

mapping(uint256 => Tracking) public trackings;
```

# **Functions and Events**

Now, add fundamental functions to our library, including:

* Add a book to the library - `addBook`
* Borrow a book - `borrowBook`
* Remove a book from the library - `deleteBook`

## addBook

```javascript solidity
/**
* @dev Add a Book with predefined `name`, `description` and `price`
* to the library.
*
* Returns a boolean value indicating whether the operation succeeded.
*
* Emits a {NewBook} event.
*/
function addBook(string memory name, string memory description, uint256 price) public returns (bool) {
       Book memory book = Book(name, description, true, price, _msgSender());

       books[bookId] = book;

       emit NewBook(bookId++);

       return true;
}

/**
* @dev Emitted when a new book is added to the library.
* Note bookId starts from 0.
*/
event NewBook(uint256 bookId);
```

## borrowBook

```javascript solidity
/**
* @dev Borrow a book has `_bookId`. The rental period starts from
* `startTime` ends with `endTime`.
*
* Returns a boolean value indicating whether the operation succeeded.
*
* Emits a `NewRental` event.
*/
function borrowBook(uint256 _bookId, uint256 startTime, uint256 endTime) public payable returns(bool) {
       Book storage book = books[_bookId];

       require(book.valid == true, "The book is currently on loan");

       require(_msgValue() == book.price * _days(startTime, endTime), "Incorrect fund sent.");

       _sendTRX(book.owner, _msgValue());

       _createTracking(_bookId, startTime, endTime);

       emit NewRental(_bookId, trackingId++);
}
```

## deleteBook

```javascript solidity
/**
* @dev Delete a book from the library. Only the book's owner or the
* library's owner is authorised for this operation.
*
* Returns a boolean value indicating whether the operation succeeded.
*
* Emits a `DeleteBook` event.
*/
function deleteBook(uint256 _bookId) public returns(bool) {
       require(_msgSender() == books[_bookId].owner || isOwner(),
               "You are not authorised to delete this book.");
      
       delete books[_bookId];

       emit DeleteBook(_bookId);

       return true;
}
```

We use two tool methods in the `borrowBook` method: `_sendTRX` and `_createTracking`. We do not want users to invoke these APIs. Therefore, in accordance with Solidity's standards, we identify them as `internal`, which means they can be accessed only within the contract.

## \_sendTRX

```javascript solidity
/**
* @dev Send TRX to the book's owner.
*/
function _sendTRX(address receiver, uint256 value) internal {
       payable(address(uint160(receiver))).transfer(value);
}
```

## \_createTracking

```javascript solidity
/**
* @dev Create a new rental tracking.
*/
function _createTracking(uint256 _bookId, uint256 startTime, uint256 endTime) internal {
         trackings[trackingId] = Tracking(_bookId, startTime, endTime, _msgSender());

         Book storage book = books[_bookId];

         book.valid = false;
 }
```

The contract is done, and it’s time to deploy it.

# **Deployment and Testing**

[TronIDE](http://www.tronide.io/) is used to compile and deploy contracts. For easier testing, it is recommended that you utilize TRON's Nile test network for the initial deployment.

> 📘 Nile Testnet
>
> Nile is TRON's pilot test network, which can be the first place to launch new features that are to be launched on the Mainnet later. You can visit the [Nile's official website](https://nileex.io/) for additional information.

You need to stake or burn TRX to pay for Energy consumption during contract deployment. By clicking [here](https://nileex.io/join/getJoinPage), you can obtain some test coins. Please note that each address is only valid once.

The logged-in TronLink will automatically connect to TronIDE. However, you must ensure that the correct network is selected:

![](https://files.readme.io/05612c5-Picture1.png "Picture1.png")

If this is your first time using TronIDE, you must first enable two modules: Solidity Compiler and DEPLOYMENT.

![](https://files.readme.io/3e99c78-1.png "1.png")

After the two modules are activated, the left-side menu bar should appear as follows:

![](https://files.readme.io/a28b97a-2.png "2.png")

Create a new contract file, Library.sol, and paste the entire contract code here.

![](https://files.readme.io/9d9fcc5-Picture5.png "Picture5.png")

For the sample contract in this chapter, select "0.8.0+commit7c2e641" from the "Compiler" drop-down menu.

The contract that has been successfully compiled is now ready for deployment. To ensure proper deployment, you must specify the relevant feelimit in the field selected in the figure below. Enter 1000000000 as the feelimit. You can also refer to this figure for more detailed settings on feelimit.

![](https://files.readme.io/7adc193-3.png "3.png")

Click "Accept" in the pop-up window to sign for this deployment.

![](https://files.readme.io/6a8286c-4.png "4.png")

When the contract is deployed, the section selected in the figure below will show the methods that this contract is capable of calling.

![](https://files.readme.io/85f4568-5.png "5.png")

# **Build the DApp**

To begin with, copy the contract address that was previously deployed into the `libraryContractAddress` variable in utils.js.

## **Link the UI to TronLink**

The following step is to link the user interface (UI) to the TronLink Chrome wallet. TronLink injects the TronWeb object into each browser page, allowing the DApp to communicate with the TRON network.

## **Functions**

After connecting our UI to TronLink, we need to analyze how the UI interacts with smart contracts. Therefore, a contract object must be created to represent the decentralized library smart contract.

Create the following code in dapp-ui/plugins/utils.js to retrieve the smart contract object and save it to the global variable. Then, you can directly interact with the contract via the global variable.

```javascript
export async function setLibraryContract() {
     bookRentContract = await        
     window.tronWeb.contract().at('TMH1jAzAjCp2GdWm7hXSmhYyD3iKdpExoZ');
}
```

The library should have three fundamental functions：

* Add a book
* Browse available books
* Borrow a book

In index.vue, call setLibraryContract() to initialize the contract object.

```javascript
async mounted() {
   // init contract object
   await setLibraryContract();
   // fetch all books
   const books = await fetchAllBooks();
   this.posts = books;
 },
```

## **Add a Book**

To begin with, construct an add-book form for users to submit information about books for rental. On the back end, it will communicate with the library contract's addBook function.

Add the following code to dapp-ui/components/postAd() bookForm.vue's function:

```javascript
postAd() {
     // convert price from TRX to SUN
     postBookInfo(this.title,this.description,tronWeb.toSun(this.price));
 }
```

Add the following code to postBookInfo() of dapp-ui/plugins/utils.js:

```javascript
const result = await bookRentContract.addBook(name,description,price).send({
   feeLimit:100_000_000,
   callValue:0,
   shouldPollResponse:true
 });
```

## **Browse All Available Books**

The `fetchAllBooks()` function returns the book list, which contains a list of all available books.

Add the following code to dapp-ui/plugins/fetchAllBooks() utils.js's function:

```javascript
const books = [];

 const bookId  = await bookRentContract.bookId().call();
 //iterate from 0 till bookId
 for (let i = 0; i < bookId; i++){
   const book = await bookRentContract.books(i).call()
   if(book.name!="") // filter the deleted books
   {
     books.push(
       {id: i,name: book.name,description: book.description,price: tronWeb.fromSun(book.price)}
     )
   } 
 }
return books
```

In index.vue, call `fetchAllBooks()` to retrieve book information and show it on the homepage.

## **Borrow a Book**

The user may borrow the book after viewing the book's information.\
In the book() function of dapp-ui/components/detailsModal.vue, add the following code:

```javascript
// get Start date
     const startDay = this.getDayOfYear(this.startDate)
     // get End date
     const endDay = this.getDayOfYear(this.endDate)
     // price calculation
     const totalPrice =tronWeb.toSun(this.propData.price) * (endDay - startDay)
     // call metamask.bookProperty
     borrowBook(this.propData.id, startDay, endDay, totalPrice)
```

For dapp-ui/plugins/utils.js, add the following code to the borrowBook() function:

```javascript
const result = await bookRentContract.borrowBook(spaceId,checkInDate,checkOutDate).send({
   feeLimit:100_000_000,
   callValue:totalPrice,
   shouldPollResponse:true
 });
```

The development process of the library DApp is now completed.

# **Run the DApp**

Make sure that TronLink is logged in before running the following command to start the service:

```shell
npm run dev
```

To view the front-end page, type localhost:3000 into the browser's address bar.

![](https://files.readme.io/4f2e953-Picture9.png "Picture9.png")

To post book information for rental, click the "Rent Your Books" button in the upper-right corner. Fields for the book title, a brief description of the book, and the cost of the book for one day rental are all included in the form.

![](https://files.readme.io/9f10181-Picture10.png "Picture10.png")

After completing the form, click the "Submit" button. The information will be passed to the library contract's addBook function, which will generate a transaction that triggers the contract. Then, as presented below, a TronLink pop-up window will appear, requesting confirmation and the signature.

![](https://files.readme.io/9c21e77-Picture11.png "Picture11.png")

![](https://files.readme.io/b5ba7dc-Picture12.png "Picture12.png")

After successfully connecting the transaction to the chain, the following leasing information will be displayed on the page.

![](https://files.readme.io/775bd66-Picture13.png "Picture13.png")

Click "View" to view the book's comprehensive details and specify the rental period. To initiate a lease request, click "Lent Now", then the library contract function `borrowBook` will be called. Additionally, the leasing transaction must be signed and broadcasted to finish the process.

![](https://files.readme.io/36efcd5-Picture14.png "Picture14.png")
