#Redis安装
Window 下安装：  
1.下载地址：https://github.com/dmajkic/redis/downloads。  
2.运行 redis-server.exe  
3.运行 redis-cli.exe  
设置键值对 set myKey abc  
取出键值对 get myKey  
ping

Linux下安装：  
1.下载地址：https://redis.io/download/  

2.将下载文件放到/opt,解压下载文件tar xzf redis-2.8.17.tar.gz  

3.安装C++ yum install gcc c++  

4.执行make命令  

5.执行make install  

6.默认安装路径Redis：/usr/local/bin  

7.复制Redis配置文件到bin目录下，以后使用bin目录下配置文件启动Redis。  
[root@localhost bin]# mkdir kconfig 

[root@localhost bin]# cp /opt/redis-7.0.5/redis.conf kconfig

[root@localhost bin]# cd kconfig/

[root@localhost kconfig]# ls  
redis.conf  

8.Redis默认不是后台启动的，需要修改配置文件。  
daemonize修改为 yes  

9.
启动Redis：[root@localhost bin]# redis-server kconfig/redis.conf  

10.使用redis-cli客户端进行连接测试：  
[root@localhost bin]# redis-cli -p 6379  
127.0.0.1:6379> ping  
PONG  
127.0.0.1:6379> set name zc  
OK  
127.0.0.1:6379> get name  
"zc"  
查看所有的key：  
127.0.0.1:6379> keys *
1) "name"

11.查看Redis进程是否开启：  
[root@localhost bin]# ps -ef|grep redis  
root      19510      1  0 21:52 ?        00:00:02 redis-server 127.0.0.1:6379  

12.如何关闭redis：
（1）shutdown；（2）exit。  

13.Redis性能测试  
$ redis-benchmark -n 10000  -q  
redis 性能测试工具可选参数如下所示：

序号	选项	描述	默认值  
1	-h	指定服务器主机名	127.0.0.1  
2	-p	指定服务器端口	6379  
3	-s	指定服务器 socket	  
4	-c	指定并发连接数	50  
5	-n	指定请求数	10000  
6	-d	以字节的形式指定 SET/GET 值的数据大小	2  
7	-k	1=keep alive 0=reconnect	1  
8	-r	SET/GET/INCR 使用随机 key, SADD 使用随机值	  
9	-P	通过管道传输 <numreq> 请求	1  
10	-q	强制退出 redis。仅显示 query/sec 值	  
11	--csv	以 CSV 格式输出	  
12	-l（L 的小写字母）	生成循环，永久执行测试	  
13	-t	仅运行以逗号分隔的测试命令列表。	  
14	-I（i 的大写字母）	Idle 模式。仅打开 N 个 idle 连接并等待。  
$ redis-benchmark -h 127.0.0.1 -p 6379 -t set,lpush -n 10000 -q

SET: 146198.83 requests per second
LPUSH: 145560.41 requests per second  
以上实例中主机为 127.0.0.1，端口号为 6379，执行的命令为 set,lpush，请求数为 10000，通过 -q 参数让结果只显示每秒执行的请求数。