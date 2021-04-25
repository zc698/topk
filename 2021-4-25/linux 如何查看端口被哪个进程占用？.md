# linux 如何查看端口被哪个进程占用？ #

1. lsof  -i:端口号

2.netstat -tunlp |grep 端口号

都可以查看指定端口被哪个进程占用的情况

参考文档：  
[https://blog.csdn.net/y805805/article/details/85857887/](https://blog.csdn.net/y805805/article/details/85857887/)

