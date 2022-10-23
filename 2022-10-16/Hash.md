#Hash
1.hset myhash field1 zxc：set一个具体的key-value  
2.hget myhash field1：获取一个字段值  
3.hmset myhash field1 hello field2 world：set多个key-value  
4.hmget myhash field1 field2：获取多个字段值  
5.hgetall myhash:获取全部数据  
6.hdel myhash field1：删除指定key字段，valu也就删除了  
7.hlen myhash:获取hash表的字段数量  
8.HEXISTS myhash field1:判断hash中指定字段是否存在  
9.hkeys myhash:只获取所有field  
10.hvals myhash:只获取所有value  
11.HINCRBY myhash field3 1:指定增量1  
12.HINCRBY nyhash field3 -1:指定增量-1  
13.hsetnx myhash field4 hello:如果不存在则可以设置  
14.hsetnx myhash field4 world:如果存在则不能设置  