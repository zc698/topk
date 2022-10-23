#Set  
sadd myset "hello":set集合中添加元素  

SMEMBERS myset:查看指定set的所有值  

SISMEMBER myset hello:判断某一个值在不在set集合中  

scard myset:获取set集合中的内容元素个数  

srem myset hello:移除set集合中的指定元素  


SRANDMEMBER myset：随机抽选出一个元素  

SRANDMEMBER myset 2：随机抽选出指定个数的元素  

spop myset：随机删除一些set集合中的元素  

smove myset myset2 "zc":将一个指定的值移动到另外一个set集合  

SDIFF key1 key2:差集  

SINTER key1 key2:交集，共同好友实现  

SUNION key1 key2:并集  

