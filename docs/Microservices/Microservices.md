---
title: Microservices
category: microservices
tags: microservices
---

# Microservices

## MicroServices

[microservices.io](https://microservices.io/patterns/index.html)

[Introduction to microservices](https://www.nginx.com/blog/introduction-to-microservices/)

### Scala

[Lagom](https://www.lagomframework.com/)

### .NET

[Microservices in C#](https://docs.microsoft.com/en-us/dotnet/articles/csharp/tutorials/microservices)

## API Protocols

### REST (Representational State Transfer)

- Uses standard HTTP methods (GET, POST, PUT, DELETE).
- Best for public-facing APIs and generic CRUD operations.

### gRPC

- Uses HTTP/2 and Protocol Buffers (Protobuf).
- Excellent for high-performance internal microservice communication.

```protobuf
// Example Protobuf definition
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}
message HelloRequest { string name = 1; }
message HelloReply { string message = 1; }
```

### GraphQL

- Enables clients to request exactly the data they need.
- Great for complex front-ends.

```graphql
query {
  user(id: "1") {
    name
    email
    friends {
      name
    }
  }
}
```
