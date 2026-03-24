---
title: TronLink Events
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
TronLink currently supports sidechains and mainchains. Developers can detect the event message sent by TronLink in DApp to analyze whether is the sidechain or mainchain currently selected by TronLink, and which account is currently selected. Let's learn it with a simple example.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<script>
    window.addEventListener('message', function (e) {
        if (e.data.message && e.data.message.action == "tabReply") {
            console.log("tabReply event", e.data.message)
            if (e.data.message.data.data.node.chain == '_'){
                console.log("tronLink currently selects the main chain")
            }else{
                console.log("tronLink currently selects the side chain")
            }
        }

        if (e.data.message && e.data.message.action == "setAccount") {
            console.log("setAccount event", e.data.message)
            console.log("current address:", e.data.message.data.address)

        }
        if (e.data.message && e.data.message.action == "setNode") {
            console.log("setNode event", e.data.message)
            if (e.data.message.data.node.chain == '_'){
                console.log("tronLink currently selects the main chain")
            }else{
                console.log("tronLink currently selects the side chain")
            }
          
       // Tronlink chrome v3.22.1 & Tronlink APP v4.3.4 started to support 
        if (e.data.message && e.data.message.action == "connect") {
            console.log("connect event", e.data.message.isTronLink)
        }
          
       // Tronlink chrome v3.22.1 & Tronlink APP v4.3.4 started to support 
        if (e.data.message && e.data.message.action == "disconnect") {
            console.log("disconnect event", e.data.message.isTronLink)
        }
          
       // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support 
        if (e.data.message && e.data.message.action == "accountsChanged") {
            console.log("accountsChanged event", e.data.message)
            console.log("current address:", e.data.message.data.address)
        }
          
       // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support  
        if (e.data.message && e.data.message.action == "connectWeb") {
            console.log("connectWeb event", e.data.message)
            console.log("current address:", e.data.message.data.address)
        }
          
       // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support   
        if (e.data.message && e.data.message.action == "accountsChanged") {
            console.log("accountsChanged event", e.data.message)
        }
          
        // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support      
        if (e.data.message && e.data.message.action == "acceptWeb") {
            console.log("acceptWeb event", e.data.message)
        }
        // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support      
        if (e.data.message && e.data.message.action == "disconnectWeb") {
            console.log("disconnectWeb event", e.data.message)
        }
          
        // Tronlink chrome v3.22.0 & Tronlink APP v4.3.4 started to support     
        if (e.data.message && e.data.message.action == "rejectWeb") {
            console.log("rejectWeb event", e.data.message)
        }
           
        }
    })
    var obj = setInterval(async ()=>{
      //if (window.tronLink.tronWeb)
        if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
            clearInterval(obj)
          //let tronweb = window.tronLink.tronWeb
            let tronweb = window.tronWeb
        }
    }, 10)

</script>

</body>
</html>
```

The above code involves three events: `tabReply`, `setAccount`, and `setNode`. The following are the triggering scenarios of these events:

|                                                            |                     |
| :--------------------------------------------------------- | :------------------ |
| The completion of TronLink initialization(after page load) | tabReply            |
| Main chain and side chain switching in TronLink:           | setAccount, setNode |
| Setting nodes in TronLink                                  | setAccount, setNode |

* Before the DApp page is loaded, you can judge the `data.message.data.data.node.chain` field of the tabReply event to determine whether TronLink chose the side chain or the main chain when the page was loaded. If it is '_', it means the main chain. Otherwise it is the side chain, and the number of the side chain represented by chain. The number of each side chain is unique.

* After the DAPP page is loaded, you can judge the `data.message.data.data.node.chain` field of the setNode event to determine whether the user manually selected the side chain or the main chain in TronLink. If it is '_', it means the main chain. Otherwise it is the side chain, and the number of the side chain represented by chain. The number of each side chain is unique.

When `MainChain` is selected, the node in the returned message event is the selected network.

![2480](https://files.readme.io/cf23c32-demo3.png "demo3.png")

When `DAppChain` is selected, the node in the returned message event is the selected network.

![2492](https://files.readme.io/5d597a7-demo4.png "demo4.png")

When the `Shasta` test network is selected, the node in the returned message event is the selected network.

![2492](https://files.readme.io/824acc1-demo5.png "demo5.png")

## Add an Initialization Event

> 📘 Note:
>
> TronLink chrome v3.22.0 starts to support this initialization injection event, and TronLink APP (Android and iOS versions) will start to support this initialization injection event in v4.3.4.

When the variables are injected, the `tronLink#initialized` event is sent and the DApp developer can listen for this event to use the `tronWeb` and `tronLink` variables.

```javascript
// Tronlink Sending Code
window.dispatchEvent(new Event('tronLink#initialized'));

// Example
// Suggested reception method
if (window.tronLink) {
  handleTronLink();
} else {
  window.addEventListener('tronLink#initialized', handleTronLink, {
    once: true,
  });

  // If the event is not dispatched by the end of the timeout,
  // the user probably doesn't have TronLink installed.
  setTimeout(handleTronLink, 3000); // 3 seconds
}

function handleTronLink() {
  const { tronLink } = window;
  if (tronLink) {
    console.log('tronLink successfully detected!');
    // Access the decentralized web!
  } else {
    console.log('Please install TronLink-Extension!');
  }
}
```

## New Notification Event

> 📘 Note:
>
> Tronlink chrome v3.22.0 starts to support this initialization injection event, and TronLink APP (Android and iOS versions) will start to support this initialization injection event in v4.3.4.

### `accountsChanged` event

TronLink sends the `accountsChanged` event when switching accounts.

```javascript
{
  message: {
    action: 'accountsChanged',
    data: {
      address: currentAddress
    }
  },
  isTronLink: true
}
```

### `connectWeb` event

TronLink sends this event when the `active connection` dapp is made in the plugin popup page.

```json
{
  message: {
    action: 'connectWeb',
    data: {
      websiteName: '',
      websiteIcon: '',
      origin: '',
      hostname:''
    },
  }
}
```

### `acceptWeb` event

TronLink sends this event when a user `accepts` an authorization request initiated by dapp in the plugin whitelist authorization page.

```javascript
{
  message: {
    action: 'acceptWeb',
    data: {
      websiteName: '',
      websiteIcon: '',
      origin: '',
      hostname:''
    },
  }
}
```

### `disconnectWeb` event

TronLink sends this event when the `active reject` dapp is in the plugin popup page.

```javascript
{
  message: {
    action: 'disconnectWeb',
    data: {
      websiteName: '',
      websiteIcon: '',
      origin: '',
      hostname:''
    },
  }
}
```

### `rejectWeb` event

TronLink sends this event when a user `rejects` a dapp-initiated authorization request on the plugin whitelist authorization page.

```javascript
{
  message: {
    action: 'rejectWeb',
    data: {
      websiteName: '',
      websiteIcon: '',
      origin: '',
      hostname:''
    },
  }
}
```

> 📘 Note:
>
> TronLink chrome v3.22.1 & TronLink APP v4.3.4 (Android & iOS versions) start to support connect & disconnect notification events.

### `connect`event

When the popup screen actively connects to the dapp and whitelist authorization screens, the input variable will be updated and Tronlink will send a connect event when the update is complete.

```javascript
{
message: {
  action: 'connect'
},
isTronLink: true
}
```

### `disconnect`event

When the popup screen actively rejects a request from a user in the dapp and whitelist authorization screens, the input variable will be updated, and Tronlink will send a disconnect event when the update is complete.

```javascript
{
   message: {
      action: 'disconnect'
},
  isTronLink: true
}
```
