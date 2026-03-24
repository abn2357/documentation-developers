---
title: Adding Assets to TronLink
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
TronLink's TronWeb and tronLink objects provide APIs for developers to add Tokens to TronLink to be displayed in the TronLink asset list.

Developers can provide a button in the project to add the specified Token directly to the list of assets displayed in the user's TronLink Chrome plugin.

> 📘 Note:
>
> Currently, only the main network and Nile test network assets can be added, not Shasta testnet assets.

The request function and its parameters are described as follows:

```javascript
await tronWeb.request({
    method: 'wallet_watchAsset',
    params: <WatchAssetParams>,
})
```

The TronWeb request calls a method of the TronLink plugin.

## Parameter description  

request receives one parameter, which is an object containing method and params  
method: The method of the TronLink plugin to be called. Currently `wallet_watchAsset` is supported.  
params: The parameters of the method method above. The following is the description of the wallet_watchAsset parameters

## Add TRC-10 asset

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
        var obj = setInterval(async ()=>{
          //if (window.tronLink.tronWeb) 
            if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
                clearInterval(obj)
              //var tronweb = window.tronLink.tronWeb
                var tronweb = window.tronWeb
                var tx = await tronweb.request({method: 'wallet_watchAsset',
                                                params:{type: 'trc10',
                                                        options: {address: '1002000'},
                                                        },
                                                }
                                               )

            }
        }, 10)
    </script>
</body>
</html>
```

When the code is executed, TronLink will pop up a window for the user to confirm or cancel the addition of the TRC-10 asset.

![1051](https://files.readme.io/7420393-demo10_en.png "demo10_en.png")

Click the "Add" button, and the asset will be displayed in the asset list.

![357](https://files.readme.io/252c42e-demo10_en_01.png "demo10_en_01.png")

## Add TRC-20 asset

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
        var obj = setInterval(async ()=>{
          //if (window.tronLink.tronWeb) 
            if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
                clearInterval(obj)
              //var tronweb = window.tronLink.tronWeb
                var tronweb = window.tronWeb
                var tx = await tronweb.request({method: 'wallet_watchAsset',
                                                params:{type: 'trc20',
                                                        options: {address: 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t'},
                                                        },
                                                }
                                               )

            }
        }, 10)
    </script>
</body>
</html>
```

When the code is executed, TronLink will pop up a window for the user to confirm or cancel the addition of the TRC-20 asset.

![1231](https://files.readme.io/de5564a-demo20_en.png "demo20_en.png")

Click the "Add" button, and the asset will be displayed in the asset list.

![358](https://files.readme.io/17eab66-demo20_en_01.png "demo20_en_01.png")

## Add TRC-721 asset

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
        var obj = setInterval(async ()=>{
          //if (window.tronLink.tronWeb) 
            if (window.tronWeb && window.tronWeb.defaultAddress.base58) {
                clearInterval(obj)
              //var tronweb = window.tronLink.tronWeb
                var tronweb = window.tronWeb
                var tx = await tronweb.request({method: 'wallet_watchAsset',
                                                params:{type: 'trc721',
                                                        options: {address: 'TCzUYnFSwtH2bJkynGB46tWxWjdTQqL1SG'},
                                                        },
                                                }
                                               )

            }
        }, 10)
    </script>
</body>
</html>
```

When the code is executed, TronLink will pop up a window for the user to confirm or cancel the addition of the TRC-721 asset.

![1242](https://files.readme.io/245ca1b-demo721_en.png "demo721_en.png")

Click the "Add" button, and the TRC-721 asset will be displayed in the collectibles list.

![357](https://files.readme.io/88e5fd2-demo721_en_01.png "demo721_en_01.png")
