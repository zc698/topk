# ThreadLocal 实现原理是什么？ #

ThreadLocal能让线程拥有自己内部独享的变量。

原理：

每一个线程都有一个对应的Thread对象，而Thread类有一个成员变量，它是一个Map集合，这个Map集合的key就是ThreadLocal的引用，而value就是当前线程在key所对应的ThreadLocal中存储的值。当某个线程需要获取存储在ThreadLocal变量中的值时，ThreadLocal底层会获取当前线程的Thread对象中的Map集合，然后以ThreadLocal作为key，从Map集合中查找value值。这就是ThreadLocal实现线程独立的原理。也就是说，ThreadLocal能够做到线程独立，是因为值并不存在ThreadLocal中，而是存储在线程对象中。

参考文档：  
[https://www.cnblogs.com/tuyang1129/p/12713815.html#22-threadlocal的实现原理](https://www.cnblogs.com/tuyang1129/p/12713815.html#22-threadlocal的实现原理)  
[https://www.jianshu.com/p/0ba78fe61c40](https://www.jianshu.com/p/0ba78fe61c40)  
[https://www.cnblogs.com/kancy/p/10702310.html](https://www.cnblogs.com/kancy/p/10702310.html)  


