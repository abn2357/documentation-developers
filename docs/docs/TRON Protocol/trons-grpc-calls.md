---
title: TRON's gRPC Calls
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
## 1. Overview

gRPC is a modern, open-source, high-performance RPC framework based on the HTTP/2 protocol and Protocol Buffers (Protobuf) for data serialization. Compared to traditional HTTP/1.1 RESTful APIs, gRPC offers higher performance, lower latency, smaller packet sizes, bi-directional streaming capabilities, and a robust code generation mechanism, making it an ideal choice for efficient and stable interaction with blockchain nodes.

TRON provides a set of gRPC-based API interfaces, allowing developers to interact with TRON nodes in a high-performance and strongly typed manner. This article will use Java as an example to explain how to perform a basic gRPC call in details, from obtaining .proto files to completion.

## 2. Understanding TRON's gRPC Interfaces and Protocol Buffers

All on-chain operations and data queries in TRON are exposed through gRPC services. The definitions of these services are located in .proto files. **Protocol Buffers** is a language-neutral, platform-neutral, extensible mechanism for serializing structured data, used to define service interfaces and message structures.

Through .proto files, you can:

* **Define Services:** Contain methods (RPCs) that can be called by clients.
* **Define Messages:** Describe the data structures for requests and responses.

The gRPC toolchain automatically generates client and server code based on these .proto files. The code includes all the underlying logic required for communicating with TRON nodes.

***

## 3. Complete gRPC Call Process

### 3.1 Obtaining TRON's .proto Files

TRON officially maintains a GitHub repository for all .proto files. These files are the foundation for generating gRPC client code.

1. **Access the TRON Protocol Repository:**\
   Open TRON's official `protocol` GitHub repository: [https://github.com/tronprotocol/protocol](https://github.com/tronprotocol/protocol)

2. **Download .proto Files:**\
   You can find core .proto files in the `core/src/main/proto` directory, for example:

   * `api/api.proto`: Define the main gRPC services and methods (e.g., `Wallet` service).
   * `core/Tron.proto`: Defines core TRON data structures (e.g., `Block`, `Transaction`, `Account`, etc.).
   * `core/contract/account_contract.proto`, `core/contract/asset_issue_contract.proto`, etc.: Define message structures for various system contract operations.

***

### 3.2 Generating gRPC Client Code

After obtaining the .proto files, you need to generate Java client code.

To avoid affecting other local settings and projects, and to simplify the generation process, we strongly recommend using Maven or Gradle's Protobuf plugin in your Java project.

**Maven (`pom.xml`) Configuration Description:**

Configure the necessary dependencies and build plugins in your project's `pom.xml` file.

This typically includes **`grpc-netty-shaded`** for network communication, **`grpc-protobuf`** for Protobuf message processing, and **`grpc-stub`** for gRPC client stubs.

At the same time, you also need to add the **Protobuf Java runtime libraries**, including `protobuf-java` and `protobuf-java-util`. These dependencies are essential to ensure that your project can correctly handle Protobuf messages and perform gRPC communication. In addition, you need to configure the **`protobuf-maven-plugin`**, which will be used to automatically detect the operating system, specify the Maven coordinates of the Protobuf compiler and the gRPC Java plugin, and set the source directory for .proto files so that Java code can be automatically generated during the build process.

**Code Generation Steps:**\
Place the .proto files downloaded from TRON's GitHub in the configured source directory of your project (e.g., `src/main/proto` for Maven projects). Then, execute the corresponding build command in the project's root directory (`mvn clean install` for Maven, `gradle build` for Gradle), after which the build tool's Protobuf plugin will automatically generate the required Java gRPC client code.

**Gradle (`pom.xml`) Configuration Description:**

The dependencies required for Gradle are basically the same as Maven. Here is an example of the configuration file (build.gradle). Please modify the version numbers based on your actual data:

```groovy
dependencies {
    implementation 'io.github.tronprotocol:trident:0.9.2'
    
    implementation 'io.grpc:grpc-netty-shaded:1.64.0'
    implementation 'io.grpc:grpc-protobuf:1.64.0'
    implementation 'io.grpc:grpc-stub:1.64.0'
    implementation 'com.google.protobuf:protobuf-java:3.25.1' 
}
```

After finishing the configurations, use `gradle clean build`.

***

### 3.3 Building the gRPC Client and Making Calls

Once the code is generated, you can use these generated classes in your Java project to build a gRPC client and communicate with a TRON node.

#### 3.3.1 Core Concepts

* **`ManagedChannel`:** Represents a connection to a gRPC server, managing the underlying network connection.
* **`Stub`:** The client interface generated from the .proto file. The interface provides a convenient way to call methods defined in the gRPC service. Common types include `BlockingStub` (blocking) and `FutureStub` (asynchronous).
* **TRON Node Endpoint:** TRON's gRPC service typically runs on port `50051`. Accessing TronGrid public nodes may require an API Key.

#### 3.3.2 Calling Process

The basic process for calling a gRPC method is as follows:

1. **Create`ManagedChannel`:** You need to configure the target TRON node's address and the port to establish a connection with the gRPC server.
2. **Create`Stub`:** Use the `WalletGrpc` class generated from the .proto file to create the corresponding stub instance, for example, `WalletGrpc.newBlockingStub(channel)` for blocking calls.
3. **Attach API Key (if required):** If you are using TronGrid or similar public node services that require an API Key, you typically need to add your API Key as metadata to the request header.
4. **Call Method:** Use the stub instance you created to call the method defined in the TRON gRPC service, passing in the appropriate request message.
5. **Process Response:** Receive and parse the response message returned from the TRON node.
6. **Shut down`ManagedChannel`:** When your application ends or the connection is no longer needed, be sure to shut down  `ManagedChannel` to release network resources.

**Trident** has highly encapsulated all the complex steps of the above gRPC interactions, especially those involving **transaction construction, signing, and broadcasting**, freeing developers from handling these underlying details. Below is the relevant source code implementation in Trident. Please note that only part of the code in the `ApiWrapper` class is demonstrated here. For the complete code, please refer to: [ApiWrapper.java](https://github.com/tronprotocol/trident/blob/main/core/src/main/java/org/tron/trident/core/ApiWrapper.java)

```java
package org.tron.trident.core;

// Import core classes related to the gRPC framework and Google Protobuf
import com.google.protobuf.ByteString; // Handles byte sequences. In the TRON protocol, data like addresses and hashes are often represented as ByteString.
import com.google.protobuf.Message; // The base class for all Protobuf messages, used for generic handling of different types of Protobuf messages.
import io.grpc.ClientInterceptor; // Allows interception and modification of gRPC client requests before sending or after receiving responses, often used for adding authentication information (e.g., API Key).
import io.grpc.ManagedChannel; // The connection channel between the client and the gRPC server, responsible for managing the connection's lifecycle.
import io.grpc.ManagedChannelBuilder; // Facilitates building and configuring ManagedChannel instances, e.g., setting the target address or specifying whether to use encryption.
import io.grpc.Metadata; // Stores and transmits metadata (HTTP/2 header information) for gRPC requests and responses, such as the API Key or authentication tokens.
import io.grpc.stub.MetadataUtils; // Provides helper methods to manipulate and attach metadata to gRPC stubs.

// Import related classes from TridentSDK and TRON Protobuf definitions
import org.tron.trident.api.WalletGrpc; // The base class for gRPC client stubs generated from TRON Protobuf service definitions, used to call RPC services on TRON full nodes (e.g., creating and broadcasting transactions).
import org.tron.trident.api.WalletSolidityGrpc; // Base class for gRPC client stubs generated from TRON Protobuf service definitions, used to call TRON Solidity RPC services (e.g., querying blocks and transaction history).
import org.tron.trident.core.key.KeyPair; // Class in Trident for managing TRON account private keys, responsible for handling signing operations.
import org.tron.trident.proto.Chain.Transaction; // The Protobuf definition for "transactions" on the TRON blockchain, containing various transaction information.
import org.tron.trident.proto.Contract.TransferContract; // The Protobuf definition for the system contract used for TRX transfers in the TRON protocol.
import org.tron.trident.proto.Response.TransactionExtention; // Transaction extension information, including the unsigned transaction object and auxiliary information like the transaction ID.

/**
 * The ApiWrapper class encapsulates the core functionality for interacting with the TRON network via gRPC.
 * It is responsible for managing gRPC connections, calling node services, and the process of transaction creation, signing, and broadcasting.
 */
public class ApiWrapper implements Api {

    // Define gRPC client stubs and ManagedChannel, which are interfaces for communicating with TRON nodes
    public final WalletGrpc.WalletBlockingStub blockingStub; // `blockingStub` is used for synchronous (blocking) gRPC calls to a TRON full node, such as creating and broadcasting transactions.
    public final WalletSolidityGrpc.WalletSolidityBlockingStub blockingStubSolidity; // `blockingStubSolidity` is used for TRON Solidity RPC calls, primarily for querying blockchain data.
    public final KeyPair keyPair; // The `keyPair` object stores the account private and public key information used to sign TRON transactions.
    public final ManagedChannel channel; // `channel` is the gRPC channel connected to the TRON full node, responsible for underlying network communication management.
    public final ManagedChannel channelSolidity; // `channelSolidity` is the channel connected to TRON Solidity RPC.


    /**
     * Constructor for the ApiWrapper class.
     * It is responsible for initializing the gRPC connection to the TRON full node, creating the corresponding client stubs, and setting the API Key for authentication.
     * Additionally, it initializes the `KeyPair` object with the provided private key string for transaction signing.
     *
     * @param grpcEndpoint full node's gRPC address, e.g., "grpc.trongrid.io:50051".
     * @param grpcEndpointSolidity Solidity RPC address, e.g., "grpc.trongrid.io:50052".
     * @param hexPrivateKey The account’s private key used to sign TRON transactions, must be in hexadecimal string format.
     * @param apiKey The API Key required to access TRON nodes (especially public services like TronGrid). If the node does not require one, the API Key can be left null or an empty string.
     */
    public ApiWrapper(
        String grpcEndpoint, // full node's gRPC service address
        String grpcEndpointSolidity, // Solidity RPC service address
        String hexPrivateKey, // User's private key, used for signing
        String apiKey // API Key, used for authentication
    ) {
        // Create ManagedChannel and use ManagedChannelBuilder.forTarget() to build the gRPC connection channel to the full node.
        channel = ManagedChannelBuilder.forTarget(grpcEndpoint).usePlaintext().build();

        // Similarly, build the Solidity RPC connection channel.
        channelSolidity = ManagedChannelBuilder.forTarget(grpcEndpointSolidity)
            .usePlaintext()
            .build();

        // Attach API Key and create a Metadata object to store header information (e.g., API Key) to be sent with gRPC requests.
        Metadata header = new Metadata();
        // Define a Metadata.Key to identify the API Key header.
        Metadata.Key<String> key = Metadata.Key.of(
            "TRON-PRO-API-KEY",
            Metadata.ASCII_STRING_MARSHALLER
        );
        // Put the actual API Key string into the Metadata object.
        header.put(key, apiKey);

        // Create BlockingStub and attach an interceptor. Use WalletGrpc.newBlockingStub(channel) to build a blocking client stub for the Wallet service based on the created channel.
        // .withInterceptors(MetadataUtils.newAttachHeadersInterceptor(header)) attaches an interceptor to the Stub.
        // This interceptor will automatically add the Metadata information from `header` (including the API Key) to each gRPC request before it is sent.
        blockingStub = WalletGrpc.newBlockingStub(channel).withInterceptors(
            MetadataUtils.newAttachHeadersInterceptor(header)
        );

        // Similarly, create a blocking client stub for the WalletSolidityGrpc service and attach the API Key interceptor.
        blockingStubSolidity = WalletSolidityGrpc.newBlockingStub(channelSolidity).withInterceptors(
            MetadataUtils.newAttachHeadersInterceptor(header)
        );

        // Initialize the KeyPair object. It uses the provided hexadecimal private key string to manage the user's account keys, for subsequent transaction signing operations.
        keyPair = new KeyPair(hexPrivateKey);
    }

    /**
     * Execute a TRX transfer operation.
     * This method encapsulates the logic for creating the Protobuf message of a TRX transfer and requesting the TRON node to generate an unsigned transaction.
     *
     * @param fromAddress Sending address, e.g., "TABCD...XYZ"
     * @param toAddress Receiving address, e.g., "TZYXW...VUQ"
     * @param amount Transfer amount, in SUN. 1 TRX = 1,000,000 SUN
     * @return TransactionExtention Refer to TransactionExtention in imports
     * @throws IllegalException
     */
    @Override
    public TransactionExtention transfer(String fromAddress, String toAddress, long amount)
        throws IllegalException {
        // Parse the Base58 encoded TRON address (e.g., "TABC...") into the Protobuf `ByteString` format.
        // `parseAddress` is an internal method defined in ApiWrapper or other helper classes for address conversion.
        ByteString rawFrom = parseAddress(fromAddress);
        ByteString rawTo = parseAddress(toAddress);

        // Build the `TransferContract` Protobuf message body.
        // This is the contract content for a TRX transfer operation, including the sender, receiver, and amount.
        TransferContract transferContract = TransferContract.newBuilder()
            .setOwnerAddress(rawFrom) // Set the sender address of the transfer
            .setToAddress(rawTo) // Set the receiver address of the transfer
            .setAmount(amount) // Set the transfer amount (in SUN)
            .build();

        // Call a helper method `createTransactionExtention`, passing the constructed `TransferContract` message
        // and the contract type `TransferContract` to it. This method will build the transaction locally,
        // and return an unsigned transaction extension object (`TransactionExtention`).
        return createTransactionExtention(
            transferContract,
            Transaction.Contract.ContractType.TransferContract // The type of the system contract, here for TRX transfer.
        );
    }

    /**
     * Locally sign a TRON transaction.
     * This method receives a `TransactionExtention` object containing an unsigned transaction and a `KeyPair` object,
     * uses the private key in the `KeyPair` to cryptographically sign the transaction, and adds the signature to the transaction.
     *
     * @param txnExt The `TransactionExtention` object containing the unsigned transaction, usually returned by methods like `createTransactionExtention`.
     * @param keyPair The `KeyPair` object used for signing, containing the user's private key information.
     * @return Returns a `Transaction` object that already contains a valid signature, which can be directly used for broadcasting.
     */
    @Override
    public Transaction signTransaction(TransactionExtention txnExt, KeyPair keyPair) {
        byte[] txId = txnExt.getTxid().toByteArray();
        // Use the `signTransaction` method of the `KeyPair` class to sign the `txId`.
        byte[] signature = KeyPair.signTransaction(txId, keyPair);
        // Get the original `Transaction` object from `TransactionExtention` and convert it to a modifiable Builder.
        // `addSignature(ByteString.copyFrom(signature))` adds the generated signature to the `signature` field of the transaction.
        return txnExt
            .getTransaction()
            .toBuilder()
            .addSignature(ByteString.copyFrom(signature))
            .build();
    }

    /**
     * Broadcast a signed transaction.
     * This method receives a `Transaction` object that has been locally signed and sends it to the TRON full node for broadcasting via the gRPC client stub.
     *
     * @param txn A `Transaction` object that already contains a valid signature
     * @return Returns the the transaction hash (Transaction ID) in the hexadecimal string format. If the broadcast is successful, this is the unique string identifying the transaction.
     * @throws RuntimeException if broadcasting fails (A runtime exception is thrown if the broadcast operation fails due to network issues, invalid transactions, node response errors, etc.).
     */
    @Override
    public String broadcastTransaction(Transaction txn) throws RuntimeException {
        // Call the `broadcastTransaction` method of `blockingStub`.
        // Send the signed `Transaction` object as a parameter to the node.
        // The node will return a `Response.TransactionReturn` object, which contains the broadcast result (success/failure) and possible error information.
        Response.TransactionReturn ret = blockingStub.broadcastTransaction(txn);
        if (!ret.getResult()) {
            String errorMessage = new String(ret.getMessage().toByteArray());
            // `resolveResultCode` is an internal method defined in ApiWrapper or other helper classes for parsing error codes.
            String message = resolveResultCode(ret.getCodeValue()) + ", " + errorMessage;
            throw new RuntimeException(message);
        } else {
            // Calculate the hash value of the signed `Transaction` object, which will be the final transaction ID.
            // `calculateTransactionHash` is an internal method defined in ApiWrapper or other helper classes for calculating the transaction hash.
            byte[] txId = calculateTransactionHash(txn);
            // Convert the transaction ID that is in the byte array format to a hexadecimal string, which is the standard expression for TRON transaction IDs.
            // `ByteArray.toHexString` is a helper utility method.
            return ByteArray.toHexString(txId);
        }
    }

    /**
     * Closes all established gRPC connection channels.
     * This is an important resource cleanup step, ensuring network resources are released when the application's lifecycle ends.
     */
    public void close() {
        // Call the `shutdown()` method of `ManagedChannel` to close the gRPC channel to the full node, which prevents new RPC requests from being sent.
        channel.shutdown();
        // Similarly, call the `shutdown()` method to close the Solidity RPC channel.
        channelSolidity.shutdown();
    }
}
```

***

## 4. Using Trident-java

Manually calling gRPC interfaces can be quite cumbersome in actual development. Trident is an official Java SDK provided by TRON, which has encapsulated most of the gRPC call work, including client construction, message serialization and deserialization, and complex operations like transaction signing and broadcasting. If you want to interact with TRON more conveniently, you can directly refer to or use Trident for gRPC calls.

## 5. Related References and Documentation

* **TRON Protocol Buffers Definitions:**
  * [https://github.com/tronprotocol/protocol](https://github.com/tronprotocol/protocol)
* **gRPC Java Official Documentation:**
  * [https://grpc.io/docs/languages/java/](https://grpc.io/docs/languages/java/)
* **Protocol Buffers Official Documentation:**
  * [https://developers.google.com/protocol-buffers](https://developers.google.com/protocol-buffers)
* **TronGrid Official Website (Get API Key):**
  * [https://www.trongrid.io/](https://www.trongrid.io/)
* **Trident GitHub Repository:**
  * [https://github.com/tronprotocol/trident/](https://github.com/tronprotocol/trident/)
* **Trident Documentation:**
  * [https://tronprotocol.github.io/trident/](https://tronprotocol.github.io/trident/)
