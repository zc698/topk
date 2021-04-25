volatile 关键字解决了什么问题，它的实现原理是什么？  

 作用  
如果一个变量是volatile类型，则对该变量的读写就将具有原子性。如果是多个volatile操作或类似于volatile++这种复合操作，这些操作整体上不具有原子性。volatile变量自身具有下列特性：

  [可见性]：对一个volatile变量的读，总是能看到（任意线程）对这个volatile变量最后的写入。  
[原子性]：对任意单个volatile变量的读/写具有原子性，但类似于volatile++这种复合操作不具有原子性。

volatile的实现原理：

JMM会针对编译器制定的volatile重排序规则表

下面是基于保守策略的JMM内存屏障插入策略：
在每个volatile写操作的前面插入一个StoreStore屏障。
在每个volatile写操作的后面插入一个StoreLoad屏障。
在每个volatile读操作的后面插入一个LoadLoad屏障。
在每个volatile读操作的后面插入一个LoadStore屏障。
具体底层的实现是基于操作系统的Lock指令来实现的，当写两条线程Thread-A与Threab-B同时操作主存中的一个volatile变量i时，Thread-A写了变量i，那么：

1. Thread-A发出LOCK#指令
2. 发出的LOCK#指令锁总线（或锁缓存行），同时让Thread-B高速缓存中的缓存行内容失效
3. Thread-A向主存回写最新修改的i
Thread-B读取变量i，那么：

Thread-B发现对应地址的缓存行被锁了，等待锁的释放，缓存一致性协议会保证它读取到最新的值

由此可以看出，volatile关键字的读和普通变量的读取相比基本没差别，差别主要还是在变量的写操作上。

参考文档：  
[https://github.com/weitingyuk/Java-Basic-Notes/blob/main/2021-03-29/Volatile.md](https://github.com/weitingyuk/Java-Basic-Notes/blob/main/2021-03-29/Volatile.md)