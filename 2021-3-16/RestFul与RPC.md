# RestFul 与 RPC 的区别是什么？RestFul 的优点在哪里？ #

RPC
RPC（Remote Procedure Call）—远程过程调用，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。RPC协议假定某些传输协议的存在，如TCP或UDP，为通信程序之间携带信息数据。在OSI网络通信模型中，RPC跨越了传输层和应用层，RPC使得开发包括网络分布式多程序在内的应用程序更加容易。

简而言之就是 在A (client) 调用 B (server) 提供的A方法.

例如在某庞大商场系统中，你可以把整个商场拆分为N个微服务（理解为N个独立的小模块也行），例如：订单系统 ,用户管理系统

此时在订单系统要调用用户系统的方法，则为远程调用

而调用过程实现的通讯协议可以有很多，可以是http协议或者tcp协议

在一个完整的Rpc中,包含了:

1:服务端,提供Rpc服务接口的服务端,可以有多个

2:客户端,请求Rpc服务端,可以有多个,客户端也可以是服务端,服务端也可以是客户端,互相调用不同的服务

3:如何进行序列化和反序列化.

4:如何进行网络传输（选择何种网络协议）多数RPC框架选择TCP作为传输协议，也有部分选择HTTP。如gRPC使用HTTP2。不同的协议各有利弊

这就有点像我们传统使用的restful接口

RESTFUL
RESTful是一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件。它主要用于客户端和服务器交互类的软件。通过http协议中的POST/GET/PUT/DELETE等方法和一个可读性强的URL来提供一个http请求。而rpc则不一定通过http,更常用的是使用TCP来实现。

RESTFUL 与RPC的区别
1.restfull和rpc都是client/server模式的，都是在 Server端 把一个个函数封装成接口暴露出去

2.restful使用http协议实现，而rpc则不一定使用http，一般比较常用的是tcp， RPC 可以获得更好的性能（省去了 HTTP 报头等一系列东西）,TCP更加高效，而HTTP在实际应用中更加的灵活。

3.从使用上来说：Http接口只关注服务提供方（服务端），对于客户端怎么调用，调用方式怎样并不关心；而RPC服务则需要客户端接口与服务端保持一致，服务端提供一个方法，客户端通过接口直接发起调用。

参考文档：  
[https://www.wolai.com/river1235r/xq2RjErJatTWeBUCzT8rdB](https://www.wolai.com/river1235r/xq2RjErJatTWeBUCzT8rdB)