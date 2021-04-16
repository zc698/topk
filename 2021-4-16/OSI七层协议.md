# OSI七层协议分别是什么，每一层功能 #

OSI模型，即开放式通信系统互联参考模型（Open System Interconnection Reference Model），是国际标准化组织提出的一个试图使各种计算机在世界范围内互连为网络的标准框架，简称OSI。  
OSI分层（7层）：物理层、数据链路层、网络层、传输层、会话层、表示层、应用层  
TCP/IP分层（4层）：网络接口层、网际层、传输层、应用层  
五层协议：物理层、数据链路层、网络层、传输层、应用层  

每层的作用及协议：  
物理层：通过媒介传输比特，确定机械及电气规范。RJ45,CLOCK,IEEE802.3（中继器、集线器）  
数据链路层：将比特组装成帧和点到点的传递帧。PPP,FR,VLAN,MAC（网桥、交换机）  
网络层：负责数据包从源到目的端的传递和网际互联（包packet）,路由寻址。IP,ICMP,ARP,RARP,OSPF,IPX,RIP,IGRP（路由器）  
传输层：提供端到端的可靠报文传递和错误恢复（段Segment）。TCP,UDP  
会话层：建立、管理和终止会话（会话协议数据单元SPDU）。NFS,SQL,NETBIOS,RPC  
表示层：对数据进行翻译、加密和压缩（表示协议数据单元PPDU）。JPEG，MPEG  
应用层：允许访问OSI环境的手段（应用协议数据单元APDU）。FTP,DNS,Telnet,SMTP,HTTP,WWW,NFS