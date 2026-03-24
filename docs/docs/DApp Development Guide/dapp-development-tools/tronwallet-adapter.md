---
title: Tronwallet Adapter
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
# Overview

[Tronwallet Adapter](https://walletadapter.org/) is a set of packages that contain wallet adapters and components for TRON DApps. With out-of-the-box components and unified methods, developers can easily interact with multiple kinds of wallets, `select/connect/disconnect` wallets and sign messages or transactions.

## Adapters

Wallet adapters help you access TRON wallets with consistent API.

There are many wallets supporting the TRON network such as TronLink, Ledger and so on. **Different wallets** and **different versions** of one wallet may have different interface to use. The aim of **Adapters** relavant pacakges is to shield these differences and offer consistent interface for DApp developers. DApps don't need to change their code frequently if they have accessed the TRON wallet dapters code.

For example, if you want to connect to different wallets, you have to use different methods:

```js
// TronLink
window.tronLink.request({ method: 'tron_requestAccounts' });

// Ledger
const transport = await TransportWebHID.create();
const app = new Trx(transport);

// WalletConnect
const wallet = new WalletConnectWallet({
 network: this._config.network,
 options: this._config.options
});
```

With the adapter, you can use consistent APIs for different wallets:

```js
// TronLink
const tronlinkAdapter = new TronLinkAdapter();
await tronlinkAdapter.connect();
await tronlinkAdapter.signMessage(message);

// Ledger
const ledgerAdapter = new LedgerAdapter();
await ledgerAdapter.connect();
await ledgerAdapter.signMessage(message);

// WalletConnect
const walletconnectAdapter = new WalletConnectAdapter();
await walletconnectAdapter.connect();
await walletconnectAdapter.signMessage(message);
```

## React Hooks

Adapter wallet hooks export a `useWallet()` hook which manages the global state of wallets, such as the current selected wallet and the connection state, address, and so on. It also provides some methods to interact with wallets.

When your DApp supports multiple wallets, with the help of the`useWallet()` hook you can easily:

* select which wallet to use
* connect to the selected wallet
* disconnect from the selected wallet
* call `signMessage` or `signTransaction` of the selected wallet

Examples:

```jsx
function Comp() {
 const { wallet, address, connected, select, connect, disconnect, signMessage, signTransaction } = useWallet();
 return (
   <div>
     <button onClick={() => select('TronLink')}>Select Wallet</button>
     <button onClick={connect}>Connect</button>
     <button onClick={disconnect}>Disconnect</button>
     <button onClick={() => signMessage('Hello World')}>Sign Message</button>
   </div>
 );
}
```

React UI Components

`useWallet()` only contains logic to manage wallet state. Besides, we provide a set of out-of-the-box components to help you interact with wallets:

* `WalletSelectButton`: Show the wallets dialog to select a wallet.
* `WalletConnectButton`: Connect to the selected wallet.
* `WalletDisconnectButton`: Disconnect from the selected wallet.
* `WalletActionButton`: A Button with multiple actions include `select/connect/disconnect`.

You can find react demos [here](https://github.com/tronprotocol/tronwallet-adapter/tree/main/demos/react-ui).

Here is the demo image:  
![](https://raw.githubusercontent.com/tronprotocol/tronwallet-adapter/main/demo.png)

# Wallet Adapters

`@tronweb3/tronwallet-adapters` provides multiple wallet adapters to help developers connect to TRON wallet like [TronLink](https://www.tronlink.org/) with consistent APIs.

## Installation

```shell
npm install @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or pnpm install @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or yarn add @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
```

## Usage

### React

You can use `@tronweb3/tronwallet-adapters` in your component. Use `useMemo` to memorize the `adapter` to improve your web performance.

```tsx
import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';

function App() {
 const [readyState, setReadyState] = useState(WalletReadyState.NotFound);
 const [account, setAccount] = useState('');
 const [netwok, setNetwork] = useState({});
 const [signedMessage, setSignedMessage] = useState('');

 const adapter = useMemo(() => new TronLinkAdapter(), []);
 useEffect(() => {
   setReadyState(adapter.state);
   setAccount(adapter.address!);

   adapter.on('connect', () => {
     setAccount(adapter.address!);
   });

   adapter.on('readyStateChanged', state => {
     setReadyState(state);
   });

   adapter.on('accountsChanged', data => {
     setAccount(data);
   });

   adapter.on('chainChanged', data => {
     setNetwork(data);
   });

   adapter.on('disconnect', () => {
     // when disconnect from wallet
   });
   return () => {
     // remove all listeners when components is destroyed
     adapter.removeAllListeners();
   };
 }, []);

 async function sign() {
   const res = await adapter!.signMessage('helloworld');
   setSignedMessage(res);
 }

 return (
   <div className="App">
     <div>readyState: {readyState}</div>
     <div>current address: {account}</div>
     <div>current network: {JSON.stringify(netwok)}</div>
     <button disabled={adapter.connected} onClick={() => adapter.connect()}>
       Connect to TronLink
     </button>
     <button onClick={sign}>sign message</button>
     <br />
     SignedMessage: {signedMessage}
   </div>
 );
}
```

### Vue

In Vue, as the `created/mounted` hook just can be executed once, you can init the adapter in the `mounted` or `created` hook.

```js
// vue2.x
export default {
   created() {
       this.adapter = new TronLinkAdapter();
       this.adapter.on('connect', () => {
           // here you can do something
       });
   },
   beforeDestroy() {
       this.adapter.removeAllListeners();
   }
}

// vue3
export default {
   setup() {
       onMounted(function() {
           const adapter = new TronLinkAdapter();
           adapter.on('connect', () => {
               // here you can do something
           });
       });
       onBeforeUnmount(function() {
           // remove all listeners when components is destroyed
           adapter.removeAllListeners();
       });
       return {};
   }
}
```

## API Reference

### Adapter

The `Adapter` class defines the common interface for all adapters of specified wallets.

#### Constructor

* `constructor(config)`: the adapter constructor method. It accepts an optional `config` object. For detailed configuration types, refer to the [adapter](#tronlinkadapter) section.

#### Properties

* `name`: The name of the adapter.
* `url`: The website of the adapter's wallet.
* `icon`: The icon of the adapter's wallet.
* `readyState`: The wallet's state, which includes three value:
* `Loading`: When the adapter is checking if the wallet is available or not.
* `NotFound`: The wallet is not detected in the current browser.
* `Found`: The wallet is detected in the current browser.
* `address`: The address of current account when the adapter is connected.
* `connecting`: Whether the adapter is trying to connect to the wallet.
* `connected`: Whether the adapter is connected to the wallet.

#### Methods

* `connect(): Promise<void>`: connect to the wallet.
* `disconnect(): Promise<void>`: disconnect from the wallet.
* `signMessage(message, privateKey?): Promise<string>`: sign a string; returns the signature result. An optional `privateKey` can be provided.
* `signTransaction(transaction, privateKey?)`: sign a transaction; returns the signature result of the transaction. An optional `privateKey` can be provided.
* `multiSign(transaction, privateKey: string | null, permissionId?)`: sign a Account Permission Management transaction.
* If `privateKey` is not `null`, will use the privateKey to sign rather than TronLink.
* If `permissionId` is not provided, will use `0`(OwnerPerssion) as default.
* Please refer to [here](https://developers.tron.network/docs/multi-signature) for more about Account Permission Management,
* `switchChain(chainId: string): Promise<void>;`: request wallet to switch chain by `chainId`.

#### Events

`Adapter` extends the `EventEmitter` class in the `eventemitter3` package. So you can listen to the events by `adapter.on('connect', function() {})`.

Events are as follows:

* `connect(address)`: Emit when the adapter is connected to the wallet. The parameter is the address of current account.
* `disconnect()`: Emit when the adapter is disconnected from the wallet.
* `readyStateChanged(state: WalletReadyState)`: Emit when wallet's `readyState` is changed. The parameter is the state of the wallet.

```typescript
enum WalletReadyState {
  /**
  * Adapter will start to check if wallet exists after adapter instance is created.
  */
  Loading = 'Loading',
  /**
  * When checking ends and wallet is not found, readyState will be NotFound.
  */
  NotFound = 'NotFound',
  /**
  * When checking ends and wallet is found, readyState will be Found.
  */
  Found = 'Found'
}
```

* `accountsChanged(address: string, preAddress: string)`: Emit when users change the current selected account in the wallet. The parameter is the address of the new account.
* `chainChanged(chainInfo: ChainInfo)`: Emit when users change the current selected chain in wallet. The parameter is the new network config:

```typescript
interface ChainInfo {
  chainId: string;
}
```

* `error(WalletError)`: Emit when there are some errors when call the adapter's method is called. The [WalletError Types] is defined as follows.

### WalletError

`WalletError` is a superclass which defines the error when using adapter.  
All error types are extended from this class.  
Developers can check the error type according to the error instance.

```typescript
try {
 // do something here
} catch (error: WalletError) {
 if (error instanceof WalletNotFoundError) {
   console.log('Wallet is not found');
 }
}
```

All errors are as follows:

* `WalletNotFoundError`: Occurs when no wallet is installed.
* `WalletNotSelectedError`: Occurs when no selected wallet is found during connection.
* `WalletDisconnectedError`: Occurs when wallet is disconnected. Used by some wallets which won't connect automatically when `signMessage()` or `signTransaction()`is called.
* `WalletConnectionError`: Occurs when trying to connect a wallet.
* `WalletDisconnectionError`: Occurs when trying to disconnect a wallet.
* `WalletSignMessageError`: Occurs when calling `signMessage()`.
* `WalletSignTransactionError`: Occurs when calling `signTransaction()`.
* `WalletSwitchChainError`: Occurs when calling `switchChain()`. Only supported by TronLink.
* `WalletGetNetworkError`: Occurs when calling `network()` to get network information.

Following example shows how to get original error info with `WalletError`:

```js
const adapter = new TronLinkAdapter();
try {
   await adapter.connect();
} catch (e: any) {
   const originalError = e.error;
}
```

<h3 id="tronlinkadapter">TronLinkAdapter</h3>

* `Constructor(config: TronLinkAdapterConfig)`

```typescript
interface TronLinkAdapterConfig {
  /**
  * Set if open Wallet's website url when wallet is not installed.
  * Default is true.
  */
  openUrlWhenWalletNotFound?: boolean;
  /**
  * Timeout in millisecond for checking if TronLink wallet exists.
  * Default is 30 * 1000ms
  */
  checkTimeout?: number;
  /**
  * Set if open TronLink app using DeepLink on mobile device.
  * Default is true.
  */
  openTronLinkAppOnMobile?: boolean;
  /**
  * The icon of your dapp. Used when open TronLink app in mobile device browsers.
  * Default is current website icon.
  */
  dappIcon?: string;
  /**
  * The name of your dapp. Used when open TronLink app in mobile device browsers.
  * Default is `document.title`.
  */
  dappName?: string;
}
```

* The `network()` method is supported to get current network information. The type of the `Network` returned value is as follows:

  ```typescript
  export enum NetworkType {
      Mainnet = 'Mainnet',
      Shasta = 'Shasta',
      Nile = 'Nile',
      /**
       * When use custom node
       */
      Unknown = 'Unknown',
  }

  export type Network = {
      networkType: NetworkType;
      chainId: string;
      fullNode: string;
      solidityNode: string;
      eventServer: string;
  };
  ```
* **`disconnect` is not supported for DApp**. As TronLinkAdapter doesn't support disconnecting via DApp websites, calling `adapter.disconnect()` won't actually disconnect from the TronLink extension.
* **Auto open TronLink app in mobile browser**. If developers call the `connect()` method in a mobile browser, it will open the DApp in the TronLink app to access the TronLink wallet.

Others adapters  
Other adapters' `Constructor` config API can be found in their source code `README`.

* [TokenPocketAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/tokenpocket)
* [BitKeepAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/bitkeep)
* [OkxWalletAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/okxwallet)
* [WalletConnectAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/walletconnect)
* [LedgerAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/ledger)
* [ImTokenAdapter](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/imtoken)

# Adapter React Hooks

`@tronweb3/tronwallet-adapter-react-hooks` provides a `useWallet()` hook which will make it easy to "Connect Wallet" and listen to the state change for developers.

## Installation

```bash
npm install @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or pnpm install @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or yarn add @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
```

## Usage

`@tronweb3/tronwallet-adapter-react-hooks` uses [`Context` of React](https://reactjs.org/docs/context.html) to maintain shared data. So developers need to wrap `App` content within the `WalletProvider`.

You can provide a `onError` callback to handle various errors such as `WalletConnectionError` and `WalletNotFoundError`.

```jsx
import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-react-hooks';
import { WalletDisconnectedError, WalletError, WalletNotFoundError } from '@tronweb3/tronwallet-abstract-adapter';
import toast, { Toaster } from 'react-hot-toast';

function App() {
    // use `react-hot-toast` npm package to notify user what happened here
    function onError(e: WalletError) {
        if (e instanceof WalletNotFoundError) {
            toast.error(e.message);
        } else if (e instanceof WalletDisconnectedError) {
            toast.error(e.message);
        } else toast.error(e.message);
    }
    return (
        <WalletProvider onError={onError}>
            <ConnectComponent></ConnectComponent>
            <Profile></Profile>
        </WalletProvider>
    );
}
function ConnectComponent() {
    const { connect, disconnect, select, connected } = useWallet();
    return (<div>
      <button type="button" onClick={() => select('TronLink Adapter' as any)}> Select TronLink</button>
      <button type="button" disabled={connected} onClick={connect}>Connect</button><br>
      <button type="button" disabled={!connected} onClick={disconnect}>Disconnect</button>
    </div>);
}
function Profile() {
    const { address, connected, wallet } = useWallet();
    return (<div>
        <p> <span>Connection Status:</span> {connected ? 'Connected' : 'Disconnected'}</p>
        <p> <span>Your selected Wallet:</span> {wallet?.adapter.name} </p>
        <p> <span>Your Address:</span> {address} </p>
    </div>);
}
```

## `WalletProvider`

`WalletProvider` and `useWallet` work together like `Context.Provider` and `useContext()`. There is a `WalletProviderContext` underlying which maintains some state and can be obtained with `useWallet`. So developers need to wrap application components with `WalletProvider`.

```jsx
import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-react-hooks';
function App() {
    return <WalletProvider>/* here is application components */</WalletProvider>;
}
```

### Props

#### adapters:

* Required: `false`
* Type: `Adapter[]`
* Default: `[ new TronLinkAdapter() ]`

Used to specify what wallet adapters are supported. All wallet adapters can be imported from the `@tronweb3/tronwallet-adapters` package or their standalone package.

* Example
  ```jsx
  import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-react-hooks';
  import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';
  function App() {
      const adapters = useMemo(() => [new TronLinkAdapter()]);
      return <WalletProvider adapters={adapters}>/* here is application components */</WalletProvider>;
  }
  ```

#### onError

* Required: `false`
* Type: `(error: WalletError): void`
* Default: `function(error) { console.error(error); }`

Used to handle errors occured when using wallets. Developers can use the callback to tell users what happened according to the `error` type. All error types can be found [here](https://github.com/web3-geek/tronwallet-adapter/blob/main/packages/adapters/abstract-adapter/src/errors.ts).

* Example
  ```jsx
  functon onError(e) {
  if (e instanceof WalletNotFoundError) {
          console.error(e.message);
      } else if (e instanceof WalletDisconnectedError) {
          console.error(e.message);
      } else console.error(e.message);
  }
  ```

#### autoConnect

* Required: `false`
* Type: `boolean`
* Default: `true`

Whether to connect to the specified wallet automatically when loading the page and selecting a wallet.

#### disableAutoConnectOnLoad

* Required: `false`
* Type: `boolean`
* Default: `false`

When `autoConnect` is enabled, whether to automatically connect to the current selected wallet when loading the page.  
If you don't want to connect the wallet when the page is first loaded, set `disableAutoConnectOnLoad: true`.

#### localStorageKey

* Required: `false`
* Type: `string`
* Default: `tronAdapterName`

Specify the key used to cache wallet names in `localStorage`. When the user selects a wallet, applications will cache the wallet name to localStorage.

#### Event handlers

You can provide event handlers to listen for adapter events, such as `connect`,`disconnect`, and `accountsChanged`. Available event handlers and their types are as follows:

* `readyStateChanged: (readyState: 'Found' | 'NotFound') => void`: Called when the current adapter emits the `readyStateChanged` event.
* `onConnect: (address: string) => void`: Called when the current adapter emits the `connect` event.
* `onDisconnect: () => void`: Called when the current adapter emits the `disconnect` event.
* `onAccountsChanged: (newAddress: string; preAddress?: string) => void`: Called when the current adapter emits the `accountsChanged` event.
* `onChainChanged: (chainData: unknow) => void`: Called when the current adapter emits the `chainChanged` event.

An event handler named `onAdapterChanged` is also available to get noticed when the selected adapter is changed.

* `onAdapterChanged: (adapter: Adapter | null) => void`: Called when the current adapter is changed.

Here is an example:

```jsx
import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-react-hooks';
import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';
function App() {
    const adapters = useMemo(() => [new TronLinkAdapter()]);
    const onAccountsChanged = useCallback((curAddr, preAddr) => {
        console.log('new address is: ', curAddr, ' previous address is: ', preAddr);
    }, []);
    return (
        <WalletProvider adapters={adapters} onAccountsChanged={onAccountsChanged}>
            /* here is application components */
        </WalletProvider>
    );
}
```

## `useWallet()`

`useWallet` is a react hook providing a set of properties and methods which can be used to select and connect wallet, get wallet state and so on.

> `useWallet()` must be used in the descendant components of `WalletProvider`!

### ReturnedValue

#### `autoConnect`

* Type: `boolean`  
  Synchronous with the `autoConnect` property passed to `WalletProvider`.

#### `disableAutoConnectOnLoad`

* Type: `boolean`  
  Synchronous with the `disableAutoConnectOnLoad` property passed to `WalletProvider`.

#### `wallet`

* Type: `Wallet | null`  
  The wallet currently selected. If no wallet is selected, the value is `null`.

`Wallet` is defined as follow:

```typescript
interface Wallet {
    adapter: Adapter; // wallet adapter
    state: AdapterState;
}
enum AdapterState {
    NotFound = 'NotFound',
    Disconnect = 'Disconnected',
    Connected = 'Connected',
}
```

#### `address`

* Type: `string | null`  
  Address of the current selected wallet. If no wallet is selected, the value is `null`.

#### `wallets`

* Type: `Wallet[]`  
  Wallet list based on currently used adapters when initializing `WalletProvider`.

#### `connecting`

* Type: `boolean`  
  Indicates if the wallet is connecting.

#### `connected`

* Type: `boolean`  
  Indicates if the wallet is connected.

#### `disconnecting`

* Type: `boolean`  
  Indicates if the wallet is disconnecting.

### Methods

#### select

* Type: `(walletAdapterName: AdapterName) => void`  
  Select a wallet by walletAdapterName. Valid adapters can be found [here](https://github.com/web3-geek/tronwallet-adapter/tree/main/packages/adapters/adapters).

#### connect

* Type: `() => Promise<void>`  
  Connect to the current selected wallet.

#### disconnect

* Type: `() => Promise<void>`  
  Disconnect from the current selected wallet.

### signTransaction

* Type: `(transaction: Transaction) => Promise<SignedTransaction>`  
  Sign an unsigned transaction. This method is the same as the TronWeb API.

### signMessage

* Type: `(message: string) => Promise<string>`  
  Sign a message.

### Example

```js
import { useWallet } from '@tronweb3/tronwallet-adapter-react-hooks';
import { AdapterName } from '@tronweb3/tronwallet-abstract-adapter';

function Content() {
    const { connect, disconnect, select, connected } = useWallet();
    return (
        <div>
            <button type="button" onClick={() => select('TronLink Adapter')}>
                Select TronLink
            </button>
            <button type="button" disabled={connected} onClick={connect}>
                Connect
            </button>
            <button type="button" disabled={!connected} onClick={disconnect}>
                Disconnect
            </button>
        </div>
    );
}
```

# Adapter React UI Components

`@tronweb3/tronwallet-adapter-react-ui` provides a set of out-of-the-box components to make it easy to select, change, connect and disconnect wallets.

This package relies on `@tronweb3/tronwallet-adapter-react-hooks` for functionality. So developers must wrap `App` content within the `WalletProvider`.

## Installation

```shell
npm install @tronweb3/tronwallet-adapter-react-ui @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or pnpm install @tronweb3/tronwallet-adapter-react-ui @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or yarn add @tronweb3/tronwallet-adapter-react-ui @tronweb3/tronwallet-adapter-react-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
```

## Usage

`@tronweb3/tronwallet-adapter-react-ui` provides a `Select Wallet Modal` by `Context.Provider`. Developers must wrap `App` content within the `WalletProvider` and `WalletModalProvider`.

```jsx
import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-react-hooks';
import { WalletModalProvider, WalletActionButton } from '@tronweb3/tronwallet-adapter-react-ui';
import '@tronweb3/tronwallet-adapter-react-ui/style.css';
import { WalletDisconnectedError, WalletError, WalletNotFoundError } from '@tronweb3/tronwallet-abstract-adapter';
import toast, { Toaster } from 'react-hot-toast';

function App() {
 // here use `react-hot-toast` npm package to notify user what happened
 function onError(e: WalletError) {
   if (e instanceof WalletNotFoundError) {
     toast.error(e.message);
   } else if (e instanceof WalletDisconnectedError) {
     toast.error(e.message);
   } else toast.error(e.message);
 }
 return (
   <WalletProvider onError={onError}>
     <WalletModalProvider>
       <ConnectComponent></ConnectComponent>
       <Profile></Profile>
     </WalletModalProvider>
   </WalletProvider>
 );
}
function ConnectComponent() {
 const { connect, disconnect, select, connected } = useWallet();
 return <WalletActionButton></WalletActionButton>;
}
function Profile() {
 const { address, connected, wallet } = useWallet();
 return (
   <div>
     <p>
       <span>Connection Status:</span> {connected ? 'Connected' : 'Disconnected'}
     </p>
     <p>
       <span>Your selected Wallet:</span> {wallet?.adapter.name}
     </p>
     <p>
       <span>Your Address:</span> {address}
     </p>
   </div>
 );
}
```

## API Reference

### WalletModalProvider and useWalletModal

`WalletModalProvider` provides a `Select Wallet Modal` by `Context.Provider`. The modal can be controled by `useWalletModal`.

```jsx
function App() {
 const { visible, setVisible } = useWalletModal();
 function toggle() {
   setVisible(visible => !visible);
 }
 return (
   <div>
     <button onClick={toggle}>{visible ? 'Close Modal' : 'Open Modal'}</button>
   </div>
 );
}
```

### WalletConnectButton

Button to connect to the selected wallet. The button is disabled when:

* no wallet is selected
* the wallet is connecting
* the wallet is connected
* disabled by props

#### Props

```jsx
type ButtonProps = PropsWithChildren<{
 className?: string,
 disabled?: boolean,
 onClick?: (e: MouseEvent<HTMLButtonElement>) => void,
 style?: CSSProperties,
 tabIndex?: number,
 icon?: string
}>;
```

### WalletDisconnectButton

Button to connect to the selected wallet. The button is disabled when:

* no wallet is selected
* the wallet is connecting
* disabled by props

#### Props

Same as `WalletConnectButton`.

### WalletSelectButton

Button to open `Select Wallet Modal`.

#### Props

Same as `WalletConnectButton`.

### WalletActionButton

Button with multiple features including:

* Select wallet
* Connect to wallet
* Disconnect from wallet
* Show current selected wallet and address
* Copy address

It's recommended to use this component to connect wallet easily.  
Here is the demo:  
![](https://raw.githubusercontent.com/tronprotocol/tronwallet-adapter/main/docs/action-button.gif)

#### Props

Same as `WalletConnectButton`.

# Vue Hooks

`@tronweb3/tronwallet-adapter-vue-hooks` provides a `useWallet()` hook which will make it easy to "Connect Wallet" and listen to the state change for developers.

## Installation

```bash
npm install @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or pnpm install @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
# or yarn install @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
```

## Usage

`@tronweb3/tronwallet-adapter-vue-hooks` uses [`Provide / Inject ` in Vue](https://vuejs.org/guide/components/provide-inject.html) to maintain shared data. So developers need to wrap `App` content within the `WalletProvider`.

You can provide an `error` event listener to handle various errors such as `WalletConnectionError` and `WalletNotFoundError`.

Here is a [Demo project](https://github.com/web3-geek/tronwallet-adapter/tree/main/demos/vue-ui/vite-app):

```html
<script setup>
    import { defineComponent, h } from 'vue';
    import { WalletProvider, useWallet } from '@tronweb3/tronwallet-adapter-vue-hooks';
    import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';
    const tronLink = new TronLinkAdapter();

    const adapters = [tronLink];

    function onConnect(address) {
        console.log('[wallet hooks] onConnect: ', address);
    }
    function onDisconnect() {
        console.log('[wallet hooks] onDisconnect');
    }

    const VueComponent = defineComponent({
        setup() {
            // Here you can use `useWallet` API
            const { wallet, connect, signMessage, signTransaction } = useWallet();
            return () =>
                h('div', [
                    h('div', { style: 'color: #222;' }, `Current Adapter: ${(wallet && wallet.adapter.name) || ''}`),
                ]);
        },
    });
</script>

<template>
    <WalletProvider :adapters="adapters" @connect="onConnect" @disconnect="onDisconnect">
        <VueComponent />
    </WalletProvider>
</template>
```

## `WalletProvider`

`WalletProvider` and `useWallet` work together. `WalletProvider` uses `provide()` in Vue to provide a shared state. `useWallet` uses `inject()` to get the shared state. Developers need to wrap application components with `WalletProvider`.

```html
<html>
    <WalletProvider>/* here is application components */</WalletProvider>
</html>
<script setup>
    import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-vue-hooks';
</script>
```

### Props

#### adapters:

* Required: `false`
* Type: `Adapter[]`
* Default: `[ new TronLinkAdapter() ]`

Used to specify what wallet adapters are supported. All wallet adapters can be imported from the `@tronweb3/tronwallet-adapters` package or their standalone package.

* Example
  ```html
  <template>
      <WalletProvider :adapters="adapters">/* here is application components */</WalletProvider>
  </template>
  <script setup>
      import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-vue-hooks';
      import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';
      const adapters = [new TronLinkAdapter()];
  </script>
  ```

#### autoConnect

* Required: `false`
* Type: `boolean`
* Default: `true`

Whether to connect to the specified wallet automatically after a wallet is selected.

#### disableAutoConnectOnLoad

* Required: `false`
* Type: `boolean`
* Default: `false`

Whether to automatically connect to the current selected wallet after the page is loaded when `autoConnect` is enabled.  
If you don't want to connect to the wallet when the page is first loaded, set `disableAutoConnectOnLoad: true`.

#### localStorageKey

* Required: `false`
* Type: `string`
* Default: `tronAdapterName`

Specify the key used to cache wallet name in `localStorage`. When the user selects a wallet, applications will cache the wallet name to localStorage.

#### Events

You can provide event handlers to listen for adapter events, such as `connect`, `disconnect`, and`accountsChanged`. Available events and their types are as follows:

* `readyStateChanged: (readyState: 'Found' | 'NotFound') => void`: Emits when the current adapter emits the `readyStateChanged` event.
* `connect: (address: string) => void`: Emits when the current adapter emits the `connect` event.
* `disconnect: () => void`: Emits when the current adapter emits the `disconnect` event.
* `accountsChanged: (newAddress: string; preAddress?: string) => void`: Emits when the current adapter emits the `accountsChanged` event.
* `chainChanged: (chainData: unknow) => void`: Emits when the current adapter emits the `chainChanged` event.
* `error: (error) => void`: Emits when errors occur in methods calls.

An event named `adapterChanged` is also available to get noticed when the selected adapter is changed.

* `adapterChanged: (adapter: Adapter | undefined) => void`: Called when the current adapter is changed.

Here is an example:

````
```html
<template>
    <WalletProvider :adapters="adapters" @accountsChanged="onAccountsChanged">/* here is application components */</WalletProvider>
</template>
<script setup>
    import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-vue-hooks';
    import { TronLinkAdapter } from '@tronweb3/tronwallet-adapters';
    const adapters = [new TronLinkAdapter()];

    function onAccountsChanged(curAddress, preAddress) {}
</script>
```
````

## `useWallet()`

`useWallet` is a react hook providing a set of properties and methods which can be used to select and connect wallets, get wallet states and so on.

> `useWallet()` must be used in the descendant components of `WalletProvider`!

### ReturnedValue

#### `autoConnect`

* Type: `ComputedRef<boolean>`  
  Synchronous with the `autoConnect` property passed to `WalletProvider`.

#### `disableAutoConnectOnLoad`

* Type: `ComputedRef<boolean>`  
  Synchronous with the `disableAutoConnectOnLoad` property passed to `WalletProvider`.

#### `wallet`

* Type: `ComputedRef<Wallet | null>`  
  The wallet currently selected. If no wallet is selected, the value is `null`.

`Wallet` is defined as follow:

```typescript
interface Wallet {
    adapter: Adapter; // wallet adapter
    state: AdapterState;
}
enum AdapterState {
    NotFound = 'NotFound',
    Disconnect = 'Disconnected',
    Connected = 'Connected',
}
```

#### `address`

* Type: `ComputedRef<string | null>`  
  Address of the current selected wallet. If no wallet is selected, the value is `null`.

#### `wallets`

* Type: `Ref<Wallet[]>`  
  Wallet list based on currently used adapters when initializing `WalletProvider`.

#### `connecting`

* Type: `Ref<boolean>`  
  Indicate if the wallet is connecting.

#### `connected`

* Type: `Ref<boolean>`  
  Indicate if the wallet is connected.

#### `disconnecting`

* Type: `Ref<boolean>`  
  Indicate if the wallet is disconnecting.

### Methods

#### select

* Type: `(walletAdapterName: AdapterName) => void`  
  Select a wallet by walletAdapterName. Valid adapters can be found [here](https://github.com/tronprotocol/tronwallet-adapter/tree/main/packages/adapters/adapters)

#### connect

* Type: `() => Promise<void>`  
  Connect to current selected wallet.

#### disconnect

* Type: `() => Promise<void>`  
  Disconnect from current selected wallet.

#### signTransaction

* Type: `(transaction: Transaction) => Promise<SignedTransaction>`  
  Sign a unsigned transaction. This method is the same as TronWeb API.

#### signMessage

* Type: `(message: string) => Promise<string>`  
  Sign a message.

### Example

```html
<template>
    <div>
        <button type="button" @click="() => select('TronLink Adapter')">Select TronLink</button>
        <button type="button" :disabled="connected" @click="connect">Connect</button>
        <button type="button" :disabled="!connected" @click="disconnect">Disconnect</button>
    </div>
</template>
<script setup>
    import { useWallet } from '@tronweb3/tronwallet-adapter-vue-hooks';
    import { AdapterName } from '@tronweb3/tronwallet-abstract-adapter';

    const { connect, disconnect, select, connected } = useWallet();
</script>
```

# Adapter Vue UI Components

`@tronweb3/tronwallet-adapter-vue-ui` provides a set of out-of-the-box components to make it easy to select, change, connect and disconnect wallet.

`@tronweb3/tronwallet-adapter-vue-ui` depends on `@tronweb3/tronwallet-adapter-vue-hooks` to work. So developers must wrap `App` content within the `WalletProvider`.

## Installation

```bash
npm install @tronweb3/tronwallet-adapter-vue-ui @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters

# or pnpm install @tronweb3/tronwallet-adapter-vue-ui @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters

# or yarn install @tronweb3/tronwallet-adapter-vue-ui @tronweb3/tronwallet-adapter-vue-hooks @tronweb3/tronwallet-abstract-adapter @tronweb3/tronwallet-adapters
```

## Usage

`@tronweb3/tronwallet-adapter-vue-ui` provide a `Select Wallet Modal` by `provide()` in Vue. So developers must wrap `App` content within the `WalletProvider` and `WalletModalProvider`.

> Note: A stylesheet must be imported to make components work fine.

Here is a [Demo project](https://github.com/tronprotocol/tronwallet-adapter/tree/main/demos/vue-ui/vite-app);

```html
<template>
    <WalletProvider @error="onError">
        <WalletModalProvider>
            <WalletActionButton></WalletActionButton>
            <Profile></Profile>
        </WalletModalProvider>
    </WalletProvider>
</template>
<script setup>
    import { h, defineComponent } from 'vue';
    import { useWallet, WalletProvider } from '@tronweb3/tronwallet-adapter-vue-hooks';
    import { WalletModalProvider, WalletActionButton } from '@tronweb3/tronwallet-adapter-vue-ui';
    // This is necessary to keep style normal.
    import '@tronweb3/tronwallet-adapter-vue-ui/style.css';
    import { WalletDisconnectedError, WalletError, WalletNotFoundError } from '@tronweb3/tronwallet-abstract-adapter';

    function onError(e: WalletError) {
        if (e instanceof WalletNotFoundError) {
            console.error(e.message);
        } else if (e instanceof WalletDisconnectedError) {
            console.error(e.message);
        } else console.error(e.message);
    }

    const ConnectComponent = defineComponent({
        setup() {
            return () => h(WalletActionButton);
        },
    });

    const Profile = defineComponent({
        setup() {
            const { wallet } = useWallet();
            return () => h('div', `Current adapter: ${wallet?.adapter.name}`);
        },
    });
</script>
```

## `WalletModalProvider` and `useWalletModal`

`WalletModalProvider` provide a `Select Wallet Modal` by `provide()` in Vue. The modal can be controled by `useWalletModal`.

```html
<template>
    <div>
        <button @click="toggle">{{visible ? 'Close Modal' : 'Open Modal'}}</button>
    </div>
</template>
<script setup>
    const { visible, setVisible } = useWalletModal();
    function toggle() {
        setVisible((visible) => !visible);
    }
</script>
```

## `WalletConnectButton`

Button to connect to the selected wallet. The button is disabled when:

* no wallet is selected
* the wallet is connecting
* the wallet is connected
* disabled by props

### Props

```jsx
type ButtonProps = PropsWithChildren<{
    className?: string,
    disabled?: boolean,
    onClick?: (e: MouseEvent<HTMLButtonElement>) => void,
    style?: CSSProperties,
    tabIndex?: number,
    icon?: string,
}>;
```

## `WalletDisconnectButton`

Button to connect to the selected wallet. The button is disabled when:

* no wallet is selected
* the wallet is connecting
* disabled by props

### Props

Same as `WalletConnectButton`.

## `WalletSelectButton`

Button to open `Select Wallet Modal`.

### Props

Same as `WalletConnectButton`.

## `WalletActionButton`

Button with multiple functions including:

* Select the wallet
* Connect to the wallet
* Disconnect from the wallet
* Show currently selected wallet and address
* Copy address

It's recommended to use this component to connect wallet easily.  
![](https://raw.githubusercontent.com/tronprotocol/tronwallet-adapter/main/docs/action-button.gif)

### Props

Same as `WalletConnectButton`.
