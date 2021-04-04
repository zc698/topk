TCP 与 UDP 在网络协议中的哪一层，他们之间有什么区别？

TCP与UDP都位于网络模型中的传输层，负责传输应用层产生的数据

1.UDP
UDP（User Datagram Protocol 用户数据报协议）：UDP不需要所谓的握手操作，从而加快了通信速度，允许网络上的其他主机在接收方同意通信之前进行数据传输

数据报是与分组交换网络关联的传输单元

UDP特点：

UDP低延迟
UDP能够发送大量数据包
UDP能够允许DNS查找（DNS是应用层协议）

2.
TCP（Transfer Control Protocol 传输控制协议）：通过三次握手建立TCP连接，一旦建立就可以发生数据，传输完成之后，会通过关闭虚拟电路来断开连接

TCP特点：

TCP可以确保连接的建立和数据包发送可靠性
TCP支持差错重传
TCP支持拥塞控制，能够在网络发生堵塞的情况下延迟发送
TCP能够提供差错检验，甄别有害数据包

3.TCP和UDP对比
TCP	                               UDP
面向连接的	                       无连接的
先建立连接，在发送数据	               无需连接，直接发送大量数据
顺序排列数据包	                   数据包相互独立
传输速度较慢	                       传输速度较快
头部字节20	                       头部字节8
错误校验并恢复	                   差错校验但丢弃错误数据包
有发送确认	                       无发送确认
握手：SYN、SYN-ACK、ACK	           无握手
可靠的	                           不能保证数据传送到


TCP是重量级的：在发送任何数据前，TCP都需要三次握手建立连接
UDP是轻量级的：没有跟踪连接、消息排列等


[tcpudp1](https://github.com/zc698/topk/blob/master/2021-3-30/tcpudp.png)  
[tcpudp2](https://github.com/zc698/topk/blob/master/2021-3-30/tcpudp2.png)

版权声明：本文为CSDN博主「我是小杨我就这样」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44478378/article/details/107699196