# HashMap 与 ConcurrentHashMap 的实现原理是怎样的？ConcurrentHashMap 是如何保证线程安全的？ #

HashMap：数据结构为数组+链表（红黑树），使用良好的哈希函数使得键值尽可能均匀的分布到数组中，使用链表处理哈希冲突问题。

当map中的元素数量达到阈值时，会重新创建一个新的数组，长度为旧数组的两倍(如果长度没有达到上限的话)，这时会依次对旧数组(包括其中的链表)按顺序重新计算索引插入，之后重新赋值引用即可。

多线程环境容易造成get死锁。

ConcurrentHashMap ：本质是使用Segment来代替原来的HashMap，而Segment继承了ReentrantLock 可重入锁，这使得HashMap在Segment内变成了HashTable（同步），然后ConcurrentHashMap持有多个Segment，
这样其实就是选择了HashTable和HashMap的一个中间版。

get方法无需加锁，由于其中涉及到的共享变量都使用volatile修饰，volatile可以保证内存可见性，所以不会读取到过期数据。

concurrentHashMap代理到Segment上的put方法，Segment中的put方法是要加锁的。只不过是锁粒度细了而已。

参考文档：  
[https://www.wolai.com/river1235r/t2hzEppyJrBFt9fmg24UfG](https://www.wolai.com/river1235r/t2hzEppyJrBFt9fmg24UfG)