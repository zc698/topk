# TCP 的 keepalive 了解吗？说一说它和 HTTP 的 keepalive 的区别？ #

1、TCP连接往往就是我们广义理解上的长连接，因为它具备双端连续收发报文的能力；开启了keep-alive的HTTP连接，也是一种长连接，但是它由于协议本身的限制，服务端无法主动发起应用报文。

2、TCP中的keepalive是用来保鲜、保活的；HTTP中的keep-alive机制主要为了让支撑它的TCP连接活的的更久，所以通常又叫做：HTTP persistent connection（持久连接） 和 HTTP connection reuse（连接重用）。


参考文档：  
[https://blog.csdn.net/lpf463061655/article/details/108460311](https://blog.csdn.net/lpf463061655/article/details/108460311)
