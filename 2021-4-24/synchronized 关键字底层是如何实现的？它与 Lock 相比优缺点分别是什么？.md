synchronized 关键字底层是如何实现的？它与 Lock 相比优缺点分别是什么？  

Synchronized原理  
Synchronized在Jdk 1.6后通过对象Mark word实现。会在同步块的前后分别生成 monitorenter 和 monitorexit 字节码指令，这两个字节码指令都需要一个引用类型的参数来指明要锁定和解锁的对象。Synchronized实现了偏向锁，轻量级锁，自旋锁，重量级锁。 偏向锁是对轻量级锁的优化，轻量级锁是对重量级锁的优化。

Synchronized锁的升级流程：  
每一个线程在准备获取共享资源时：

偏向锁：第一步，检查MarkWord里面是不是放的自己的ThreadId ,如果是，表示当前线程是处于 “偏向锁” 。  
轻量级锁：第二步，如果MarkWord不是自己的ThreadId，锁升级，这时候，用CAS来执行切换，新的线程根据MarkWord里面现有的ThreadId，通知之前线程暂停，之前线程将Markword的内容置为空。  
第三步，两个线程都把锁对象的HashCode复制到自己新建的用于存储锁的记录空间，接着开始通过CAS操作，把锁对象的MarKword的内容修改为自己新建的记录空间的地址的方式竞争MarkWord。  
自旋锁：第四步，第三步中成功执行CAS的获得资源，失败的则进入自旋。  
第五步，自旋的线程在自旋过程中，成功获得资源(即之前获的资源的线程执行完成并释放了共享资源)，则整个状态依然处于 轻量级锁的状态，如果自旋失败 。  
重量级锁：第六步，进入重量级锁的状态，这个时候，自旋的线程进行阻塞，等待之前线程执行完成并唤醒自己。

与 Lock 相比优缺点

内置+性能：lock是一个接口，而synchronized是java的关键字，synchronized是内置的语言实现；synchronized优化以后性能和lock差不多。  
释放锁：synchronized在发生异常时，会自动释放线程占有的锁，因此不会导致死锁现象发生；而lock在发生异常时，如果没有主动通过unlock（）去释放锁，则很可能造成死锁现象，因此使用lock（）时需要在finally块中释放锁；  
响应中断：lock可以让等待锁的线程响应中断，而synchronized却不行，使用synchronized时，等待的线程会一直等待下去，不能响应中断  
*功能丰富：通过lock可以知道有没有成功获取锁， lock的功能非常丰富，而synchronized却无法办到。  