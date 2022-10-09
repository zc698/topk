#Redis-String  

设置值：
127.0.0.1:6379> set key1 v1  
OK  
获得值：
127.0.0.1:6379> get key1  
"v1"  
获得所有的key：
127.0.0.1:6379> keys *  
1) "key1"  
判断某一个key是否存在：
127.0.0.1:6379> EXISTS key1  
(integer) 1  
追加字符串，如果当前key不存在，就相对于setkey  
127.0.0.1:6379> APPEND key1 "hello"  
(integer) 7  

127.0.0.1:6379> get key1
"v1hello"  
获取字符串长度：
127.0.0.1:6379> STRLEN key1  
(integer) 7  

127.0.0.1:6379> APPEND key1 ".zxc"  
(integer) 11  
127.0.0.1:6379> STRLEN key1  
(integer) 11  
127.0.0.1:6379> get key1  
"v1hello.zxc"  

incr views：自增1  
decr views：自减1  
INCRBY views 10：指定步长，指定增量加10  
DECRBY views 5：指定步长，指定减少5  

GETRANGE key1 0 3 ：截取字符串0到3范围字符  
GETRANGE key1 0 -1 ：获取全部的字符串和get key一样  
SETRANGE key2 1 xx:替换指定位置开始的字符串  
setex:set with expire 设置过期时间  
setnx:set if not exist 不存在，再设置，存在创建失败。  

mset k1 v1 k2 v2：  同时设置多个值  
mget k1 k2：  同时获取多个值  
msetnx:原子操作，要么一起成功，要么一起失败。  

对象：  
set user:1{name:zhangsan,age:3}:设置一个user：1对象，值为json字符来保存一个对象！  
这里的key：user：{id}：{filed}，如此设计在redis是完全可以的。  

getset：先get再set，如果不存在值，返回nil，如果存在值，获取原来的值，并设置新的值。  

value除了是字符串还可以是数字  ：
计数器、统计 多单位的数量、粉丝数、对象缓存存储  
