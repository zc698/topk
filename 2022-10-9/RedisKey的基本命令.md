#RedisKey的基本命令  
Redis介绍：  
Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.  

Redis是一个开源（BSD许可），内存存储的数据结构服务器，可用作数据库，高速缓存和消息队列代理。它支持字符串、哈希表、列表、集合、有序集合，位图，hyperloglogs等数据类型。内置复制、Lua脚本、LRU收回、事务以及不同级别磁盘持久化功能，同时通过Redis Sentinel提供高可用，通过Redis Cluster提供自动分区。  

基本命令：  
1.查看所有 的key：keys *  
2.set key：set name zxc  
3.判断当前的key是否存在：EXISTS name  
4.移除当前key：move name 1  
5.设置key的过期时间，单位是秒：EXPIRE name 10  
6.查看当前key的剩余时间：ttl name  
7.查看当前key的类型：type name  

相关文档：  
https://www.redis.net.cn/order/