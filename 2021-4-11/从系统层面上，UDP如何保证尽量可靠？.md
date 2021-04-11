# 从系统层面上，UDP如何保证尽量可靠？ #

1.UDP概念
   用户数据报协议（英语：User Datagram Protocol，缩写为 UDP），又称使用者资料包协定，是一个简单的面向数据报的传输层协议，正式规范为RFC 768

   在TCP/IP模型中，UDP为网络层以上和应用层以下提供了一个简单的接口。UDP只提供数据的不可靠传递，它一旦把应用程序发给网络层的数据发送出去，就不保留数据备份（所以UDP有时候也被认为是不可靠的数据报协议）。UDP在IP数据报的头部仅仅加入了复用和数据校验（字段）。

2.UDP丢包问题分析


由于UDP协议只提供数据的不可靠传输，数据包发出去后就不管了，数据包在网络的传输过程中都可能丢失。甚至即使数据包成功到达了接收端节点，也不意味着应用程序能够收到，因为要从网卡到达应用程序还需要经历很多阶段，每个阶段都可能丢包。

上图描述了一种应用程序接受网络数据包的典型路径图。

首先，NIC(网卡)接收和处理网络数据包。网卡有自己的硬件数据缓冲区，当网络数据流量太大，大到超过网卡的接收数据硬件缓冲区，这时新进入的数据包将覆盖之前缓冲区的数据包，导致丢失。网卡是否丢包取决于网卡本身的计算性能和硬件缓冲区的大小。

其次，网卡处理后把数据包交给操作系统缓冲区。数据包在操作系统阶段丢包主要取决于以下因素：

操作系统缓冲区的大小
系统的性能
系统的负载
网络相关的系统负载
最后，当数据包到达应用程序的socket缓冲区，如果应用程序不能及时从socket缓冲区把数据包取走，累积的数据包将会超出应用程序socket缓冲区阀值，导致缓冲区溢出，数据包丢失。数据包在应用程序阶段丢包主要取决于以下因素：

应用程序缓冲区大小
应用程序处理数据包的能力，即如何尽可能快的从缓冲区取走数据包
3. 针对UDP丢包问题，进行系统层面和程序层面调优  
3.1 诊断
n  网卡缓冲区溢出诊断

在Linux操作系统中，可以通过netstat -i –udp <NIC> 命令来诊断网卡缓冲区是否溢出，RX-DRP列显示网卡丢失的数据包个数。

For example: netstat -i –udp eth1

[root@TENCENT64 /usr/local/games/udpserver]# netstat -i –udp eth1
Kernel Interface table
Iface       MTU   Met    RX-OK     RX-ERR  RX-DRP RX-OVR    TX-OK     TX-ERR TX-DRP TX-OVR   Flg
eth1       1500   0   1295218256      0      3      0      7598497      0      0      0      BMRU
上图的输出显示3个数据包被网卡丢掉

可以通过增大网卡缓冲区来有效减少网卡缓冲区溢出。

n  操作系统内核网络缓冲区溢出诊断

在Linux操作系统中可以通过cat /proc/net/snmp | grep -w Udp命令来查看，InErrors 列显示当操作系统UDP队列溢出时丢失的UDP数据包总个数。

[root@TENCENT64 /usr/local/games/udpserver]# cat /proc/net/snmp | grep -w Udp
Udp: InDatagrams NoPorts   InErrors OutDatagrams RcvbufErrors SndbufErrors
Udp: 859428331   12609927 166563611 151449         166563611        0
有如下几种方法可以有效减缓操作系统缓冲区溢出：

1)     增大操作系统内核网络缓冲区的大小

2)     在数据包路径图中直接绕过操作系统内核缓冲区，通过使用用户空间栈或一些可以            绕过内核缓冲区的中间件 (e.g. Solarflare's OpenOnload).

3)     关闭未使用的网络相关的应用和服务使操作系统的负载降到最低

4)     系统中仅保留适当数量的工作的网卡，最大效率的合理化利用网卡和系统资源

 

n  应用程序socket缓冲区溢出诊断

在Linux操作系统中可以通过cat /proc/net/snmp | grep -w Udp命令来查看，RcvbufErrors 列显示当应用程序socket缓冲区溢出时丢失的UDP数据包总个数。

[root@TENCENT64 /usr/local/games/udpserver]# cat /proc/net/snmp | grep -w Udp
Udp: InDatagrams NoPorts InErrors OutDatagrams RcvbufErrors SndbufErrors
Udp: 859428331  12609927 166563611 151449        166563611       0
有如下几种方法可以有效减缓应用程序socket缓冲区溢出：

1)    接受缓冲区尽可能快地处理接受到的数据包（e.g.通过使用NIO的方式来异步非阻塞接受UDP数据包或者提高接受UDP数据包线程的优先级）

2)    增大应用程序接受socket缓冲区大小，注意这个受限于全局socket缓冲区大小，如果应用程序的socket缓冲区大于全局socket缓冲区将没有效果。

3)    把应用程序或接受线程指定到CPU专用的核上

4)    提高应用程序的io优先级(e.g.使用nice或ionice命令来调节)

5)    关闭所有未使用的网络相关的应用和服务使操作系统的负载降到最低

3.2 调优
n  网卡缓冲区调优

Linux下运行ethtool -g <NIC> 命令查询网卡的缓冲设置，如下：

[root@TENCENT64 /usr/local/games/udpserver]# ethtool -g eth1
Ring parameters for eth1:
Pre-set maximums:
RX:             4096
RX Mini:        0
RX Jumbo:       0
TX:             4096
Current hardware settings:
RX:             256
RX Mini:        0
RX Jumbo:       0
TX:             256
       通过命令ethtool -G d<NIC> rx NEW-BUFFER-SIZE可以设置RX ring的缓冲区大小，改变会立即生效不需要重启操作系统或刷新网络栈，这种变化直接作用于网卡本身而不影响操作系统，不影响操作系统内核网络栈但是会影响网卡固件参数。更大的ring size能承受较大的数据流量而不会丢包，但是因为工作集的增加可能会降低网卡效率，影响性能，所以建议谨慎设置网卡固件参数。

n  操作系统内核缓冲区调优

运行命令sysctl -A | grep net | grep 'mem\|backlog' | grep 'udp_mem\|rmem_max\|max_backlog'查看当前操作系统缓冲区的设置。如下：

[root@TENCENT64 /usr/local/games]# sysctl -A | grep net | grep 'mem\|backlog' | grep 'udp_mem\|rmem_max\|max_backlog'net.core.netdev_max_backlog = 1000net.core.rmem_max = 212992net.ipv4.udp_mem = 188169       250892  376338
增加最大socket接收缓冲区大小为32MB：

sysctl -w net.core.rmem_max=33554432

增加最大可分配的缓冲区空间总量,数值以页面为单位，每个页面单位等于4096 bytes：

sysctl -w net.ipv4.udp_mem="262144 327680 393216"

增加接收数据包队列大小：

sysctl -w net.core.netdev_max_backlog=2000

修改完成后，需要运行命令 sysctl –p 使之生效

n  应用程序调优

      要减少数据包丢失，应用程序必须尽可能快从缓冲区取走数据，可以通过适当增大socket缓冲区和采用异步非阻塞的IO来快速从缓冲区取数据，测试采用JAVA NIO构建一个Asynchronous UDP server。

            //建立            DatagramChannel dc = DatagramChannel.open();            dc.configureBlocking(false);            //本地绑定端口            SocketAddress address = new InetSocketAddress(port);            DatagramSocket ds = dc.socket();            ds.setReceiveBufferSize(1024 * 1024 * 32);//设置接收缓冲区大小为32M            ds.bind(address);            //注册            Selector select = Selector.open();            dc.register(select, SelectionKey.OP_READ);            ByteBuffer buffer = ByteBuffer.allocateDirect(1024);            System.out.println("Listening on port " + port);            while (true) {                int num = select.select();                if (num == 0) {                    continue;                }                //得到选择键列表                Set Keys = select.selectedKeys();                Iterator it = Keys.iterator();                while (it.hasNext()) {                    SelectionKey k = (SelectionKey) it.next();                    if ((k.readyOps() & SelectionKey.OP_READ)                        == SelectionKey.OP_READ) {                        DatagramChannel cc = (DatagramChannel) k.channel();                        //非阻塞                        cc.configureBlocking(false);
4. 其他减少丢包策略
      UDP发送端增加流量控制，控制每秒发送的数据包，尽量避免由于发送端发包速率过快，导致UDP接收端缓冲区很快被填满从而出现溢出丢包。测试采用google提供的工具包guava。RateLimiter类来做流控，采用了一种令牌桶的流控算法，RateLimiter会按照一定的频率往桶里扔令牌，线程拿到令牌才能执行，比如你希望自己的应用程序QPS不要超过1000，那么RateLimiter设置1000的速率后，就会每秒往桶里扔1000个令牌。

       采用流控后每秒发指定数量的数据包，而且每秒都会出现波谷波峰，如果不做流控，UDP发送端会全力发包一直在波峰附近抖动，大流量会一直持续，随着时间的增加，UDP发送端生产的速率肯定会超过UDP接收端消费的速率，丢包是迟早的。

5. 真实测试数据
n  机器类型

发送端和接收端均采用C1类型机器，配置如下：

C1
Intel(R) Xeon(R) CPU X3440 @ 2.53GHz:8
8G
500G:7200RPM:1:SATA
NORAID
接收端网卡信息如下：

[root@TENCENT64 /usr/local/games]# ethtool eth1                     Settings for eth1:        Supported ports: [ TP ]        Supported link modes:   10baseT/Half 10baseT/Full                                 100baseT/Half 100baseT/Full                                 1000baseT/Full         Supports auto-negotiation: Yes        Advertised link modes:  10baseT/Half 10baseT/Full                                 100baseT/Half 100baseT/Full                                 1000baseT/Full         Advertised pause frame use: Symmetric        Advertised auto-negotiation: Yes        Speed: 1000Mb/s        Duplex: Full        Port: Twisted Pair        PHYAD: 1        Transceiver: internal        Auto-negotiation: on        MDI-X: on        Supports Wake-on: pumbg        Wake-on: g        Current message level: 0x00000007 (7)        Link detected: yes[root@TENCENT64 /usr/local/games]# ethtool -g eth1Ring parameters for eth1:Pre-set maximums:RX:             4096RX Mini:        0RX Jumbo:       0TX:             4096Current hardware settings:RX:             256RX Mini:        0RX Jumbo:       0TX:             256
n  实际调优

接收端服务器调优后的参数如下：

[root@TENCENT64 /usr/local/games]# sysctl -A | grep net | grep 'mem\|backlog' | grep 'udp_mem\|rmem_max\|max_backlog'net.core.rmem_max = 67108864net.core.netdev_max_backlog = 20000net.ipv4.udp_mem = 754848       1006464 1509696
 发送端是否做发送流量控制在测试场景中体现

n  测试场景

场景1：发送100w+数据包，每个数据包大小512byte，数据包都包含当前的时间戳，不限流，全速发送。发送5次，测试结果如下：

测试客户端:

发100w个512字节的udp包，发100w数据包耗时4.625s，21wQPS



测试服务器端：

客户端发5次包，每次发包100w(每个包512字节)，第一次服务端接受90w丢约10w，第二次服务端接受100w不丢，第三次接受100w不丢，第四次接受97w丢3w,第五次接受100w不丢

服务端记录日志：



 服务端操作系统接收UDP记录情况：(和日志记录结果完全一致)



 场景2：发送端增加流量控制，每秒4w数据包，每个数据包512byte,包含当前时间戳，发送时间持续2小时，测试结果如下：

1.Udpclient端,加入流量控制:

QPS:4W

datapacket:512byte,包含发送的时间戳

持续发送时长:2h

累计发包数: 287920000(2.8792亿)

CPU平均消耗: 16% (8cpu)

内存平均消耗: 0.3%(8G)

2.Udpserver端:

Server端接受前网卡记录的UDP 详情:

[root@TENCENT64 ~]# cat /proc/net/snmp | grep -w UdpUdp: InDatagrams NoPorts InErrors OutDatagrams RcvbufErrors SndbufErrorsUdp: 1156064488 753197150 918758960 1718431901 918758960 0
Server端接受完所有的udp数据包后网卡记录的UDP详情:

[root@TENCENT64 ~]# cat /proc/net/snmp | grep -w UdpUdp: InDatagrams NoPorts InErrors OutDatagrams RcvbufErrors SndbufErrorsUdp: 1443984568 753197150 918758960 1718432045 918758960 0
前后变化分析:

InDatagrams: (1443984568-1156064488)= 287920080

InErrors:0 (记录操作系统层面udp丢包,丢包可能是因为系统udp队列满了)

RcvbufErrors:0(记录应用程序层面udp丢包),丢包可能是因为应用程序socket buffer满了)

Server端日志情况:

总记录日志文件:276个,总大小:138G

日志总数: 287920000 (和udpclient发送数据包总量一致,没有丢包)

根据日志时间戳,简单计算处理能力:

time cost:(1445410477654-1445403277874)/1000=7199.78s

process speed: 287920000/7199.78 = 3.999w/s

 

CPU消耗: 平均46% (8cpu),要不停异步写日志,IO操作频繁,消耗比较多cpu资源

内存消耗: 平均4.7%(8G)

 

  场景3：发送端增加流量控制，每秒6w数据包，每个数据包512byte,包含当前时间戳，发送时间持续2小时，出现丢包，测试结果如下：

1.Udpclient端,加入流量控制:

QPS:6W

datapacket:512byte,包含发送的时间戳

持续发送时长:2h

累计发包数: 432000000 (4.32亿)

CPU平均消耗: 70% (8cpu)

内存平均消耗: 0.3%(8G)

2.Udpserver端:

Server端接受前网卡记录的UDP 详情:

[root@TENCENT64 ~]# cat /proc/net/snmp | grep -w UdpUdp: InDatagrams NoPorts InErrors OutDatagrams RcvbufErrors SndbufErrorsUdp: 2235178200 753197150 918960131 1720242603 918960131 0
Server端接受完所有的udp数据包后网卡记录的UDP详情:

[root@TENCENT64 ~]# cat /proc/net/snmp | grep -w UdpUdp: InDatagrams NoPorts InErrors OutDatagrams RcvbufErrors SndbufErrorsUdp: 2667158153 753197150 918980378 1720242963 918980378 0
前后变化分析:

InDatagrams: (2667158153 -2235178200)= 431979953

InErrors: (918980378 -918960131)= 20247 (记录操作系统层面udp丢包,丢包可能是因为系统udp队列满了)

RcvbufErrors: (918980378 -918960131)= 20247 (记录应用程序层面udp丢包),丢包可能是因为应用程序socket buffer满了)

Server端日志情况:

总记录日志文件:413个,总大小:207G

日志总数: 431979753 (和网卡收到udp包总数一致,写日志文件没有丢包)

丢包情况：

Client端发送：432000000，

服务端网卡接受udp包总数：431979953，

日志记录：431979953，

udp网卡接受丢包：20247，

丢包率：1/20000

由于测试服务器硬盘资源有限，只测试了2个小时，随着发送和接受时间增长，丢包率可能会增大。

 对比图：不加流控和加流控(限流4w)发送100w个512byte数据包，每毫秒发送数据包雷达波型对比图，雷达波型图中，外围波型值为发送数据包的毫秒值，雷达轴距为每毫秒发送的数据包数取值范围。按顺序，图1为限流4w生成的图，图2为不限流生成的图。从图中可以看出限流时每秒都会出现波谷波峰，不会一直持续高流量发送，能适当缓解UDP接收端的压力；不限流时数据在波峰附近波动，持续高流量发送，对UDP接收端有很多压力，接收端如没及时从缓冲区取走数据或消费能力低于发送端的生成能力，则很容易丢包。



----------------------------------------------------------------------------------------------

 总结：UDP发包在不做流控的前提下，发送端很快到达一个相对稳定的波峰值并一直持续发送，接收端网卡或操作系统缓冲区始终有限，随着发包时间不断增加，到某个时间点必定填满接收端网卡和系统的缓冲区，而且发送端的生产速率将远远超过接收端消费速率，必然导致丢包。发送端做了流量控制后，发送速率得到有效控制，不会一直持续高流量发送，每秒都会出现波谷波峰，有效缓解了接收端的压力，在合理发包速率的前提下，通过相关系统调优，基本可以保证不丢包，但要确保数据的高完整性，由于UDP协议的天生不可靠性，还是要在UDP协议基础上做相关扩展，增加数据完整性校验，方能确保业务数据的完整。



参考文档：  
[https://www.cnblogs.com/x_wukong/p/9304595.html](https://www.cnblogs.com/x_wukong/p/9304595.html)  
[https://blog.csdn.net/pangyemeng/article/details/50387078](https://blog.csdn.net/pangyemeng/article/details/50387078)