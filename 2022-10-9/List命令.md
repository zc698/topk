#List  
将一个值或者多个值，插入到列表头部：  
127.0.0.1:6379> LPUSH list one  
(integer) 1  
127.0.0.1:6379> LPUSH list two  
(integer) 2  
127.0.0.1:6379> LPUSH list three  
(integer) 3  

获取list中值：  
127.0.0.1:6379> LRANGE list 0 -1  
1) "three"
2) "two"
3) "one"  
127.0.0.1:6379> LRANGE list 0 1  
1) "three"
2) "two"  
127.0.0.1:6379> LRANGE list 0 -1  
1) "three"
2) "two"
3) "one"  

将一个值或者多个值插入到列表尾部：  
127.0.0.1:6379> RPUSH list right  
(integer) 4  
127.0.0.1:6379> LRANGE list 0 -1  
1) "three"
2) "two"
3) "one"
4) "right"  
移除list的第一个元素：  
127.0.0.1:6379> LPOP list  
"three"  
移除list的最后一个元素：  
127.0.0.1:6379> Rpop list  
"right"  
127.0.0.1:6379> LRANGE list 0 -1  
1) "two"
2) "one"  
127.0.0.1:6379> Lindex list 1  
"one"
127.0.0.1:6379> LRANGE list 0 -1  
1) "two"
2) "one"  
返回列表长度：  
127.0.0.1:6379> Llen list  
(integer) 2  
移除指定的值：  移除指定个数的value
127.0.0.1:6379> lrem list 1 one  
(integer) 1  
127.0.0.1:6379> LRANGE list 0 -1  
1) "two"  
127.0.0.1:6379> Rpush mylist "hello"  
(integer) 1  
127.0.0.1:6379> Rpush mylist "hello1"  
(integer) 2  
127.0.0.1:6379> Rpush mylist "hello2"  
(integer) 3  
127.0.0.1:6379> Rpush mylist "hello3"  
(integer) 4  
截断：  通过下标截断list，list已经改变，只剩下截取的元素了。
127.0.0.1:6379> ltrim mylist 1 2
OK  
127.0.0.1:6379> LRANGE mylist 0 -1  
1) "hello1"
2) "hello2"  

127.0.0.1:6379> Rpush mylist1 "hello"
(integer) 1  
127.0.0.1:6379> Rpush mylist1 "hello1"
(integer) 2  
127.0.0.1:6379> Rpush mylist1 "hello2"
(integer) 3  
移除列表的最后一个元素，将他移动到新的列表中。
127.0.0.1:6379> rpoplpush mylist1 myotherlist
"hello2"  
查看原来列表：  
127.0.0.1:6379> lrange mylist1 0 -1
1) "hello"
2) "hello1"  
查看目标列表：  
127.0.0.1:6379> lrange myotherlist 0 -1
1) "hello2"  
判断这个列表是否存在：  
127.0.0.1:6379> EXISTS list
(integer) 1  

lset list 0 item:如果列表不存在，我们更新会 报错，如果存在，更新当前下标的值  

将某个具体的value插入到列表中某个元素的前面或者后面。
127.0.0.1:6379> linsert mylist after worl new  

小结：  
它实际上是一个链表，before node after，left，right都可以插入值。  
如果key不存在，创建新的链表  
如果key存在，新增内容  
如果移除了所有值，空链表也代表不存在。  
在两边插入或者改动值，效率最高。中间元素效率会低一点。  
